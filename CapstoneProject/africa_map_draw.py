#drow africa map

from brachiograph import BrachioGraph
from linedraw import *

inner_arm = 8
outer_arm = 8

bg = BrachioGraph(inner_arm, outer_arm)

if __name__ == "__main__":

    # vectorise an image to json file
    image_to_json("africa", draw_contours=2, draw_hatch=16)
    # draw with the plotter
    bg.plot_file("images/africa.json")
