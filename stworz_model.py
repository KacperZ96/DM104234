import pandas as pd
#models
from sklearn.neighbors import KNeighborsClassifier
#success metric
from sklearn.metrics import accuracy_score


def transform_string_into_number(string):
    return int(string == 'm')


n_neighbors = 5


df = pd.read_csv("polish_names.csv")


print(df.info())


print(df['gender'].value_counts())


print(df.sample(5))


df['target'] = df['gender'].map(lambda x: int(x == 'm'))


df['last_letter_a'] = df['name'].map(lambda x: int(x.endswith('a')))


X = df[['last_letter_a']].values


y = df['target'].values

model= KNeighborsClassifier(n_neighbors, weights='distance')

model.fit(X, y)


y_pred = model.predict(X)


accuracy = accuracy_score(y, y_pred)
print(f"Dokladnosc modelu to {accuracy}")
