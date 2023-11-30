# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:06:51 2023

@author: KIIT
"""

import numpy as np 
import pickle
import streamlit as st
from PIL import Image

loaded_model = pickle.load(open('C:/Users/KIIT/Documents/1 My Documents/Projects/SpaceX first stage Landing prediction System/trained_model.sav', 'rb'))

#creating a function for prediction


#def landing_prediction(inputs):
    #try:
        # Ensure all input values are in the correct data types
        #payload, orbit, boosterv, missions = map(lambda val: float(val) if str(val).replace('.', '', 1).isdigit() else val, inputs)

        # Make prediction using the loaded model
       # prediction = loaded_model.predict([[payload, orbit, boosterv, missions]])

       # if prediction[0] == 0:
     #       return 'It seems that the rocket landing will be unsuccessful in this scenario'
     #   else:
     #       return 'Yes, the rocket will land successfully'

  #  except ValueError:
      #  return 'Error: Please enter valid numeric values for the input features.

#def landing_prediction(inputs):
  #  try:
        # Ensure all input values are in the correct data types
  #      payload, orbit, boosterv, missions = map(lambda val: float(val) if str(val).replace('.', '', 1).isdigit() else val, inputs)

        # Make prediction using the loaded model
 #       prediction = loaded_model.predict([[payload, orbit, boosterv, missions]])

 #       if prediction[0] == 0:
 #           return 'It seems that the rocket landing will be unsuccessful in this scenario'
  #      else:
   #         return 'Yes, the rocket will land successfully'

  #  except ValueError:
#        return 'Error: Please enter valid numeric values for the input features.'


#creating a function for prediction

def landing_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 0:
        return 'It seems that the rocket landing will be unsuccessful in this scenario'
    else:
        return 'Yes, the rocket will land successfully'

def main():
    # Giving a title for the web page
    img1 = Image.open('C:/Users/KIIT/Documents/1 My Documents/Projects/SpaceX first stage Landing prediction System/spacex.png')
    img1 = img1.resize((156, 145))
    st.image(img1, use_column_width=False)
    st.title('SpaceX First Stage Landing Prediction Web App')

    # Getting the input data from the user
    payload = st.text_input('Payload mass in Kg')
    orbit = st.text_input('Orbit launch (For LEO-1, GTO-2, HEO-3, Polar-4, SSO-5, MEO-6)')
    boosterv = st.text_input('Booster Version (For F9v1.0-1, F9v1.1-2, F9vFT-3, F9vB4-4, F9vB5-5)')
    missions = st.text_input('Mission Success (For Yes-1, No-0)')

    # code for Prediction
    analysis = ''


    # creating a button for Prediction
    if st.button('Landing Outcome Result'):
     #check if conversion is successful before calling landing_prediction
        if isinstance(payload, (float, int)) and isinstance(missions, int):
            analysis = landing_prediction([payload, orbit, boosterv, missions])
        else:
            st.error("Please enter valid numeric values for Payload and Mission Success.")

    st.success(analysis)
    

#def main():
    
 #   #giving a title for the web page
 #   img1 = Image.open('C:/Users/KIIT/Documents/1 My Documents/Projects/SpaceX first stage Landing prediction System/spacex.png')
 #   img1 = img1.resize((156,145))
 #   st.image(img1,use_column_width=False)
 #   st.title('SpaceX First Stage Landing Prediction Web App')
    
    #getting the input data from the user
    
 #   payload = st.text_input('Payload mass in Kg')
 #   orbit = st.text_input('Orbit launch(For LEO-1, GTO-2, HEO-3, Polar-4, SSO-5, MEO-6)')
 #   boosterv = st.text_input('Booster Version(For F9v1.0-1, F9v1.1-2, F9vFT-3, F9vB4-4, F9vB5-5)')
 #   missions = st.text_input('Mission Success(For Yes-1, No-0)')

    
    #code for Prediction
    #analysis = ''
    
    #creating a button for Prediction
    
    #if st.button('Landing Outcome Result'):
        #analysis = landing_prediction([payload, orbit, boosterv, missions])
        
    
    #st.success(analysis)
    # converting inputs to appropriate data types
 #   try:
 #       payload = float(payload)
 #       missions = int(missions)
 #   except ValueError:
#            st.error("Please enter valid numeric values for Payload and Mission Success.")

    # code for Prediction
   # analysis = ''


    # creating a button for Prediction
 #   if st.button('Landing Outcome Result'):
   #  check if conversion is successful before calling landing_prediction
  #      if isinstance(payload, (float, int)) and isinstance(missions, int):
   #         analysis = landing_prediction([payload, orbit, boosterv, missions])
  #      else:
  #          st.error("Please enter valid numeric values for Payload and Mission Success.")

 #   st.success(analysis)
    
    
if __name__ == '__main__':
    main()

