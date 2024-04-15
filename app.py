from flask import Flask, jsonify, request
from funcoes import maior_de_50, mais_2000
from randomdata import pessoas

app = Flask(__name__)
@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Alexandre Camargo "})


@app.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/<string:nome>", methods=("GET",))
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos", methods=("GET",))
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@app.route("/maior_de_cinquenta", methods = ["GET"])
def maior_que_cinquenta():
    maior_de_cinquenta = maior_de_50(pessoas)
    return jsonify({"Status":200, "mensagem":maior_de_cinquenta})

@app.route("/mais_doismil", methods = ["GET"])
def mais_de_doismil():
    maisdoismil = mais_2000(pessoas)
    return jsonify({"Status":200, "mensagem":maisdoismil})

if __name__ == '__main__':
    app.run(debug=True)