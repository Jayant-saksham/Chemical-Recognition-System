# Tesseract OCR Installation Guide for macOS

Welcome to the Tesseract OCR installation guide for macOS! This guide provides comprehensive instructions to install Tesseract OCR and its Python packages, enabling you to perform optical character recognition (OCR) tasks on your macOS system.

## Installation Steps

### Step 1: Install Tesseract using Homebrew

First, let's install Tesseract using Homebrew, a popular package manager for macOS.

```bash
brew install tesseract
```

This command will download and install the Tesseract OCR engine on your system. Please note that the installation process may take around 15 minutes to complete.

### Step 2: Install Tesseract Python Packages

To interact with Tesseract using Python, we need to install the relevant Python packages. Execute the following command to install the required packages:

```bash
pip3 install pytesseract
pip3 install tesseract-ocr
```

These commands will install the `pytesseract` package, providing a Python interface to Tesseract, and the `tesseract-ocr` package, which includes the Tesseract OCR engine.

## Project Features

### Capture and Store Images

This project allows you to capture images using a camera and store them in the `static` folder of your Flask application. These captured images can then be utilized for OCR tasks to extract ingredients mentioned within them.

### Required Packages

Ensure that you have the following packages installed in your Python environment:

- Flask: A web framework for Python.
- OpenCV: A library for computer vision tasks, used for capturing images from the camera.
- Pillow: A Python Imaging Library (PIL) fork, required for image processing tasks.
- pytesseract: A Python wrapper for the Tesseract OCR engine, used for extracting text from images.

## Folder Structure

Make sure to create an `uploads` folder in your project directory. This folder will be utilized to temporarily store uploaded images before processing them.
