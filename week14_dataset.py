import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic = sns.load_dataset('titanic')

titanic = titanic.drop({'who', 'deck', 'embark_towm', 'alive', 'class', 'adult_male', 'alone'}, axis=1)
titanic = titanic.dropna()
titanic['sex'] = titanic['sex'].map({'male':0, 'female':1})
titanic['embarked'] = titanic['embarked'].map({'S': 0, 'C': 1, 'Q': 2})
x = titanic.drop('survived', axis=1)
y = titanic['survived']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=5)
model = LogisticRegression(solver='liblinear')
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(f'정확도: {accuracy_score(y_test, y_pred)}')

