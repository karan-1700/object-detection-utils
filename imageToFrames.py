"""
Created on Tue Jul 21 18:34:39 2020
@author: karan
"""

# importing library
import cv2
import os

# path of the Video file
# For Ubuntu OS : Example : VIDEO_PATH = '/home/karan/Desktop/temp/vtest.mp4'
# For Windows OS : Example : VIDEO_PATH = 'F:\\temp\\vtest.mp4'
VIDEO_PATH = 'path\\to\\video\\file\\video.mp4'

# path of the Folder where you want to save the frame
SAVE_IN = os.path.join(os.path.split(VIDEO_PATH)[0], 
                       os.path.split(VIDEO_PATH)[-1].split(".")[0])

if not os.path.exists(SAVE_IN):
    print("[INFO] Folder created...")
    os.mkdir(SAVE_IN)
else: 
    print("[INFO] Folder already exists. Contents of the folder will be overwritten...")
# initialize the class
capture = cv2.VideoCapture(VIDEO_PATH)

# initialize the Frame Count
count = 0
frameCounter = 0

# get the frames per second value
fps = capture.get(cv2.CAP_PROP_FPS)
print("[INFO] fps = ", fps)

while (True):
    # capture the video frame-by-frame
    retVal, frame = capture.read()
    
    # resize the frame to 720(width) X 405(height)
    dim = (720, 405)
    frame = cv2.resize(src=frame, dsize=dim, interpolation=cv2.INTER_AREA)
    
    if retVal==False:
        break
    
    else:    
        count += 1
        # display the frame
        cv2.imshow("frame", frame)
        
        # save the frame
        if (count % 50 == 0):
            frameCounter += 1
            IMAGE_NAME = os.path.join(SAVE_IN, 
                                      os.path.split(SAVE_IN)[-1] + "_"+str(frameCounter)+'.jpg')        
            
            cv2.imwrite(filename=IMAGE_NAME, img=frame)
        
        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

# release the 'capture' object
capture.release()
# destroy all windows
cv2.destroyAllWindows()
print("[INFO] Task completed...")
print("[INFO] {} images generated at {}".format(frameCounter, SAVE_IN))


