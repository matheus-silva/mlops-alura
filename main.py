from flask import Flask, request, jsonify
from textblob import TextBlob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/casas.csv")
colunas = ["tamanho", "ano", "garagem"]
X = df.drop("preco", axis="columns")
y = df["preco"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
modelo = LinearRegression()
modelo.fit(X_train, y_train)

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
