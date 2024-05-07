from flask import Flask, jsonify, request
from funcoes import maior_de_50, mais_2000, maior_salario, media_profissoes, maior_2000_sexo
from randomdata import pessoas

app = Flask(__name__)
