import cv2
import numpy as np

file = "E:/Files/Programation/Casio_Draw/rick.jpg"

img = cv2.imread(file, cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

scale_percent = (127/860)*100  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

cv2.imshow('image', img)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)


cv2.imshow("Resized image", resized)

cv2.imwrite('output_rick.bmp', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()


