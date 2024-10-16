from PIL import Image

def cells_to_image(sector_cells: dict, image_width: int, image_height: int):
    img = Image.new("RGB", (image_width, image_height), "black")
    pixels = img.load()

    for index, cell in sector_cells.items():
        if cell["type"] == "STRING":
            rgb = cell["value"].split()
            if len(rgb) == 3:
                try:
                    r, g, b = map(int, rgb)
                    x = index % image_width
                    y = index // image_width
                    pixels[x, y] = (r, g, b)
                except ValueError:
                    continue

    return img

def image_to_cells(image: Image, start_index: int):
    sector_cells = {}
    index = start_index
    pixels = image.load()
    image_width, image_height = image.size

    for y in range(image_height):
        for x in range(image_width):
            pixel = pixels[x, y]
            pixel_ = " ".join(map(str, pixel[:3]))
            sector_cells[index] = {"type": "STRING", "value": pixel_}
            index += 1

    return sector_cells
