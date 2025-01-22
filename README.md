# Content-Based Image Retrieval (CBIR) Project

## Overview

The Content-Based Image Retrieval (CBIR) project is a Python application designed to retrieve visually similar images from a dataset based on the content of a query image. Built with **Streamlit**, this interactive tool utilizes advanced image descriptors like **GLCM**, **BitDesc**, and **Haralick**, combined with **LDA classification**, to deliver accurate and efficient retrieval.

## Dataset

This project uses an image dataset that can be stored locally or on the cloud.

## Features

- **Image Upload**: Upload an image as a query.
- **Feature Extraction**: Choose from GLCM, BitDesc, or Haralick for content analysis.
- **LDA Classification**: Classify images to improve retrieval accuracy.
- **Visualization**:
  - Retrieve and display similar images.
  - View a bar graph illustrating the folder-wise distribution of similar images.

## How to Use

1. **Upload an Image**: Select an image file using the upload widget.
2. **Select a Descriptor**: Choose a feature extraction method (e.g., GLCM, BitDesc, Haralick).
3. **Retrieve Results**: View the most similar images alongside statistical insights.

## Installation

### Prerequisites

Ensure **Python 3.8+** is installed on your system.

## Technologies Used

- **Programming Language**: Python
- **Frontend Framework**: Streamlit
- **Libraries**:
  - **NumPy**: Numerical operations
  - **OpenCV**: Image processing
  - **Scikit-learn**: Machine learning algorithms
  - **Matplotlib**: Data visualization
  - **Pillow**: Image file handling

## License

This project is licensed under the [MIT License](LICENSE).
