from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from peewee import *
import base64
import datetime
import bcrypt

app = Flask(__name__)
app.secret_key = 'flash_alerta'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=5)  # Definir a duração desejada p/ logout automático

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'

'''--------------------BANCO DE DADOS------------------'''
db = SqliteDatabase('emailsenha.db') #nome do banco de dados

class BaseModel(Model):
    class Meta:
        database = db

class emailsenha(BaseModel, UserMixin):
    nome = CharField(unique=True, null=False)
    email = CharField(unique=True, null=False)
    senha = CharField(null=False)
    foto = BlobField()

class agenda(BaseModel, UserMixin):
    usuario = ForeignKeyField(emailsenha, backref='agendas')  # Chave estrangeira referenciando emailsenha
    tarefa = CharField(unique=True, null=False)
    start_date = DateField(null=False)
    end_date = DateField(null=False)
    description = CharField(unique=True, null=False)
    color = CharField(null=False)

# Conectar ao banco de dados e criar as tabelas
db.connect()
db.create_tables([emailsenha, agenda])


'''---------------------------ROTAS DO FLASK LOGIN E REGISTRO---------------------------------------'''
@login_manager.user_loader
def load_user(user_id):
    return emailsenha.get_or_none(id=user_id)


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
        heashed_senha = bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())
        try:
            emailsenha.create(nome=nome, email=email, senha=heashed_senha, foto=foto)
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

    if user and bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        login_user(user)
        session.permanent = True  # torna a sessão permanente
        return redirect(url_for('protected'))

    flash('LOGIN/SENHA INCORRETO')
    return render_template('login.html')


@app.route("/protected")
@login_required
def protected():
    return render_template('home.html', user=current_user)

'''---------------------------ROTAS DO AGENDA DE EVENTOS---------------------------------------'''

@app.route("/agenda") #visualizar a agenda
@login_required
def overview():
    tarefa = agenda.select().where(agenda.usuario == current_user.id)
    events = []
    for x in tarefa:
        detalhe_evento = {
                'tarefa': x.tarefa,
                'date': x.start_date,
                'end_date': x.end_date,
                'description': x.description,
                'color': x.color,
            }
        events.append(detalhe_evento)

    return render_template('agenda.html', user=current_user, events=events, tarefa=tarefa)


@app.route("/cadastrar_evento", methods=['POST']) #cadastrar evento no banco de dados
@login_required
def cadastrar_evento():
    usuario = current_user
    tarefa = request.form["tarefa"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    description = request.form["description"]
    color = request.form["color"]

    agenda.create(usuario=usuario, tarefa=tarefa, start_date=start_date, end_date=end_date, description=description, color=color)
    return redirect(url_for('overview'))


@app.route("/excluir_evento/<int:evento_id>", methods=['POST']) #excluir evento no banco de dados
@login_required
def excluir_evento(evento_id):
    try:
        evento = agenda.get(agenda.id == evento_id)
        evento.delete_instance()  # Exclui o evento do banco de dados
        flash("Evento excluído com sucesso!")
    except agenda.DoesNotExist:
        flash("Evento não encontrado!")

    return redirect(url_for('overview'))  # Recarrega a página após a exclusão


'''---------------------------ROTAS DO FLASK CONFIGURAÇÕES DE CONTA---------------------------------------'''
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
    return redirect(url_for('settings'))


@app.route("/upload_dados", methods=['POST'])
@login_required
def upload_dados():
    nome = request.form.get("nome")
    senha = request.form.get("password")
    senha2 = request.form.get("password2")

    if senha == senha2:
        user = current_user
        user.nome = nome
        user.senha = senha
        try:
            user.save()
            flash('Alteração realizada com sucesso!')
        except IntegrityError:
            flash('Este e-mail/nickname já está registrado ou preencha todos os campos.')
            return render_template('settings.html', user=user)
    else:
        flash('Senha não coincide, tente novamente.')

    return redirect(url_for('settings'))


@app.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.')
    return redirect(url_for('home'))


@app.context_processor
def inject_foto_data_url():
    if current_user.is_authenticated:
        if current_user.foto == b'':
            foto_data_url = url_for('static', filename='assets/img/user_icon.png')
        else:
            foto_base64 = base64.b64encode(current_user.foto).decode('utf-8')
            foto_data_url = f"data:image/jpeg;base64,{foto_base64}"
    else:
        foto_data_url = None

    return dict(foto_data_url=foto_data_url)

if __name__ == "__main__":
    app.run(debug=True)
