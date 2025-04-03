import streamlit as st;

st.title("File uploadier")
st.markdown("---")

# img=st.file_uploader("please upload your file", type=["png","jpg","jpeg"])

# if img is not None:
#     st.image(img)


# for uploading the video you have to change the type to mp4
# and in the if blog you have to show st.video(vid) to-show it on the app


#for uploading multiple files:

imgs=st.file_uploader("upload your file here", type=["png","jpg","jpeg"],accept_multiple_files=True)

if imgs is not None:
    for ims in imgs:
        st.image(ims)