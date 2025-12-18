
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model

vgg = VGG16()
vgg_model = Model(inputs=vgg.inputs, outputs=vgg.layers[-2].output)

def extract_features(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, 224, 224, 3))
    image = preprocess_input(image)

    features = vgg_model.predict(image)
    return features


def generate_caption(features):
    if np.mean(features) > 0:
        return "A picture containing objects and peoples"
    else:
        return "An image of something"

image_path ="E:\\Codsoft github\\Codsoft\\lion.jpg"
features = extract_features(image_path)
caption = generate_caption(features)

print("Generated Caption:")
print(caption)
