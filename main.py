from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from peewee import *
import base64

app = Flask(__name__)
app.secret_key = 'flash_alerta'

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)  # Inicializa o LoginManager com a aplicação Flask
login_manager.login_view = 'home'  # Redireciona para a página de login se o usuário não estiver autenticado

'''--------------------BANCO DE DADOS------------------'''
db = SqliteDatabase('emailsenha.db')

class BaseModel(Model):
    class Meta:
        database = db

class emailsenha(BaseModel, UserMixin):
    nome = CharField(unique=True, null=False)
    email = CharField(unique=True, null=False)
    senha = CharField(null=False)
    foto = BlobField()

db.connect()
db.create_tables([emailsenha])

'''---------------------------LOGIN MANAGER ------------------------'''
@login_manager.user_loader
def load_user(user_id):
    return emailsenha.get_or_none(id=user_id)

'''---------------------------ROTAS DO FLASK ---------------------------------------'''
@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('protected'))
    return render_template('login.html')

@app.route("/pagina_registro")
def registro():
    return render_template('registro.html')

@app.route("/register", methods=['POST'])
def registrar():
    nome = request.form["nome"]
    email = request.form["email"]
    email2 = request.form["email2"]
    senha = request.form["password"]
    senha2 = request.form["password2"]
    foto = b''  # Usar bytes vazios como padrão
    if email == email2 and senha == senha2:
        try:
            emailsenha.create(nome=nome, email=email, senha=senha, foto=foto)
            flash('Registro realizado com sucesso! Faça login.')
            return redirect(url_for('home'))
        except IntegrityError:
            flash('Este e-mail/nickname já está registrado ou preencha todos os campos.')
            return render_template('registro.html')
    else:
        flash('e-mail/senha não coincidem, tente novamente.')
        return render_template('registro.html')

@app.route("/login", methods=['POST'])
def login():
    email = request.form["email"]
    senha = request.form["password"]
    user = emailsenha.get_or_none(emailsenha.email == email)

    if user and user.senha == senha:
        login_user(user)
        return redirect(url_for('protected'))

    flash('LOGIN/SENHA INCORRETO')
    return render_template('login.html')

@app.route("/protected")
@login_required
def protected():
    return render_template('home.html', user=current_user)

@app.route("/overview")
@login_required
def overview():
    return render_template('overview.html', user=current_user)

@app.route("/settings")
@login_required
def settings():
    return render_template('settings.html', user=current_user)

@app.route("/upload_foto", methods=['POST'])
@login_required
def upload_foto():
    file = request.files['file']
    if file:
        file_content = file.read()
        user = current_user
        user.foto = file_content
        user.save()

        flash('Foto atualizada com sucesso!')
    return redirect(url_for('settings'))  # Redireciona para a página de configurações após o upload

@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.')
    return redirect(url_for('home'))

# Função que será executada antes de renderizar qualquer template
@app.context_processor
def inject_foto_data_url():
    if current_user.is_authenticated:
        if current_user.foto == b'':  # Verifica se a foto está vazia (ou usa algum outro critério para definir "sem foto")
            foto_data_url = url_for('static', filename='assets/img/user_icon.png')
        else:
            foto_base64 = base64.b64encode(current_user.foto).decode('utf-8')
            foto_data_url = f"data:image/jpeg;base64,{foto_base64}"
    else:
        foto_data_url = None

    return dict(foto_data_url=foto_data_url)

if __name__ == "__main__":
    app.run(debug=True)
