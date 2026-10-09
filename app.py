
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():

    resultado = False

    if request.method == 'POST':

        nome = request.form['nome']
        altura = float(request.form['altura'])
        peso = float(request.form['peso'])

        imc = peso / (altura * altura)

        if imc < 18.5 :
            mensagem = 'Abaixo do Peso'
            cor = 'alert-info'

        elif imc < 25:
            mensagem = 'Peso Normal'
            cor = 'alert-success'

        elif imc < 30:
            mensagem = 'Sobrepeso'
            cor = 'alert-warning'

        else:
            mensagem = 'Obesidade'
            cor = 'alert-danger'

        return render_template(
            'index.html',
            nome=nome,
            altura=altura,
            peso=peso,
            imc=round(imc, 2),
            mensagem=mensagem,
            cor=cor
        )

    return render_template('index.html', resultado=resultado)




@app.route('/equipe')
def equipe():
     return render_template('equipe.html')


























## --------------------------------------------------

if __name__ == '__main__':
        app.run(debug=True)
