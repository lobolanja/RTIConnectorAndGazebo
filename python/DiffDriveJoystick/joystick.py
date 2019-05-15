###############################################################################
# (c) 2005-2019 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

"""Bridge Between ShapesDemo And Differential Drive plugin."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep

filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../../../")
import rticonnextdds_connector as rti

class Joystick():

    def __init__(self):
        self.connector = rti.Connector("MyParticipantLibrary::Zero",
                                filepath + "/../ShapeExample.xml")
        self.connector2 = rti.Connector("MyParticipantLibrary::Zero",
                                filepath + "/../tech.xml")
        self.inputDDS = self.connector.getInput("MySubscriber::MySquareReader")
        self.outputDDS = self.connector2.getOutput("MyPublisher::DiffDriveWriter")


    def set_volicity(self, linear_x, angular_z):
        """set the linear speed, to go forward or backward and
        the angular speed to turn left and right"""
        self.outputDDS.instance.setNumber("linear.x", linear_x)
        self.outputDDS.instance.setNumber("angular.z", angular_z)
        self.outputDDS.write()

    def calc_velocity(self, pos, initial_pos, multiplier):
        """Calculate the speed as a function of the position
        of the square in ShapesDemo"""
        if (pos < 80):
            velocity = 1-(pos - initial_pos)/80
        else:
            velocity = (pos - initial_pos)/80
        velocity = velocity*multiplier
        return velocity
        
    def select_comand(self, x, y):

        if(y < 80):
            if (x < 80):
                # Front and left
                self.set_volicity(
                    self.calc_velocity(y, 0, 2),
                    self.calc_velocity(x, 0, -1))
            elif (x < 160):
                # Front
                self.set_volicity(
                    self.calc_velocity(y, 0, 2),
                    0)
            else:
                # Front and right
                self.set_volicity(
                    self.calc_velocity(y, 0, 2),
                    self.calc_velocity(x, 160, 1)) 

        elif(y < 160):
            
            if (x < 80):
                # Left
                self.set_volicity(
                    0,
                    self.calc_velocity(x, 0, -1)) 
            elif (x < 160):
                # Stop
                self.set_volicity(0, 0)
            else :
                # Right
                self.set_volicity(
                    0,
                    self.calc_velocity(x, 160, 1)) 

        else:
            if (x < 80):
                # Back and left
                self.set_volicity(
                    self.calc_velocity(y, 160, -2),
                    self.calc_velocity(x, 0, -1)) 
            elif (x < 160):
                # Back
                self.set_volicity(
                    self.calc_velocity(y, 160, -2),
                    0) 
            else :
                # Back and right
                self.set_volicity(
                    self.calc_velocity(y, 160, -2),
                    self.calc_velocity(x, 160, 1)) 

    def loop_joystick(self):
        "Loop of the reader"
        for i in range(1, 5000):
            self.inputDDS.take()
            numOfSamples = self.inputDDS.samples.getLength()
            for j in range(0, numOfSamples):
                if self.inputDDS.infos.isValid(j):
                    # Access each single field with the connector API:
                    x = self.inputDDS.samples.getNumber(j, "x")
                    y = self.inputDDS.samples.getNumber(j, "y")

                    self.select_comand(x, y)           
            sleep(0.1) 

if __name__ == '__main__':
    my_joystick = Joystick()
    my_joystick.loop_joystick()
