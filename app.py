from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import model

app = Flask(__name__, template_folder='templates')
Bootstrap(app)


model_names = model.create_model(5)


@app.route('/', methods=['GET','POST'])
def index():

    
    if request.method == 'POST':

        
        name = request.form['name']

        
        gender_number = model.get_prediction(model_names, name)

        
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
