import streamlit as st
import cv2
import time
from datetime import datetime
import numpy as np

source = 0
title = "Opencv Video Straming"

def vision(frame):
    '''
    Write your cv code here to change the frames
    '''
    return frame

def video_stream():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(source)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    # Create a placeholder for the video frames
    count = 0
    prev = 0
    frame_placeholder = st.empty()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Convert the frame to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame_rgb = vision(frame_rgb)
        frame_placeholder.image(frame_rgb, channels="RGB")
        # Sleep for a short duration so that the Streamlit interface can update
        time.sleep(0.01)

    # Release the VideoCapture object
    cap.release()

def main():
    st.title(title)
    # Start the video stream
    video_stream()

if __name__ == "__main__":
    main()
