from flask import Flask, render_template, request, redirect, url_for, flash
import os
import csv
import requests
from admin.routes import diretorio_base, arquivo_processos, ler_processos

app = Flask(__name__)
app.secret_key = "chave_secreta_super_secreta"

from admin import admin_bp

app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form.get("telefone", "")
        assunto = request.form["assunto"]

        caminho_csv = os.path.join("data", "dados.csv")
        arquivo_existe = os.path.isfile(caminho_csv)

        with open(caminho_csv, mode="a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)

            if not arquivo_existe:
                writer.writerow(["Nome", "Email", "Telefone", "Assunto"])
            
            writer.writerow([nome, email, telefone, assunto])

            flash("Mensagem enviada com sucesso!", "sucesso")
        
        url_webhook = "https://hook.us2.make.com/2co6w7ldul6cv3f8l763ti7pt7exbplj"

        dados = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "assunto": assunto
        }

        requests.post(url_webhook, json=dados)

        return redirect(url_for("contato"))
    return render_template("contato.html")

@app.route('/processos')
def processos_seletivos():

    processos= ler_processos()

    return render_template('processos.html', processos=processos)

@app.route("/agendamentos", methods=["GET", "POST"])
def agendamentos():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        data = request.form["data"]
        horario = request.form["horario"]
        local = request.form["local"]
        publico = request.form["publico"]
        tema = request.form["tema"]

        caminho_csv = os.path.join("data", "agendamentos.csv")
        arquivo_existe = os.path.isfile(caminho_csv)

        with open(caminho_csv, mode="a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)

            if not arquivo_existe:
                writer.writerow([
                    "Nome", "Email", "Telefone", "Data",
                    "Horario", "Local", "Publico", "Tema"
                ])

            writer.writerow([
                nome, email, telefone, data,
                horario, local, publico, tema
            ])
        
        url_webhook = "https://hook.us2.make.com/8txrcg0nhsb34h6guoxlz2h28nukfc1s"

        dados = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "data": data,
            "horario": horario,
            "local": local,
            "publico": publico,
            "tema": tema
        }

        requests.post(url_webhook, json=dados)

        flash("Agendamento enviado com sucesso!", "sucesso")
        return redirect(url_for("agendamentos"))

    return render_template("agendamentos.html")


if __name__ == "__main__":
    app.run(debug=True)