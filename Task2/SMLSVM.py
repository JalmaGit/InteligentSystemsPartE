from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Step 1: Loading data
df = pd.read_csv("WineQTCali.csv")

# Step 2: Data Preprocessing
X = df.drop('quality', axis=1)
X = X.drop('dataCount', axis=1)
y = df['quality']

# Step 3: Splitting Data

## We are keeping 30% of the Data for testing, and 80% of the data for training
## Randomstate utilized to generate the same train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)

# Step 4: Rescaling

##Utilized to rescale so that no feature is dominating in the machine learning
scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

## First Set of hyperparameters
print("____________FIRST SET OF HYPERPARAMETERS_______________")
model = SVC(kernel='rbf',
             C=1.0
            ).fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)


print("Train score: ",round(model.score(X_train_scaled, y_train),4))
print("Accuracy: ", round(accuracy_score(y_test, y_pred),4))
print("Classification Report: ", classification_report(y_test, y_pred))


## Second Set of hyperparameters
print("____________SECOND SET OF HYPERPARAMETERS_______________")
model1 = SVC(kernel='poly',
             C=10,
             degree=1,
             class_weight='balanced'
             ).fit(X_train_scaled, y_train)

y_pred1 = model1.predict(X_test_scaled)

print("Train score: ",round(model1.score(X_train_scaled, y_train),4))
print("Accuracy: ", round(accuracy_score(y_test, y_pred1),4))
print("Classification Report: ", classification_report(y_test, y_pred1))

## Third Set of hyperparameters
print("____________THIRD SET OF HYPERPARAMETERS_______________")
model2 = SVC(kernel='poly',
             C=10,
             degree=1,
             class_weight='balanced'
             ).fit(X_train_scaled, y_train)

y_pred2 = model2.predict(X_test_scaled)

print("Train score: ",round(model2.score(X_train_scaled, y_train),4))
print("Accuracy: ", round(accuracy_score(y_test, y_pred2),4))
print("Classification Report: ", classification_report(y_test, y_pred2))