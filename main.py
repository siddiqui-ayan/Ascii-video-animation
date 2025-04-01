import cv2
import numpy as np
import os
from PIL import Image, ImageSequence
import time

ASCII_CHARS = "@%#*+=-:. "[::-1]

# convert each individual frame to ASCII characters
def imgToAscii(image, new_width=120):
    image = image.convert("L")  
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5) 
    image = image.resize((new_width, new_height))
    pixels = np.array(image)
    ascii_str = "".join(ASCII_CHARS[min(len(ASCII_CHARS) - 1, pixel // (256 // len(ASCII_CHARS)))] for pixel in pixels.flatten())
    
    ascii_image = "\n".join(ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width))
    return ascii_image

# Play all the Ascii frames
def playAsciiVideo(video_path, new_width=120):  
    if video_path.lower().endswith(".gif"): 
        gif = Image.open(video_path)
        frames = [frame.copy().convert("RGB") for frame in ImageSequence.Iterator(gif)]
        frame_rate = gif.info.get("duration", 100) // 10
    else:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            return
    
    frame_index = 0
    try:
        while True:
            if video_path.lower().endswith(".gif"):
                frame_rgb = np.array(frames[frame_index % len(frames)])
                frame_index += 1
                
            else:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
            image = Image.fromarray(frame_rgb)
            ascii_frame = imgToAscii(image, new_width)
            
            os.system("cls" if os.name == "nt" else "clear")

            print(ascii_frame)
            
            if video_path.lower().endswith(".gif"):
                time.sleep(frame_rate / 100)
            else:
                time.sleep(1 / 30)
                # play at 30 frames per second 
    
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        if not video_path.lower().endswith(".gif"):
            cap.release()


if __name__ == "__main__":
    video_path = input("Enter video file path: ")
    playAsciiVideo(video_path)