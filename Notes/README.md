# Thought Process

<h2> <b style="color:cyan"> Goal: Given 2 sock image, determine if they are a pair or not. </b></h2>

## 1. &nbsp; How to get the training and testing images

### Issues

- Find training data online, then they might not be as realistic as the real time picture. Then the model does well on training but not on real time.
- Take pictures of socks. This is more realistic, but it is time consuming. And I only have black socks.

### Solutions

- Take image from online and also take pictures of socks. Then combine them together.
  - How to find images online? The image I need is pair of socks on 2 different image files. So there could be an issue?
    - This raises a question, <b>is the left sock and right sock the same? Are they just 2 production of the same design?</b> Interesting. That could be why we don't know which sock to put on which foot. If they are the same, then I can just take one image and flip it to get the other one. If they are different, then I need to find 2 images for each pair of socks.
    - After some research we found that for regular socks, the left and right are the same. But for socks with a specific design, the left and right are different. Since our application will deal with regular socks in most cases, we just need a data source with single image of either left or right sock.
    - <b>Potential Data Source</b>:
      - Online Dataset (if any)
      - Amazon socks page (online stores)
      - Bing Image Search API
      - Use AI to generate images (Shakky idea)

## 2. &nbsp; Background image when taking photos of socks?

### Issues

- The background of the image is not consistent. This will affect the model's performance.

### Solutions

- So we use U2Net model to remove background. But the model is not perfect. It will include some other backgroung elements in the image. So we need to find a way to remove those elements.
- We then assume the center of the image is part of the sock. And then BFS from the center outward in the four direction until we get black (0, 0, 0) pixel. This is successful in most cases.
  - One issue is that if the sock is not centered in the image, it will crash. To force this, we need to make the client move the sock to be centered on a cross icon on the screen.
  - To be be more safe, we can do the BFS in all 8 directions including diagonals.

## 3. &nbsp; Zoom level and Orientation of the socks

### Issues

- The zoom level and orientation of the socks are not consistent. This will affect the model's performance.

### Solutions

- Take 1 image of each sock and use image augmentation to with 360 rotation and zoom in/out to create more images and different brightness ...
- If orientation highly affects the model's performance, then we will force the client to take the picture in a specific orientation. TO be able to do this later, the image should be taken with consistent orientation, before we apply image augmentation.

<h4><center><b style="color:lime">**** Dec 24, 2023: Taking images of socks found missing in West House's Laundry Room - (49 images)****</b></center></h4>

## 4. &nbsp; How to train the model

### Options

- Using tranfeer learning
  - <b>Option 1:</b> Take off the last layer of the model and feed the image. Take the last layer (hoping it contains information for extracted features) and do this for 2 image. Now you have 2 vectors with same size. Then use cosine similarity or euclidean distance b/n them. Feed that to a new trainable neural network. When training the new network, augmented images of the same sock should give a 1 (pair) and augmented images of different socks should give a 0 (not pair).
  - <b>Option 2:</b>

## Reference / Reference

- <b>Deep Learning for sock classification to finite classes</b>
  - https://simon-aubury.medium.com/sorting-my-socks-with-deep-learning-part-1-1b5651d35f3e
  - https://simon-aubury.medium.com/kafka-stream-processing-sorting-socks-with-ksqldb-e4174ae5e703
- Using bing to get images
  - https://pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/
