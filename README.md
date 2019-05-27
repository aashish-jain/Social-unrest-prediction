# Election Violence Prediction
<p align="center">
<img src="assets/ada.png" width="300">
</p>

This repository consists of code for the CSE 635 project developed by [Aashish Jain](https://github.com/aashish-jain), [Ateendra Ramesh](https://github.com/ateexd) and [Daniel Amirtharaj](https://github.com/dani-amirtharaj).


Data Collection:

* TOI data collection:
 To collect the TOI dataset follow the steps given below:
	1. Open TOI/TOI_Scrapper.ipynb using jupyter notebook.
	2. Enter the start_date and end_date for which article has to be scrapped
	3. Run all the cells to download the TOI news articles.
	4. This process can be automated to scrape articles everyday using a cron job in UNIX based operating systems.


* Twitter data collection: 
To collect the Twitter dataset follow the steps given below:
	1. Open twitter/Twitter_Collector_v3.ipynb using jupyter notebook.
	2. Run all the cells to download Election related Twitter data for the last 7 days.
	3. Subsequent runs (run after 7 days) will append data to data extracted in step 2.
	4. This process can be automated to scrape tweets using a cron job in UNIX based operating systems.




Machine Learning Models:

* Twitter Models: 
	In order to run the twitter, goto the nlp_on_tweets.ipynb for visualization as well as getting the results from the deep learning and extra trees model.
* Headlines Models:
	 For obtaining results of the headlines model, run headlines_dataset.ipynb and execute all cells for executing all ML models.
* Both datasets use the same underlying python files for computing the sentiment.
* Results are provided in a tabular format and with graphs for the continual prediction model.


Automation:

* We setup cron job to automatically scrape tweets as well as news articles at a specified time of the day. This will also make predictions for all locations and given date and save it in a json
file (NLP_on_tweets.ipynb is run). 
* The the back-end (flask) will send the cached results every time a request is made for the day or day and city from the front-end (Angular JS).


Doc2Vec:

* We came across this algorithm in gensim in which we can represent a document as a set of vectors. We tried to use this to use historical data for making predictions.  But any given model is only 	as good as the data which is used for training. We were limited to 50,000 articles and hence the model wasn’t good. But we think that this could be used for 




UI:
* Frontend: To run the frontend angular app server, follow these steps:
   * Install node and angular cli, if unavailable in the system.
   * Navigate to angular_app/violence-pred/ and run the command, `ng serve --open`
   * This will open the angular app on the default browser (port 4200)


* Backend: To run the backend Flask server, follow these steps:
   * Run all the to initialize and start the server
   * The server will start on port 5000, and serve the angular app
