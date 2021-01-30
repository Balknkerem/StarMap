import cv2
import numpy as np
Temp=True
big_pic=input('Enter Big Picture Path => ')
small_pic=input('Enter Small Picture Path => ')

while(Temp):
    template = cv2.imread(small_pic,0)
    for i in range(0,360):
        (height, width) = template.shape[:2]
        center = (width / 2, height / 2)
        scale = 1.0
        M = cv2.getRotationMatrix2D(center, i, scale)
        rotated = cv2.warpAffine(template, M, (height, width))
        img_rgb = cv2.imread(big_pic)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray,rotated,cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        loc=list(loc)
        if len(loc[0])>0:
            break
    Temp=False

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (255,0,0), 1)
top_left=pt
top_right=(pt[0]+width,pt[1])
bottom_left=(pt[0],pt[1]+height)
bottom_right=(pt[0] + width, pt[1] + height)
print("Top Left coordinate = {}, Top Right coordinate = {}".format(top_left,top_right))
print("Bottom Left coordinate = {}, Bottom Right coordinate = {}".format(bottom_left,bottom_right))
cv2.imshow('Image',img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
