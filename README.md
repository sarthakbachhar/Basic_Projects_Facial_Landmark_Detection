# Facial Landmark Detection with OpenCV

This project demonstrates facial landmark detection using OpenCV's Haar Cascade Classifier and Local Binary Features (LBF) model. It detects faces and landmarks on the face, displaying the results with landmarks plotted on the image.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Pre-trained LBF model (`lbfmodel.yaml`)
- Haar Cascade Classifier for face detection (`haarcascade_frontalface_default.xml`)

## Features

- **Face Detection**: Uses a pre-trained Haar Cascade Classifier to detect faces in an image.
- **Landmark Detection**: Identifies facial landmarks using the LBF model.

## Usage

1. Update the file paths for the image, Haar Cascade XML, and LBF model in the code.
2. Run the script:

   ```bash
   python facial_landmark_detection.py

3. The image with detected landmarks will be displayed.

## License

This project is licensed under the MIT License.
