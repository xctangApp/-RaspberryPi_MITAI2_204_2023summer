#download a new image and draw

import sys
import requests
from brachiograph import BrachioGraph
from linedraw import *

inner_arm = 8
outer_arm = 8

bg = BrachioGraph(inner_arm, outer_arm)

if __name__ == "__main__":

    file_url = sys.argv[1]
    file_object = requests.get(file_url)
    file_name = "download"
    with open("images/" + file_name + ".jpg", "wb") as local_file:
        local_file.write(file_object.content)

    # vectorise an image to json file
    image_to_json(file_name, draw_contours=2, draw_hatch=16)
    # draw with the plotter
    bg.plot_file("images/" + file_name + ".json")
