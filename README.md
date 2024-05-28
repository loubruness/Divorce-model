# Divorce-model
Are you getting divorced ? Fill in our survey and find out !

This project requires the flask, streamlit and requests libraries. ALl of them can be installed using the following commands :
```pip install flask```
```pip install streamlit```
```pip install requests```

To test it out, download all the files and place them in a repository. Open two terminals :
- In the first one, enter the command ```streamlit run front.py``` to launch the front server. A window should open in your browser. If it doesn't, you should be able to access it at the following address : http://localhost:8501/
- In the second one, enter the command ```flask --app server run``` to launch the API.
Then, you should answer all the questions in the window of your browser and submit them to know your fate.

If it doesn't work, please check that the flask server is running on the port 5000 of your localhost. If not, you should replace the api_url with "http://localhost:<your_port>/predict".
You can find the url used by flask in your terminal :
![image](https://github.com/loubruness/Divorce-model/assets/94390007/4e64eaad-13ba-426d-86bb-a5ad8c17a9bf)
