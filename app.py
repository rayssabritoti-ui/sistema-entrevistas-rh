from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuário e senha fixos
USUARIO = "admin"
SENHA = "1234"

# Base de dados em memória
dados = []

# Página de login
@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == USUARIO and senha == SENHA:
            return redirect(url_for("home"))
        else:
            msg = "❌ Usuário ou senha incorretos"
    return render_template("login.html", msg=msg)

# Página principal do site (cadastro)
@app.route("/home")
def home():
    return render_template("index.html", dados=dados)

# Rota para cadastrar um candidato
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    status = request.form.get("status")
    data = request.form.get("data")
    if nome:
        dados.append({
            "Nome": nome,
            "CPF": cpf,
            "Status": status,
            "Data": data
        })
    return redirect(url_for("home"))

# Rota para excluir um candidato
@app.route("/excluir/<int:index>")
def excluir(index):
    if 0 <= index < len(dados):
        dados.pop(index)
    return redirect(url_for("home"))

if __name__== "__main__":
    app.run(debug=True)