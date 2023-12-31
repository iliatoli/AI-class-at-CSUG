'''
I genuinely had difficulty determining 'path_to_your_image.jpg'
in this case, but it worked with other links from the web.


Write Python code to import this image. Download this image.
Write Python code to display the image.
Write Python code to write a copy of the image to any directory on your desktop.
'''

'''
ILIA TOLI
comment, uncomment as appropriate to check the three programs below.
'''

import cv2
import os

# Path to the image you want to work with
image_path = 'path_to_your_image.jpg'  # Replace with your image path

def display_image(image):
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(image, output_dir):
    # Check if the directory exists, create it if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, 'image_copy.jpg')
    cv2.imwrite(output_path, image)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    # Load the image
    img = cv2.imread(image_path)

    # Display the image
    display_image(img)

    # Save a copy of the image to a directory on the desktop
    desktop_directory = os.path.join(os.path.expanduser('~'), 'Desktop')  # Path to desktop
    output_directory = os.path.join(desktop_directory, 'image_copies')  # Folder name for image copies
    save_image(img, output_directory)
