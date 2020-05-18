from PIL import Image
import os
# Conversion to RBG format if required
files = os.listdir("images_pipe")
i = 0
for file in files:
    png = Image.open("images_pipe/" + file)
    png.load()
    if len(png.split()) > 3:
        background = Image.new("RGB", png.size, (255, 255, 255))
        background.paste(png, mask=png.split()[3])
    else:
        background = png

    background.save("image_train/"+str(i)+".png", "PNG")
    i = i + 1
