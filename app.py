import pandas as pd
import numpy as np
import pickle
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

import uvicorn
from fastapi import FastAPI
from SalesInfos import SalesInfo

# Creating the app
app = FastAPI()
pred_model = load_model('keras_trained_model.h5')

# Loading the scaler
with open('scalers.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Future sales prediction API'}

# Route with a single parameter, returns the parameter within a message
# Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{num_of_days}')
def get_name(num_of_days: int):
    return {'message': f'You can predict the net future sales for {num_of_days} days here.'}


@app.post('/predict')
def predict_sales(data: SalesInfo):
    features = [data.lag_1, data.lag_2, data.lag_3, data.lag_4, data.lag_5]
    temp1 = []
    for f in features:
        temp1.append(f)
    temp2 = [temp1]
    print(temp2)
    future_sales_predictions = pred_model.predict(temp2)[0, 0]
    future_sales_predictions = float(future_sales_predictions)
    print(future_sales_predictions)

    # temp4 = np.zeros((1, 11))
    # temp4[0, 0] = future_sales_predictions
    # # Applying inverse transformation using the loaded scaler
    # predicted_value = np.array(temp4).reshape(1, -1)
    # future_sales_predictions = scaler.inverse_transform(predicted_value)
    # future_sales_predictions = future_sales_predictions[0, 0]
    return {'future_sales_predictions': future_sales_predictions}


# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# --------------------------------------------------------------------- #

# Command to run this python script -->
# uvicorn app:app --reload


# Testcase -->
# {
#   "lag_1": 0.47923356,
#   "lag_2": 0.46374405,
#   "lag_3": 0.48067927,
#   "lag_4": 0.74060375,
#   "lag_5": 0.84755089,
#   "lag_6": 0.77915399,
#   "lag_7": 0.56764024,
#   "lag_8": 0.48112283,
#   "lag_9": 0.4561315,
#   "lag_10": 0.51765537
# }