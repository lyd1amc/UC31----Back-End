from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    deu_certo = False
    aluno_cadastrado = {}

    if request.method == 'POST':
        nome = request.form['nome'].strip()
        email = request.form['email'].strip()
        telefone = request.form['telefone'].strip()
        cpf = request.form['cpf'].strip()
        cidade = request.form['cidade'].strip()
        estado = request.form['estado'].strip()
        curso = request.form['curso'].strip()
        idade = request.form['idade'].strip()
        senha = request.form['senha'].strip()

        nome = nome.title()
        email = email.lower()

        telefone_limpo = telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        cpf_limpo = cpf.replace('.', '').replace('-', '')

        valido = True

        if nome == "" or email == "" or telefone == "" or cpf == "" or cidade == "" or estado == "" or curso == "" or idade == "" or senha == "":
            valido = False
        
        if len(nome) < 8:
            valido = False

        if "@" not in email or ".com" not in email:
            valido = False

        if len(telefone_limpo) != 11 or telefone_limpo.isdigit() == False:
            valido = False

        if len(cpf_limpo) != 11 or cpf_limpo.isdigit() == False:
            valido = False

        if len(cidade) < 3:
            valido = False

        if len(estado) != 2 or estado.isalpha() == False:
            valido = False

        if idade.isdigit() == False:
            valido = False
        else:
            if int(idade) < 16:
                valido = False

        tem_numero = False
        for letra in senha:
            if letra.isdigit():
                tem_numero = True

        if len(senha) < 8 or tem_numero == False:
            valido = False

        if valido == True:
            deu_certo = True
            aluno_cadastrado = {
                'nome': nome,
                'email': email,
                'telefone': telefone_limpo,
                'cpf': cpf_limpo,
                'cidade': cidade,
                'estado': estado.upper(),
                'curso': curso,
                'idade': idade
            }

    return render_template('cadastro.html', sucesso=deu_certo, aluno=aluno_cadastrado)

if __name__ == '__main__':
    app.run(debug=True)