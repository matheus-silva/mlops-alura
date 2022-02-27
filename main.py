from flask import Flask, request, jsonify
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

colunas = ["tamanho", "ano", "garagem"]
with open("modelo.sav", "rb") as f:
    modelo = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Minha primeira API."

@app.route("/sentimento/<frase>")
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to="en")
    polaridade = tb_en.sentiment.polarity
    return f"polaridade: {polaridade}"

@app.route("/cotacao/", methods=["POST"])
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

if __name__ == "__main__":
    app.run(debug=True)
