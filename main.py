from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from peewee import *

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

# A classe emailsenha agora herda de UserMixin, o que facilita a integração com o Flask-Login
class emailsenha(BaseModel, UserMixin):
    nome = CharField(unique=True)
    email = CharField(unique=True)
    senha = CharField()

db.connect()
db.create_tables([emailsenha])

'''---------------------------LOGIN MANAGER ------------------------'''
# Função que carrega um usuário com base no ID (necessária para o Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return emailsenha.get_or_none(id=user_id)

'''---------------------------ROTAS DO FLASK ---------------------------------------'''
@app.route("/")
def home():
    if current_user.is_authenticated:  # Verifica se o usuário está autenticado
        return redirect(url_for('protected'))  # Redireciona para uma página protegida se já estiver logado
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
    if email == email2 and senha == senha2:
        try:
            emailsenha.create(nome=nome, email=email, senha=senha)
            flash('Registro realizado com sucesso! Faça login.')
            return redirect(url_for('home'))  # Redireciona para a página de login após o registro bem-sucedido
        except IntegrityError:
            flash('Este e-mail/nickname já está registrado. Tente outro.')
            return render_template('registro.html')
    else:
        flash('e-mail/senha não coincidem, tente novamente.')
        return render_template('registro.html')

@app.route("/login", methods=['POST'])
def login():
    email = request.form["email"]
    senha = request.form["password"]
    user = emailsenha.get_or_none(emailsenha.email == email)  # Busca o usuário no banco de dados pelo e-mail

    if user and user.senha == senha:
        login_user(user)  # Autentica o usuário se o e-mail e senha forem válidos
        return redirect(url_for('protected'))  # Redireciona para uma página protegida após o login

    flash('LOGIN/SENHA INCORRETO')
    return render_template('login.html')

# Rota protegida que requer que o usuário esteja logado para acessar
@app.route("/protected")
@login_required
def protected():
    return render_template('home.html',  user=current_user)#colocar a variável user.nome no html nome

# Rota para logout, que também requer que o usuário esteja logado
@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()  # Faz o logout do usuário
    flash('Você saiu da sua conta.')
    return redirect(url_for('home'))  # Redireciona para a página de login após o logout

if __name__ == "__main__":
    app.run(debug=True)
