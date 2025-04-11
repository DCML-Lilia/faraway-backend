import tensorflow as tf
import os

model_sanctu = tf.keras.models.load_model(os.path.join("models", "model_sanctuaires.h5"))
model_region = tf.keras.models.load_model(os.path.join("models", "model_regions.h5"))
