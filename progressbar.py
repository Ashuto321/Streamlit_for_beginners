import streamlit as st
import time as ts
from datetime import time

# creating function to convert in the time 
def convert(value):
     m,s,mm=value.split(":")
     t_s=int(m)*60+int(s)+int(mm)/1000
     return t_s

val=st.time_input("set time", value=time(0,0,0))
if str(val)=="00:00:00":
    st.write("please set the time")
else:
    sec=convert(str(val))
    bar=st.progress(0)
    progress_status=st.empty()
    for i in range(10):
          bar.progress(i+1)
          progress_status.write(str(i+1)+"%")
          ts.sleep(1)