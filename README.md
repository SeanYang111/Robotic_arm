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
## How it works
1. A user interface:   
   We use PyQt5 to simulate a GUI for users. There're five buttons on it. When a user click one button, it will establish a ROS topic, sending the "floor imformation" to the topic, and waiting for a subscriber to receive it.   
<img width="179" alt="image" src="https://github.com/SeanYang111/Robotic_arm/assets/90599095/d0861c20-9911-472b-a129-d0183d952ccd">

2. Start the MOveit:   
   Moveit is an open-soucrce platform which allows users to plan the robot's movement path. We set our joints as a group called "arm". Launch the file "move_group.launch" will avtivate moveit, so that users can start planing the path for the robotic arm.   
   <img width="293" alt="image" src="https://github.com/SeanYang111/Robotic_arm/assets/90599095/44c5261c-a71a-48fc-a69f-f0a4be089897">

3. Run the control node:   
   We create another node, receiving the message from the topic created by the user interface. Then according to the floor the user choose, it will create a certain list for the group "arm", setting a specific angle for revolution joints and length for prismetic joints. Then this list will be sent to moveit to plan the robotic arm's movement.   
   ![image](https://github.com/SeanYang111/Robotic_arm/assets/90599095/89e7e322-88ba-424d-94a9-663d5a94e534)

4. Rviz simulation and Gazebo :   
   After planning the path, Moveit can send the result on a simulation platform called "Rviz". In Rviz, we can see the results of planing path for the robotic arm. In the meanwhile, the result will be sent to a real-world simulation platform calledf "Gazebo". Ideally, the result on Rviz and Gazebo should be the same. If not, we should adjust the PID controller for Gazebo simulation.   
<img width="349" alt="image" src="https://github.com/SeanYang111/Robotic_arm/assets/90599095/3bc8ed42-7cff-46e8-8de6-bcbb286bb71c">
<img width="262" alt="image" src="https://github.com/SeanYang111/Robotic_arm/assets/90599095/041b1d3e-50ee-47d5-beec-ea4e48903b0d">

![image](https://github.com/SeanYang111/Robotic_arm/assets/90599095/9bbd5fa4-b7f0-4893-88db-b2cc7b91b8fe)
(The reason why the robotic arm model on gazebo is all grey is that we use URDF format to write the robotic model. However, Gazebo is using SDF format, and Gazebo has a limitation in converting URDF to SDF. It's Gazebo's native object description format. This means that Gazebo may not read the material color in URDF. We've tried every methods but it still doesn't work. Luckily in Rviz, it works perfectly.)

5. Demo :
   

https://github.com/SeanYang111/Robotic_arm/assets/90599095/2b2a8bb9-bb54-42fc-9726-0b270130699f

