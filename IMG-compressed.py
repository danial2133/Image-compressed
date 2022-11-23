from PTL import Image
from tkinter.filedialog import *

##Selection of the image
file_path = askopenfilename()
image = Image.open(file_path)
myHeight, myWidth = image.size

##Reduce volume
image = image.resize((myHeight, myWidth), Image.ANTIALIAS)

##Save the desired file
save_path = asksaveasfilename()
image.save(save_path+"_compressed.JPG")