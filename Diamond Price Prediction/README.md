# Diamond Price Prediction: 
# Predicting the price of a diamond based on its characteristics

## Dataset description and visualization

[Diamonds](https://www.kaggle.com/datasets/shivam2503/diamonds/)

<table>
  <thead>
    <tr>
      <th>carat</th>
      <th>cut</th>
      <th>color</th>
      <th>clarity</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.23</td>
      <td>Ideal</td>
      <td>E</td>
      <td>SI2</td>
      <td>61.5</td>
      <td>55.0</td>
      <td>326</td>
      <td>3.95</td>
      <td>3.98</td>
      <td>2.43</td>
    </tr>
    <tr>
      <td>0.21</td>
      <td>Premium</td>
      <td>E</td>
      <td>SI1</td>
      <td>59.8</td>
      <td>61.0</td>
      <td>326</td>
      <td>3.89</td>
      <td>3.84</td>
      <td>2.31</td>
    </tr>
    <tr>
      <td>0.23</td>
      <td>Good</td>
      <td>E</td>
      <td>VS1</td>
      <td>56.9</td>
      <td>65.0</td>
      <td>327</td>
      <td>4.05</td>
      <td>4.07</td>
      <td>2.31</td>
    </tr>
    <tr>
      <td>0.29</td>
      <td>Premium</td>
      <td>I</td>
      <td>VS2</td>
      <td>62.4</td>
      <td>58.0</td>
      <td>334</td>
      <td>4.20</td>
      <td>4.23</td>
      <td>2.63</td>
    </tr>
    <tr>
      <td>0.31</td>
      <td>Good</td>
      <td>J</td>
      <td>SI2</td>
      <td>63.3</td>
      <td>58.0</td>
      <td>335</td>
      <td>4.34</td>
      <td>4.35</td>
      <td>2.75</td>
    </tr>
  </tbody>
</table>

***price:*** price in US dollars (\$326--\$18,823)

***carat:*** weight of the diamond (0.2--5.01)

***cut:*** quality of the cut (Fair, Good, Very Good, Premium, Ideal)

***color:*** diamond color, from J (worst) to D (best)

***clarity:*** a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))

***x:*** length in mm (0--10.74)

***y:*** width in mm (0--58.9)

***z:*** depth in mm (0--31.8)

***table:*** width of the top of the diamond relative to widest point (43--95)

***depth:*** total depth percentage = z / mean(x, y) = 2 * z / (x + y)  (43--79)

![diamond-14](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/6adc78fa-b160-4d7f-a156-024531782d11)

![Data Visualization](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/6038175a-32cf-456a-9a46-49c019fe5170)

## Numerical features descriptive statistics

<table border="1">
  <tr>
    <th></th>
    <th>carat</th>
    <th>depth</th>
    <th>table</th>
    <th>price</th>
    <th>x</th>
    <th>y</th>
    <th>z</th>
  </tr>
  <tr>
    <td>count</td>
    <td>53940.000000</td>
    <td>53940.000000</td>
    <td>53940.000000</td>
    <td>53940.000000</td>
    <td>53940.000000</td>
    <td>53940.000000</td>
    <td>53940.000000</td>
  </tr>
  <tr>
    <td>mean</td>
    <td>0.797940</td>
    <td>61.749405</td>
    <td>57.457184</td>
    <td>3932.799722</td>
    <td>5.731157</td>
    <td>5.734526</td>
    <td>3.538734</td>
  </tr>
  <tr>
    <td>std</td>
    <td>0.474011</td>
    <td>1.432621</td>
    <td>2.234491</td>
    <td>3989.439738</td>
    <td>1.121761</td>
    <td>1.142135</td>
    <td>0.705699</td>
  </tr>
  <tr>
    <td>min</td>
    <td>0.200000</td>
    <td>43.000000</td>
    <td>43.000000</td>
    <td>326.000000</td>
    <td>0.000000</td>
    <td>0.000000</td>
    <td>0.000000</td>
  </tr>
  <tr>
    <td>25%</td>
    <td>0.400000</td>
    <td>61.000000</td>
    <td>56.000000</td>
    <td>950.000000</td>
    <td>4.710000</td>
    <td>4.720000</td>
    <td>2.910000</td>
  </tr>
  <tr>
    <td>50%</td>
    <td>0.700000</td>
    <td>61.800000</td>
    <td>57.000000</td>
    <td>2401.000000</td>
    <td>5.700000</td>
    <td>5.710000</td>
    <td>3.530000</td>
  </tr>
  <tr>
    <td>75%</td>
    <td>1.040000</td>
    <td>62.500000</td>
    <td>59.000000</td>
    <td>5324.250000</td>
    <td>6.540000</td>
    <td>6.540000</td>
    <td>4.040000</td>
  </tr>
  <tr>
    <td>max</td>
    <td>5.010000</td>
    <td>79.000000</td>
    <td>95.000000</td>
    <td>18823.000000</td>
    <td>10.740000</td>
    <td>58.900000</td>
    <td>31.800000</td>
  </tr>
</table>


## Label encoding of categorical features 

Ordinal encoding on [cut, color, clarity] based on their order which is mentioned in the dataset description 

<table>
  <thead>
    <tr>
      <th>carat</th>
      <th>cut</th>
      <th>color</th>
      <th>clarity</th>
      <th>depth</th>
      <th>table</th>
      <th>price</th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.23</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>61.5</td>
      <td>55.0</td>
      <td>326</td>
      <td>3.95</td>
      <td>3.98</td>
      <td>2.43</td>
    </tr>
    <tr>
      <td>0.21</td>
      <td>3</td>
      <td>5</td>
      <td>2</td>
      <td>59.8</td>
      <td>61.0</td>
      <td>326</td>
      <td>3.89</td>
      <td>3.84</td>
      <td>2.31</td>
    </tr>
    <tr>
      <td>0.23</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>56.9</td>
      <td>65.0</td>
      <td>327</td>
      <td>4.05</td>
      <td>4.07</td>
      <td>2.31</td>
    </tr>
    <tr>
      <td>0.29</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>62.4</td>
      <td>58.0</td>
      <td>334</td>
      <td>4.20</td>
      <td>4.23</td>
      <td>2.63</td>
    </tr>
    <tr>
      <td>0.31</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>63.3</td>
      <td>58.0</td>
      <td>335</td>
      <td>4.34</td>
      <td>4.35</td>
      <td>2.75</td>
    </tr>
  </tbody>
</table>

## Feature scaling for input features using MinMax scaler

<table>
  <thead>
    <tr>
      <th>carat</th>
      <th>cut</th>
      <th>color</th>
      <th>clarity</th>
      <th>depth</th>
      <th>table</th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.006237</td>
      <td>1.00</td>
      <td>0.833333</td>
      <td>0.142857</td>
      <td>0.513889</td>
      <td>0.230769</td>
      <td>0.367784</td>
      <td>0.067572</td>
      <td>0.076415</td>
    </tr>
    <tr>
      <td>0.002079</td>
      <td>0.75</td>
      <td>0.833333</td>
      <td>0.285714</td>
      <td>0.466667</td>
      <td>0.346154</td>
      <td>0.362197</td>
      <td>0.065195</td>
      <td>0.072642</td>
    </tr>
    <tr>
      <td>0.006237</td>
      <td>0.25</td>
      <td>0.833333</td>
      <td>0.571429</td>
      <td>0.386111</td>
      <td>0.423077</td>
      <td>0.377095</td>
      <td>0.069100</td>
      <td>0.072642</td>
    </tr>
    <tr>
      <td>0.018711</td>
      <td>0.75</td>
      <td>0.166667</td>
      <td>0.428571</td>
      <td>0.538889</td>
      <td>0.288462</td>
      <td>0.391061</td>
      <td>0.071817</td>
      <td>0.082704</td>
    </tr>
    <tr>
      <td>0.022869</td>
      <td>0.25</td>
      <td>0.000000</td>
      <td>0.142857</td>
      <td>0.563889</td>
      <td>0.288462</td>
      <td>0.404097</td>
      <td>0.073854</td>
      <td>0.086478</td>
    </tr>
  </tbody>
</table>

## Result comparison of fitting different regressors from the scikit-learn module

<table>
  <thead>
    <tr>
      <th>Regressor</th>
      <th>MSE</th>
      <th>MAE</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LinearRegression</td>
      <td>1492535.35</td>
      <td>811.16</td>
      <td>0.906150</td>
    </tr>
    <tr>
      <td>DecisionTreeRegressor</td>
      <td>561965.17</td>
      <td>359.68</td>
      <td>0.964664</td>
    </tr>
    <tr>
      <td>SVR</td>
      <td>11168952.50</td>
      <td>1920.16</td>
      <td>0.297698</td>
    </tr>
    <tr>
      <td>MLPRegressor</td>
      <td>1691029.00</td>
      <td>944.06</td>
      <td>0.893668</td>
    </tr>
    <tr>
      <td>RandomForestRegressor_n=50</td>
      <td>316868.40</td>
      <td>275.03</td>
      <td>0.980075</td>
    </tr>
    <tr>
      <td>RandomForestRegressor_n=100</td>
      <td>316820.58</td>
      <td>273.69</td>
      <td>0.980078</td>
    </tr>
    <tr>
      <td >RandomForestRegressor_n=150</td>
      <td>315192.45</td>
      <td>273.56</td>
      <td>0.980181</td>
    </tr>
    <tr>
      <td>RandomForestRegressor_n=200</td>
      <td>317126.84</td>
      <td>273.09</td>
      <td>0.980059</td>
    </tr>
    <tr>
      <td>RandomForestRegressor_n=250</td>
      <td>315197.28</td>
      <td>273.25</td>
      <td>0.980180</td>
    </tr>
    <tr>
      <td>RandomForestRegressor_n=300</td>
      <td>315874.12</td>
      <td>272.99</td>
      <td>0.980138</td>
    </tr>
    <tr>
      <td>KNeighborsRegressor_n=3</td>
      <td>533839.73</td>
      <td>374.70</td>
      <td>0.966432</td>
    </tr>
    <tr>
      <td>KNeighborsRegressor_n=5</td>
      <td>555840.27</td>
      <td>376.65</td>
      <td>0.965049</td>
    </tr>
    <tr>
      <td>KNeighborsRegressor_n=7</td>
      <td>560219.40</td>
      <td>376.96</td>
      <td>0.964773</td>
    </tr>
    <tr>
      <td>KNeighborsRegressor_n=9</td>
      <td>572656.57</td>
      <td>381.07</td>
      <td>0.963991</td>
    </tr>
    <tr>
      <td>KNeighborsRegressor_n=11</td>
      <td>585846.07</td>
      <td>387.10</td>
      <td>0.963162</td>
    </tr>
    <tr>
      <td>KNeighborsRegressor_n=13</td>
      <td>608806.14</td>
      <td>394.71</td>
      <td>0.961718</td>
    </tr>
  </tbody>
</table>



**Best results**
<table>
<tr>
      <td>RandomForestRegressor_n=150</td>
      <td>315192.45</td>
      <td>273.56</td>
      <td>0.980181</td>
    </tr>
</table>

## Model diagram

![flow diagram](https://github.com/mohdakrory/Machine-Learning-Practice/assets/67663339/7308a442-269d-4881-a198-a752769a7368)

## Kaggle notebook

[Diamond Price Prediction](https://www.kaggle.com/code/mohamedeldakrory8/diamond-price-prediction)
