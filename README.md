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
|      Dehradun      |             1    |            1    |        1    |     1    |       1    |          0.28 |
|      Lucknow       |             0.94 |            1    |        1    |     1    |       1    |          0.53 |
|      Madurai       |             0.97 |            1    |        1    |     1    |       1    |          0.47 |
|      Sangrur       |             1    |            1    |        1    |     1    |       1    |          0.51 |
|       Shimla       |             0.66 |            1    |        1    |     1    |       1    |          0.26 |
|  Tiruchirappalli   |             1    |            1    |        1    |     1    |       1    |          0.35 |
|  Delhi-New Delhi   |             0.97 |            0.82 |        0.82 |     1    |       0.9  |          0.93 |
|       Jammu        |             1    |            0.82 |        0.82 |     1    |       0.9  |          0.95 |
|     Ahmedabad      |             0.94 |            0.73 |        0.73 |     1    |       0.84 |          0.44 |
|      Amritsar      |             1    |            0.73 |        0.73 |     1    |       0.84 |          0.93 |
|      Ludhiana      |             0.94 |            0.73 |        0.73 |     1    |       0.84 |          0.88 |
|      Srinagar      |             1    |            0.73 |        0.73 |     1    |       0.84 |          0.93 |
|      Agartala      |             0.97 |            0.64 |        0.64 |     1    |       0.78 |          0.74 |
|     Bengaluru      |             0.97 |            0.64 |        0.64 |     1    |       0.78 |          0.81 |
|     Hyderabad      |             0.94 |            0.64 |        0.64 |     1    |       0.78 |          0.86 |
|      Kolkata       |             1    |            0.64 |        0.64 |     1    |       0.78 |          0.91 |
|       Patna        |             0.72 |            0.64 |        0.64 |     1    |       0.78 |          0.47 |
|       Jaipur       |             0.84 |            0.55 |        0.55 |     1    |       0.71 |          0.26 |
|       Salem        |             1    |            0.55 |        0.55 |     1    |       0.71 |          0.56 |
|     Coimbatore     |             0.94 |            0.45 |        0.45 |     1    |       0.62 |          0.79 |
|      Gurgaon       |             0.97 |            0.45 |        0.45 |     1    |       0.62 |          0.23 |
|     Jalandhar      |             0.97 |            0.45 |        0.45 |     1    |       0.62 |          0.56 |
|       Karnal       |             0.94 |            0.45 |        0.45 |     1    |       0.62 |          0.47 |
|      Patiala       |             0.97 |            0.36 |        0.36 |     1    |       0.53 |          0.7  |
| Thiruvananthapuram |             0.94 |            0.36 |        0.36 |     1    |       0.53 |          0.79 |
|      Bathinda      |             1    |            0.27 |        0.27 |     1    |       0.43 |          0.81 |
|     Chandigarh     |             0.97 |            0.18 |        0.18 |     1    |       0.31 |          0.77 |
|      Chennai       |             1    |            0.18 |        0.18 |     1    |       0.31 |          0.79 |
|      Guwahati      |             0.94 |            0.18 |        0.18 |     1    |       0.31 |          0.74 |
|       Imphal       |             0.97 |            0.18 |        0.18 |     1    |       0.31 |          0.63 |
|     Puducherry     |             1    |            0.09 |        0.09 |     1    |       0.17 |          0.77 |
|      Pulwama       |             0.97 |            0    |        0    |     0    |       0    |          0.49 |
|       Ranchi       |             0.59 |            0    |        0    |     0    |       0    |          0.42 |
|      Average       |             0.94 |            0.56 |        0.56 |     0.94 |       0.66 |          0.64 |
