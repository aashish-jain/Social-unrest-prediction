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
|      Location      |   Train Accuracy |   Test Accuracy |   Precision |   Recall |   F1 Score |   +'s in data |
|:------------------:|-----------------:|----------------:|------------:|---------:|-----------:|--------------:|
|      Agartala      |             0.97 |            0.5  |        0.5  |     1    |       0.67 |          0.71 |
|     Ahmedabad      |             0.91 |            0.83 |        0.83 |     1    |       0.91 |          0.42 |
|      Amritsar      |             1    |            0.58 |        0.58 |     1    |       0.74 |          0.89 |
|      Bathinda      |             1    |            0.17 |        0.17 |     1    |       0.29 |          0.78 |
|     Bengaluru      |             1    |            0.5  |        0.5  |     1    |       0.67 |          0.78 |
|     Chandigarh     |             1    |            0.08 |        0.08 |     1    |       0.15 |          0.73 |
|      Chennai       |             1    |            0.08 |        0.08 |     1    |       0.15 |          0.76 |
|     Coimbatore     |             0.94 |            0.42 |        0.42 |     1    |       0.59 |          0.76 |
|      Dehradun      |             1    |            1    |        1    |     1    |       1    |          0.27 |
|  Delhi-New Delhi   |             1    |            0.67 |        0.67 |     1    |       0.8  |          0.89 |
|      Gurgaon       |             1    |            0.5  |        0.5  |     1    |       0.67 |          0.22 |
|      Guwahati      |             0.94 |            0.08 |        0.08 |     1    |       0.15 |          0.71 |
|     Hyderabad      |             0.94 |            0.5  |        0.5  |     1    |       0.67 |          0.82 |
|       Imphal       |             0.97 |            0.08 |        0.08 |     1    |       0.15 |          0.6  |
|       Jaipur       |             0.88 |            0.58 |        0.58 |     1    |       0.74 |          0.24 |
|     Jalandhar      |             0.97 |            0.33 |        0.33 |     1    |       0.5  |          0.53 |
|       Jammu        |             1    |            0.67 |        0.67 |     1    |       0.8  |          0.91 |
|       Karnal       |             0.94 |            0.42 |        0.42 |     1    |       0.59 |          0.44 |
|      Kolkata       |             1    |            0.5  |        0.5  |     1    |       0.67 |          0.87 |
|      Lucknow       |             0.97 |            1    |        1    |     1    |       1    |          0.51 |
|      Ludhiana      |             0.97 |            0.58 |        0.58 |     1    |       0.74 |          0.84 |
|      Madurai       |             1    |            1    |        1    |     1    |       1    |          0.44 |
|      Patiala       |             1    |            0.42 |        0.42 |     1    |       0.59 |          0.67 |
|       Patna        |             0.76 |            0.5  |        0.5  |     1    |       0.67 |          0.44 |
|     Puducherry     |             1    |            0    |        0    |     0    |       0    |          0.73 |
|      Pulwama       |             0.94 |            0    |        0    |     0    |       0    |          0.47 |
|       Ranchi       |             0.61 |            1    |        1    |     1    |       1    |          0.4  |
|       Salem        |             0.97 |            0.67 |        0.67 |     1    |       0.8  |          0.53 |
|      Sangrur       |             1    |            1    |        1    |     1    |       1    |          0.49 |
|       Shimla       |             0.67 |            1    |        1    |     1    |       1    |          0.24 |
|      Srinagar      |             1    |            0.58 |        0.58 |     1    |       0.74 |          0.89 |
| Thiruvananthapuram |             1    |            0.25 |        0.25 |     1    |       0.4  |          0.76 |
|  Tiruchirappalli   |             1    |            1    |        1    |     1    |       1    |          0.33 |
|      Average       |             0.95 |            0.53 |        0.53 |     0.94 |       0.63 |          0.61 |
