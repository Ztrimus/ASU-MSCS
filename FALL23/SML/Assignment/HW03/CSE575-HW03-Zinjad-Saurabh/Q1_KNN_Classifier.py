'''
-----------------------------------------------------------------------
File: Q1_KNN_Classifier.py
Creation Time: Dec 1st 2023 1:42 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''

""" # 1. Initial Setup """

# from google.colab import drive
# drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Project/HW-03

import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
from scipy.spatial.distance import cdist

"""# 2. All Necessary Functions"""

def load_mnist_images(file_path):
    """
    Load MNIST images from a binary file.

    Parameters:
    - file_path (str): Path to the binary file.

    Returns:
    - np.ndarray: Loaded image data in the specified format.
    """
    try:
        with open(file_path, 'rb') as file:
            file.read(16)
            image_size = 28
            train_data = np.frombuffer(file.read(), dtype=np.uint8).astype(np.float32)
            image_dim = len(train_data) // (image_size * image_size)
            return train_data.reshape(image_dim, image_size, image_size, 1)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def load_mnist_labels(file_path):
    """
    Load MNIST labels from a binary file.

    Parameters:
    - file_path (str): Path to the binary file.

    Returns:
    - list: List of loaded labels.
    """
    try:
        with open(file_path, 'rb') as file:
            file.read(8)
            return [str(i) for i in file.read()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def precompute_pairwise_distances(train_images, test_images):
    """
    Precompute pairwise distances between training and test images.

    Parameters:
    - train_images (np.ndarray): Training images data.
    - test_images (np.ndarray): Test images data.

    Returns:
    - np.ndarray: Pairwise distances between training and test images.
    """
    flattened_train = np.ravel(train_images).reshape(len(train_images), -1)
    flattened_test = np.ravel(test_images).reshape(len(test_images), -1)
    return cdist(flattened_train, flattened_test)

def predict_label(distances, train_labels, k):
    """
    Predict the label for a test image using precomputed distances.

    Parameters:
    - distances (np.ndarray): Precomputed pairwise distances.
    - train_labels (list): Training labels.
    - k (int): Number of neighbors to consider.

    Returns:
    - str: Predicted label.
    """
    img_index = np.argsort(distances)[:k]
    count = 0
    labels = {}
    prediction = ''

    for idx in img_index:
        label = train_labels[idx]
        if label not in labels:
            labels[label] = 1
        else:
            labels[label] += 1

        if labels[label] > count:
            count = labels[label]
            prediction = label

    return prediction

def train_and_evaluate_knn(train_images, test_images, train_labels, test_labels, k_values, distances):
    accuracy_map = {}


    for k in k_values:
        correct_predictions = 0
        progress_bar = trange(len(test_images), desc=f"Training Progress for k={k}", position=0)

        for i in range(len(test_images)):
            try:
                prediction = predict_label(distances[:, i], train_labels, k)
                if prediction == test_labels[i]:
                    correct_predictions += 1
            except Exception as e:
                print(f"Error predicting for test image {i}: {e}")

            progress_bar.update(1)

        try:
            accuracy = correct_predictions / len(test_images) * 100
            accuracy_map[k] = accuracy
            print(f"For k={k}, Accuracy: {accuracy:.2f}%")
        except ZeroDivisionError:
            print(f"Warning: Division by zero for k={k}, no test images provided.")

    return accuracy_map

def plot_accuracy_vs_k(accuracy_map):
    """
    Plot the accuracy versus k.

    Parameters:
    - accuracy_map (dict): Dictionary containing accuracy for each k value.
    """
    X, Y = list(accuracy_map.keys()), list(accuracy_map.values())

    plt.figure(num=None, figsize=(8, 8))
    plt.plot(X, Y, color='blue', marker='+')

    for i in range(len(X)):
        s = f"({X[i]}, {Y[i]:.2f})"
        plt.text(X[i] + 1, Y[i] - 0.04, s)

    plt.title("For each cluster K - accuracy plot.")
    plt.xlabel("k")
    plt.ylabel("Accuracy (in %)")
    plt.show()

"""# 3. Start Running Code"""

if __name__ == "__main__":
    try:
        train_images_path = './MNIST/train-images.idx3-ubyte'
        test_images_path = './MNIST/t10k-images.idx3-ubyte'
        train_labels_path = './MNIST/train-labels.idx1-ubyte'
        test_labels_path = './MNIST/t10k-labels.idx1-ubyte'

        train_images = load_mnist_images(train_images_path)
        test_images = load_mnist_images(test_images_path)
        train_labels = load_mnist_labels(train_labels_path)
        test_labels = load_mnist_labels(test_labels_path)

        """# 4. Efficient Pairwise Distance Computation for K-NN Optimization"""

        k_values = [1, 3, 5, 10, 20, 30, 40, 50, 60]
        distances = precompute_pairwise_distances(train_images, test_images)

        """# 5. Run k-NN Algorithm"""

        accuracy_map = train_and_evaluate_knn(train_images, test_images, train_labels, test_labels, k_values, distances)

        """#6. Visualize Result"""

        plot_accuracy_vs_k(accuracy_map)
    except Exception as e:
        print(f"Error: {e}")
