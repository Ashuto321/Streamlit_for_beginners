import streamlit as st

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

table=pd.DataFrame({"columns1":[1,2,3,4,5,6],"colums2":[6,5,4,3,2,1],"colums3":[2,3,1,4,5,6]})
xp=np.linspace(0,10,100)
# for bar char we need an np arry
b_x=np.array([1,2,3,4,5,6])
# st.sidebar.write("Here is your slide bar")
opt=st.sidebar.radio("Select te following", options=["Line","Bar","H-bar"])
if opt=="Line":
    st.markdown("<h1 style='text-align: center'>Line-chart</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.plot(xp, np.sin(xp))
    plt.plot(xp, np.cos(xp),"--")
    st.write(fig)

elif opt=="Bar":
    st.markdown("<h1 style='text-align: center'>Bar-chart</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.bar(b_x,b_x*10)
    st.write(fig)


else:
    st.markdown("<h1 style='text-align: center'>H-bar-chart</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.barh(b_x*10,b_x)
    st.write(fig)
