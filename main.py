# 6.95kb size

import cv2

# Configurable Parameters
source = "image.jpeg"
destination = "newImage,png"
# PERCENTAGE BY WHICH IMAGE IS RESIZED
scale_percentage = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", image)

# CALCULATE THE 50% OF ORIGINAL DIMENSIONS
width = int(image.shape[1]* scale_percentage /100)
height = int(image.shape[0]* scale_percentage /100)

# DSIZE
dsize = (width, height)

# RESIZE IMAGE
output = cv2.resize(image, dsize)

cv2.imwrite(destination, output)
#cv2.waitKey(0)