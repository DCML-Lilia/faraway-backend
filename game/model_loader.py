from tensorflow.keras.models import load_model
import os

model_sanctu = load_model(os.path.join("models", "model_sanctuaires.h5"))
model_region = load_model(os.path.join("models", "model_regions.h5"))

