# Content-Based Image Retrieval (CBIR) Project

## Overview

The Content-Based Image Retrieval (CBIR) project is a Python application designed to retrieve visually similar images from a dataset based on the content of a query image. Built with **Streamlit**, this interactive tool utilizes advanced image descriptors like **GLCM**, **BitDesc**, and **Haralick**, combined with **LDA classification**, to deliver accurate and efficient retrieval. It is an AI-powered computer vision system that automates feature extraction, classification, and similarity matching for images.

## Dataset

This project uses an image dataset that can be stored locally or on the cloud.

## Features

- **AI-Powered Feature Extraction**: Automates content analysis using GLCM, BitDesc, or Haralick descriptors.
- **LDA Classification**: Leverages Linear Discriminant Analysis to improve retrieval accuracy.
- **Interactive Visualization**:
  - Retrieves and displays similar images.
  - Shows a bar graph illustrating folder-wise distribution of similar images.
- **Scalable Design**: Efficiently handles datasets of varying sizes.

## How to Use

1. **Upload an Image**: Select an image file using the upload widget.
2. **Select a Descriptor**: Choose a feature extraction method (e.g., GLCM, BitDesc, Haralick).
3. **Retrieve Results**: View the most similar images alongside statistical insights.

## Screenshots

1. **User Interface**  
   ![UI 1](screenshots/UI%201.png)  
   ![UI 2](screenshots/UI%202.png)

2. **Image Upload Process**  
   ![Uploading a Picture](screenshots/uploading%20a%20picture.png)

3. **Results Visualization**
   - Similar Images Retrieved:  
     ![Similar Images Displayed](screenshots/similar%20images%20displayed.png)
   - Source Distribution Graph:  
     ![Source Distribution Graph](screenshots/source%20distribution%20graph.png)

## Demo Video

Watch the full demo video [here]((https://www.youtube.com/watch?v=tAgrRCHSZtg)).

## Installation

### Prerequisites

Ensure **Python 3.8+** is installed on your system.

Follow these steps to set up the project locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/HoussamImhiouach/CBIR-final.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd CBIR-final
   ```

3. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Technologies Used

This project integrates multiple technologies from the fields of AI, computer vision, and web development:

- **Programming Language**:

  - Python 3.8+

- **Libraries and Frameworks**:

  - **Streamlit**: For building an interactive user interface.
  - **NumPy**: For numerical operations.
  - **OpenCV**: For image processing.
  - **Scikit-learn**: For implementing LDA classification and other machine learning techniques.
  - **Matplotlib**: For data visualization.
  - **Pillow**: For image file handling.
  - **Mahotas**: For Haralick descriptor calculations.
  - **BitDesc**: For feature extraction using bio-inspired descriptors.
  - **Seaborn**: For enhancing visualizations.

- **Tools**:
  - **GitHub**: For version control and collaboration.
  - **Streamlit Cloud**: For deployment (if hosted).
  - **VS Code**: As the primary development environment.

## Directory Structure

The project is structured as follows:

```
CBIR-final/
├── dataset/                  # Contains the image dataset used by the app
├── app.py                   # Main Python script for running the app
├── app_distance.py          # Script for distance calculations
├── data_processing.py       # Script for data preprocessing
├── descriptor.py            # Script for feature extraction (GLCM, BitDesc, etc.)
├── distances.py             # Contains distance metrics
├── input_parameters.py      # Handles input parameters for the app
├── streamlit_app.py         # Main Streamlit UI script
├── requirements.txt         # Dependencies for the project
├── packages.txt             # Additional packages needed for deployment
├── README.md                # Documentation for the project
└── <other files/directories>
```

## Usage

1. **Start the Streamlit App**:

   ```bash
   streamlit run streamlit_app.py
   ```

2. **Upload an Image**: Use the interface to upload a query image.

3. **View Results**: The app will display images from the dataset that are similar to the uploaded image.

## Challenges Faced

- **Dependency Management**: Resolving conflicts between required packages and ensuring compatibility with Streamlit Cloud.
- **Module Import Issues**: Adjusting paths and fixing case-sensitive imports during deployment.
- **Dataset Handling**: Organizing and processing a large dataset efficiently for real-time querying.
- **Visualization**: Creating an intuitive UI for both image retrieval and statistical insights.

## Lessons Learned

- Gained expertise in setting up and deploying Streamlit applications.
- Learned to troubleshoot and resolve Python package issues effectively.
- Improved understanding of image descriptors and their application in CBIR systems.
- Enhanced skills in optimizing project structure for better maintainability.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request for review.

## Acknowledgments

- [BitDesc Documentation](https://pypi.org/project/Bitdesc/)
- [GLCM and Haralick Descriptor References]

## Future Enhancements

- Add support for more advanced descriptors.
- Optimize for larger datasets.
- Enhance the UI with additional visualization options.
