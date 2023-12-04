# Customer Data Segmentation

Divide customer data into 5 clusters for personalized marketing purposes

## Dataset description and visualization

[Customer_Data_Clustering](https://www.kaggle.com/datasets/mohamedeldakrory8/customer-clustering/)

**Samples from the dataset**

<table border="1">
  <tr>
    <th>customer_id</th>
    <th>age</th>
    <th>gender</th>
    <th>income</th>
    <th>education</th>
    <th>marital_status</th>
    <th>spending_score</th>
    <th>purchase_history</th>
    <th>website_visits</th>
    <th>loyalty_points</th>
  </tr>
  <tr>
    <td>1</td>
    <td>25</td>
    <td>M</td>
    <td>50000</td>
    <td>Bachelor</td>
    <td>Single</td>
    <td>70</td>
    <td>High</td>
    <td>10</td>
    <td>100</td>
  </tr>
  <tr>
    <td>2</td>
    <td>35</td>
    <td>F</td>
    <td>60000</td>
    <td>Master</td>
    <td>Married</td>
    <td>50</td>
    <td>Medium</td>
    <td>5</td>
    <td>50</td>
  </tr>
  <tr>
    <td>3</td>
    <td>45</td>
    <td>F</td>
    <td>80000</td>
    <td>PhD</td>
    <td>Married</td>
    <td>80</td>
    <td>High</td>
    <td>15</td>
    <td>200</td>
  </tr>
  <tr>
    <td>4</td>
    <td>40</td>
    <td>M</td>
    <td>70000</td>
    <td>Master</td>
    <td>Single</td>
    <td>65</td>
    <td>High</td>
    <td>8</td>
    <td>150</td>
  </tr>
  <tr>
    <td>5</td>
    <td>30</td>
    <td>F</td>
    <td>40000</td>
    <td>Bachelor</td>
    <td>Single</td>
    <td>35</td>
    <td>Low</td>
    <td>3</td>
    <td>20</td>
  </tr>
</table>

**Data visualization**
![Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/46462675-5c6c-4b04-b695-e21c5d4f4e5f)

**Numerical data descriptive statistics**

<table border="1">
  <tr>
    <th></th>
    <th>age</th>
    <th>income</th>
    <th>spending_score</th>
    <th>website_visits</th>
    <th>loyalty_points</th>
  </tr>
  <tr>
    <td>count</td>
    <td>397</td>
    <td>397</td>
    <td>397</td>
    <td>397</td>
    <td>397</td>
  </tr>
  <tr>
    <td>mean</td>
    <td>39.02015113</td>
    <td>67443.32494</td>
    <td>64.48110831</td>
    <td>10.697733</td>
    <td>139.3073048</td>
  </tr>
  <tr>
    <td>std</td>
    <td>8.127121136</td>
    <td>17700.79428</td>
    <td>17.54367626</td>
    <td>6.581986429</td>
    <td>89.31889454</td>
  </tr>
  <tr>
    <td>min</td>
    <td>25</td>
    <td>40000</td>
    <td>35</td>
    <td>3</td>
    <td>20</td>
  </tr>
  <tr>
    <td>25%</td>
    <td>31</td>
    <td>55000</td>
    <td>48</td>
    <td>6</td>
    <td>70</td>
  </tr>
  <tr>
    <td>50%</td>
    <td>39</td>
    <td>60000</td>
    <td>65</td>
    <td>9</td>
    <td>110</td>
  </tr>
  <tr>
    <td>75%</td>
    <td>46</td>
    <td>80000</td>
    <td>80</td>
    <td>15</td>
    <td>210</td>
  </tr>
  <tr>
    <td>max</td>
    <td>57</td>
    <td>120000</td>
    <td>98</td>
    <td>30</td>
    <td>350</td>
  </tr>
</table>

## Label encoding of categorical features

**Ordinal encoding of [gender,	marital_status, purchase_history]**

purchase_history_label_mapping = {
    'Low': 0,
    'Medium': 1,
    'High': 2
}

gender_label_mapping = {
    'F': 0,
    'M': 1
}

marital_status_label_mapping = {
    'Single': 0,
    'Married': 1
}

**One-hot encoding of [education]**

Mapping table

<table border="1">
  <tr>
    <th>category</th>
    <th>is_master</th>
    <th>is_phd</th>
  </tr>
  <tr>
    <td>bachelor</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>master</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>phd</td>
    <td>0</td>
    <td>1</td>
  </tr>
</table>

These 3 categories were mapped into 2 columns to avoid the dummy variable trap

<table border="1">
  <tr>
    <th>age</th>
    <th>gender</th>
    <th>income</th>
    <th>marital_status</th>
    <th>spending_score</th>
    <th>purchase_history</th>
    <th>website_visits</th>
    <th>loyalty_points</th>
    <th>is_master</th>
    <th>is_phd</th>
  </tr>
  <tr>
    <td>25</td>
    <td>1</td>
    <td>50000</td>
    <td>0</td>
    <td>70</td>
    <td>2</td>
    <td>10</td>
    <td>100</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>35</td>
    <td>0</td>
    <td>60000</td>
    <td>1</td>
    <td>50</td>
    <td>1</td>
    <td>5</td>
    <td>50</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>45</td>
    <td>0</td>
    <td>80000</td>
    <td>1</td>
    <td>80</td>
    <td>2</td>
    <td>15</td>
    <td>200</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>40</td>
    <td>1</td>
    <td>70000</td>
    <td>0</td>
    <td>65</td>
    <td>2</td>
    <td>8</td>
    <td>150</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>30</td>
    <td>0</td>
    <td>40000</td>
    <td>0</td>
    <td>35</td>
    <td>0</td>
    <td>3</td>
    <td>20</td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>

## Feature scaling using Standard Scaler 

<table border="1">
  <tr>
    <th>age</th>
    <th>gender</th>
    <th>income</th>
    <th>marital_status</th>
    <th>spending_score</th>
    <th>purchase_history</th>
    <th>website_visits</th>
    <th>loyalty_points</th>
    <th>is_master</th>
    <th>is_phd</th>
  </tr>
  <tr>
    <td>-1.727283</td>
    <td>1.081387</td>
    <td>-0.986698</td>
    <td>-1.210718</td>
    <td>0.314977</td>
    <td>0.747177</td>
    <td>-0.106140</td>
    <td>-0.440634</td>
    <td>-0.817354</td>
    <td>-0.599657</td>
  </tr>
  <tr>
    <td>-0.495283</td>
    <td>-0.924738</td>
    <td>-0.421039</td>
    <td>0.825956</td>
    <td>-0.826473</td>
    <td>-0.632494</td>
    <td>-0.866748</td>
    <td>-1.001132</td>
    <td>1.223460</td>
    <td>-0.599657</td>
  </tr>
  <tr>
    <td>0.736718</td>
    <td>-0.924738</td>
    <td>0.710280</td>
    <td>0.825956</td>
    <td>0.885702</td>
    <td>0.747177</td>
    <td>0.654467</td>
    <td>0.680363</td>
    <td>-0.817354</td>
    <td>1.667619</td>
  </tr>
  <tr>
    <td>0.120717</td>
    <td>1.081387</td>
    <td>0.144621</td>
    <td>-1.210718</td>
    <td>0.029614</td>
    <td>0.747177</td>
    <td>-0.410383</td>
    <td>0.119865</td>
    <td>1.223460</td>
    <td>-0.599657</td>
  </tr>
  <tr>
    <td>-1.111283</td>
    <td>-0.924738</td>
    <td>-1.552357</td>
    <td>-1.210718</td>
    <td>-1.682561</td>
    <td>-2.012164</td>
    <td>-1.170991</td>
    <td>-1.337431</td>
    <td>-0.817354</td>
    <td>-0.599657</td>
  </tr>
</table>

## Fitting the K-means algorithm to get 5 clusters

Silhouette Score: 0.5981532592652027

**clusters count**

<table border="1">
  <tr>
    <th>Cluster</th>
    <th>Count</th>
  </tr>
  <tr>
    <td>0</td>
    <td>131</td>
  </tr>
  <tr>
    <td>3</td>
    <td>82</td>
  </tr>
  <tr>
    <td>1</td>
    <td>79</td>
  </tr>
  <tr>
    <td>2</td>
    <td>78</td>
  </tr>
  <tr>
    <td>4</td>
    <td>27</td>
  </tr>
</table>

