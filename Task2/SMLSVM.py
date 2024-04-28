from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt

#Loading data
df = pd.read_csv("WineQTCali.csv")

X = df.drop('quality', axis=1)
X = X.drop('dataCount', axis=1)
y = df['quality']


## We are keeping 30% of the Data for testing, and 70% of the data for training
## Randomstate utilized to generate the same train test split
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=21)

scalar = StandardScaler()

xTrainScaled = scalar.fit_transform(xTrain)
xTestScaled = scalar.transform(xTest)

def SVCRun (exp, i, kernel, C, degree):
    if degree != -1:
        model = SVC(kernel=kernel,
             C=C,
             degree=degree,
             class_weight='balanced',
            ).fit(xTrainScaled, yTrain)
    else:
        model = SVC(kernel=kernel,
             C=C,
             class_weight='balanced',
            ).fit(xTrainScaled, yTrain)
    
    y_pred = model.predict(xTestScaled)
    
    trainScore = round(model.score(xTrainScaled, yTrain),4)
    accuracyScore = round(accuracy_score(yTest, y_pred),4)
    print(f"____________EXPERIMENT {exp} WITH {i} SET OF HYPERPARAMETERS_______________")
    print("Train score: ",round(model.score(xTrainScaled, yTrain),4))
    print("Accuracy: ", round(accuracy_score(yTest, y_pred),4))
    print("Classification Report: ", classification_report(yTest, y_pred))
    
    return model, trainScore, accuracyScore

numCols = 3
numRows = 1

kernels = ["rbf","linear", "sigmoid"]
kernelsId = [1,2,3]

degrees = [1,2,3,4,5,6,7,8,9,10]

Cs = [1,2,3,4,5,6,7,8,9,10]

models = []
accs = []
trainScores = []

figs, axs = plt.subplots(numRows, numCols, figsize=(30,10))

def experiments(j, experiment):

    if experiment == "kernels":
        for i, kernel in enumerate(kernels):
            model, trainScore, acc = SVCRun(j,i, kernel, 1, -1)

            if i == 1:
                models.append(model)
            accs.append(acc)
            trainScores.append(trainScore)
        axs[j].plot(kernelsId,accs, label="Test Score")
        axs[j].plot(kernelsId,trainScores, label="Training Score")
        axs[j].set_xlabel("Kernels Utilized") # X-axis label
        axs[j].set_ylabel("Accuracy") # Y-axis label
        axs[j].set_title("Experiment 1")
        axs[j].legend()
        axs[j].set_xticks(kernelsId)
        axs[j].set_xticklabels(kernels)
    elif experiment == "C":
        for i, c in enumerate(Cs):
            model, trainScore, acc = SVCRun(j,i, "rbf", c, -1)

            if i == 3:
                models.append(model)
            accs.append(acc)
            trainScores.append(trainScore)
        axs[j].plot(Cs,accs, label="Test Score")
        axs[j].plot(Cs,trainScores, label="Training Score")
        axs[j].set_xlabel("C Values Utilized") # X-axis label
        axs[j].set_ylabel("Accuracy") # Y-axis label
        axs[j].set_title("Experiment 2")
        axs[j].legend()
        axs[j].set_xticks(Cs)
    elif experiment == "degree":
        for i, degree in enumerate(degrees):
            model, trainScore, acc = SVCRun(j,i, "poly", 1, degree)

            if i == 1:
                models.append(model)
            accs.append(acc)
            trainScores.append(trainScore)
        axs[j].plot(degrees,accs, label="Test Score")
        axs[j].plot(degrees,trainScores, label="Training Score")
        axs[j].set_xlabel("Degree Values Utilized with Poly") # X-axis label
        axs[j].set_ylabel("Accuracy") # Y-axis label
        axs[j].set_title("Experiment 3")
        axs[j].legend()
        axs[j].set_xticks(degrees)

experiments(0,"kernels")
accs = []
trainScores = []
experiments(1,"C")
accs = []
trainScores = []
experiments(2,"degree")



from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, roc_curve

plt.figure(figsize=(8, 6))

# Roc curves from chatgpt
for i, model in enumerate(models, start=1):
    fpr, tpr, _ = roc_curve((yTest == 6).astype(int), model.decision_function(xTestScaled))
    roc_auc = roc_auc_score((yTest == 6).astype(int), model.decision_function(xTestScaled))
    plt.plot(fpr, tpr, label=f'Test {i} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Random Guessing')

# Set labels and title
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.grid(True)

# Show plot
plt.show()