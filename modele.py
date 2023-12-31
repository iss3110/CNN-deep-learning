import os
from PIL import Image

# Chemin vers le dossier contenant vos images
image_folder = "img"

# Chemin vers le dossier où vous voulez enregistrer les images prétraitées
output_folder = "img-pretraitees"

# Obtenir la liste des fichiers JPG dans le dossier
image_files = filter(lambda file: file.endswith(".jpg"), os.listdir(image_folder))

# Prétraitement avec PIL et redimensionner à 245x245
resize_and_save = lambda filename: Image.open(os.path.join(image_folder, filename)).resize((245, 245)).save(
    os.path.join(output_folder, filename)
)

# Utiliser la fonction map pour appliquer la transformation à chaque fichier
list(map(resize_and_save, image_files))
