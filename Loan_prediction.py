# -*- coding: utf-8 -*-
"""DATA SCIENCE- Loan Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VF13DFjZSiXkEbLhoMZdVddQhv-5quo_

# **Loan Prediction**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

"""Importing & Loading the dataset"""

train_df = pd.read_csv('/train.csv')
train_df.head()

"""Dataset Info:"""

train_df.info()

"""Observations from the above Info:

There are a total of 13 columns, including the target variable, and each column is self-explanatory. Some columns have missing values. For categorical columns, identify the possible values, and for numerical columns, determine their possible range

Dataset Shape:
"""

train_df.shape

"""Dataset Description:

"""

train_df.describe()

"""Checking the Missing Values

"""

train_df.isnull().sum()

"""First we will fill the Missing Values in "LoanAmount" & "Credit_History" by the 'Mean' & 'Median' of the respective variables.


"""

train_df['LoanAmount'] = train_df['LoanAmount'].fillna(train_df['LoanAmount'].mean())

train_df['Credit_History'] = train_df['Credit_History'].fillna(train_df['Credit_History'].median())

"""Let's confirm if there are any missing values in 'LoanAmount' & 'Credit_History'

"""

train_df.isnull().sum()

"""Now, Let's drop all the missing values remaining.

"""

train_df.dropna(inplace=True)

"""Let's check the Missing values for the final time!"""

train_df.isnull().sum()

"""Here, we have dropped all the missing values to avoid disturbances in the model. The Loan Prediction requires all the details to work efficiently and thus the missing values are dropped.

Now, Let's check the final Dataset Shape
"""

train_df.shape

"""Exploratory Data Analyis

**Comparison between Genders in getting the Loan:**

"""

sns.countplot(x='Gender', hue='Loan_Status', data=train_df, palette='Set1')
print(pd.crosstab(train_df['Gender'], train_df['Loan_Status']))

"""**Observation :**

Here, we can see that the **Males** have more chances to get the Loan.

Comparison between Married Status in getting the Loan:
"""

sns.countplot(x='Married', hue='Loan_Status', data=train_df, palette='Set1')
print(pd.crosstab(train_df['Married'], train_df['Loan_Status']))

"""**Observation :**

Here, we can see that the **Married Person** has more chance of getting the Loan.

Comparison between Education Status of an Individual in getting the Loan:
"""

sns.countplot(x='Education', hue='Loan_Status', data=train_df, palette='Set1')
print(pd.crosstab(train_df['Education'], train_df['Loan_Status']))

"""Here, we can see that a **Graduate Individual** has more chance of getting the Loan.

**Comparison between Self-Employed or Not in getting the Loan:**
"""

sns.countplot(x='Self_Employed', hue='Loan_Status', data=train_df, palette='Set1')
print(pd.crosstab(train_df['Self_Employed'], train_df['Loan_Status']))

"""Here, we can see that **Not Self-Employed** has more chance of getting the Loan.

**Comparison between Property Area for getting the Loan:**
"""

sns.countplot(x='Property_Area', hue='Loan_Status', data=train_df, palette='Set1')
print(pd.crosstab(train_df['Property_Area'], train_df['Loan_Status']))

"""Here, we can see that People living in **Semi-Urban** Area have more chance to get the Loan."""

import seaborn as sns
import matplotlib.pyplot as plt
categorical_columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area','Credit_History','Loan_Amount_Term']

fig,axes = plt.subplots(4,2,figsize=(12,15))
for idx,cat_col in enumerate(categorical_columns):
    row,col = idx//2,idx%2
    sns.countplot(x=cat_col,data=train_df,hue='Loan_Status',ax=axes[row,col])


plt.subplots_adjust(hspace=1)

"""**Let's replace the Variable values to Numerical form & display the Value Counts**

The data in Numerical form avoids disturbances in building the model.
"""

train_df['Loan_Status'].replace('Y',1,inplace=True)
train_df['Loan_Status'].replace('N',0,inplace=True)

train_df['Loan_Status'].value_counts()

train_df.Gender=df.Gender.map({'Male':1,'Female':0})
train_df['Gender'].value_counts()

train_df.Married=df.Married.map({'Yes':1,'No':0})
train_df['Married'].value_counts()

train_df.Dependents=df.Dependents.map({'0':0,'1':1,'2':2,'3+':3})
train_df['Dependents'].value_counts()

train_df.Education=df.Education.map({'Graduate':1,'Not Graduate':0})
train_df['Education'].value_counts()

train_df.Self_Employed=df.Self_Employed.map({'Yes':1,'No':0})
train_df['Self_Employed'].value_counts()

train_df.Property_Area=df.Property_Area.map({'Urban':2,'Rural':0,'Semiurban':1})
train_df['Property_Area'].value_counts()

train_df['LoanAmount'].value_counts()

train_df['Loan_Amount_Term'].value_counts()

train_df['Credit_History'].value_counts()

"""**Display the Correlation Matrix**"""

plt.figure(figsize=(16,5))
sns.heatmap(train_df.corr(),annot=True)
plt.title('Correlation Matrix (for Loan Status)')

"""From the above figure, we can see that **Credit_History** (Independent Variable) has the maximum correlation with Loan_Status (Dependent Variable). Which denotes that the **Loan_Status** is heavily dependent on the Credit_History.

**Final DataFrame**
"""

train_df.head()

"""**Importing Packages for Classification algorithms**"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import warnings
from sklearn.exceptions import ConvergenceWarning

"""Splitting the data into Train and Test set"""

X = train_df.iloc[1:542,1:12].values
y = train_df.iloc[1:542,12].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=0)

print(X_train)

print(X_test)

print(y_train)

"""#**Model 1: Logistic Regression (LR)italicized text:**"""

warnings.filterwarnings("ignore", category=ConvergenceWarning)

model = LogisticRegression()
model.fit(X_train, y_train)

lr_prediction = model.predict(X_test)
accuracy = metrics.accuracy_score(lr_prediction, y_test)
final_val = accuracy * 100

print('Logistic Regression accuracy = {:.2f}'.format(final_val))

"""#**Model 2: Support Vector Machine (SVM):**"""

model = svm.SVC()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
svc_prediction = model.predict(X_test)
accuracy = metrics.accuracy_score(svc_prediction, y_test)

print('SVM accuracy = {:.2f}'.format(accuracy * 100))

"""#**Model 3: Decision Tree**:"""

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
dt_prediction = model.predict(X_test)
accuracy = metrics.accuracy_score(dt_prediction, y_test)

print('Decision Tree accuracy = {:.2f}'.format(accuracy * 100))

"""#**Model 4: K-Nearest Neighbors (KNN):**"""

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create KNN model
model = KNeighborsClassifier()

# Make predictions and evaluate the model
knn_prediction = final_model.predict(X_test_scaled)
accuracy = metrics.accuracy_score(knn_prediction, y_test)

print('KNN accuracy = {:.2f}'.format(accuracy * 100))

"""
**CONCLUSION:**

The Loan Status is heavily dependent on the Credit

1.   The Loan Status is heavily dependent on the Credit History for Predictions.

2.   The Logistic Regression algorithm gives us the maximum Accuracy (81% approx) compared to the other 3 Machine Learning Classification Algorithms.
"""

