from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    num = request.form['number']
    print(num)
    return render_template('submit_form.html')
if __name__ == '__main__':
    app.run()