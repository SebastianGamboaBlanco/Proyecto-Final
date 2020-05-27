from flask import Flask, render_template, request, make_response, jsonify
from compilador import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods = ['POST', 'GET'])
def compilador():
    lexer = analizadorLexico()
    parser = analizadorParser()
    env = { }
    while True:
        try:
            txt = request.form['texto']
            txto = txt
            "texto = input('Entrada: ')"
        except EOFError:
            break
        '''if texto:
            arbol = parser.parse(lexer.tokenize(texto))
            Ejecucion(arbol, env)'''
        if txt:
            arbol = parser.parse(lexer.tokenize(txt))
            aux = Ejecucion(arbol, env) 
            if aux:
                return make_response(jsonify(aux.r_arbol(arbol)), 200)


@app.route('/documentacion')
def document():
    return render_template('documentacion.html')

if __name__ == "__main__":
    app.run(debug=True)
