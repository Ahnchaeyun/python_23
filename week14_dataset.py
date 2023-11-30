import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.info())
print(titanic.head())

survived_human = titanic[titanic["survived"] == 1]["survived"].count()
dead_human = titanic[titanic["survived"] == 0]["survived"].count()
print(f"생존자 수 : {survived_human}명")
print(f"사망자 수 : {dead_human}명")
