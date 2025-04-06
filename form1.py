import streamlit as st


# first method of creating a form 

# form=st.form("form 1")
# form.text_input("First Name")
# form.form_submit_button("submit")

#second method of creating a form 

st.markdown("<h1 style='text-align:center'>Registration Form<h1>",unsafe_allow_html=True)
with st.form("form 2", clear_on_submit=True):
    # dividing the columd into  
    col1,col2=st.columns(2)
    f_name=col1.text_input("First name")
    l_name=col2.text_input("Last name")
    st.text_input("Email Adress")
    st.text_input("Password")
    st.text_input("conform Password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    status=st.form_submit_button("Submit")
    if status:
        if f_name=="" and l_name=="":
            st.warning("Please fill mandatory feilds")
        else:
            st.success("Form submitted Successfully")

