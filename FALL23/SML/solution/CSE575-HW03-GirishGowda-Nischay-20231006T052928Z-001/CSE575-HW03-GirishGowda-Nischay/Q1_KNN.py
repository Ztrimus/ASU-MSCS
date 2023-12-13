import numpy as np
import matplotlib.pyplot as plt
import pickle
from tqdm import trange


# --------------------------- train images----------------------------
''' Images Train '''
# Using MNIST handwritten digits recognition train images file.
file_train = open(r'train-images.idx3-ubyte', 'rb')
# reading a binary valued file.
file_train.read(16)
image_size = 28

# convert data to buffer 1d type.
train_data = np.frombuffer(file_train.read(), dtype=np.uint8).astype(np.float32)
image_dim = int(len(train_data)/(28*28))
train_images = train_data.reshape(image_dim, image_size, image_size,1)

# --------------------------- test images -----------------------------
file_img_test = open(r't10k-images.idx3-ubyte', 'rb')
image_size = 28
file_img_test.read(16)

train_data_img = np.frombuffer(file_img_test.read(), dtype=np.uint8).astype(np.float32)
image_dim = int(len(train_data_img)/(28*28))
test_images = train_data_img.reshape(image_dim, image_size, image_size, 1)


# --------------------------- train labels -----------------------------
file_img_labels = open(r'train-labels.idx1-ubyte', 'rb')
file_img_labels.read(8)

train_labels = []
for i in file_img_labels.read():
    train_labels.append(str(i))

# --------------------------- test labels ------------------------------
file_img_test_labels = open(r't10k-labels.idx1-ubyte', 'rb')
file_img_test_labels.read(8)

test_labels = []
for i in file_img_test_labels.read():
    test_labels.append(str(i))


# Model prediction function.
def model_predict(train_img, test_img, train_lables, k):

    test_pixel = np.ravel(test_img)
    distances = []
    for img in train_img:
        train_pixel = np.ravel(train_img)
        if len(train_pixel) != len(test_pixel):
            dist = 0
        else:
            dist = np.sum((train_pixel-test_pixel)**2)
        distances.append(dist)
    img_index = np.argsort(distances)[:k]
    count = 0
    labels = {}
    prediction = ''
    for idx in img_index:
        label = train_labels[i]
        if label not in labels:
            labels[label] = 1
        else:
            labels[label] += 1
        
        if labels[label] > count:
            count = labels[label]
            prediction = label
    return prediction

# ---------------------------- Model training --------------------------

# K value given.
K = [1, 3, 5, 10, 20, 30, 40, 50, 60]
accuracy_map = {}

for k in K:
    # progress bar to know the training status.
    progress_bar = trange(len(test_images), desc="Training Progress", position=0)
    correct_pred = 0
    for i in range(len(test_images)):
        prediction = model_predict(train_images, test_images[i], train_labels, k)
        if prediction == test_labels[i]:
            correct_pred += 1
        progress_bar.set_description(f"Taining for k = {k}")
        progress_bar.update(1)
        
    accuracy = correct_pred / len(test_images)
    accuracy *= 100
    accuracy_map[k] = accuracy
    print("k =" + str(k) + ", Accuracy: " + str(accuracy))



# Plot 
X = list(accuracy_map.keys())
Y = []

for i in X:
    Y.append(accuracy_map[i])

plt.title("Loss Trend v/s k")
plt.figure(num=None, figsize=(8,8))
plt.plot(X, Y, color='blue', marker='+')
for i in range(len(X)):
    s = "(" + str(X[i]) + ", " + str(Y[i]) + ")"
    plt.text(X[i]+1, Y[i]-0.04, s)
plt.title("For each cluster K - accuracy plot.")
plt.xlabel("k")
plt.ylabel("Accuracy (in %)")
plt.show()