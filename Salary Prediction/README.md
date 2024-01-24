# Salary Prediction

Predict the salary of an employee based on some relevant information using Python, Scikit-learn, Matplotlib, Seaborn, and Pandas

## Dataset description

<table border="1">
  <tr>
    <th>Column</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>FIRST NAME</td>
    <td>The first name of the employee.</td>
  </tr>
  <tr>
    <td>LAST NAME</td>
    <td>The last name of the employee.</td>
  </tr>
  <tr>
    <td>SEX</td>
    <td>The gender of the employee (F for female, M for male).</td>
  </tr>
  <tr>
    <td>DOJ</td>
    <td>Date of Joining - The date when the employee joined the company.</td>
  </tr>
  <tr>
    <td>CURRENT DATE</td>
    <td>The current date or the date for which the data is recorded.</td>
  </tr>
  <tr>
    <td>DESIGNATION</td>
    <td>The job title or position of the employee within the company.</td>
  </tr>
  <tr>
    <td>AGE</td>
    <td>The age of the employee.</td>
  </tr>
  <tr>
    <td>SALARY</td>
    <td>The salary of the employee (target variable for prediction).</td>
  </tr>
  <tr>
    <td>UNIT</td>
    <td>The department or unit to which the employee belongs.</td>
  </tr>
  <tr>
    <td>LEAVES USED</td>
    <td>The number of leaves (days of) the employee has used.</td>
  </tr>
  <tr>
    <td>LEAVES REMAINING</td>
    <td>The number of leaves the employee has remaining.</td>
  </tr>
  <tr>
    <td>RATINGS</td>
    <td>Ratings given to the employee.</td>
  </tr>
  <tr>
    <td>PAST EXP</td>
    <td>The past work experience of the employee before joining the company.</td>
  </tr>
</table>

## Notebook content list


**This notebook contains the following topics**


---------------------------------------------
### 1 Dataset description 
---------------------------------------------
#### 1.1 Load data & preview
#### 1.2 Column description
#### 1.3 Dropping unnecessary columns
---------------------------------------------
### 2 Exploratory data analysis
---------------------------------------------
#### 2.1 Missing values
#### 2.2 Data types
#### 2.3 Unique values of each column
#### 2.4 Value count of categorical features
#### 2.5 Count plot of categorical features
#### 2.6 SEX vs SALARY stats
#### 2.7 DESIGNATION vs SALARY stats
#### 2.8 UNIT vs SALARY stats
#### 2.9 Box plot of categorical features VS SALARY
#### 2.10 Descriptive statistics of numeric variables
#### 2.11 value count of discrete numeric features
#### 2.12 Count plot of discrete numeric features
#### 2.13 PAST EXP vs SALARY stats
#### 2.14 RATINGS vs SALARY stats
#### 2.15 AGE vs SALARY stats
#### 2.16 box plot of discrete numeric features VS SALARY
#### 2.17 SALARY distribution
#### 2.18 Correlation heatmap
#### 2.19 Pair plot
#### 2.20 Pandas profile report
---------------------------------------------
### 3 Feature Engineering & Preprocessing
---------------------------------------------
#############################################
#### 3.1 Missing values
##### 3.1.1 Missing values in the 'DOJ' column
##### 3.1.2 Missing values in 'AGE' column
##### 3.1.3 Imputing missing values in 'LEAVES USED' & 'LEAVES REMAINING'
##### 3.1.4 Imputing missing values in 'RATINGS'
#############################################
#### 3.2 Driving new variables
##### 3.2.1 DURATION variable
##### 3.2.2 Correlation between DURATION and SALARY
##### 3.2.3 'DURATION' descriptive stats
#############################################
#### 3.3 Feature encoding
##### 3.3.1 Label encoding of 'SEX'
##### 3.3.2 Ordinal encoding of 'DESIGNATION'
##### 3.3.3 One-hot encoding of 'UNIT'
#############################################
### 3.4 Imputation of 'RATING' using KNN Imputer
#############################################
### 3.5 Train-test split (0.8 : 0.2)


---------------------------------------------
### 4 Regression model development & Evaluation
---------------------------------------------
#### 4.1 Fitting different regressors with all features
#### 4.2 Best performing model
#### 4.3 Fitting the best performing model on highly correlated features
#### 4.4 Saving the best model
---------------------------------------------
### 5 Pipeline diagram
---------------------------------------------
### 6 Deployment code
---------------------------------------------

## PyQt5 GUI Demo

![Demo](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/6368fa8d-36af-4ad1-a3eb-837cb68f575d)

