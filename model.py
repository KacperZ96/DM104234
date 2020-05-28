import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# transformacja reprezentacji string do liczbowej
def transform_string_into_number(string):
    return int(string == 'm')

# stworz model
def create_model(n_neighbors):

    # wczytanie danych
    df = pd.read_csv("polish_names.csv")

    # konwersja kolumny gender na reprezentacje liczbowa
    df['target'] = df['gender'].map(lambda x: int(x == 'm'))

    # dodanie kolumny z infomracją czy dane imię konczy się na a, jeśli tak to 1, jeśli nie to 0
    df['last_letter_a'] = df['name'].map(lambda x: int(x.endswith('a')))

    # tablica zmiennych na podstawie których chcemy przeprowadzić analizę
    X = df[['last_letter_a']].values

    # wyniki dla uczenia z nadzorem
    y = df['target'].values

    model= KNeighborsClassifier(n_neighbors, weights='distance')

    # dopasuj model do danych
    model.fit(X, y)

    return model

# klasyfikacja danych
def get_prediction(model, name):

    # przetworzenie imienia w dane wejsciowe klasyfikatora
    X = [[int(name.endswith('a'))]]

    # klasyfikacja imienia
    return model.predict(X)