from flask import Flask, render_template, request, redirect, url_for, flash
import os
import csv

app = Flask(__name__)
app.secret_key = "chave_secreta_super_secreta"

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

        return redirect(url_for("contato"))
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
