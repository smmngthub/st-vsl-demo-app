# Bismillahirrahumanirrahim

import streamlit as st
from PIL import Image
import os

st.title(":blue[You are in Photo Upload Section]") # :red

def load_image(image_file):
  img = Image.open(image_file)
  return img

image_file = st.file_uploader("Upload an Image", type=["png", "jpeg", "jpeg"])
if image_file is not None:
  file_details = {"File Name": image_file.name,
                 "File Type": image_file.type,
                 "File Size": image_file.size,
                 "File ID": image_file.file_id}
 
  img = load_image(image_file)
  st.image(img, use_container_width=150)

  with open(os.path.join("images", image_file.name), "wb") as f:
    f.write(image_file.getbuffer())
  
  st.write(file_details)
  st.download_button("Download Image", data=image_file, file_name='ZZZ_download.png', mime='image/png')
  st.success("File Saved")

  # video_file = open("myvideo.mp4", "rb")
  # video_bytes = video_file.read()

  # st.video(video_bytes)

  # VIDEO_URL = "https://example.com/not-youtube.mp4"
  # st.video(VIDEO_URL, subtitles="subtitles.vtt")

