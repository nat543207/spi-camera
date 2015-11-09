""" Implements functions that save video buffer stored in memory to a file.
    Will probably use OpenCV funcitons/types to accomtypes to accomplish this.
"""
import cv
import cv2

camera = cv2.VideoCapture()
file_props = { "filename" : "out.vid",
                 "fourcc" : int(camera.get(cv.CV_CAP_PROP_FOURCC)),
                    "fps" : int(camera.get(cv.CV_CAP_PROP_FPS)),
                   "size" : (int(camera.get(cv.CV_CAP_PROP_FRAME_WIDTH)), int(camera.get(cv.CV_CAP_PROP_FRAME_HEIGHT))), }

def take_picture():
    camera.open(0)
    output = cv2.VideoWriter(file_props["filename"], file_props["fourcc"], file_props["fps"], file_props["size"])
    tmp, frame = camera.read()
    cv2.imshow("test", frame)
    cv2.waitKey(0)
#    output.write(frame)

if __name__ == "__main__":
    take_picture()
