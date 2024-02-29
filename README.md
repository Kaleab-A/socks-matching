# Sock Pairing Solution

## Inspiration

Living in a dorm with shared laundry facilities often leads to the common occurrence of losing a single leg of socks. Meanwhile, there is a box of lone socks in the laundry room. The task of sorting through this box to find a pair is time-consuming and frustrating.

![photo_2024-02-29_14-01-58](https://github.com/Kaleab-A/socks-matching/assets/50099796/c6b7d571-427e-4671-9825-3eafcd085ffe)

This issue isn't isolated to just one laundry room. Imagine the magnitude of this problem across various dormitories and across all university campuses in the United States.

## Solution

### Machine Learning Model

- Develop a machine-learning model that can analyze images of socks to determine if they form a pair.

### Cross-Platform Application

The model will be integrated into an application. Here's how it will work:

- Users register their lost socks in a database through the app by uploading images of the single socks they have.
- The app uses the machine learning model to predict matches based on the user's uploaded photo and compares it against all the photos in the database.
- The app then displays 5 images that have a high likelihood of being a match.
- Admins can add images to the database when a sock is found lost. 

### Pair Recovery

Users can then select from the presented images. The application will assist in coordinating how they can retrieve their matched socks, thereby solving the problem of lost and unpaired socks.

## Working

### Image Preprocessing
![photo_2024-02-29_13-54-01](https://github.com/Kaleab-A/socks-matching/assets/50099796/eeaf3985-e103-4537-91c2-935f06409cdf)

### Image Augmentation
![photo_2024-02-29_13-53-59](https://github.com/Kaleab-A/socks-matching/assets/50099796/18fb6d08-f370-47c3-b72c-3269b04d4c0c)

### Training 
- Pairs are the same sock but after augmentation
![photo_2024-02-29_13-54-02](https://github.com/Kaleab-A/socks-matching/assets/50099796/df622a8c-3f2d-4896-84eb-9b6e0d1afbe0)

- No Paris are augmented version of different socks
![photo_2024-02-29_13-54-32](https://github.com/Kaleab-A/socks-matching/assets/50099796/d8a9175e-8260-4360-ab89-e9234646b391)

### Testing [In Progress...]
