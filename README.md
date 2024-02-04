# Monitored-Model-Deployment-MarketGPT-Project

Command to start -->
uvicorn app:app --host 0.0.0.0 --port 10001

Model is deployed on Render
https://monitored-model-deployment-marketgpt.onrender.com/

All code files have been added in this git repo
https://github.com/ManasiBharatIngle/Monitored-Model-Deployment-MarketGPT-Project

Currently the model will be taking 5 sales values, each corresponding to one lag as input and will be giving the scaled sales prediction as output. Each lag would in turn require 5 sales values because time-series cross validation has been used for model training. A testcase has been given in testcase.txt file for reference. Currently we have not deployed monitored model. A basic model has been deployed. 
To get the actual sales value we will have to change the model pipeline. Other features can also be added according to our requirement.

After https://monitored-model-deployment-marketgpt.onrender.com/ this, add "/docs" in the url ( "https://monitored-model-deployment-marketgpt.onrender.com/docs" ) to get the FastAPI page for sales prediction.
