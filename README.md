# ai-powered-forgery-detection
# INTRODUCTION
This project detects forged or tampered JPEG images using Error Level Analysis (ELA) and a simple Python-based GUI. It is built as a personal project to apply image forensics and basic machine learning concepts in real-world scenarios.

# Key Features
Detects tampered or modified areas in JPEG images
Uses Error Level Analysis (ELA) technique
GUI built with Tkinter for ease of use
Supports image upload, analysis, and side-by-side comparison
Exports results with visual ELA image
Packaged as .exe for offline desktop use

# Tech Stack & Tools
Python

PIL (Python Imaging Library)

Tkinter

OpenCV

Numpy

Error Level Analysis (ELA)

PyInstaller (for .exe packaging)

# How It Works
1. User uploads a JPEG image
2. ELA analysis is applied to detect compression differences
3. These differences help highlight potential forged areas
4. The GUI displays:
Original image
ELA result
Tampering verdict (forged / genuine)
