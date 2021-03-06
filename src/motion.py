""" Handle motion-related events, e. g. beginning capture.
    Should accept input from the IR sensor, and may interface with
    OpenCV to detect motion in buffered video.

    The video capture and image processing should probably be done in
    parallel (separate threads / python equivalent)
"""

import cv2

# Determine if there is motion in the frames using a computer vision algorithm
def CV_detects_motion(frame):
    # Accept some arguments, probably background and captured image
    # Utilize one of OpenCV's vision algorithms, probably background subtraction
    # Return result (bool or movement mask, not sure which one yet)

    #Thanks to the user 'ravwojdyla' on StackOverflow for this Python
    #alternative to static funciton variables
    #http://stackoverflow.com/questions/279561

    try:
        CV_detects_motion.background_reset_counter += 1
    except AttributeError:
        CV_detects_motion.background_reset_counter = 1


    motion = CV_detects_motion.motion_detector.apply(frame)
    contours, h = cv2.findContours(motion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("Motion", motion)
    cv2.waitKey(1)

    #Occasionally reset background model to account for noise
    if 90 < CV_detects_motion.background_reset_counter:
        CV_detects_motion.motion_detector = cv2.BackgroundSubtractorMOG()
        CV_detects_motion.background_reset_counter = 1

    threshold = 25
    for c in contours:
        if threshold**2 < cv2.contourArea(c):
            return True;
    return False
CV_detects_motion.motion_detector = cv2.BackgroundSubtractorMOG()


try:
    import RPi.GPIO as gpio
    
    
    io_pin = 7
    gpio.setmode(gpio.BOARD)
    gpio.setup(io_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    
    # Determine if the IR sensor on the Pi is detecting motion
    def IR_detects_motion():
        if gpio.input(io_pin):
            #print "Motion detected by IR!"
            print IR_detects_motion.testvar
            IR_detects_motion.testvar += 1
            return True
            #return bool(gpio.input(io_pin))
    IR_detects_motion.testvar = 0
except ImportError:
    print "This machine is not a Raspberry Pi, disabling GPIO support..."

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    CV_detects_motion(camera.read()[1])
