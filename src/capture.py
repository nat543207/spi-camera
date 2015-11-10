""" Implements functions that save video buffer stored in memory to a file.
    Will probably use OpenCV funcitons/types to accomtypes to accomplish this.
"""
import cv
import cv2

camera = cv2.VideoCapture()
file = {  "name" : "out.avi", # If this doesn't end in .avi, errors happen
        "fourcc" : cv.CV_FOURCC(*"XVID"),
           "fps" : 60,
          "size" : (640, 480), 
         "color" : True, }



# Capture a single image from the default camera, display it,
# and write it to a file.
def take_picture():
    camera.open(0)
    if not camera.isOpened():
        print "Error opening camera"

    tmp, frame = camera.read()

    cv2.imshow("test", frame)
    cv2.imwrite("pic.jpg", frame)
    cv2.waitKey(1000)
    camera.release()


# Capture a video and write it to a file.
#
# Currently, the file can be written but seems to lack contents
def record_video(duration):
    camera.open(0)
    output = cv2.VideoWriter(file["name"], file["fourcc"], file["fps"], file["size"], file["color"])
    
    for i in range(0,50):
        tmp, frame = camera.read()
        cv2.imshow("test", frame)
        output.write(frame)
        cv2.waitKey(1)

    camera.release()
    output.release()



if __name__ == "__main__":
    take_picture()
    record_video(5)
