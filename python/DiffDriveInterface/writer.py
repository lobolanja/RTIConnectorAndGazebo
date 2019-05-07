###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################


"""Interface to send commands to the Differential Drive"""

from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../../../")
import rticonnextdds_connector as rti
from tkinter import *
from tkinter import ttk

class Aplication():
    def __init__(self):

        self.connector = rti.Connector("MyParticipantLibrary::Zero",
                                filepath + "/../tech.xml")
        self.outputDDS = self.connector.getOutput("MyPublisher::DiffDriveWriter")
        self.inputDDS = self.connector.getInput("MySubscriber::DiffDriveReader")

        self.root = Tk()
        self.root.geometry('300x200')


        self.root.resizable(width=False, height=False)
        self.root.title("Differential Drive")

        self.b_increase_vel = ttk.Button(self.root, text="+ VEL", command=self.increase_vel)
        self.b_increase_vel.pack(side=TOP)
        self.b_decrease_vel = ttk.Button(self.root, text="- VEL", command=self.decrease_vel)
        self.b_decrease_vel.pack(side=BOTTOM)

        self.b_rigth = ttk.Button(self.root, text="-->", command=self.right)
        self.b_rigth.pack(side=RIGHT)
        self.b_left = ttk.Button(self.root, text="<--", command=self.left)
        self.b_left.pack(side=LEFT)

        self.vel=0
        self.turn=0
        self.root.mainloop()
    
    def increase_vel(self):
        self.vel = self.vel + 0.2
        self.outputDDS.instance.setNumber("linear.x", self.vel)
        self.outputDDS.write()
        print(self.vel)

    def decrease_vel(self):
        self.vel = self.vel - 0.2
        self.outputDDS.instance.setNumber("linear.x", self.vel)
        self.outputDDS.write()
        print(self.vel)

    def right(self):
        self.turn = self.turn + 0.2
        self.outputDDS.instance.setNumber("angular.z", self.turn)
        self.outputDDS.write()
        print(self.turn)

    def left(self):
        self.turn = self.turn - 0.2
        self.outputDDS.instance.setNumber("angular.z", self.turn)
        self.outputDDS.write()
        print(self.turn)



def main():
    my_app = Aplication()
    return 0

if __name__ == '__main__':
    main()
     
    
