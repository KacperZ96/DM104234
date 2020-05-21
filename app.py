from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import model

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

# stworzenie modelu
model_names = model.create_model(5)


@app.route('/', methods=['GET','POST'])
def index():

    # pobierz dane jesli zostaly wyslane
    if request.method == 'POST':

        # pobierz nazwe name z formularza
        name = request.form['name']

        # klasyfikuj imię
        gender_number = model.get_prediction(model_names, name)

        # jesli gender rowna sie 1 to mezczyzna
        if gender_number:
            gender = 'Male'
        else:
            gender = 'Female'

        result = {
            'name' : name,
            'gender' : gender
        }
        return render_template('result.html', result = result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')