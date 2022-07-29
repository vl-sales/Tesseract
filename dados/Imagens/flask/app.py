from flask import Flask, render_template, request
import pandas as pd
import numpy as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
df = sns.load_dataset('iris')

@app.route('/') #Criando uma rota
def home():
    nome = 'Vinicius'

    return render_template('home.html', nome=nome, df=df)

@app.route('/flask')
def flask():
    return 'Flask'

@app.route('/pesquisa')
def pesquisa():
    especie = request.args.get('digitado')
    filtro = df[df['species'] == especie]

    if filtro.shape[0] > 0:
        sns.scatterplot(data=filtro, x='sepal_length', y='petal_length')
        plt.savefig('static/imagens/grafico.png')

    return render_template('home.html', df=filtro, nome='Vinicius')