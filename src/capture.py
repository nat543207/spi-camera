""" Implements functions that save video buffer stored in memory to a file.
    Will probably use OpenCV funcitons/types to accomtypes to accomplish this.
"""
import cv2
from Queue import Queue
from datetime import datetime, timedelta
import motion

file = {  "name" : "out.avi", # If this doesn't end in .avi, errors happen
        "fourcc" : cv2.cv.CV_FOURCC(*"XVID"),
           "fps" : 30,
          "size" : (640, 480),
         "color" : True, }
camera = cv2.VideoCapture()
recording = cv2.VideoWriter()
vidbuf = Queue()


class Frame:
    def __init__(self, timestamp, image, has_motion):
        self.timestamp = timestamp
        self.image = image
        self.has_motion = has_motion


def capture():
    success, img = camera.read()
    return Frame(datetime.now(), img, motion.CV_detects_motion(img))


def threshold(seconds):
    return timedelta(0, seconds)


def dump_buffer(buf, file):
    if not file.isOpened():
        return False
    file.write(buf)


def func():
    bufsize = 60
    camera.open(0)
    output = cv2.VideoWriter(file["name"], file["fourcc"], file["fps"], file["size"], file["color"])
    recording = False

    for i in range(0, 60):
        vidbuf.put(capture())

    while True:
        frame = capture()
        if frame.has_motion:
            recording = True
            while 0 < vidbuf.qsize():
                output.write(vidbuf.get().image)
            output.write(frame.image)
        else: #if not frame.has_motion:
            vidbuf.put(capture())
            if bufsize < vidbuf.qsize():
                vidbuf.get(True)
                if recording == True:
                    while 0 < vidbuf.qsize():
                        output.write(vidbuf.get().image)
                    output.close()
                    recording = False
                    break




# # Capture a single image from the default camera, display it,
# # and write it to a file.
# def take_picture():
#     camera.open(0)
#     if not camera.isOpened():
#         print "Error opening camera"
#     tmp, frame = camera.read()
#     cv2.imshow("test", frame)
#     cv2.imwrite("pic.jpg", frame)
#     cv2.waitKey(1000)
#     camera.release()


## Capture a video and write it to a file.
##
## Currently, the file can be written but seems to lack contents
#def record_video(duration):
#    camera.open(0)
#    output = cv2.VideoWriter()
#    for i in range(0,file["fps"]*duration):
#        tmp, frame = camera.read()
#        if not output.isOpened():
#            output.open(file["name"], file["fourcc"], file["fps"], file["size"], file["color"])
#            if not output.isOpened():
#                print "Error opening output file"
#                break
##        if frame.empty():
##            break
##        print type(frame)
##        cv2.imshow("test", frame)
##        cv2.imwrite("out/%.3d.jpg" % i, frame)
#        frame[0:i][0:50] = [0,255,0]
#        output.write(frame)
#        cv2.waitKey(1)
#
#    camera.release()
#    output.release()



if __name__ == "__main__":
    func()
#    take_picture()
#    record_video(1)

