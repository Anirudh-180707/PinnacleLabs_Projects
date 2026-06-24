# 🚗 Road Lane Detection Using OpenCV

## 📌 Overview

This project is a Computer Vision-based Road Lane Detection System developed using Python, OpenCV, and NumPy. The system processes road images and identifies lane markings using image processing techniques such as grayscale conversion, Gaussian blurring, edge detection, and Hough Line Transform.

The objective of this project is to detect and highlight road lane lines from road images, which is a fundamental component of Advanced Driver Assistance Systems (ADAS) and autonomous driving technologies.

---

## 🎯 Features

* Road lane line detection from images
* Image preprocessing using OpenCV
* Edge detection using Canny Edge Detection
* Lane extraction using Hough Line Transform
* Automatic processing of multiple road images
* Output image generation with detected lane markings

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy

---

## 📂 Dataset

This project utilizes road images from the Indian Road Dataset available on Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/mansayy/indian-road-dataset

### Dataset Information

The dataset contains a collection of Indian road images and videos with clearly visible lane markings that can be used for lane detection and computer vision applications.

### Note

The original dataset is quite large in size and exceeds practical GitHub repository limits. Uploading the complete dataset would significantly increase repository size and affect cloning performance.

Therefore, the dataset has not been included in this repository.

Please download the dataset directly from the Kaggle link above and extract it into the project directory before running the program.

Expected folder structure:

```text
Road-Lane-Detection/
│
├── data/
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── image3.jpg
│   └── ...
│
├── output/
├── main.py
└── README.md
```

---

## ⚙️ Working Principle

The system follows the following pipeline:

1. Load road image
2. Convert image to grayscale
3. Apply Gaussian Blur
4. Perform Canny Edge Detection
5. Detect lane lines using Hough Line Transform
6. Draw detected lane markings
7. Save processed output image

---

## ▶️ Installation

Install the required libraries:

```bash
pip install opencv-python numpy
```

---

## ▶️ Running the Project

Execute the program using:

```bash
python main.py
```

The program will automatically process all supported images located inside the dataset folder and generate output images containing the detected lane markings.

---

## 📁 Output

Processed images with highlighted lane lines will be stored in the:

```text
output/
```

directory.

---

## 📚 Learning Outcomes

* Image Processing Fundamentals
* Edge Detection Techniques
* Computer Vision using OpenCV
* Hough Line Transform
* Road Lane Detection Systems
* Autonomous Driving Concepts

---

## 🚀 Future Enhancements

* Real-time lane detection using video streams
* Lane curvature estimation
* Deep Learning-based lane detection
* Autonomous vehicle integration
* Live webcam support

---

## 👨‍💻 Author

Anirudh L

Project completed as part of the Pinnacle Labs Internship Program.
