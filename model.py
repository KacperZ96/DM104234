import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


def transform_string_into_number(string):
    return int(string == 'm')


def create_model(n_neighbors):

  
    df = pd.read_csv("polish_names.csv")

 
    df['target'] = df['gender'].map(lambda x: int(x == 'm'))

    
    df['last_letter_a'] = df['name'].map(lambda x: int(x.endswith('a')))

    
    X = df[['last_letter_a']].values

    
    y = df['target'].values

    model= KNeighborsClassifier(n_neighbors, weights='distance')

    
    model.fit(X, y)

    return model


def get_prediction(model, name):

    
    X = [[int(name.endswith('a'))]]

    
    return model.predict(X)