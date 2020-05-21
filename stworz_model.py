import pandas as pd
#models
from sklearn.neighbors import KNeighborsClassifier
#success metric
from sklearn.metrics import accuracy_score

# transformacja reprezentacji string do liczbowej
def transform_string_into_number(string):
    return int(string == 'm')

# liczba k sasiadow
n_neighbors = 5

# wczytanie danych
df = pd.read_csv("polish_names.csv")

# informacje o danych
print(df.info())

# rozklad imion
print(df['gender'].value_counts())

# przykladowe rekordy
print(df.sample(5))

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

# stwórz tablicę z predykcjami
y_pred = model.predict(X)

# zobacz ile predykcji model dobrze oznaczył
accuracy = accuracy_score(y, y_pred)
print(f"Dokladnosc modelu to {accuracy}")
