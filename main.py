import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='calculator'
)

st.title('A simple calculator')

num_1 = st.number_input('The first number',1,100)
num_2 = st.number_input('The second number',1,100)

choice = st.selectbox('Please choose: ',['+','-','*','/'])

if choice == '+':
    result = num_1+num_2
elif choice == '-':
    result = num_1-num_2
elif choice == '*':
    result = num_1*num_2
else:
    result = num_1/num_2

st.write('The result is ',result) 