# Robotic Arm for people using wheelchairs
A project for 601  
* Zheng, Yu-Jie  
* Yang, Bo-Shiang
## Product Mission
1. A robotic arm extends the user's reach and capabilities beyond the limitations of their wheelchair.
2. The robotic arm can enable wheelchair users to perform essential daily tasks independently. 
3. The goal is to recognize and match the digit pressed on the touch screen with the corresponding elevator button, initiating the elevator to the desired floor.
4. We'll simulate the scene on Gazebo
## Environments
* Camera
* Touch Screen
* Robotic Arm
* Wheelchair
## Progress for now
1. Set the Elevator Scene on Gazebo  
   (Still need to adjust the Color And Texture Models.  Resource: https://classic.gazebosim.org/tutorials?tut=color_model&cat= )
![2c0087fad9c601217bcbc27ca240aec](https://github.com/SeanYang111/Robotic_arm/assets/90599095/28740c56-a286-4e96-9d85-9d8aeea5e549)
2. Design the robotic arm on Rviz
   * Using the urdf. file to design the model. Basically it's just a XML format.
   * It has one base-link and three links. Each two links have a sphere as an revolute joint. At the edge, it has a rectangular cuboid serving as a prismatic link, which means it can only move linearly. The last link's goal is set to touch the button on the elevator.
   * I had it have color :)
   * Also, right now it has four topics to control the angle of each joint manually. In the future, that's all automatically.
![image](https://github.com/SeanYang111/Robotic_arm/assets/90599095/c25529b1-0f19-467c-a085-e62156edac5c)
3. I wrote a python script to simulate the touch screen. It has 9 buttons on it. I use PyQt5 to create a window and buttons.
   (resource: https://pypi.org/project/PyQt5/)   
   * Right now the topic contains the message of the buttons I press. And I'm still trying to find a way to let the robotic arm receive the message.
![image](https://github.com/SeanYang111/Robotic_arm/assets/90599095/d38a8fad-9c00-44cf-846e-b4d7952651e9)
