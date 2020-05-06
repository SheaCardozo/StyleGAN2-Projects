from PIL import Image
import os
# StyleGAN2 only accepts RBG formatted images, this script converts RGBA images into RGB for training
files = os.listdir("faces_pipe")
i = 0
for file in files:
    png = Image.open("images_train/" + file)
    png.load()

    if len(png.split()) > 3:
        background = Image.new("RGB", png.size, (255, 255, 255))
        background.paste(png, mask=png.split()[3])
    else:
        background = png

    background.save("images_train/" + str(i)+".png", "PNG")
    i = i + 1