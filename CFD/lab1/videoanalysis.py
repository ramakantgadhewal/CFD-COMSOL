import cv2
import numpy as np
from time import sleep
# from imanal import *
filename = "/home/henrik/Documents/umu/CFD/lab1/experiment_vid_v0.mp4"
cap =cv2.VideoCapture(filename)
startframe = 34
framenr = 1


# change it according to your need !
# sensitivity = 15
# lower_white = np.array([0,0,255-sensitivity])
# upper_white = np.array([255,sensitivity,255])


green = 60;
blue = 100;
yellow = 30;
sensitivity = 15

# Change color with your actual color
lower_blue = np.array([blue- 1*sensitivity, 90, 40]) 
upper_blue = np.array([blue+ sensitivity, 255, 255])

######################################################
# print(len(img[1]))
# print(len(img))
# print(img[0,0])
# # crop = i
def find_left(cols,img):
    white = [1,1,1]
    
    if np.size(img[0,0])<3:
        white = 1
    for i in range(cols):
        if np.any(img[:,i]==white):
            return i
    print("returning standard left")
    return 200

def find_right(cols,img):
    white = [1,1,1]
    if np.size(img[0,0])<3:
        white = 1
    for i in range(cols):
        if np.any(img[:,-(i+1)]==white):
            return cols-(i+1)
    print("returning standard right")
    return cols

def find_upper(col,rows,img):
    white = [1,1,1]
    if np.size(img[0,0])<3:
        white = 1
    for i in range(rows):
        if np.any(img[i,col]==white):
            return i
    print("returning standard upper")
    return 0

def find_lower(rows,img):
    white = [1,1,1]
    print(np.size(img[0,0]))
    if np.size(img[0,0])<3:
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

# import cv2
# import numpy as np
# from time import sleep
def makeline(img):

    if np.all(img==None):
        return None
    # img = cv2.imread(filename)
    rows,cols = img.shape


    # left_border = 200
    left_border = find_left(cols,img)+4
    right_border = find_right(cols,img)
    upper_border = find_upper(range(cols),rows,img)
    lower_border = find_lower(rows,img)
    point15 = left_border+int((right_border-left_border)*2.5/35)
    upper15 = find_upper(point15,rows,img)
    print(f"{upper_border},{lower_border}")
    cv2.rectangle(img,(left_border,upper_border),(right_border,lower_border),(255,255,255))
    # cv2.line(img,(point15,lower_border),(point15,upper15),(255,0,0))
    ###########################################
    # THIS ONE!!!!
    cv2.imshow("img",img)
    # sleep(10)
    # k = cv2.waitKey(0) & 0xFF
    # if k == 27: 
        # # break
        # pass
    return point15


# if __name__=="__main__":
    # makeline()
          



######################################################

def white_in_col(col,img):
    nrpixels=0
    nrpixels = np.count_nonzero(img[:,col])
    return nrpixels





checkrange = range(1000)
lenrange = len(checkrange)
height= np.zeros([1,lenrange])
grabbed, frame = cap.read()
while grabbed:

    grabbed, frame = cap.read()
    if not grabbed:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # nr 1 and 3
    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    print(framenr)
    if framenr in checkrange:
        # print(mask[0,0])
        point15 = makeline(mask)
        nrpixels = white_in_col(point15,mask)
        print(framenr)
        height[0,framenr] = nrpixels#/275*16
        print(f"Nr of white pixels: {nrpixels}")
        # sleep(1)
    k = cv2.waitKey(25) & 0xFF
    if k == 27 or framenr>lenrange:
        break
    framenr = framenr+1
    # if framenr ==startframe:
        # print(mask)
        # print(f"width mask: {len(mask[1])}\n width im: {len(frame[1])}")
        # cv2.imwrite("startframe_mask.jpg",mask)
        # break

cv2.destroyAllWindows()


print(framenr)
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
t = np.linspace(1,lenrange,lenrange)

np.savetxt("videoheight_v0.txt",height[0,:framenr])

plt.plot(t[startframe:],height[0,startframe:lenrange],'r-*')
plt.show()




