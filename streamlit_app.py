# This page is mainly for my streamlit user interface
import streamlit as st
from input_parameters import user_input_parameters
from descriptor import glcm, bitdesc, haralick, concatenate_descriptors
from distances import manhattan, euclidean, chebyshev, canberra, retrieve_similar_images
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

# Load signatures
glcm_signatures = np.load('glcm_signatures.npy', allow_pickle=True)
bitdesc_signatures = np.load('bitdesc_signatures.npy', allow_pickle=True)
haralick_signatures= np.load('haralick_signatures.npy', allow_pickle=True)
concatenated_signatures = np.load('concatenated_signatures.npy', allow_pickle=True)


descriptor_funcs = {
    "GLCM": glcm,
    "Bitdesc": bitdesc,
    "Haralick": haralick,
    "Concatenated": concatenate_descriptors
}
distance_funcs = {"Manhattan": manhattan, "Euclidean": euclidean, "Chebyshev": chebyshev, "Canberra": canberra}


def plot_folder_distribution(similar_images):
    # Count how many images come from each folder
    folder_counts = {}
    for _, _, label in similar_images:
        folder_counts[label] = folder_counts.get(label, 0) + 1
    
    # Plotting the bar graph
    fig, ax = plt.subplots()
    ax.bar(folder_counts.keys(), folder_counts.values())
    ax.set_xlabel('Folder')
    ax.set_ylabel('Number of Images')
    ax.set_title('Distribution of Similar Images')
    st.pyplot(fig)



def main():
    st.set_page_config(page_title='Image Search', page_icon=':camera:')
    st.title(':green[Content-Based Image Retrieval]')
    
    # File uploader with multiple extensions
    file = st.file_uploader("Upload a file", type=["csv", "txt", "jpg", "png"])
    
    # to display the sidebar, the options and taking the different inputs
    input_values = user_input_parameters()
    
    # dsiplaying values on checkboxes
    st.write("Selected Options:")
    st.write(input_values)
    
    if file is not None:
        # Read the uploaded image
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), 0)
        
        # Extract features based on the chosen descriptor
        descriptor_func = descriptor_funcs[input_values["Descriptor"]]
        query_features = descriptor_func(img)
        
        # Choose the signature
        if input_values["Descriptor"] == "Concatenated":
            signature_db = concatenated_signatures
        elif input_values["Descriptor"] == "GLCM":
            signature_db = glcm_signatures
        elif input_values["Descriptor"] == "Bitdesc":
            signature_db = bitdesc_signatures
        elif input_values["Descriptor"] == "Haralick":
            signature_db = haralick_signatures
        # Choose the correct distance function
        distance_func = distance_funcs[input_values["Distance"]]
        
        # retrieve the "similar" images
        similar_images = retrieve_similar_images(signature_db, query_features, distance_func, input_values["Number"])
        
        
        st.write(f"Extracted features: {query_features}")
        
        # Display the similar images in rows of 3
        st.write("Similar images:")
        for i in range(0, len(similar_images), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(similar_images):
                    img_path, dist, label = similar_images[i + j]
                    full_img_path = os.path.join('./dataset', img_path)  
                    st.write(f"Displaying image from: {full_img_path}")
                    if os.path.exists(full_img_path):
                        cols[j].image(full_img_path, caption=f"Similar image {i + j + 1} with distance {dist}")
                    else:
                        cols[j].write(f"Image not found: {full_img_path}")
        plot_folder_distribution(similar_images)
        
        

    


if __name__ == '__main__':
    main()

#to be deploted on the 21st of january 2025(delete this later)