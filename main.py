#!/bin/bash

import numpy as np
import getopt, sys
#import argparse

def getArgs ():

    # Remove 1st argument from the list of command line arguments
    argumentList = sys.argv[1:]

    # Options
    options = "h"

    # Long options
    long_options = ["help", "heigth=", "arc="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        return arguments

    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        sys.exit(1)

def main ():
    print("Executing main")
    print(np.__version__)

    arguments = getArgs()
    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print ("Displaying Help")

if __name__ == "__main__":
    main()
