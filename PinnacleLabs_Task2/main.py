import cv2
import numpy as np
import os

# Input and output folders
input_folder = "data"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

# Process all images in data folder
for filename in os.listdir(input_folder):

    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(input_folder, filename)

        image = cv2.imread(image_path)

        if image is None:
            continue

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Blur image
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Edge detection
        edges = cv2.Canny(blur, 50, 150)

        # Detect lines
        lines = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi / 180,
            threshold=50,
            minLineLength=50,
            maxLineGap=20
        )

        # Draw detected lines
        line_image = image.copy()

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(
                    line_image,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    3
                )

        # Save output
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, line_image)

        print(f"Processed: {filename}")

print("\nLane detection completed!")
print("Results saved in 'output' folder.")