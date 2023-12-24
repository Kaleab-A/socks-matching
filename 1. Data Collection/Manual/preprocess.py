import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


PATH = "1. Data Collection/Manual/Socks Images"


def preprocess(img):
    pass


def displaySample(imgCnt=10):
    for i in range(imgCnt):
        img = cv2.imread(PATH + os.listdir(PATH)[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show()


if __name__ == "__main__":
    displaySample()
