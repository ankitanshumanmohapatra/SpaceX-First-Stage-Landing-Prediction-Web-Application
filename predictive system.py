# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:00:44 2023

@author: KIIT
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/KIIT/Documents/1 My Documents/Projects/SpaceX first stage Landing prediction System/trained_model.sav', 'rb'))

input_data = (1000, 1, 3, 81,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,.77,78,79)
input_data_as_numpy_array = np.asarray(input_data)

# Ensure the shape is compatible with the model's expectations
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Use the best SVM model for prediction
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print('It seems that the rocket landing will be unsuccessful in this scenario')
else:
    print('Yes, the rocket will land successfully')