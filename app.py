from flask import Flask, render_template, request
import model
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    print(request.form.getlist('sectors'))
    #insert function conversion
    #temporary (sample form results that match input for model.py)
    temporaryFormReponseCorrectFormat = np.array([9, 3, 3, 2, 4, 7, 1, 0.1, 1, 1, 2, 2, 1, 0.1, 0.1, 1, 1]) # ENV, SOC, GOV, CON, FEM, MIN, 11 Sectors
    answer = model.runModel(temporaryFormReponseCorrectFormat)
    print(answer)
    return render_template('submit_form.html', )
if __name__ == '__main__':
    app.run()