from PIL import Image
import os

images = [
    'hero-kitchen.jpg',
    'hero-wardrobe.jpg',
    'service-kitchen.jpg',
    'service-wardrobe.jpg',
    'service-fullhome.jpg',
    'service-paneling.jpg',
    'service-ceiling.jpg',
    'service-doors.jpg',
    'service-furniture.jpg',
    'service-painting.jpg',
    'service-electrical.jpg',
    'portfolio-mandir.jpg',
    'portfolio-kitchen.jpg',
    'portfolio-bedroom.jpg',
    'portfolio-living.jpg',
    'portfolio-tvunit.jpg',
    'portfolio-office.jpg',
    'about-workshop.jpg'
]

for f in images:
    path = os.path.join('assets/images', f)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{f:25}: size={im.size}, mode={im.mode}")
