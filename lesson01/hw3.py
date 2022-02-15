import cv2
SRC = 'images/image_1.jpg'

image_rgb = cv2.imread("img.png")
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
image_blend = cv2.divide(image_gray, image_blur, scale=255)
cv2.imwrite('result.jpg', image_blend)