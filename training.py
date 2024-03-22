import mlflow
import mlflow.keras
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Set the MLflow tracking URI with access token
mlflow.set_tracking_uri("https://dagshub.com/yusufM03/MLflow_Tracking.mlflow")

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess the data
X_train = X_train / 255.0
X_test = X_test / 255.0
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Define the neural network model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Start MLflow run
with mlflow.start_run():

    # Train the model
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, batch_size=32)

    # Log parameters
    mlflow.log_param("epochs", 5)
    mlflow.log_param("optimizer", "adam")

    # Log metrics
    mlflow.log_metric("train_loss", history.history['loss'][-1])
    mlflow.log_metric("train_accuracy", history.history['accuracy'][-1])
    mlflow.log_metric("val_loss", history.history['val_loss'][-1])
    mlflow.log_metric("val_accuracy", history.history['val_accuracy'][-1])

    # Log the trained model
    mlflow.keras.log_model(model, "mnist_model")
