from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import InternalError
import time

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost:3306/nome_do_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Aluno
class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

# Rota para listar alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    retries = 5
    for attempt in range(retries):
        try:
            alunos = Aluno.query.all()
            return jsonify([{'id': aluno.id, 'nome': aluno.nome, 'idade': aluno.idade} for aluno in alunos])
        except InternalError as e:
            print(f"Tentativa {attempt + 1} falhou: {str(e)}")
            if attempt < retries - 1:  # se não for a última tentativa
                time.sleep(1)  # aguarda 1 segundo antes de tentar novamente
            else:
                return jsonify({'erro': 'Erro ao listar alunos. Tente novamente mais tarde.'}), 500

# Rota para adicionar um novo aluno
@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.get_json()
    novo_aluno = Aluno(nome=data['nome'], idade=data['idade'])
    db.session.add(novo_aluno)
    
    retries = 5
    for attempt in range(retries):
        try:
            db.session.commit()
            return jsonify({'mensagem': 'Aluno adicionado com sucesso!', 'id': novo_aluno.id}), 201
        except InternalError as e:
            db.session.rollback()  # Desfaz as alterações na sessão
            print(f"Tentativa {attempt + 1} de adicionar aluno falhou: {str(e)}")
            if attempt < retries - 1:  # se não for a última tentativa
                time.sleep(1)  # aguarda 1 segundo antes de tentar novamente
            else:
                return jsonify({'erro': 'Erro ao adicionar aluno. Tente novamente mais tarde.'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas se não existirem
    app.run(debug=True)
