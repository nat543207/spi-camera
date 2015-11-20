""" Implements functions that save video buffer stored in memory to a file.
    Will probably use OpenCV funcitons/types to accomtypes to accomplish this.
"""
import cv2
from Queue import Queue
from datetime import datetime
import motion


class Frame:
    def __init__(self, timestamp, image, has_motion):
        self.timestamp = timestamp
        self.image = image
        self.has_motion = has_motion


def capture_from(camera):
    success, img = camera.read()
    has_motion = motion.IR_detects_motion() or  motion.CV_detects_motion(img)
    return Frame(datetime.now(), img, has_motion)


camera = cv2.VideoCapture(0)

def record_on_motion(savedir='.', fourcc=cv2.cv.CV_FOURCC(*"XVID"), fps=30, size=(640,480), color=True):
    vidbuf = Queue()
    output = cv2.VideoWriter()
    bufsize = 60
    recording = False

    for i in range(0, bufsize):
        vidbuf.put(capture_from(camera))

    while True:
        frame = capture_from(camera)
        if frame.has_motion:
            recording = True
            if not output.isOpened():
                filename = savedir + '/' + str(datetime.now()) + ".avi"
                output.open(filename, fourcc, fps, size, color)
            while 0 < vidbuf.qsize():
                output.write(vidbuf.get().image)
            output.write(frame.image)
        else: #if not frame.has_motion:
            vidbuf.put(capture_from(camera))
            if bufsize < vidbuf.qsize():
                vidbuf.get(True)
                if recording == True:
                    while 0 < vidbuf.qsize():
                        output.write(vidbuf.get().image)
                    recording = False
                    break


if __name__ == "__main__":
    record_on_motion(str(datetime.now()) + ".avi")
