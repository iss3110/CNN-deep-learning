# principe de filtre
# Avant de nous attaquer au deep learning il est important de comprendre ce qu'on fait en terme de traitement d'image.
# On va notamment s'intéresser dans cette première partie à la notion de noyau appliqué sur une image.
# Une image est un condensé de données, que l'on appel les pixels.
import cv2
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import datetime
from tensorflow import keras
from tensorflow.keras.models import Model
import tensorflow as tf

ticket = r'?raw=true'
resp = requests.get(ticket, stream=True).raw
image_array_ticket = np.asarray(bytearray(resp.read()), dtype="uint8")
print(f'Shape of the image {image_array_ticket.shape}')
image_ticket = cv2.imdecode(image_array_ticket, cv2.IMREAD_COLOR)
plt.axis('off')
plt.imshow(cv2.cvtColor(image_ticket, cv2.COLOR_BGR2RGB)) #opencv if BGR color, matplotlib usr RGB so we need to switch otherwise
# the ticket will be blue ... O:)
plt.show()
