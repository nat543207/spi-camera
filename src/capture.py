""" Implements functions that save video buffer stored in memory to a file.
    Will probably use OpenCV funcitons/types to accomtypes to accomplish this.
"""
import cv
import cv2

camera = cv2.VideoCapture()
file_props = { "filename" : "out.vid",
                 "fourcc" : "XVID",
                    "fps" : 60,
                   "size" : (640, 480), }



# Capture a single image from the default camera, display it,
# and write it to a file.
#
# Currently, the 'write to a file' bit doesn't work
def take_picture():
    camera.open(0)
    
    # This thing doesn't work yet
    output = cv2.VideoWriter(file_props["filename"], cv.CV_FOURCC('D','I','V','X'), file_props["fps"], file_props["size"], True)
    #

    tmp, frame = camera.read()
    cv2.imshow("test", frame)
    
    # Also broken
    output.write(frame)
    #

    cv2.waitKey(0)
    camera.release()



# Capture a video and write it to a file.
# Probably need to get take_photo working first
def record_video(duration):
    pass



if __name__ == "__main__":
    take_picture()
