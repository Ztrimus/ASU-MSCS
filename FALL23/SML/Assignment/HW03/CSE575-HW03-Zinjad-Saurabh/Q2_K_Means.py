'''
-----------------------------------------------------------------------
File: K_Means_Clustering.py
Creation Time: Dec 1st 2023 8:08 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
import pandas as pd
import numpy as np
import random 
import matplotlib.pyplot as plt
from typing import List, Dict

plt.switch_backend('TkAgg')

def calculate_euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def initialize_clusters(data, k):
    clusters = {}
    for cluster_idx in range(k):
        center_idx = random.randrange(int(cluster_idx * len(data) / k), int((cluster_idx + 1) * len(data) / k))
        clusters[cluster_idx] = {"center": data[center_idx], "points": []}
    return clusters

def update_clusters(clusters):
    for cluster_idx in clusters:
        clusters[cluster_idx]["center"] = np.mean(clusters[cluster_idx]["points"], axis=0)
        clusters[cluster_idx]["points"] = []

def calculate_loss(data, clusters):
    total = 0
    for point in data:
        distances = [calculate_euclidean_distance(clusters[cluster_idx]['center'], point) for cluster_idx in clusters]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx]['points'].append(point)

    for cluster_idx in clusters:
        tmp = np.sum((clusters[cluster_idx]["points"] - clusters[cluster_idx]["center"])**2)
        total += tmp

    return total

def k_means_clustering(data, k_values):
    k_cluster = {}
    k_loss = {}

    for k in k_values:
        clusters = initialize_clusters(data, k)
        prev_loss = float('inf')

        while True:
            loss = calculate_loss(data, clusters)
            k_loss.setdefault(k, []).append(loss)

            if loss >= prev_loss:
                k_cluster[k] = clusters
                break

            update_clusters(clusters)
            prev_loss = loss

    return k_cluster, k_loss

def plot_loss_trend(k_loss):
    for k_value, losses in k_loss.items():
        iterations = list(range(1, len(losses) + 1))
        losses_values = losses  # Use all losses without excluding the last one
        plt.plot(iterations, losses_values, label=f'k={k_value}', marker='+')

    plt.title("Loss Trend v/s k")
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

def plot_clusters(clusters):
    for cluster_idx, cluster in clusters.items():
        points = np.array(cluster["points"])
        center = cluster["center"]

        plt.scatter(points[:, 0], points[:, 1], label=f'Cluster {cluster_idx + 1}')
        plt.scatter(center[0], center[1], c='black', marker='x', s=400)

    plt.title("Clusters for K=2")
    plt.xlabel("Feature-1")
    plt.ylabel("Feature-2")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Read data
    df = pd.read_csv("CSE575-HW03-Data.csv", header=None)
    df_array = np.array(df)

    # Set K values
    K_values = [2, 3, 4, 5, 6, 7, 8, 9]

    # Perform K-means clustering
    k_cluster, k_loss = k_means_clustering(df_array, K_values)

    # Plot loss trend
    plot_loss_trend(k_loss)

    # Plot clusters for K=2
    plot_clusters(k_cluster[2])
