#!/usr/bin/env python
# coding: utf-8

import os
import streamlit as st
from PIL import Image
import subprocess

# Title
st.write("""
# Car Defect Detector
Aplikasi browser ini dapat mendeteksi cacat pada eksterior mobil, seperti: penyok, goresan, dan retakan!""")

# Show image
image = Image.open('./sample_images/car_assembly_line.jpeg')
st.image(image, use_column_width=True)

# add sidebar for aesthetics
st.sidebar.header('Prototipe Tugas Akhir')
st.sidebar.write('Object Detection pada Eksterior Mobil')
st.sidebar.write('Model: YOLOv5')
st.sidebar.write('I Made Atmavidya V.')

st.sidebar.markdown("""---------""") # separator
st.sidebar.write('Sample input:')
st.sidebar.image('./sample_images/0050.JPEG')
st.sidebar.write('Sample output:')
st.sidebar.image('./sample_images/0050_pred.JPEG')

# Create a page dropdown 
page = st.selectbox("Pilih tipe input:", ["Image", "Video"]) 

if page == "Image":
    # Upload image prompt
    uploaded_img = st.file_uploader("Upload your input JPEG/JPG/PNG file", type=["jpeg","jpg","png"])

    if uploaded_img is not None:
        file_details = {"FileName":uploaded_img.name,"FileType":uploaded_img.type}
        st.write(file_details)
        img = Image.open(uploaded_img)
        st.image(img, 
                width=250,
                )
    
        os.makedirs(os.path.join("./uploaded_images", uploaded_img.name), exist_ok=True)

        with open(os.path.join("./uploaded_images", uploaded_img.name, uploaded_img.name),"wb") as f: 
            f.write(uploaded_img.getbuffer())         
        st.success("Saved File")

        # import torch??
        subprocess.run('pip install torch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 opencv-python', shell=True)

        # run detect py
        src_img_dir = 'uploaded_images'
        dest_img_dir = 'predictions'

        venv_path = 'python'
        script_file = f'./yolov5/detect.py --source ./uploaded_images/0003.JPEG --project ./predictions --weights .yolov5/runs/train/yolo_car_dmg_plustf/weights/best.pt --conf 0.25 --name pilottest'

        subprocess.run(venv_path + ' ' + script_file, shell=True)
        
        # prediction result
        # labeled_img_dir = f'predictions/{uploaded_img.name}' 
        # img_filename = os.listdir(labeled_img_dir)[0]
        # final_img_path = os.path.join(labeled_img_dir, img_filename)

        st.write('Result')
        final_image = Image.open('./predictions/pepe_placeholder.jpeg')
        st.image(final_image,  
                width=250,
                    )

elif page == "Video":
    # Upload video prompt
    uploaded_vid = st.file_uploader("Upload your input MP4 file", type=["mp4"])

    if uploaded_vid is not None:
        st.video(uploaded_vid) # showcase uploaded video

        # # Save video in local dir
        # os.makedirs(os.path.join("uploaded_videos", uploaded_vid.name), exist_ok=True)

        # with open(os.path.join("uploaded_videos", uploaded_vid.name, uploaded_vid.name),"wb") as f: 
        #     f.write(uploaded_vid.getbuffer())         
        # st.success("Saved File")

        # # run detect py
        # src_vid_dir = 'uploaded_videos'
        # dest_vid_dir = 'labeled_videos'

        # venv_path = '/Users/atmavidyavirananda/Documents/Univ/Tingkat_4/Semester_8/TA_II/Code/YOLOv5/yolov5_env/bin/python'
        # script_file = f'../YOLOv5/yolov5/detect.py --source ../car_dmg_webapp/{src_vid_dir}/{uploaded_vid.name} --project ../car_dmg_webapp/{dest_vid_dir} --weights ../YOLOv5/yolov5/runs/train/yolo_car_dmg_plustf/weights/best.pt --conf 0.25 --name {uploaded_vid.name}'

        # subprocess.run(venv_path + ' ' + script_file, shell=True)
        
        # # prediction result
        # labeled_vid_dir = f'labeled_videos/{uploaded_vid.name}' 
        # vid_filename = os.listdir(labeled_img_dir)[0]
        # final_vid_path = os.path.join(labeled_img_dir, vid_filename)

        # st.write('Result')
        # st.video(final_vid_path)
