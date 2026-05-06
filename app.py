from flask import Flask

app = Flask(__name__)

@app.route('/ola/<nome>')
def exercicio_1(nome):
    return f"Olá, {nome}! Seja bem-vinda ao sistema."

@app.route('/calculo/<int:n1>/<int:n2>')
def exercicio_2(n1, n2):
    return f"A soma de {n1} + {n3} é {n1 + n2}"

@app.route('/idade/<nome>/<int:idade>')
def exercicio_3(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."

@app.route('/produto/<nome>/<float:preco>')
def exercicio_4(nome, preco):
    return f"O produto {nome} custa R$ {preco}"

@app.route('/repetir/<palavra>/<int:vezes>')
def exercicio_5(palavra, vezes):
    return (palavra + " ") * vezes

if __name__ == '__main__':
    app.run()