from PIL import Image
from torchvision.transforms import functional as TF

def hflip(image):
    return TF.hflip(image)

image = Image.open("attack.png")
new_image = hflip(image)
new_image.save("attackRight.png")