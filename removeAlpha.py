from PIL import Image
import os

def findMainColors(image):
    main_colors = []
    data = image.getdata()
    color_count = {}
    for item in data:
        if item in color_count:
            color_count[item] += 1
        else:
            color_count[item] = 1
    for color in sorted(color_count, key=color_count.get, reverse=True):
        main_colors.append(color)
    return main_colors

def printMainColors(main_colors):
    i = 0
    for color in main_colors:
        print(i, color)
        i += 1

def changeColor(image, old_color, new_color):
    data = image.getdata()
    new_data = []
    new_image = image.copy()
    for item in data:
        if item[:4] == old_color[:4]:
            new_data.append(new_color)
        else:
            new_data.append(item)
    new_image.putdata(new_data)
    return new_image

def main():
    image = Image.open("princess.png").convert("RGBA")
    color = findMainColors(image)[0]
    printMainColors(findMainColors(image))
    new_image = changeColor(image, color, (0, 0, 0, 0))
    new_image.save("princess2.png")
    
main()