import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mat

st.set_page_config(
    page_title='draw'
)
st.title('for drawing')
st.balloons()
x = np.arange(0,4*np.pi,0.01)
choice = st.selectbox('please choose the diagram',['sin','cos','tan'])

if choice == 'sin':
    y = np.sin(x)
elif choice == 'cos':
    y = np.cos(x)
else:
    y = np.tan(x)

st.success('hey! Here is your diagram!')

fig, ax = mat.pyplot.subplots()
mat.pyplot.plot(x,y)
st.pyplot(fig)
