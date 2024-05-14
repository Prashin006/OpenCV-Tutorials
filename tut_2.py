import cv2
from random import randint

img = cv2.imread("./assets/logo.jpg")
# print(type(img))
# print(img.shape)    # (height,width,channels) or (rows,columns,channels)
# print(img.shape[0])
# print(img.shape[1])
# print(img.shape[2])
# print(img[0])
# print(img[994][399])

tag = img[350:550,300:600]
img[100:300,600:900] = tag

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.imshow('Modified logo',img)
cv2.waitKey(0)
