import tensorflow as tf
from tensorflow.keras import layers, models

def get_radio_cnn(input_shape=(2, 128, 1), num_classes=11, dr=0.5):
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.ZeroPadding2D((0, 2)),
        layers.Conv2D(256, (1, 3), activation='relu', name="conv1"),
        layers.Dropout(dr),
        layers.ZeroPadding2D((0, 2)),
        layers.Conv2D(80, (2, 3), activation='relu', name="conv2"),
        layers.Dropout(dr),
        layers.Flatten(),
        layers.Dense(256, activation='relu', name="dense1"),
        layers.Dropout(dr),
        layers.Dense(num_classes, activation='softmax', name="output")
    ])
    return model