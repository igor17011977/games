import pandas
data = pandas.read_csv("titanic.csv", index_col="PassengerId")
print (data["Sex"].value_counts())

sex_counts = data['Sex'].value_counts()

print(1, '{} {}'.format(sex_counts['male'], sex_counts['female']))


l=data["Survived"].value_counts()
Survived=data['Survived'].value_counts(normalize=True) * 100
print (round(Survived,2))

surv_counts = data['Survived'].value_counts()

surv_percent = 100.0 * surv_counts[1] / surv_counts.sum()

print(2, "{:0.2f}".format(surv_percent))
# ----------------------------------------------------
Pclass=data['Pclass'].value_counts(normalize=True) * 100
print (round(Pclass,2))

pclass_counts = data['Pclass'].value_counts()

pclass_percent = 100.0 * pclass_counts[1] / pclass_counts.sum()

print(3, "{:0.2f}".format(pclass_percent))
# ----------------------------------------
corr = data['SibSp'].corr(data['Parch'])

print(5, "{:0.2f}".format(corr))
#
# Age=data['Age'].mean()
# Age1=data['Age'].median()
# print(round(Age,2))
# print(Age1)
# Name = data.groupby("Sex")

# print (Name.value_counts(sort="Miss"))