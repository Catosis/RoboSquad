#include <stdio.h>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <math.h>
#include <pigpio.h>
#include <squad/Kiwi.h>

//#include <opencv2/opencv.hpp>
//using namespace cv;


/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
// %Tag(CALLBACK)%
//oid poseMessageReceived ( const turtlesim : : Pose& msg) 
void kiwiDrive(const squad::Kiwi &msg)
{
  //ROS_INFO("Components: [%f, %f, %f]", (msg.w1, msg.w2, msg.w3)) 
  //GPIO PWM outputs
  gpioPWM(17, msg.w1); //Pin 17, 255 is 100% power
  gpioPWM(12, msg.w2);
  gpioPWM(14, msg.w3);
}

void initalizeGPIO()
{
  if (gpioInitialise() < 0)
  {
    // pigpio initialisation failed.
    ROS_DEBUG("GPIO INIT FAILED");
  }
  else
  {
    // pigpio initialised okay.
    return;
  }
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "robot_key_drive");
  initalizeGPIO();
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("turtle1/cmd_vel", 1000, kiwiDrive);


  ros::spin();

  gpioTerminate();
  return 0;
}

