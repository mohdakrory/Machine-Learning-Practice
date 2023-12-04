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

397 rows × 9 columns

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

## Clusters description and visualization

**Clusters descriptive statistics**

<table border="1">
  <tr>
    <th>cluster</th><th>count</th><th>mean_age</th><th>std_age</th><th>min_age</th><th>25%_age</th><th>50%_age</th><th>75%_age</th><th>max_age</th><th>count_income</th><th>mean_income</th><th>std_income</th><th>min_income</th><th>25%_income</th><th>50%_income</th><th>75%_income</th><th>max_income</th><th>count_spending_score</th><th>mean_spending_score</th><th>std_spending_score</th><th>min_spending_score</th><th>25%_spending_score</th><th>50%_spending_score</th><th>75%_spending_score</th><th>max_spending_score</th><th>count_website_visits</th><th>mean_website_visits</th><th>std_website_visits</th><th>min_website_visits</th><th>25%_website_visits</th><th>50%_website_visits</th><th>75%_website_visits</th><th>max_website_visits</th><th>count_loyalty_points</th><th>mean_loyalty_points</th><th>std_loyalty_points</th><th>min_loyalty_points</th><th>25%_loyalty_points</th><th>50%_loyalty_points</th><th>75%_loyalty_points</th><th>max_loyalty_points</th><th>count_gender_F</th><th>count_gender_M</th><th>count_education_Bachelor</th><th>count_education_Master</th><th>count_education_PhD</th><th>count_marital_status_Married</th><th>count_marital_status_Single</th><th>count_purchase_history_High</th><th>count_purchase_history_Low</th><th>count_purchase_history_Medium</th>
  </tr>
  <tr>
    <td>0</td><td>131</td><td>40.67938931</td><td>3.543720721</td><td>35</td><td>39</td><td>40</td><td>44</td><td>45</td><td>131</td><td>67900.76336</td><td>7455.359416</td><td>58000</td><td>60000</td><td>70000</td><td>72000</td><td>78000</td><td>131</td><td>68.16793893</td><td>5.090190675</td><td>60</td><td>65</td><td>70</td><td>70</td><td>75</td><td>131</td><td>10.01526718</td><td>1.116207403</td><td>8</td><td>9</td><td>10</td><td>10</td><td>12</td><td>131</td><td>131.221374</td><td>22.15410713</td><td>100</td><td>110</td><td>140</td><td>140</td><td>180</td><td>26</td><td>105</td><td>51</td><td>80</td><td>0</td><td>130</td><td>1</td><td>131</td><td>0</td><td>0</td>
  </tr>
  <tr>
    <td>1</td><td>79</td><td>31.02531646</td><td>1.768489748</td><td>27</td><td>29</td><td>31</td><td>33</td><td>35</td><td>79</td><td>52670.88608</td><td>3433.326558</td><td>48000</td><td>48000</td><td>55000</td><td>55000</td><td>60000</td><td>79</td><td>45.17721519</td><td>5.286071426</td><td>38</td><td>38</td><td>48</td><td>50</td><td>50</td><td>79</td><td>5</td><td>1.664100589</td><td>3</td><td>3</td><td>5</td><td>7</td><td>7</td><td>79</td><td>53.03797468</td><td>17.27265739</td><td>30</td><td>30</td><td>60</td><td>70</td><td>70</td><td>79</td><td>0</td><td>0</td><td>79</td><td>0</td><td>1</td><td>78</td><td>0</td><td>27</td><td>52</td>
  </tr>
  <tr>
    <td>2</td><td>78</td><td>48.02564103</td><td>2.233012984</td><td>45</td><td>46</td><td>47</td><td>51</td><td>53</td><td>78</td><td>85064.10256</td><td>4225.278731</td><td>80000</td><td>80000</td><td>85000</td><td>90000</td><td>95000</td><td>78</td><td>85.06410256</td><td>4.160231461</td><td>80</td><td>80</td><td>85</td><td>90</td><td>92</td><td>78</td><td>17.38461538</td><td>2.14555275</td><td>15</td><td>15</td><td>17</td><td>20</td><td>23</td><td>78</td><td>242.9487179</td><td>29.1484768</td><td>200</td><td>210</td><td>240</td><td>280</td><td>280</td><td>78</td><td>0</td><td>0</td><td>0</td><td>78</td><td>78</td><td>0</td><td>78</td><td>0</td><td>0</td>
  </tr>
  <tr>
    <td>3</td><td>82</td><td>30.86585366</td><td>4.033079867</td><td>25</td><td>26</td><td>31</td><td>36</td><td>36</td><td>82</td><td>50414.63415</td><td>4294.559347</td><td>40000</td><td>45000</td><td>52000</td><td>55000</td><td>55000</td><td>82</td><td>47.58536585</td><td>5.29138881</td><td>35</td><td>42</td><td>48</td><td>52</td><td>70</td><td>82</td><td>5.329268293</td><td>1.100559656</td><td>3</td><td>4</td><td>6</td><td>6</td><td>10</td><td>82</td><td>69.20731707</td><td>16.31990212</td><td>20</td><td>50</td><td>75</td><td>85</td><td>100</td><td>31</td><td>51</td><td>82</td><td>0</td><td>0</td><td>1</td><td>81</td><td>1</td><td>28</td><td>53</td>
  </tr>
  <tr>
    <td>4</td><td>27</td><td>53.11111111</td><td>1.050030525</td><td>50</td><td>53</td><td>53</td><td>53</td><td>57</td><td>27</td><td>109259.2593</td><td>4744.167209</td><td>90000</td><td>110000</td><td>110000</td><td>110000</td><td>120000</td><td>27</td><td>94.92592593</td><td>1.141049649</td><td>90</td><td>95</td><td>95</td><td>95</td><td>98</td><td>27</td><td>27.66666667</td><td>1.687054785</td><td>20</td><td>28</td><td>28</td><td>28</td><td>30</td><td>27</td><td>344.4444444</td><td>21.18296364</td><td>250</td><td>350</td><td>350</td><td>350</td><td>350</td><td>0</td><td>27</td><td>0</td><td>0</td><td>27</td><td>26</td><td>1</td><td>27</td><td>0</td><td>0</td>
  </tr>
</table>

**Clusters visualization**

![Cluster_ 0 Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/26c3d40b-b360-4f63-84d7-682adf725ab4)

![Cluster_ 1 Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/595b6d8c-d96c-41d8-9a96-06be5cb8ee06)

![Cluster_ 2 Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/f7a78d69-d661-4727-b0a2-d49e44d2e576)

![Cluster_ 3 Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/51662cba-7796-4634-acc4-051a2927197f)

![Cluster_ 4 Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/b3276914-d980-499a-a683-3464ae8638ab)

## Model diagram

![diagram](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/f303c067-96fb-44db-84f0-9575cef66fe3)

## Kaggle notebook

[Notebook](https://www.kaggle.com/code/mohamedeldakrory8/customer-segmentation-for-personalized-marketing)
