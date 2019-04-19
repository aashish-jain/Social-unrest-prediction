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
|  Delhi-New Delhi   |             0.97 |            0.82 |        0.82 |     1    |       0.9  |          0.93 |
|       Jammu        |             1    |            0.82 |        0.82 |     1    |       0.9  |          0.95 |
|      Amritsar      |             1    |            0.73 |        0.73 |     1    |       0.84 |          0.93 |
|      Ludhiana      |             0.94 |            0.73 |        0.73 |     1    |       0.84 |          0.88 |
|      Srinagar      |             1    |            0.73 |        0.73 |     1    |       0.84 |          0.93 |
|     Bengaluru      |             0.97 |            0.64 |        0.64 |     1    |       0.78 |          0.81 |
|     Hyderabad      |             0.94 |            0.64 |        0.64 |     1    |       0.78 |          0.86 |
|      Kolkata       |             1    |            0.64 |        0.64 |     1    |       0.78 |          0.91 |
|    Bhubaneswar     |             0.94 |            0.55 |        0.55 |     1    |       0.71 |          0.84 |
|       Patna        |             0.94 |            0.55 |        0.6  |     0.86 |       0.71 |          0.47 |
|      Agartala      |             1    |            0.55 |        0.62 |     0.71 |       0.67 |          0.74 |
|     Coimbatore     |             0.94 |            0.55 |        0.5  |     1    |       0.67 |          0.79 |
|     Ahmedabad      |             1    |            0.73 |        0.5  |     0.67 |       0.57 |          0.44 |
| Thiruvananthapuram |             0.94 |            0.36 |        0.36 |     1    |       0.53 |          0.79 |
|     Jalandhar      |             1    |            0.36 |        0.38 |     0.6  |       0.46 |          0.56 |
|      Bathinda      |             1    |            0.27 |        0.27 |     1    |       0.43 |          0.81 |
|       Karnal       |             1    |            0.27 |        0.29 |     0.4  |       0.33 |          0.47 |
|     Chandigarh     |             0.97 |            0.18 |        0.18 |     1    |       0.31 |          0.77 |
|      Chennai       |             1    |            0.18 |        0.18 |     1    |       0.31 |          0.79 |
|      Guwahati      |             0.94 |            0.18 |        0.18 |     1    |       0.31 |          0.74 |
|       Imphal       |             0.97 |            0.18 |        0.18 |     1    |       0.31 |          0.63 |
|      Patiala       |             1    |            0.45 |        1    |     0.14 |       0.25 |          0.7  |
|     Puducherry     |             1    |            0.09 |        0.09 |     1    |       0.17 |          0.77 |
|      Dehradun      |             0.97 |            1    |        0    |     0    |       0    |          0.28 |
|      Gurgaon       |             0.97 |            0.45 |        0    |     0    |       0    |          0.23 |
|       Jaipur       |             0.84 |            0.55 |        0    |     0    |       0    |          0.26 |
|      Lucknow       |             0.97 |            0.45 |        0    |     0    |       0    |          0.53 |
|      Madurai       |             1    |            1    |        0    |     0    |       0    |          0.47 |
|      Pulwama       |             1    |            0    |        0    |     0    |       0    |          0.49 |
|       Ranchi       |             0.84 |            0.91 |        0    |     0    |       0    |          0.42 |
|       Salem        |             1    |            0.55 |        0    |     0    |       0    |          0.56 |
|      Sangrur       |             1    |            0.91 |        0    |     0    |       0    |          0.51 |
|       Shimla       |             0.78 |            0.27 |        0    |     0    |       0    |          0.26 |
|  Tiruchirappalli   |             1    |            1    |        0    |     0    |       0    |          0.35 |
|      Average       |             0.97 |            0.54 |        0.34 |     0.6  |       0.39 |          0.64 |
