#!/bin/bash

import numpy as np
#from sys import exit
import argparse

def getArgs ():

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-t", "--turns", type = float, help = "Define the number of turns")
    parser.add_argument("-H", "--height", type = float, help = "Define the net height (cm)")
    parser.add_argument("-r", "--radious", type = float, default=60.0, help = "Define radious (cm)")
    parser.add_argument("-f", "--footprint", type = float, help = "Define footprint at the radious distance (cm)")
    parser.add_argument("-s", "--steps", type = int, help = "Define the steps (final level included)")
    parser.add_argument("-d", "--diameter", type = float, help = "Central tube diameter (cm)")


    # Read arguments from command line
    try:
        args = parser.parse_args()
    except Exception as e:
        print("{}".format(str(e)))

    return args

def main ():
    print("Executing Spiral Staircase Calculator")
    print(np.__version__)

    height = 0 # Spacing between steps
    radious = 0 # Max distance from the tube to the external step edge
    steps = 0 # Steps in the stair
    turns = 0 # Number of turns the spiral stair does
    working_angle = 0 # The working angle = turns * 2 * np.pi
    step_angle = 0 # Radians # Angle for each stair's step

    min_height_contstep = 17.5 # cm # Minimun spacing between steps
    min_mid_step = 25 # cm # Minimun withd at the middle of a step

    result = "Resulting data:"
    args = getArgs()
    if args.height:
        result += "\nDisplaying height as: {}".format(args.height)
        height = args.height

    if args.radious:
        result += "\nDisplaying radious as: {}".format(args.radious)
        radious = args.radious

    if args.steps:
        result += "\nDisplaying steps as: {}".format(args.steps)
        steps = args.steps
        h_for_step = height / steps
        result += "\nHeight for step: {}".format(h_for_step)

    if args.turns:
        turns = args.turns

        if turns > 4:
            raise ValueError("Too many turns.")
        result += "\nDisplaying turns as: {}".format(args.turns)


        working_angle = turns*2*np.pi
        step_angle = working_angle/steps

        result += "\n\nDisplaying angle (radians) as: {}".format(step_angle)
        result += "\nDisplaying angle (degrees) as: {}\n".format(step_angle*180/np.pi)

        min_rad = radious * np.cos(step_angle / 2)
        min_footprint = 2 * radious * np.sin(step_angle / 2)

        result += "\nDisplaying triangle height (cm) as: {}".format(min_rad)
        result += "\nDisplaying min footprint (cm) as: {}".format(min_footprint)

    if args.footprint:
        result += "\n\nDisplaying given footprint as: {}".format(args.footprint)
        result += "\nDisplaying given half-step footprint as: {}".format(args.footprint/2)

    ### Get the mid step
    # mstep = mid_step()

    print(result)

if __name__ == "__main__":
    main()
