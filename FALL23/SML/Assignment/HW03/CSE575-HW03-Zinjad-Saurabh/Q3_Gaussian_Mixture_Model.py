'''
-----------------------------------------------------------------------
File: Q3_GaussianMixtureModel.py
Creation Time: Dec 1st 2023 9:33 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math


def initialize_clusters(data, num_clusters):
    """
    Initialize clusters with random centers.

    Parameters:
    - data: Input data
    - num_clusters: Number of clusters

    Returns:
    Dictionary containing cluster information
    """
    clusters = {}
    for i in range(num_clusters):
        center_idx = random.randrange(int(i * 128 / num_clusters), int((i+1) * 128/ num_clusters))
        clusters[i] = {"center": data[center_idx], "points": []}
    return clusters


def update_cluster_centers(clusters):
    """
    Update cluster centers based on assigned data points.

    Parameters:
    - clusters: Dictionary containing cluster information

    Returns:
    Updated cluster dictionary
    """
    for index in clusters:
        clusters[index]["center"] = np.mean(clusters[index]["points"], axis=0)
        clusters[index]["points"] = []
    return clusters


def calculate_loss(data, clusters):
    """
    Calculate the total loss of the clustering.

    Parameters:
    - data: Input data
    - clusters: Dictionary containing cluster information

    Returns:
    Total loss of the clustering
    """
    total_loss = 0
    for point in data:
        distances = []
        for idx in clusters:
            distance = math.sqrt(np.sum((clusters[idx]["center"] - point) ** 2))
            distances.append(distance)
        idx = np.argmin(distances)
        clusters[idx]["points"].append(point)

    for idx in clusters:
        tmp_loss = np.sum((clusters[idx]["points"] - clusters[idx]["center"])**2)
        total_loss += tmp_loss

    return total_loss


def gaussian(x, mu, covariance):
    """
    Gaussian function for computing probabilities.

    Parameters:
    - x: Input data
    - mu: Mean vector
    - covariance: Covariance matrix

    Returns:
    Probability values
    """
    n = x.shape[1]
    diff = (x - mu).T
    return np.diagonal(1/((2*np.pi) ** (n/2) * np.linalg.det(covariance) ** 0.5) * np.exp(-0.5 * np.dot(np.dot(diff.T, np.linalg.inv(covariance)), diff))).reshape(-1, 1)


def mixture(data, clusters):
    """
    Execute one iteration of the EM algorithm for Gaussian Mixture Model.

    Parameters:
    - data: Input data
    - clusters: Dictionary containing cluster information

    Returns:
    Likelihood and log-likelihood values
    """
    totals = np.zeros((data.shape[0], 1), dtype=np.float64)

    for idx in clusters:
        pi = clusters[idx]["pi"]
        mu = clusters[idx]["mu"]
        covariance = clusters[idx]["covariance"]
        gamma = (pi * gaussian(data, mu, covariance))

        for i in range(len(data)):
            totals[i] += gamma[i]
        clusters[idx]["gamma"] = gamma
        clusters[idx]["totals"] = totals

    for idx in clusters:
        clusters[idx]["gamma"] /= clusters[idx]["totals"]

    N = float(len(data))

    for idx in clusters:
        gamma = clusters[idx]["gamma"]
        n = np.sum(gamma, axis=0)
        pi = n / N
        mu = np.sum(gamma * data, axis=0) / n
        covariance = np.zeros((data.shape[1], data.shape[1]))

        for i in range(len(data)):
            covariance += gamma[i] * np.dot((data[i] - mu).reshape(-1, 1), (data[i] - mu).reshape(-1, 1).T)
        covariance = covariance / n
        clusters[idx]["pi"] = pi
        clusters[idx]["mu"] = mu
        clusters[idx]["covariance"] = covariance

    totals = []

    for index in clusters:
        totals.append(clusters[index]["totals"])
    totals = np.array(totals)
    l = np.log(totals)
    return np.sum(l), l


def model_train(data, num_clusters, clusters, num_epochs):
    """
    Train the Gaussian Mixture Model.

    Parameters:
    - data: Input data
    - num_clusters: Number of clusters
    - clusters: Dictionary containing cluster information
    - num_epochs: Number of training epochs
    """
    likeli_hood = np.zeros((num_epochs,))

    for i in range(num_epochs):
        sum_l, _ = mixture(data, clusters)
        likeli_hood[i] = sum_l


def finalize_cluster_parameters(clusters, data_shape):
    """
    Finalize cluster parameters.

    Parameters:
    - clusters: Dictionary containing cluster information
    - data_shape: Shape of the input data
    """
    for idx in clusters:
        clusters[idx]["covariance"] = np.identity(data_shape[1], dtype=np.float64)
        clusters[idx]["mu"] = clusters[idx]["center"]
        clusters[idx]["pi"] = 1.0 / len(clusters)
        del clusters[idx]["center"]


def assign_data_points(data, clusters):
    """
    Assign data points to clusters.

    Parameters:
    - data: Input data
    - clusters: Dictionary containing cluster information

    Returns:
    Updated cluster dictionary
    """
    for point in data:
        distances = []
        for i in clusters:
            d = math.sqrt(np.sum((clusters[i]["center"] - point)**2))
            distances.append(d)
        i = np.argmin(distances)
        clusters[i]["points"].append(point)
    
    return clusters


def plot_clusters(clusters):
    """
    Plot the clusters and their centers.

    Parameters:
    - clusters: Dictionary containing cluster information
    """
    plt.figure(figsize=(10, 8))

    for idx in clusters:
        color = "red" if idx == 0 else "blue"
        marker = "o" if idx == 0 else "s"

        plt.scatter(
            np.array(clusters[idx]["points"])[:, 0],
            np.array(clusters[idx]["points"])[:, 1],
            label=f'Cluster {idx + 1}',
            c=color,
            marker=marker,
            alpha=0.7,
            edgecolors='k',
        )

        center_marker = "*" if idx == 0 else "D"
        center_color = "gold" if idx == 0 else "limegreen"
        center_size = 240 if idx == 0 else 200
        plt.scatter(
            [clusters[idx]["center"][0]],
            [clusters[idx]["center"][1]],
            c=center_color,
            marker=center_marker,
            s=center_size,
            label=f'Cluster {idx + 1} Center',
            edgecolors='k',
        )

    plt.title("Gaussian Mixture Model Clustering for K = 2")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.show()

def main():
    try:
        tmp_data = pd.read_csv(
            "/home/saurabh/ASU-MSCS/FALL23/SML/Assignment/HW03/CSE575-HW03-Data.csv",
            header=None,
        )
        data = np.array(tmp_data)

        num_epochs = 50
        num_clusters = 2
        k_loss = {}

        clusters = initialize_clusters(data, num_clusters)
        l = calculate_loss(data, clusters)
        k_loss[num_clusters] = [l]

        while True:
            prev_cluster = clusters
            clusters = update_cluster_centers(clusters)
            prev_loss = l
            l = calculate_loss(data, clusters)
            k_loss[num_clusters].append(l)

            if l >= prev_loss:
                clusters = prev_cluster
                break

        for k in k_loss:
            l = []
            for i in range(1, len(k_loss[k]) + 1):
                l.append(i)
        
        finalize_cluster_parameters(clusters, data.shape)

        model_train(data, num_clusters, clusters, num_epochs)

        for i in clusters:
            clusters[i]["center"] = clusters[i]["mu"]

        clusters = assign_data_points(data, clusters)
        print(f"clusters: {clusters}")
        plot_clusters(clusters)

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: Empty dataset. Please check the file content.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
