import cv2

# Load image 
img = cv2.imread("C:\\Users\\Acer\\Desktop\\Project 20\\elon.jpg")

# Resize image
img = cv2.resize(img, (512,512))

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the Haar Cascade model for face detection
harcascade = "C:\\Users\\Acer\\Desktop\\Project 20\\haarcascade_frontalface_default.xml"

detector = cv2.CascadeClassifier(harcascade)

# Detect faces in the image 
faces = detector.detectMultiScale(img_gray)

# Load the LBF model for facial landmark detection
LBF_model = "C:\\Users\\Acer\\Desktop\\Project 20\\lbfmodel.yaml"
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel(LBF_model)

# Check if faces are detected 
if len(faces) > 0:
    # Detect landmarks on the original image
    _, landmarks = landmark_detector.fit(img, faces)

    # Loop through the landmarks and draw circles on the image 
    for landmark in landmarks:
        for (x, y) in landmark[0]:
            # Convert the coordinates to integers
            x = int(x)
            y = int(y)
            # Draw small green circles on each landmark point
            cv2.circle(img, (x, y), 2, (0, 255, 0), 2)

    # Display the image with landmarks
    cv2.imshow('Face with Landmarks', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No faces detected")