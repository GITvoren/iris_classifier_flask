import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load data file
data = load_iris()
# print(data)

# Select independent and dependent variables ( Features/Input, Labels/Target/Output )
# Organize data and labels w/ DataFrames from pandas
X = pd.DataFrame(data.data, columns=(data.feature_names))
y = pd.DataFrame(data.target, columns=['Target'])

# Split data set for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.3)


# Create/Instantiate model using Decision Tree Algorithm
# Train Model 'model.fit(X, Y)'
def training_model():
    model = DecisionTreeClassifier()
    trained_model = model.fit(X_train, y_train)
    return trained_model

