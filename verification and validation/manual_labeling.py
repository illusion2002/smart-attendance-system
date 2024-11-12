import os

# Define the directory containing your images
images_directory = 'path/to/images'

# Dictionary to map student names to lists of image filenames
student_images = {
    'John Doe': ['john_doe1.jpg', 'john_doe2.jpg', 'john_doe3.jpg'],
    'Jane Smith': ['jane_smith1.jpg', 'jane_smith2.jpg'],
    'Alice Johnson': ['alice_johnson1.jpg'],
    # Add more student names and corresponding lists of image filenames as needed
}

# Iterate through the student images dictionary
for student_name, image_filenames in student_images.items():
    print(f"Student: {student_name}")
    for filename in image_filenames:
        image_path = os.path.join(images_directory, student_name, filename)  # Update the image path
        print(f" - Image: {filename}, Path: {image_path}")


# Here's what you need to change:

# Update the directory path: Replace 'path/to/images' with the path to the directory containing your student image folders. Each student's images should be stored in a separate folder named after the student.

# Update the dictionary entries: Replace the placeholder student names ('John Doe', 'Jane Smith', 'Alice Johnson') and image filenames ('john_doe1.jpg', 'john_doe2.jpg', etc.) with the actual names and filenames from your dataset.

# Ensure consistency: Make sure that the image filenames specified in the dictionary match the actual filenames in your dataset directory.

# By making these changes, the script will correctly iterate through your dataset, printing each student's name along with the filenames and paths of their images.