import cv2,numpy
from os import walk
import shutil
import os

def scaleRadius(img,scale):
	x=img[img.shape[0]/2,:,:].sum(1)
	r=(x>x.mean()/10).sum()/2
	s=scale*1.0/r
	return cv2.resize(img,(0,0),fx=s,fy=s)

def rotate_about_center(img,angle,scale=1.0):
	rows,cols=img.shape[:2]
	M=cv2.getRotationMatrix2D((cols/2.0,rows/2.0),angle,scale)
	return cv2.warpAffine(img,M,(cols,rows))
	
def square(img):
	rows,cols=img.shape[:2]
	if(rows>cols):
		rows,cols=cols,rows
	return img[0:rows,(cols-rows)/2:(cols+rows)/2]
	
    
def make_train_data(src, dest, scale = 256):
    newpath = dest 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for (dirpath, dirnames, filenames) in walk(src):
        for f in filenames:
            a=cv2.imread(dirpath+'/'+f)
            a=scaleRadius(a,scale)
            a=cv2.addWeighted(a,4,cv2.GaussianBlur(a,(0,0),scale/30),-4,128)
            b=numpy.zeros(a.shape)
            cv2.circle(b,(a.shape[1]/2,a.shape[0]/2),int(scale*0.9),(1,1,1),-1,8,0)
            a=a*b+128*(1-b)
            a=square(a)
            a = cv2.resize(a, (scale, scale))

            cv2.imwrite(dest+"1_"+f,rotate_about_center(a,0,1.0))
            cv2.imwrite(dest+"2_"+f,rotate_about_center(a,90,1.0))
            cv2.imwrite(dest+"3_"+f,rotate_about_center(a,180,1.0))
            cv2.imwrite(dest+"4_"+f,rotate_about_center(a,270,1.0))
def make_test_data(src, dest, scale = 256):
    newpath = dest 
    if os.path.exists(newpath):
        pass
    else:
        os.makedirs(newpath)
    for (dirpath, dirnames, filenames) in walk(src):
        for f in filenames:
            a=cv2.imread(dirpath+'/'+f)
            a=scaleRadius(a,scale)
            a=cv2.addWeighted(a,4,cv2.GaussianBlur(a,(0,0),scale/30),-4,128)
            b=numpy.zeros(a.shape)
            cv2.circle(b,(a.shape[1]/2,a.shape[0]/2),int(scale*0.9),(1,1,1),-1,8,0)
            a=a*b+128*(1-b)
            a=square(a)
            a = cv2.resize(a, (scale, scale))

            cv2.imwrite(dest+f,rotate_about_center(a,0,1.0))        
