import DataLoader
import Model
import pandas as pd
from joblib import dump
import Accuracy

def run_model():
    user_id = "65b30e99201ae95a40c5bb80"
    
    is_success_score = Accuracy.logging_model_score(user_id)
    # print(is_success_score)
    if is_success_score:
        print("Model scoring successful.")
    else:
        print("Model scoring failed.")
        
    data = DataLoader.retrieve_data(user_id)
    # print("After calling retrieve_data")

    is_success = Model.model_train(user_id, data)
    if is_success:
        print("Model training successful.")
    else:
        print("Model training failed.")
    
run_model()  
    