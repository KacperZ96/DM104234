from app import app, db, model_names
from flask import render_template, request, url_for, redirect

from app import db_models
import model


@app.route('/', methods=['GET','POST'])
def index():

    
    if request.method == 'POST':

        
        name = request.form['name']

        
        name_object = db_models.Name(name=name)

       
        gender_number = model.get_prediction(model_names, name)

        
        if gender_number:
            name_object.gender_predict = 'Male'
        else:
            name_object.gender_predict = 'Female'

        
        db.session.add(name_object)
        db.session.commit()

        return redirect(url_for('view_prediction', id=name_object.id))

    return render_template('index.html')


@app.route('/name/<id>', methods=['GET','POST'])
def view_prediction(id):
    name_object = db_models.Name.query.get(id)

    
    if request.method == 'POST':
        name_object.correct = request.form['correct']

    
    db.session.commit()

    return render_template('result.html', name_object=name_object)

@app.route('/names/', methods=['GET'])
def view_all_predictions():
    names = db_models.Name.query.all()

    return render_template('all.html', names=names)
