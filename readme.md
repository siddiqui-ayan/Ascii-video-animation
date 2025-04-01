# ASCII Video Player

A simple Python script that converts videos and GIFs into ASCII art and plays them in the terminal.

## Features
- Supports both **videos** and **GIFs**
- Converts frames to ASCII art in real-time
- Works directly in the terminal without additional UI dependencies

## Requirements
Make sure you have the following dependencies installed:

```sh
pip install -r requirements.txt
```

## Usage
Run the script and provide the path to the video or GIF file:

```sh
python main.py
```

Then enter the file path when prompted.

## How It Works
1. The script reads frames from a video (using OpenCV) or a GIF (using PIL).
2. Each frame is converted to grayscale and resized for ASCII conversion.
3. The script replaces pixel values with ASCII characters based on brightness.
4. The frames are displayed sequentially in the terminal.

## Example Output
When running the script, you'll see ASCII characters representing the video frames in your console
Original:

![vid2](https://github.com/user-attachments/assets/caf44ae1-e0cf-4bb2-9b2d-55957be6bbc5)


Output:

![output](https://github.com/user-attachments/assets/fb3fcb48-46fa-41b6-9441-374bb73b1db1)



## Notes
- The script automatically loops GIFs.
- Video playback speed may vary based on terminal performance.
- Works best on videos with high contrast and clear shapes.

## License
MIT License - Feel free to use and modify!

