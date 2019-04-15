# Election Violence Prediction
<p align="center">
<img src="assets/ada.png" width="300">
</p>
<p>
CSE635 Project.
</p>


## TODO list

* Try CatBoost / XGBoost / Neural nets (CNN/ LSTM/ DNN)
* Add hate speech & violent speech detection
* Do lit survey for more features
  * Go back to Terra Blevins paper maybe?

## Current Twitter Results
|      Location      |   Train Accuracy |   Test Accuracy |   Precision |   Recall |   F1 Score |   % of +'s in data |
|:------------------:|-----------------:|----------------:|------------:|---------:|-----------:|-------------------:|
|      Agartala      |             0.97 |            0.5  |        0.5  |     1    |       0.67 |              71.11 |
|     Ahmedabad      |             0.91 |            0.83 |        0    |     0    |       0    |              42.22 |
|      Amritsar      |             1    |            0.58 |        0.58 |     1    |       0.74 |              88.89 |
|      Bathinda      |             1    |            0.17 |        0.17 |     1    |       0.29 |              77.78 |
|     Bengaluru      |             1    |            0.5  |        0.5  |     1    |       0.67 |              77.78 |
|     Chandigarh     |             1    |            0.08 |        0.08 |     1    |       0.15 |              73.33 |
|      Chennai       |             1    |            0.08 |        0.08 |     1    |       0.15 |              75.56 |
|     Coimbatore     |             0.94 |            0.42 |        0.42 |     1    |       0.59 |              75.56 |
|      Dehradun      |             1    |            1    |        0    |     0    |       0    |              26.67 |
|  Delhi-New Delhi   |             1    |            0.67 |        0.67 |     1    |       0.8  |              88.89 |
|      Gurgaon       |             1    |            0.5  |        0    |     0    |       0    |              22.22 |
|      Guwahati      |             0.94 |            0.08 |        0.08 |     1    |       0.15 |              71.11 |
|     Hyderabad      |             0.94 |            0.5  |        0.5  |     1    |       0.67 |              82.22 |
|       Imphal       |             0.97 |            0.08 |        0.08 |     1    |       0.15 |              60    |
|       Jaipur       |             0.88 |            0.58 |        0    |     0    |       0    |              24.44 |
|     Jalandhar      |             0.97 |            0.33 |        0.33 |     1    |       0.5  |              53.33 |
|       Jammu        |             1    |            0.67 |        0.67 |     1    |       0.8  |              91.11 |
|       Karnal       |             0.94 |            0.42 |        0.42 |     1    |       0.59 |              44.44 |
|      Kolkata       |             1    |            0.5  |        0.5  |     1    |       0.67 |              86.67 |
|      Lucknow       |             0.97 |            1    |        0    |     0    |       0    |              51.11 |
|      Ludhiana      |             0.97 |            0.58 |        0.58 |     1    |       0.74 |              84.44 |
|      Madurai       |             1    |            1    |        0    |     0    |       0    |              44.44 |
|      Patiala       |             1    |            0.42 |        0    |     0    |       0    |              66.67 |
|       Patna        |             0.76 |            0.5  |        0.5  |     1    |       0.67 |              44.44 |
|     Puducherry     |             1    |            0    |        0    |     0    |       0    |              73.33 |
|      Pulwama       |             0.94 |            0    |        0    |     0    |       0    |              46.67 |
|       Ranchi       |             0.61 |            1    |        0    |     0    |       0    |              40    |
|       Salem        |             0.97 |            0.67 |        0    |     0    |       0    |              53.33 |
|      Sangrur       |             1    |            1    |        0    |     0    |       0    |              48.89 |
|       Shimla       |             0.67 |            1    |        0    |     0    |       0    |              24.44 |
|      Srinagar      |             1    |            0.58 |        0.58 |     1    |       0.74 |              88.89 |
| Thiruvananthapuram |             1    |            0.25 |        0.25 |     1    |       0.4  |              75.56 |
|  Tiruchirappalli   |             1    |            1    |        0    |     0    |       0    |              33.33 |
|      Average       |             0.95 |            0.53 |        0.23 |     0.58 |       0.31 |              60.87 
