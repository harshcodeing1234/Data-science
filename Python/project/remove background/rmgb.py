from rembg import remove
from PIL import Image

input_path = 'remove background/h.jpg'
output_path = 'remove background/h.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path, format='PNG') 
 

