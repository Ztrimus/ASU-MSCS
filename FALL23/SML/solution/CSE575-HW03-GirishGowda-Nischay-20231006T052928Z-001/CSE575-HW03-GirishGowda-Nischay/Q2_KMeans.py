
import pandas as pd
import numpy as np
import random 
import matplotlib.pyplot as plt
import math


def loss_function(data, clusters):

    for p in data:
        res = []
        for idx in clusters:
            distance = math.sqrt(np.sum((clusters[idx]['center'] - p)**2))
            res.append(distance)
        idx = np.argmin(res)
        clusters[idx]['points'].append(p)
    total = 0
    for i in clusters:
        tmp = np.sum((clusters[i]["points"] - clusters[i]["center"])**2)
        total += tmp
    return total

# given in pdf.
K = [2,3,4,5,6,7,8,9]
k_cluster = {}
k_loss = {}

df = pd.read_csv("CSE575-HW03-Data.csv", header = None)
df_array = np.array(df)


for k in K:
    clusters = {}
    for i in range(k):
        cluster_center_idx = random.randrange(int(i*128/k), int((i+1)*128/k))
        clusters[i] = {"center": df_array[cluster_center_idx], "points": []}
    l = loss_function(df_array, clusters)
    k_loss[k] = [l]

    while True:
        prev_cluster = clusters
        for idx in clusters:
            clusters[idx]["center"] = np.mean(clusters[idx]["points"], axis = 0)
            clusters[idx]["points"] = []
        prev_loss = 1
        l = loss_function(df_array, clusters)
        k_loss[k].append(l)
        # loss is expected to reduce as K value increases.
        if l >= prev_loss:
            k_cluster[k] = prev_cluster
            break

# Calculating loss for all K.
for k in k_loss:
    # print("k =" + str(k))
    l = []
    for i in range(1, len(k_loss[k]) + 1):
        l.append(i)


X = []
for i in k_loss.keys():
    X.append(i)

Y = []
for i in X:
    Y.append(k_loss[i][-2])
plt.figure(num = None, figsize=(9,9))
plt.plot(X, Y, color = "red", marker = "+")
for i in range(len(X)):
    s = "(" + str(X[i]) + ", " + str(round(Y[i], 2)) + ")"
    plt.text(X[i] + 0.1, Y[i]-0.02, s, fontsize = 6)

plt.title("Loss Trend v/s k")
plt.xlabel("k")
plt.ylabel("Loss")
plt.show()

plt.figure(num = None, figsize = (9,9))
plt.scatter(np.array(k_cluster[2][0]["points"])[:,:2][:,0], np.array(k_cluster[2][0]["points"])[:,:2][:,1], c = "red", marker = "x")
plt.scatter(np.array(k_cluster[2][1]["points"])[:,:2][:,0], np.array(k_cluster[2][1]["points"])[:,:2][:,1], c = "blue", marker = "o")
plt.scatter([k_cluster[2][0]["center"][:2][0]], [k_cluster[2][0]["center"][:2][1]], c = "black", marker = "x", s = 400)
plt.scatter([k_cluster[2][1]["center"][:2][0]], [k_cluster[2][1]["center"][:2][1]], c = "black", marker = "o", s = 400)

plt.title("Plot for K = 2")
plt.xlabel("Feature-1")
plt.ylabel("Feature-2")
plt.show()







