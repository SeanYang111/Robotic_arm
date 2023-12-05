#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Int32
import moveit_commander
from geometry_msgs.msg import Pose
import time

class RoboticArmControl:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('robotic_arm_control', anonymous=True)

        # Initialize MoveIt! commander for your robotic arm
        self.arm_group = moveit_commander.MoveGroupCommander("arm")  # Replace with your group name
        self.floor_sub = rospy.Subscriber('selected_floor', Int32, self.floor_callback)

    def floor_callback(self, data):
        rospy.loginfo("Received floor number: %s", data.data)
        self.move_robotic_arm(data.data)

    def move_robotic_arm(self, floor_number):
        # Example logic to adjust the joints based on the selected floor
        # Note: These positions are hypothetical. You need to adjust them based on your robot's configuration
        joint_goal = self.arm_group.get_current_joint_values()
        
        if floor_number == 1:
            joint_goal[0] = 0  # Base joint
            joint_goal[1] = 1.58  # Second joint
            joint_goal[2] = 0.47  # Third joint
            pris = 0.16  # Extendable part (prismatic joint)

        # Add conditions for other floors...
        # The following are just placeholders:
        elif floor_number == 2:
            joint_goal[0] = 0
            joint_goal[1] = 1.24
            joint_goal[2] = 0.65
            pris = 0.14

        elif floor_number == 3:
            joint_goal[0] = 0
            joint_goal[1] = 0.86
            joint_goal[2] = 0.86
            pris = 0.18
            
        elif floor_number == 4:
            joint_goal[0] = 0
            joint_goal[1] = 0.8
            joint_goal[2] = 0.62
            pris = 0.19
         
        elif floor_number == 5:
            joint_goal[0] = 0
            joint_goal[1] = 0.62
            joint_goal[2] = 0.59
            pris = 0.27
        # Send the joint goal to the MoveIt! to execute
        self.arm_group.set_max_velocity_scaling_factor(0.3)
        self.arm_group.go(joint_goal, wait=True)
        self.arm_group.set_max_velocity_scaling_factor(1.0)
        joint_goal[3] = pris
        self.arm_group.go(joint_goal, wait=True)
        # Hold the position for a second
        # Retract the prismatic joint back to 0
        self.arm_group.set_max_velocity_scaling_factor(1.0)
        joint_goal[3] = 0
        self.arm_group.go(joint_goal, wait=True)
        
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    arm_control = RoboticArmControl()
    arm_control.run()
