from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
from keras.utils import to_categorical
print('Training data shape : ', train_images.shape, train_labels.shape)
print('Testing data shape : ', test_images.shape, test_labels.shape)
# Find the unique numbers from the trpy ain labels

classes = np.unique(train_labels)
nClasses = len(classes)
print('Total number of outputs : ', nClasses)
print('Output classes : ', classes)

plt.figure(figsize=[10,5])


plt.figure(figsize=(10,10))
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i, :, :], cmap='gray')
    plt.title("Ground Truth : {}".format(test_labels[i]))
plt.show()