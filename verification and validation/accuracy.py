import cv2
import os
import numpy as np

# Function to load images from a directory and assign labels
def load_images_from_folder(folder):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isdir(img_path):
            continue
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
            labels.append(int(filename.split('_')[0]))  # Extract label from filename
    return images, labels

# Load images and corresponding labels
images, labels = load_images_from_folder('images_folder')

# Create LBPH face recognizer
lbph = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer
lbph.train(images, np.array(labels))

# Function to predict labels for new images
def predict_labels(images):
    predicted_labels = []
    for img in images:
        label, _ = lbph.predict(img)
        predicted_labels.append(label)
    return predicted_labels

# Load new test images
test_images, test_labels = load_images_from_folder('test_images_folder')

# Predict labels for test images
predicted_labels = predict_labels(test_images)

# Compare predicted labels with true labels
accuracy = np.mean(np.array(predicted_labels) == np.array(test_labels)) * 100
print("Accuracy:", accuracy)

#Note: Make sure to replace 'images_folder' and 'test_images_folder' with the paths to your image folders containing training and test images, respectively.#
# Also, ensure that your images are properly labeled according to a consistent naming convention for this code to work correctly.