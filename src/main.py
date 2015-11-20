#!/user/bin/env python2
""" Main file.  The program's subprocesses should be managed here.
    For now, the program just prints a message.
"""
import os
import capture

# Execute main loop.  Not very interesting.  Move along now.
def main():
    # Thanks to StackOverflow users Blair Conrad and jesterjunk
    # for how to make missing directories!
    # http://stackoverflow.com/questions/273192
    output_dir = "./captures"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while True:
        capture.record_on_motion(output_dir)



if __name__ == "__main__":
    main()
