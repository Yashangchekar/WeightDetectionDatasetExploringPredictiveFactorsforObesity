# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:11:32 2024

@author: yash
"""

import numpy as np
import pickle
import streamlit as st
# loaded_model=pickle.load(open('C:/Users/yash/Documents/Deployment/obestity/trained_model.sav','rb')) #rb read the binary format
loaded_model=pickle.load(open('trained_model.sav','rb'))
def obesity_prediction(input_data):
    
    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data,dtype=object)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    #standardize the input data
    #std_data=ss.transform(input_data_reshaped)
    #print(std_data)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==0:
        return"Insufficient weight"
    elif prediction[0]==1:
        return "Normal weight"
    elif prediction[0]==2:
        return"Obesity_type_I"
    elif prediction[0]==3:
        return "Obesity_type_II"
    elif prediction[0]==4:
        return "Obesity_type_III"
    elif prediction[0]==5:
        return "Overweight_Level_I"
    elif prediction[0]==6:
        return "Overweight_Level_II"
  #Age 	Height 	Weight 	FCVC 	NCP 	CH2O 	FAF 	TUE 	Gender 	family_history_with_overweight 	FAVC 	CAEC 	SMOKE 	SCC 	CALC 	MTRANS  
def main():
    st.title("Obesity prediction app")
    Age=st.text_input("enter the age")
    Height=st.text_input("enter the height")
    Weight =st.text_input("enter Weight")
    FCVC = st.text_input("FCVC (Frequency of consumption of vegetables) no 0 yes 1")
    NCP = st.text_input("NCP (Number of main meals)")
    CH2O= st.text_input("CH2O (Daily water intake in liters)")
    FAF= st.text_input("FAF (Physical activity frequency)")
    TUE = st.text_input("TUE (Time of use of electronic devices)")

# Binary features
    Gender = st.text_input("Gender female 0 male1")
    family_history_with_overweight = st.text_input("Family history with overweight no 0 yes 1")
    FAVC = st.text_input("FAVC (Frequency of high-caloric food consumption)")
    CAEC = st.text_input("CAEC (Consumption of food between meals)")

# Categorical features
    SMOKE = st.text_input("SMOKE (Smoking habits)")
    SCC = st.text_input("SCC (Caloric beverages consumption) no 0 yes 1")
    CALC = st.text_input("CALC (Consumption of alcohol)")

# Mode of transportation
    MTRANS = st.text_input("MTRANS (Mode of transportation)")
    #code for prediction
    diagnosis=''
    if st.button("Obesity test result"):
        diagnosis=obesity_prediction([Age,Height,Weight,FCVC,NCP,CH2O,FAF,TUE,Gender,family_history_with_overweight,FAVC,CAEC,SMOKE,SCC,CALC,MTRANS])
        
    st.success(diagnosis)
if __name__=='__main__':
    main()
    
        

    
