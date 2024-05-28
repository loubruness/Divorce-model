# Divorce-model
Are you getting divorced ? Fill in our survey and find out !

This project requires the flask, streamlit and requests libraries. All of them can be installed using the following commands :
```pip install flask```
```pip install streamlit```
```pip install requests```

To test it out, download all the files and place them in a repository. Open two terminals :
- In the first one, enter the command ```streamlit run front.py``` to launch the front server. A window should open in your browser. If it doesn't, you should be able to access it at the following address : http://localhost:8501/
- In the second one, enter the command ```flask --app server run``` to launch the API.
Then, you should answer all the questions in the window of your browser and submit them to know your fate.

If it doesn't work, please check that the flask server is running on the port 5000 of your localhost. If not, you should replace the api_url in server.py with "http://localhost:<your_port>/predict".
You can find the url used by flask in your terminal :
![image](https://github.com/loubruness/Divorce-model/assets/94390007/4e64eaad-13ba-426d-86bb-a5ad8c17a9bf)



## Maintenance & Update

The maintenance & update of this model is relatively stress-free, as there is no need to alter the front or api files when you alter the model without changing the number of inputs. The only thing you need to do after modifiying your model is reload the joblib file. If you do change the number of inputs, you will have to slightly modify the front, but no great complexity is involved. 


## Data Drift 

Our model is not at an important risk of data drift. Indeed, our input data type is stable, and the statistical aspect of the data is not likely to change: treating your partner poorly, or having a distant relationship should never lead to lower chances of divorce regardless of the future societal trends.

## Model Monitoring

This model is safe from most notable drifts. Gradual and sudden concept drifts shouldn't be an issue as romantic relationships and their struggles are unlikely to drastically change or disappear. Data pipeline bugs are no big threaths as our input data type is fixed and stable, and adverserial adaptation will probably not invest much time in targeting our tool. We do have potential threats on data drift and data quality issues, as the predictions of our model depend on the honesty of our sample set : if the people we based the study on lied on their relationships or marital status, we may have statistical imprecisions. 
All in all however, our model is stable over time.
