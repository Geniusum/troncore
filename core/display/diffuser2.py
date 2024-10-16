import image as im
import fluxes as fl
import configs as c
from PIL import Image
import os
import time
from concurrent.futures import ThreadPoolExecutor

# Mesurer le temps de traitement
start_time = time.time()

divider = 2

# Lire l'image
image_path = os.path.join(c.ASSETS_FOLDER_PATH, "test_frame.png")
image = Image.open(image_path)
image = image.resize((int(image.size[0] / divider), int(image.size[1] / divider)))

# Lire le fichier flux
dfs_g_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "dfs-g.flx")
dfs_g = fl.FluxFile(dfs_g_path)
dfs_g.content = dfs_g.try_get_content()

# Traduire le contenu du flux
content = dfs_g.translate()

# Fonction pour traiter une partie de l'image et retourner les cellules
def process_image_section(image_section, start_index):
    return im.image_to_cells(image_section, start_index)

# Diviser l'image en segments
def split_image(image, num_parts):
    width, height = image.size
    part_height = height // num_parts
    image_parts = []
    
    for i in range(num_parts):
        top = i * part_height
        bottom = height if i == num_parts - 1 else (i + 1) * part_height
        image_part = image.crop((0, top, width, bottom))
        image_parts.append((image_part, top * width))  # Ajouter l'indice de départ pour chaque partie
    return image_parts

# Définir le nombre de threads (ajuster selon ta machine)
num_threads = 40

# Diviser l'image en 4 parties
image_parts = split_image(image, num_threads)

# Utilisation des threads pour traiter chaque segment en parallèle
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(process_image_section, part, start_index) for part, start_index in image_parts]

# Assembler les cellules résultantes dans l'ordre
sector_cells = {}
for future in futures:
    sector_cells.update(future.result())

# Mettre à jour le contenu des cellules de pixels dans le fichier flux
content["sectors"]["PIXELS"]["cells"] = sector_cells
content["sectors"]["INFO"]["cells"][0]["value"] = image.size[0]
content["sectors"]["INFO"]["cells"][1]["value"] = image.size[1]

# Écriture du fichier de flux mis à jour
dfs_g.write_file(dfs_g_path, dfs_g.format(content))

# Mesurer et afficher le temps total
print("Done.")
print(f"Temps total: {time.time() - start_time:.2f} secondes")
