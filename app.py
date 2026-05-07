from flask import Flask, render_template

app = Flask(__name__)

fotos_pizzas = {
    "calabresa": "https://share.google/BNodOZuBwBamT6vIi",
    "margherita": "https://share.google/JZuaWsioZSa1rClg1",
    "frango": "https://share.google/bzhA0gyntsMu95MUu"
}

@app.route('/pizzaria/<sabor>')
def pagina_pizza(sabor):
    sabor = sabor.lower()

    if sabor in fotos_pizzas:
        link_foto = fotos_pizzas[sabor]
        return render_template('index.html', sabor_escolhido=sabor, foto=link_foto)
    
    return " Esse sabor ainda não temos no cardápio.", 404

if __name__ == '__main__':
    app.run(debug=True)