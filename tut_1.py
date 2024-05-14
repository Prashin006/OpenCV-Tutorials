# pip install opencv-python
# opencv is also available for other languages
import cv2

# -1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It is the default flag.
# 0, cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel
img = cv2.imread("./assets/logo.jpg", 1)

# resizing the image
# img = cv2.resize(img, (1080,400))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # scales down the image by a factor of 2

# rotating the image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# saving the image
cv2.imwrite("./assets/new_logo.jpg", img)

cv2.imshow("Tech With Prashin", img)
# cv2.waitKey(0) means to wait infinitely for a key stroke. cv2.waitKey(5000) means wait 5 seconds and then execute next line of code
cv2.waitKey(0)
cv2.destroyAllWindows()
