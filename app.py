from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Isabella Galvão "})


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

if __name__ == '__main__':
    app.run(debug=True)