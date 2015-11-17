""" Handle motion-related events, e. g. beginning capture.
    Should accept input from the IR sensor, and may interface with
    OpenCV to detect motion in buffered video.

    The video capture and image processing should probably be done in
    parallel (separate threads / python equivalent)
"""

import cv2

# Determine if the IR sensor on the Pi is detecting motion
def IR_detects_motion():
    # Read from GPIO pin(s) to determine if IR sensor is triggered
    # Return result
    pass


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

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    CV_detects_motion(camera.read()[1])
