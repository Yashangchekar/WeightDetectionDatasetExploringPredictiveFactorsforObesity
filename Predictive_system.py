# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:08:16 2024

@author: yash
"""

import numpy as np
import pickle
loaded_model = pickle.load(open('C:/Users/yash/Documents/Deployment/obestity/trained_model.sav', 'rb'))
input_data=(21.000000,1.620000 ,64.000000,2.0 ,3.0 ,2.000000 ,0.000000 ,1.000000 ,0 ,1,0 ,2 ,0,0 ,3,3 )
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = np.array(input_data_as_numpy_array).reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction[0]==0:
    print("Insufficient weight")
elif prediction[0]==1:
    print("Normal weight")
elif prediction[0]==2:
    print("Obesity_type_I")
elif prediction[0]==3:
    print("Obesity_type_II")
elif prediction[0]==4:
    print("Obesity_type_III")
elif prediction[0]==5:
    print("Overweight_Level_I")
elif prediction[0]==6:
    print("Overweight_Level_II")