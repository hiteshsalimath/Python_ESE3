import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image, ImageOps

plot_tab,image_tab, text_tab = st.tabs(["3D Plot", "Image Processing", "text analysis"])





with plot_tab:
    
    st.title("3D Plot Visualization")
    data = pd.read_csv('WomensClothingE-CommerceReviews.csv')
    gw_list = data['Age'].unique().tolist()
    menu=gw_list

    st.sidebar.header('Select Age')
    choice = st.sidebar.selectbox('Age:',menu)

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.scatter(choice, data['Rating'], data['Positive Feedback Count'])
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Rating')
    ax1.set_zlabel('Positive Feedback Count')
    ax1.set_title('Scatter Plot of Age, Rating, and Positive Feedback Count')
    st.pyplot(fig)



with image_tab:


    st.title("Image Processing")
    im = Image.open("image1.jpg")

    tq_list = ["Resize","Grayscale","cropping","rotation by 90","rotation by 180","rotation by 270"]
    menu = tq_list
    st.sidebar.header('Select Technique')
    choice = st.sidebar.selectbox('Technique:',menu)
    
    #Image cropping:-
    ToSize = (100,100,170,170)
    cropped = im.crop(ToSize)

#  Image Grascale conversion:
    grayscale = ImageOps.grayscale(im)

#Image Resizing:
    size = (100,150)
    resized = ImageOps.fit(im,size)

#Image rotation:

    flip_lateral = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    flip_vertival = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    rotate_90 = im.transpose(Image.Transpose.ROTATE_90)
    rotate_180 = im.transpose(Image.Transpose.ROTATE_180)
    rotate_270 = im.transpose(Image.Transpose.ROTATE_270)

    fig_img = plt.figure(figsize=(20,10))
    plt.subplot(331), plt.imshow(im), plt.axis('off'), plt.title("original image", size=20)
    plt.subplot(332), plt.imshow(cropped), plt.axis('off'), plt.title("Cropped image", size=20)
    plt.subplot(333), plt.imshow(grayscale), plt.axis('off'), plt.title("Grayscale image", size=20)
    plt.subplot(334), plt.imshow(resized), plt.axis('off'), plt.title("Resized image to (100,150)", size=20)
    plt.subplot(335), plt.imshow(flip_lateral), plt.axis('off'), plt.title("lateral rotation", size=20)
    plt.subplot(336), plt.imshow(flip_vertival), plt.axis('off'), plt.title("verticle rotation", size=20)
    plt.subplot(337), plt.imshow(rotate_90), plt.axis('off'), plt.title("rotation by 90 degreee", size=20)
    plt.subplot(338), plt.imshow(rotate_180), plt.axis('off'), plt.title("rotation by 180 degree", size=20)
    plt.subplot(339), plt.imshow(rotate_270), plt.axis('off'), plt.title("rotation by 270 degree", size=20)

    st.pyplot(fig_img)

