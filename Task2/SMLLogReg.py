from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt


# Loading data
df = pd.read_csv("WineQTCali.csv")

X = df.drop('quality', axis=1)
X = X.drop('dataCount', axis=1)
y = df['quality']

## We are keeping 30% of the Data for testing, and 70% of the data for training
## Randomstate utilized to generate the same train test split
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=21)

good = 0
bad = 0
for i in yTrain:
    if i == 6:
        good += 1
    else:
        bad += 1

print(f"{good=} and {bad=}")

good = 0
bad = 0
for i in yTest:
    if i == 6:
        good += 1
    else:
        bad += 1

print(f"{good=} and {bad=}")

##Utilized to rescale so that no feature is dominating in the machine learning
scalar = StandardScaler()
xTrainScaled = scalar.fit_transform(xTrain)
xTestScaled = scalar.transform(xTest)

def LogRegRun(exp, i, solver, C, l1Ratio):

    penalty = "l2"
    if (solver == "saga"): 
        penalty="elasticnet"
    model = LogisticRegression(random_state=0,
                                C = C,
                                fit_intercept= True,
                                class_weight='balanced',
                                penalty=penalty,
                                solver=solver,
                                l1_ratio=l1Ratio,
                                ).fit(xTrainScaled,yTrain)

    yPred = model.predict(xTestScaled)

    trainScore = round(model.score(xTrainScaled, yTrain),4)
    accuracyScore = round(accuracy_score(yTest, yPred),4)

    print(f"____________EXPERIMENT {exp} WITH {i} SET OF HYPERPARAMETERS_______________")
    print("Train score: ",round(model.score(xTrainScaled, yTrain),4))
    print("Accuracy: ", round(accuracy_score(yTest, yPred),4))
    print("Classification Report: ", classification_report(yTest, yPred))

    return model, trainScore, accuracyScore

numCols = 3
numRows = 1

solvers = ["lbfgs", "liblinear", "newton-cg", "newton-cholesky", "sag", "saga"]
solversId = [1,2,3,4,5,6]

l1ratios = [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1]

Cs = [0.25, 0.5,0.75,1,1.25,1.5,1.75,2]

models = []
accs = []
trainScores = []

figs, axs = plt.subplots(numRows, numCols, figsize=(30,10))
#(i, solver, C, l1Ratio):

def experiments(j, experiment):

    if experiment == "kernels":
        for i, solver in enumerate(solvers):
            model, trainScore, acc = LogRegRun(j,i, solver, 1, 0.0)

            if i == 2:
                models.append(model)
            accs.append(acc)
            trainScores.append(trainScore)
        axs[j].plot(solversId,accs, label="Test Score")
        axs[j].plot(solversId,trainScores, label="Training Score")
        axs[j].set_xlabel("Solvers Utilized") # X-axis label
        axs[j].set_ylabel("Accuracy") # Y-axis label
        axs[j].set_title("Experiment 1")
        axs[j].legend()
        axs[j].set_xticks(solversId)
        axs[j].set_xticklabels(solvers)
    elif experiment == "C":
        for i, c in enumerate(Cs):
            model, trainScore, acc = LogRegRun(j,i, "lbfgs", c, 0.0)

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
        for i, l1ratio in enumerate(l1ratios):
            model, trainScore, acc = LogRegRun(j,i, "saga", 1, l1ratio)

            if i == 2:
                models.append(model)
            accs.append(acc)
            trainScores.append(trainScore)
        axs[j].plot(l1ratios,accs, label="Test Score")
        axs[j].plot(l1ratios,trainScores, label="Training Score")
        axs[j].set_xlabel("L1 Ratios Utilized") # X-axis label
        axs[j].set_ylabel("Accuracy") # Y-axis label
        axs[j].set_title("Experiment 3")
        axs[j].legend()
        axs[j].set_xticks(l1ratios)

experiments(0,"kernels")
accs = []
trainScores = []
experiments(1,"C")
accs = []
trainScores = []
experiments(2,"degree")



from sklearn.metrics import classification_report, accuracy_score, roc_auc_score, roc_curve
...
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
