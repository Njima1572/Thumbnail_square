from PIL import Image
import glob, os

def fileLoop(filetype):
    for infile in glob.glob("*." + filetype):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        if(im.width >= im.height):
            ratio = im.width / im.height
        else:
            ratio = im.height/im.width
        width = oneside * ratio
        height = oneside
        left, top = (width - oneside) / 2 + offset * 5, 0
        right, bottom = oneside + left , oneside
        size = oneside * ratio, oneside * ratio
        im.thumbnail(size)
        im = im.crop((left, top, right, bottom))
        im.save("./thumb/"+ file+"-thumb.jpg", "JPEG")

offset = 1
oneside = input("Size?: ")
while not oneside.isdigit():
    oneside = input("Please input valid number: ")
oneside = float(oneside)
if not os.path.exists("./thumb"):
    os.mkdir("thumb")
print("Processing...")
fileLoop("jpg")
fileLoop("JPG")
print("Done!")
