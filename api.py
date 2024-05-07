from flask import Blueprint, jsonify
from funcoes import maior_de_50, mais_2000, maior_salario, media_profissoes, maior_2000_sexo
from randomdata import pessoas

bp = Blueprint("api", __name__)

@bp.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Alexandre Camargo "})


@bp.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/argumentos/<string:nome>", methods=("GET",))
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route("/argumentos", methods=("GET",))
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@bp.route("/maior_de_cinquenta", methods = ["GET"])
def maior_que_cinquenta():
    maior_de_cinquenta = maior_de_50(pessoas)
    return jsonify({"Status":200, "mensagem":maior_de_cinquenta})

@bp.route("/mais_doismil", methods = ["GET"])
def mais_de_doismil():
    maisdoismil = mais_2000(pessoas)
    return jsonify({"Status":200, "mensagem":maisdoismil})

@bp.route("/maior_salario", methods = ["GET"])
def maior_recebimento():
    maior_recibo = maior_salario(pessoas)
    return jsonify({"Status":200, "mensage":maior_recibo})

@bp.route("/media_proficoes", methods = ["GET"])
def media_trabalhos():
    media_trampo = media_profissoes(pessoas)
    return jsonify({"Status":200, "mensage":media_trampo})

@bp.route("/maior_2000_sexo", methods = ["GET"])
def maior_de_2000sexo():
    maior_2000sexo = maior_2000_sexo(pessoas)
    return jsonify({"Status":200, "mensage":maior_2000sexo})
