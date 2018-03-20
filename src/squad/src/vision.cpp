#include <stdio.h>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv )
{
    //init ros
    ros::init(argc, argv, "talker");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("vision_out", 2);

    ros::Rate rate(10);

    while(ros::ok()) {
       std_msgs::String msg;
       msg.data = "test message";
       pub.publish(msg);

       ROS_INFO("%s", msg.data.c_str());
       //Delays untill it is time to send another message
       rate.sleep();
     }

    /*\
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }
    Mat image;
    image = imread( argv[1], 1 );
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;*/
}
