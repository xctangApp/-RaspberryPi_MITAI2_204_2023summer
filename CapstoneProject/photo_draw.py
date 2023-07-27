#draw a photo image

import sys
from brachiograph import BrachioGraph
from linedraw import *

inner_arm = 8
outer_arm = 8

bg = BrachioGraph(inner_arm, outer_arm)

if __name__ == "__main__":

    photo_name = sys.argv[1]
    # vectorise an image to json file
    image_to_json(photo_name, draw_contours=2, draw_hatch=16)
    # draw with the plotter
    bg.plot_file("images/" + photo_name + ".json")
