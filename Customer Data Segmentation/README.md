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

