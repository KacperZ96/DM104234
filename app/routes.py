from app import app, db, model_names
from flask import render_template, request, url_for, redirect

from app import db_models
import model


@app.route('/', methods=['GET','POST'])
def index():

    # pobierz dane jesli zostaly wyslane
    if request.method == 'POST':

        # pobierz nazwe name z formularza
        name = request.form['name']

        # stworz obiekt Name, z domyslnymi wartosciami
        name_object = db_models.Name(name=name)

        # klasyfikuj imię
        gender_number = model.get_prediction(model_names, name)

        # jesli gender rowna sie 1 to mezczyzna
        if gender_number:
            name_object.gender_predict = 'Male'
        else:
            name_object.gender_predict = 'Female'

        # dodaj do sesji i dodaj do bazy
        db.session.add(name_object)
        db.session.commit()

        return redirect(url_for('view_prediction', id=name_object.id))

    return render_template('index.html')


@app.route('/name/<id>', methods=['GET','POST'])
def view_prediction(id):
    name_object = db_models.Name.query.get(id)

    # zapisz informacje czy imie zostało dobrze sklasyfikowane
    if request.method == 'POST':
        name_object.correct = request.form['correct']

    # zapis do bazy
    db.session.commit()

    return render_template('result.html', name_object=name_object)

@app.route('/names/', methods=['GET'])
def view_all_predictions():
    names = db_models.Name.query.all()

    return render_template('all.html', names=names)