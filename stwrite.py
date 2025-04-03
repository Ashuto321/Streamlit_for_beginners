import streamlit as st

#in order to do table part yu have to import pandas
import pandas as pd
df=pd.DataFrame({"column1":[1,2,3,4,5], "column2":[1,2,3,4,4],"column3":[2,2,3,3,4]})

# st.write() this function allows us to put styling 
#in streamlit like we can use mardown here 
# and anything like code , latex can be written in here

st.write("""

# header 1
## header 2
### header 3
""")

st.metric(label="the wind speed", value="120m/s", delta="1.4m/s")
#table
st.table(df)
#dataframe
st.dataframe(df)