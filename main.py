import os
import json
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam


def load_and_preprocess_data(directory):
    """
    Load images and their corresponding x-coordinates from the specified directory.
    Returns images and labels as numpy arrays.
    """
    images = []
    labels = []

    # List all files in the directory and sort them to ensure pairing
    files = sorted(os.listdir(directory))
    for file in files:
        if file.endswith('.jpeg'):
            base_name = file[:-5]
            json_file = base_name + '.json'
            if json_file in files:
                image_path = os.path.join(directory, file)
                json_path = os.path.join(directory, json_file)

                # Load image
                image = cv2.imread(image_path)
                image = cv2.resize(image, (128, 128))  # Resize images to a fixed size
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                images.append(image)

                # Load JSON data
                with open(json_path, 'r') as f:
                    data = json.load(f)

                # Calculate the average x-coordinate of the polygon points
                x_coords = [point[0] for point in data['shapes'][0]['points']]
                x_center = sum(x_coords) / len(x_coords)
                labels.append(x_center)

    return np.array(images), np.array(labels)


def build_model():
    """
    Builds a simple convolutional neural network model.
    """
    model = Sequential([
        Conv2D(16, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        MaxPooling2D(2, 2),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1)  # Output one coordinate
    ])
    model.compile(optimizer=Adam(lr=0.001), loss='mse')
    return model


def train_model(images, labels):
    """
    Trains the model using the provided images and labels.
    """
    model = build_model()
    model.fit(images, labels, epochs=10, batch_size=32)
    model.save('coupling_detector_model.h5')
    return model


def main():
    directory = 'data/car_coupling_train'  
    images, labels = load_and_preprocess_data(directory)
    model = train_model(images, labels)
    print("Model trained and saved!")


if __name__ == "__main__":
    main()
