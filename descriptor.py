# descriptor.py
import cv2
import numpy as np
from skimage.feature import graycomatrix, graycoprops
from Bitdesc import bio_taxo

def glcm(image):
    co_matrix = graycomatrix(image, [1], [0], symmetric=True, normed=True)
    diss = graycoprops(co_matrix, 'dissimilarity')[0, 0]
    cont = graycoprops(co_matrix, 'contrast')[0, 0]
    corr = graycoprops(co_matrix, 'correlation')[0, 0]
    ener = graycoprops(co_matrix, 'energy')[0, 0]
    asm = graycoprops(co_matrix, 'ASM')[0, 0]
    homo = graycoprops(co_matrix, 'homogeneity')[0, 0]
    return [diss, cont, corr, ener, asm, homo]

def bitdesc(image):
    return bio_taxo(image)  

def haralick(image):
    glcm = graycomatrix(image, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)

# Extract Haralick features
    haralick_features = []
    props = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
    for prop in props:
        haralick_features.append(graycoprops(glcm, prop).mean())

    return haralick_features

def concatenate_descriptors(image):
    glcm_features = glcm(image)
    bitdesc_features = bitdesc(image)
    haralick_features = haralick(image)
    
    # Concatenate the feature vectors
    return glcm_features + bitdesc_features + haralick_features
