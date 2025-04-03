import  streamlit as st

st.title("hello my streamlit learners")
st.header("hello ashutoh")
st.subheader("my name is ashutohs")
st.text("hi i am the text used in html as paragraoh p")

#if you want to apply html tags property on using 
# streamlit you can you markdown

st.markdown("""
**hello**
*world*
# hi
## hello
### ashutosh
# for adding links
[Google](https://www.google.com)

""")

st.latex("allows us to write the formulaes in streamlit or matrixes etc")
st.caption("streamlit tool to write captions")

#to write a json in streamlit we have

jason={"a":"ashu","n":"nippon"}# you have to put it as a

st.json(jason)

#to write the code blocks we have

c="""
print("hello world)

def fun():
   return 0

"""

st.code(c,language="python")