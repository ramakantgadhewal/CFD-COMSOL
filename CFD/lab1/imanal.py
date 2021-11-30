# print(len(img[1]))
# print(len(img))
# print(img[0,0])
# # crop = i
def find_left(cols,img):
    white = [1,1,1]
    if len(img[0,0])<3:
        white = 1
    for i in range(cols):
        if np.any(img[:,i]==white):
            return i
    print("returning standard left")
    return 200

def find_right(cols,img):
    white = [1,1,1]
    if len(img[0,0])<3:
        white = 1
    for i in range(cols):
        if np.any(img[:,-(i+1)]==white):
            return cols-(i+1)
    print("returning standard right")
    return cols

def find_upper(col,rows,img):
    white = [1,1,1]
    if len(img[0,0])<3:
        white = 1
    for i in range(rows):
        if np.any(img[i,col]==white):
            return i
    print("returning standard upper")
    return 0

def find_lower(rows,img):
    white = [1,1,1]
    if len(img[0,0])<3:
        white = 1
    for i in range(rows):
        if np.any(img[-(i+1),:]==white):
            return rows-(i+1)
    print("returning standard lower")
    return rows

# print(img[0,0])
# for i in range(rows):
    # for j in range(cols):
        # if np.all(img[i,j]==[1,1,1]):
            # print(f"inds: {i},{j}")
            # break

import cv2
import numpy as np
from time import sleep
def makeline(img):

    if np.all(img==None):
        return None
    # img = cv2.imread(filename)
    rows,cols,_ = img.shape
    try:
        left_border = find_left(cols,img)+4
    except Exception:
        left_border = 200


    # left_border = 200
    right_border = find_right(cols,img)
    print("upper border")
    upper_border = find_upper(range(cols),rows,img)
    lower_border = find_lower(rows,img)
    lower_border = 660
    print(type(left_border))
    print(type(right_border))
    point15 = left_border+int((right_border-left_border)/4)
    print("upper15")
    upper15 = find_upper(point15,rows,img)
    print(f"{upper_border},{lower_border}")
    cv2.rectangle(img,(left_border,upper_border),(right_border,lower_border),(255,255,255))
    cv2.line(img,(point15,lower_border),(point15,upper15),(255,0,0))
    cv2.imshow("img",img)
    # cv2.imshow("img",img)
    # sleep(10)
    k = cv2.waitKey(0) & 0xFF
    if k == 27: 
        # break
        pass


if __name__=="__main__":
    img = cv2.imread("startframe_mask.jpg")
    makeline(img)

