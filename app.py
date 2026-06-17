from flask import Flask, session, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chave_secreta_aqui'

@app.route('/contador')
def contador():
    # Se não existir a chave, começa com 0 e soma 1 a cada acesso
    session['contador'] = session.get('contador', 0) + 1
    
    html = '''
    <h1>Acessos: {{ session['contador'] }}</h1>
    <form action="/zerar" method="POST">
        <button type="submit">Zerar</button>
    </form>
    '''
    return render_template_string(html)

@app.route('/zerar', methods=['POST'])
def zerar():
    # Remove apenas o contador de forma cirúrgica
    session.pop('contador', None)
    return redirect(url_for('contador'))

if __name__ == '__main__':
    app.run(debug=True)