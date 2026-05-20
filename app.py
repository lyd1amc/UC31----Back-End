from flask import Flask, render_template

app = Flask(__name__)

cardapio_lanches = {
    1: {"nome": "X-Burguer", "preco": 15.00, "ingredientes": "Pão, carne de 120g e queijo prato."},
    2: {"nome": "X-Salada", "preco": 18.00, "ingredientes": "Pão, carne, queijo, alface, tomate e maionese."},
    3: {"nome": "X-Bacon", "preco": 22.00, "ingredientes": "Pão, carne, queijo, bacon crocante e molho barbecue."}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cardapio')
def mostrar_cardapio():
    return render_template('cardapio.html', produtos=cardapio_lanches)

@app.route('/lanche/<int:id>')
def detalhe_lanche(id):
    lanche_selecionado = cardapio_lanches.get(id)
    return render_template('lanche.html', lanche=lanche_selecionado)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)