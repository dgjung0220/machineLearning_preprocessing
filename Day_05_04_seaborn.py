# Day_05_04_seaborn.py

import seaborn as sns
import matplotlib.pyplot as plt

# https://seaborn.pydata.org/examples/index.html
def show_iris():
    print(sns.get_dataset_names())
    # ['anscombe', 'attention', 'brain_networks', 'car_crashes', 'dots', 'exercise', 'flights', 'fmri', 'gammas', 'iris', 'planets', 'tips', 'titanic']

    iris = sns.load_dataset('iris')
    print(type(iris))               # <class 'pandas.core.frame.DataFrame'>
    print(iris.columns)
    # Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
    #        'species'],
    #       dtype='object')

    sns.swarmplot(x='species', y='petal_length',data=iris)
    plt.show()

titanic = sns.load_dataset('titanic')
print(titanic)

sns.factorplot('class', 'survived', 'sex', data=titanic, kind='bar', palette='muted', legend=False)
plt.show()