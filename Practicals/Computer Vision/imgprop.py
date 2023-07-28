import cv2  
 
img = cv2.imread(r'G:\Computer_Vision\ganapathi.jpg',1)  
  
height = img.shape[0]  
width = img.shape[1]  
channels = img.shape[2]  
size1 = img.size  
  
print('Image Height       : ',height)  
print('Image Width        : ',width)  
print('Number of Channels : ',channels)  
print('Image Size  :', size1)  
