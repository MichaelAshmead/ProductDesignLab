from VideoCapture import Device

came = Device()
came.setResolution(320, 240)

img = cam.getImage()

#from VideoCapture import Device
from numpy import *
from PIL import Image
cam = Device(devnum=0, showVideoWindow=0) #devnum=0 means you are using the device set in 0 position probably your webcam
blackimg= cam.getImage() #this return a PIL image but I don't know why the first is always black
#blackimag.show()#try to check if you want
image=cam.getImage() #this is a real image PIL image
imgarray = asarray(image) #convert the image into a matrix
#imgarrayfloat = imgarray.astype('float') # in many cases of processing you have to convert to a float matrix because can occur overflow (e.g. for average images summing  pixels values of 255 and 3 of two images and divide by 2 gives you 1/2 for imgarray and 258/2 for imgarrayfloat
#recovertedimage=processedimage.astype ("uint8")#if you use the previous you have to reconvert to unit8. Note processedimage is the name of the variable of your image.p.g
