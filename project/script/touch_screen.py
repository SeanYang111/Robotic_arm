#!/usr/bin/env python3
import sys
import rospy
from std_msgs.msg import Int32
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class TouchScreen(QWidget):
    def __init__(self):
        super(TouchScreen, self).__init__()
        self.initUI()
    
    def initUI(self):
        
        rospy.init_node('touch_screen', anonymous=True)
        self.floor_pub = rospy.Publisher('selected_floor', Int32, queue_size=10)
        
        
        vbox = QVBoxLayout()
        
        for i in range(1, 6):
            btn = QPushButton('Floor {}'.format(i), self)
            btn.clicked.connect(lambda _, b=i: self.publish_floor(b))
            vbox.addWidget(btn)
        
        self.setLayout(vbox)
        self.setWindowTitle('Elevator Touch Screen')
        self.show()
    
    def publish_floor(self, floor):
        rospy.loginfo('Selected floor: %s' % floor)
        self.floor_pub.publish(floor)

def main():
    app = QApplication(sys.argv)
    ex = TouchScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

