import streamlit as st

st.checkbox("hi click me", value=False)
#if the value of the check box is true then it will 
#be check already

#also we can print a message whenver it is checked

# state=st.checkbox("click please and get messg", value=False)
# if state:
#     st.write("thanlyou for your response")
# else:
#     pass

#properties of checkboxes
def che():
    print("it has been modified")
# st.checkbox("click please and get messg", value=False, on_change=ch)
# on_change gives message that someone has changed something
def ch():
    print(st.session_state.check)

st.checkbox("click please and get messg", value=False, on_change=ch, key="check")
st.radio("in which country do yu live", options=("us","japan", "india", "madras"))
#radio button also supports callback (session state), on_change=,key=""
def btn():
    print("button clicked")
btn=st.button("click me btn", on_click=btn)
selectbox=st.selectbox("this is the select box please select",options=("atul","mummohad","randa"))

multi_select=st.multiselect("hello please multisect this ", options=("japan", "usa", "korea", "dobba"))