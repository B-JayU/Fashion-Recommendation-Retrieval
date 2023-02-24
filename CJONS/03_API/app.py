from email.policy import default
from turtle import width
from typing import Dict
import requests
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
import json
from base64 import b64encode, b64decode
from io import BytesIO
import io
import zipfile
from zipfile import ZipFile
import os
from pathlib import Path


names = ['airnd']
usernames = ['airnd']
passwords = ['airnd']




@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}

def image_utf8(file, ENCODING = 'utf-8'):
    bytes = file.read()
    base64_bytes = b64encode(bytes)
    utf8 = base64_bytes.decode(ENCODING)
    return utf8




def user_input():  
    st.title("Originality API")
    session = requests.Session()
    st.set_option("deprecation.showfileUploaderEncoding", False)
    static_store = get_static_store()
    #st.info(__doc__)

    uploaded_files = st.file_uploader("Upload", type=["png","jpg","jpeg"])

    metric = st.selectbox('Select Distance Metric', ('angular', 'euclidean'))
    tta = st.checkbox('Use Test Time Augmentation', value=False)
    topk = st.slider('Select Top K ', min_value=1, max_value=20, value=10, step = 1)
    if not uploaded_files:
        st.info("Upload one or more image files.")

    if st.button("Clear file list"):
        static_store.clear()
        uploaded_files = None
    
    if st.button('Submit'): 
        data = {'files' : [[uploaded_files.name, image_utf8(uploaded_files)]] }
        data["metric"] = metric
        data["topk"] = topk
        data['tta'] = tta
        url = f"http://localhost:8000/predict"
        print(f"url : {url}")
        
        resp = requests.get(url, data=json.dumps(data))
        st.header(f"Result of Request") 
        st.image(Image.open(uploaded_files), caption="Input Image", width=256)

        results = resp.json()['files']
        cols = st.columns(topk+1)
        with cols[0]:
            st.text(f"Order")
            st.text("FileName")
            st.text("Image")
            st.text("Distance")

        for idx in range(topk):
            with cols[idx+1]:
                st.text(f" # {idx+1}")
                st.text(results[idx][0].split('/')[-1])
                base64ed = results[idx][1]
                image = Image.open(BytesIO(b64decode(base64ed)))
                st.image(image)
                st.text(results[idx][2])


def main():  
    # authentication / login
    st.set_page_config(page_title="Originality", page_icon="🤖", layout="wide") 
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
        'some_cookie_name','some_signature_key',cookie_expiry_days=30)
    name, authentication_status, _ = authenticator.login('Login', 'main')
    if authentication_status:
        st.write('Welcome *%s*' % (name))
        user_input()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')



if __name__ == "__main__":
    import argparse
    main()
