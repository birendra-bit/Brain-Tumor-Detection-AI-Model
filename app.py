import streamlit as st 
from io import StringIO
from PIL import Image
import os
from datetime import datetime
from make_prediction import make_prediction
import time


st.sidebar.title(":green[Upload Section]")
uploaded_file = st.sidebar.file_uploader(":green[Upload MRI Image]", type=["jpg", "jpeg", "png", "tif"])
ct = st.container()
ct.title(':green[AI Model to Detect Brain Tumor]')
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    ct.image(image, caption='MRI Image Uploaded')
    
    upload_directory = "mri_image_folder"
    
    # rename image and save it 
    now = datetime.now()
    iso_format = now.strftime("%Y-%m-%dT%H:%M:%S")
    file_name = str(iso_format)
    file_name = file_name.replace('-', '_')
    file_name = file_name.replace(':', '_')
    file_name = file_name + '_' + str(uploaded_file.name)
    file_path = os.path.join(upload_directory, file_name)
    image.save(file_path)
    
    ct.success("Image Upload Successful") 

    if ct.button("Check Tumor",type="primary"):
        
        ct.write(":green[Checking...]")
        # progress_bar = st.progress(0)

        # for percent_complete in range(100):
        #     time.sleep(0.05)  # Simulate a delay for the progress bar
        #     progress_bar.progress(percent_complete + 1)
        
        predicted_value = make_prediction(file_path)
        ct.subheader(':green[Result From the Model]')
        if predicted_value > 0:
            ct.warning(":red[The model predicts that the image **Has** a brain tumor.]")
        else:
            ct.info(":green[The model predicts that the image **Does Not Have** a brain tumor.]")
    