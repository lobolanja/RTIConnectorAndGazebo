###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

"""Reader the params sent by Differential Drive in the joint topic."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep

filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../../../")
import rticonnextdds_connector as rti

connector = rti.Connector("MyParticipantLibrary::Zero",
                          filepath + "/../tech.xml")
# Create a data Reader
inputDDS = connector.getInput("MySubscriber::DiffDriveReader")

for i in range(1, 500):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(0, numOfSamples):
        if inputDDS.infos.isValid(j):
            """Get it as a dictionary and then access the field in the
            standard python way:"""
            sample = inputDDS.samples.getDictionary(j)
            # Print the sample
            print(sample)
    sleep(2)
