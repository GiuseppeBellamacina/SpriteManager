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
        if item == old_color:
            new_data.append(new_color)
        else:
            new_data.append(item)
    new_image.putdata(new_data)
    return new_image



colors_to_change = [
    ((208,32,64,255), (80,170,64,255), (32,20,192,255), (65,65,65,255)), # arancione scuro (bordino)
    ((248,76,64,255), (120,200,64,255), (82,74,200,255), (144,144,144,255)), # arancione medio
    ((254,130,92,255), (159,234,107,255), (20,150,230,255), (195,195,195,255)), # arancione chiaro
    ((149,0,27,255), (50,100,40,255), (20,14,100,255), (0,0,0,255)), # ombra (scura)
    ((163,6,35,255), (59,120,48,255), (23,16,128,255), (10,10,10,255)) # mezz'ombra (più chiara)
] # aggiungere i colori per gli occhi

enum_colors = {
    0: "Arancione",
    1: "Verde",
    2: "Blu",
    3: "Grigio",
}

def main():
    os.makedirs("sprites", exist_ok=True)
    image = Image.open("sprite.png")
    for j in range(0, len(colors_to_change[0])):
        new_image = image.copy()
        for i in range(0, len(colors_to_change)):
            new_image = changeColor(new_image, colors_to_change[i][0], colors_to_change[i][j])
        new_image.save("sprites\\sprite" + enum_colors[j] + ".png")

def test():
    image = Image.open("sprite.png")
    main_colors = findMainColors(image)
    printMainColors(main_colors)
    white = (255,255,255)
    for i in range(0, len(main_colors)):
        main_color = main_colors[i]
        new_image = changeColor(image, main_color, white)
        new_image.save("new_sprite" + str(i) + ".png")

if __name__ == "__main__":
    test()
    #main()