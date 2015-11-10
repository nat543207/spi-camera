""" Handle motion-related events, e. g. beginning capture.
    Should accept input from the IR sensor, and may interface with
    OpenCV to detect motion in buffered video.

    The video capture and image processing should probably be done in
    parallel (separate threads / python equivalent)
"""

# Determine if the IR sensor on the Pi is detecting motion
def IR_detects_motion():
    # Read from GPIO pin(s) to determine if IR sensor is triggered
    # Return result
    pass

# Determine if there is motion in the frames using a computer vision algorithm
def CV_detects_motion():
    # Accept some arguments, probably background and captured image
    # Utilize one of OpenCV's vision algorithms, probably background subtraction
    # Return result (bool or movement mask, not sure which one yet)
    pass
