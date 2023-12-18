# Notes

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
      - Google Image Search API

## Reference / Reference

- <b>Deep Learning for sock classification to finite classes</b>
  - https://simon-aubury.medium.com/sorting-my-socks-with-deep-learning-part-1-1b5651d35f3e
  - https://simon-aubury.medium.com/kafka-stream-processing-sorting-socks-with-ksqldb-e4174ae5e703
