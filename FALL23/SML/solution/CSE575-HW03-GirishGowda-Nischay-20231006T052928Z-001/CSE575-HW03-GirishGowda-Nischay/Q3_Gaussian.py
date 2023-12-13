import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math


def loss_function(data, clusters):
    for p in data:
        tmp_list = []
        for idx in clusters:
            distance = math.sqrt(np.sum((clusters[idx]["center"] - p)**2))
            tmp_list.append(distance)
        idx = np.argmin(tmp_list)
        clusters[idx]["points"].append(p)
    total = 0
    for idx in clusters:
        tmp = np.sum((clusters[idx]["points"] - clusters[idx]["center"])**2)
        total += tmp
    return total

def gaussian(x, mu, conv):
    n = x.shape[1]
    diff = (x-mu).T
    return np.diagonal(1/((2*np.pi) ** (n/2) * np.linalg.det(conv) ** 0.5) * np.exp(-0.5 * np.dot(np.dot(diff.T, np.linalg.inv(conv)), diff))).reshape(-1,1)

def mixture(data, clusters):
    totals = np.zeros((data.shape[0],1), dtype = np.float64)
    for idx in clusters:
        pi = clusters[idx]["pi"]
        mu = clusters[idx]["mu"]
        conv = clusters[idx]["conv"]
        gamma = (pi * gaussian(data, mu, conv))
        for i in range(len(data)):
            totals[i] += gamma[i]
        clusters[idx]["gamma"] = gamma
        clusters[idx]["totals"] = totals
    for idx in clusters:
        clusters[idx]["gamma"] /= clusters[idx]["totals"]
    N = float(len(data))
    for idx in clusters:
        gamma = clusters[idx]["gamma"]
        n = np.sum(gamma, axis = 0)
        pi = n/N
        mu = np.sum(gamma * data, axis = 0)/n
        conv = np.zeros((data.shape[1], data.shape[1]))
        for i in range(len(data)):
            conv += gamma[i] * np.dot((data[i] - mu).reshape(-1,1), (data[i] - mu).reshape(-1,1).T)
        conv = conv/n
        clusters[idx]["pi"] = pi
        clusters[idx]["mu"] = mu
        clusters[idx]["conv"] = conv

    totals = []
    for index in clusters:
        totals.append(clusters[index]["totals"])
    totals = np.array(totals)
    l = np.log(totals)
    return np.sum(l), l

def model_train(data, k, clusters, n_epochs):
    likeli_hood = np.zeros((n_epochs,))
    scores = np.zeros((data.shape[0], k))

    for i in range(n_epochs):
        sum_l, l = mixture(data, clusters)
        likeli_hood[i] = sum_l

tmp_data = pd.read_csv("CSE575-HW03-Data.csv", header = None)
data = np.array(tmp_data)
n_epochs = 50

k = 2
k_loss = {}
clusters = {}

for i in range(k):
    cluster_center_idx = random.randrange(int(i * 128 / k), int((i+1) * 128/ k))
    clusters[i] = {"center":data[cluster_center_idx], "points":[]}
l = loss_function(data, clusters)

k_loss[k] = [l]
while True:
    prev_cluster = clusters
    for index in clusters:
        clusters[index]["center"] = np.mean(clusters[index]["points"], axis = 0)
        clusters[index]["points"] = []
    prev_loss = l
    l = loss_function(data, clusters)
    k_loss[k].append(l)
    if l >= prev_loss:
        clusters = prev_cluster
        break

for k in k_loss:
    l = []
    for i in range(1, len(k_loss[k]) + 1):
        l.append(i)

for idx in clusters:
    clusters[idx]["conv"] = np.identity(data.shape[1], dtype = np.float64)
    clusters[idx]["mu"] = clusters[idx]["center"]
    clusters[idx]["pi"] = 1.0/k
    del clusters[idx]["center"]

model_train(data, k, clusters, n_epochs)

for i in clusters:
    clusters[i]["center"] = clusters[i]["mu"]

for p in data:
    distances = []
    for i in clusters:
        d = math.sqrt(np.sum((clusters[i]["center"] - p)**2))
        distances.append(d)
    i = np.argmin(distances)
    clusters[i]["points"].append(p)

plt.figure(figsize=(9,9), num=None)
plt.scatter(np.array(clusters[0]["points"])[:,:2][:,0], np.array(clusters[0]["points"])[:,:2][:,1], c = "red", marker="x")
plt.scatter(np.array(clusters[1]["points"])[:,:2][:,0], np.array(clusters[1]["points"])[:,:2][:,1], c = "blue", marker="o")
plt.scatter([clusters[0]["center"][:2][0]], [clusters[0]["center"][:2][1]], c="black", marker='X', s=400)
plt.scatter([clusters[1]["center"][:2][0]], [clusters[0]["center"][:2][1]], c="black", marker='o', s=400)
plt.title("For k = 2 plot.")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()


