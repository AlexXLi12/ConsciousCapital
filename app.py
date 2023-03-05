from flask import Flask, render_template, request
import model
import allocation
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
    '''print('type request form')
    print(type(request.form))
    print('actual form')
    print(request.form)'''
    print('trying to convert list')
    sectors = request.form.getlist('sectors')
    environment = request.form.getlist('environment')
    social = request.form.getlist('social')
    governance = request.form.getlist('governance')
    controversy = request.form.getlist('controversy')
    gender_diversity = request.form.getlist('gender_diversity')
    racial_diversity = request.form.getlist('racial_diversity')
    # risk = float(request.form.getlist('risk')[0]) / 100.0
    
    '''print(sectors)
    print(environment)
    print(social)
    print(governance)
    print(controversy)
    print(gender_diversity)
    print(racial_diversity)
    print(risk)'''
    #insert function conversion
    #temporary (sample form results that match input for model.py)
    temporaryFormReponseCorrectFormat = np.array([9, 3, 3, 2, 4, 7, 1, 0.1, 1, 1, 2, 2, 1, 0.1, 0.1, 1, 1]) # ENV, SOC, GOV, CON, FEM, MIN, 11 Sectors
    answer = model.inputrating(sectors, int(environment[0]), int(social[0]), int(governance[0]), int(controversy[0]), int(gender_diversity[0]), int(racial_diversity[0]))
    print('ticker predictions: ', end='')
    print(answer)
    allocationAnswer = allocation.runAllocation(answer)
    # print('allocation: ' + str(allocationAnswer))
    print(f"Weights: {allocationAnswer}\n")
    vals = list(allocationAnswer[0].values())
    for i in range(len(vals)):
        vals[i] = 100.0 * float(vals[i])
    return render_template('pie.html', **{'keys':list(allocationAnswer[0].keys()), 'vals':vals, 
                                          'return':round(100*allocationAnswer[1][0],2), 'risk':round(100*allocationAnswer[1][1],2), 'sharpe':round(100*allocationAnswer[1][2],2)})
if __name__ == '__main__':
    app.run()