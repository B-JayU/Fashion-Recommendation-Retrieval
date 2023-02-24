# -*- coding: cp949 -*-
######################################################################## Importing
import streamlit as st
import extcolors
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
from PIL import Image
import pandas as pd

from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.models import Model
from keras.layers import Dense, Dropout, Flatten
from tqdm import tqdm
from pathlib import Path

import os
import sys
import cv2
import io

from rembg.bg import remove

import nltk
from nltk import word_tokenize

import re
########################################################################

st.title('BJ X CJ Fashion Recommendation System')

######################################################################## Load DataSet

df = pd.read_csv("fashion_dataset.csv")
df = df[['PID', 'GENDER', 'TITLE', 'CATEGORY', 'season', 'NEW_TAG', 'rem_img', 'file_loc']]
ktoe = {'봄': 'Spring', '여름': 'Summer', '가을' : 'Autumn', '겨울':'Winter', 'None' : 'none'}
df['season'] = df['season'].apply(lambda x : ktoe[x])
show_df = df

########################################################################

def reload_df():
    global df, show_df
    
    show_df = df
    return show_df

######################################################################## Strealit API 01

def update_df(g, s):
    
    show_df = reload_df()
    
    if st.session_state['dataset_checkbox']:
        st.subheader('Fashion metadata set')
        
    if g != "All":
        show_df = show_df[(show_df['GENDER'] == g)]
    if s != "All":
        show_df = show_df[(show_df['season'] == s)] 
    
    st.write(show_df)
        

gender_list = ['All', 'Men', 'Women']
def updated_radio1():
    global show_df
    
    gender = st.session_state['gender']
    # st.write("****The gender user selects is****", gender, ".")

    if gender == 'Men':
        show_df = show_df[show_df['GENDER'] == 'Men']
    elif gender == 'Women':
        show_df = show_df[show_df['GENDER'] == 'Women']
    
    return gender
        
        
gender = st.radio('**Input gender you want to search :)**', gender_list, key='gender', on_change=updated_radio1)    
# st.write("****The gender user selects is****", gender, ".")

def updated_radio2( ):
    global show_df
    
    season = st.session_state['season']
    # st.write("****The season user selects is****", season, ".")
    
    if st.session_state['season'] == 'Spring':
        show_df = show_df[show_df['season'] =='Spring']
    elif st.session_state['season'] == 'Summer':
        show_df = show_df[show_df['season'] =='Summer']
    elif st.session_state['season'] == 'Autumn':
        show_df = show_df[show_df['season'] =='Autumn']
    elif st.session_state['season'] == 'Winter':
        show_df = show_df[show_df['season'] =='Winter']

    return season
        
        
season_list = ['All', 'Spring', 'Summer', 'Autumn', 'Winter']        
season = st.radio('**Input season you want to search :)**', season_list, key='season', on_change=updated_radio2)

if gender != "All":
    show_df = show_df[(show_df['GENDER'] == gender)]
if season != "All":
    show_df = show_df[(show_df['season'] == season)]

if st.checkbox('Show Fashion metadata set'):
    st.subheader('Fashion metadata set')
    st.write(show_df)

query_img = st.file_uploader("**Image You want to search**", type=['jpg', 'jpeg', 'png'])


######################################################################## VGG16 model

class FeatureExtractor:
    def __init__(self):
        base_model = VGG16(weights='imagenet')
        # print(base_model.summary())
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

    def extract(self, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)


features = []
img_paths = []

fe = FeatureExtractor()

features = []
for i in range(len(show_df)):
    png_path = show_df.iloc[0]['rem_img'].split('.') 
    path = 'features/'+ png_path[0] + '.npy'
    data = np.load(path)
    features.append(data)

######################################################################## Search Results Based on Color-Extraction
scores = []

if query_img is not None:
    q_img = Image.open(query_img)
    st.write("The below image is what user uploads")
    st.image(q_img, width=200)
    
    fig1 = plt.figure(figsize=(0.5,0.5))

    ct = ColorThief(query_img)
    dominant_color = ct.get_color(quality=1)
    plt.imshow([[dominant_color]])
    plt.show()

    fig2 = plt.figure()
    palette = ct.get_palette(color_count = 5)
    plt.imshow([[palette[i] for i in range(5)]])
    plt.show()   
    st.pyplot(fig2)

    query = fe.extract(q_img)
    dists = np.linalg.norm(features - query, axis=1)
    ids = np.argsort(dists)[:100]

    result_load_state = st.text('Loading result data...')
    
    scores = [(dists[id], show_df.iloc[id]['rem_img'], id) for id in ids]
    tags = []

    axes=[]
    fig3 = plt.figure(figsize=(8,10))
    for a in range(20):
        score = scores[a]
        axes.append(fig3.add_subplot(4, 5, a+1))
        subplot_title=str(round(score[0],2)) + "/m" + str(score[2]+1)
        axes[-1].set_title(subplot_title)  
        plt.axis('off')
        plt.imshow(Image.open(score[1]))
        tags.append(df.iloc[score[2]]['NEW_TAG'])

    fig3.tight_layout()
    plt.show()
    st.pyplot(fig3) 
    
    result_load_state.text("Done!")

######################################################################## Extraction Based on Keyword

dictionary = []
contents = []
new_tags = []

for i in range(len(show_df)):
    # print(len(show_df.iloc[i]['TAG']))
    tags = show_df.iloc[i]['NEW_TAG'][1:len(df.iloc[i]['NEW_TAG'])-1]
    # print(tags)
    # print()
    
    tags = re.split("[:/ ,']+", tags)
    tags.remove('')
    dictionary.extend(tags)
    contents.append((show_df.iloc[i]['PID'], tags))
    new_tags.append(tags)

dictionary = list(set(dictionary))
dictionary.sort()

if '' in dictionary:
    dictionary.remove('')
dictionary = dictionary[1:]

######################################################################## inverted Index

dict_post = {}
for term in dictionary:
    
    posting = {}
    
    for id , t1 in contents:
        # print(idx, tags)    
        freq = 0
        for t2 in t1:
            if (term == t2):
                # print("ID : ", id, "Term : ", term, " Word : ", t2) 
                freq += 1
        if (freq != 0):
            posting[id] = freq
    
    dict_post[term] = posting
    # print(term) 

######################################################################## tf-idf

from math import log10
N = len(df)

def tf(t, d):
    if d in dict_post[t]:
        return 1+log10(dict_post[t][d])
    else:
        return 0

def idf(t):
    df = len(dict_post[t])
    return log10(N/(df))

def tfidf(t, d):
    return tf(t,d)* idf(t)


######################################################################## Input Keywords
keywords = st.text_input('Search Keyword', 'None')

def search_keyword(keywords):

    global scores, query_img
    
    if keywords != 'None':
        tr_query = keywords.split(" ")
                
########################################################################

        feature_extra_scores = scores
        keyword_result = []
        keyword_scores = []
        keyword_max_score = 0

        for id in range(len(feature_extra_scores)):
            score = 0
            for term in tr_query:
                if term in dictionary:
                    # print(df.iloc[product]['PID'], ' : ', term)
                    score += tfidf(term, show_df.iloc[id]['PID'])
                    # print(score)
                else:
                    pass
            keyword_scores.append((score, show_df.iloc[id]['PID']))

            if (score > 0):
                keyword_result.append((score, show_df.iloc[id]['PID']))

            if score > keyword_max_score:
                keyword_max_score = score
                
            keyword_result.sort(reverse=True)

########################################################################

        n_count = 0
        show_result = []

        for r in keyword_result:
            if r[0] == keyword_max_score:
                show_result.append(r)
                n_count += 1
            elif n_count < 20:
                show_result.append(r)
                n_count += 1
            else:
                break
            

        result_img = []
        for r in show_result:
            score, id = r[0], r[1]
            for i in range(len(show_df)):
                if show_df.iloc[i]['PID'] == id:
                    result_img.append((show_df.iloc[i]['file_loc'], show_df.iloc[i]['NEW_TAG']))

        # result_img

        print("Search Keywords : " , tr_query)
        
        if query_img is not None:
            st.write("Query Image")
            st.image(q_img, width=200)
        
        fig = plt.figure(figsize=(12,15))

        for n in range(len(result_img)):
            fig.add_subplot(4,5, n+1)
            orig_img = Image.open(result_img[n][0])
            plt.imshow(orig_img)
            # print(result_img[n][1])

        st.pyplot(fig)
        st.write("Keyword retrieve result of Search Keywords : " , tr_query)
    
if keywords != None:
    search_keyword(keywords)
# keywords = st.text_input('Search Keyword', 'None', on_change=search_keyword, key='keywords')