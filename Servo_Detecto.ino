#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle  nh;

Servo servo;

void servo_cb(const std_msgs::Float32& Prediction){

  if (Prediction.data > 0.5){
    servo.write(180);
  }
  else if (Prediction.data < 0.5){
    servo.write(0);
  }
}


ros::Subscriber<std_msgs::Float32> sub("servo", servo_cb);

void setup(){
  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  
  servo.attach(9); //attach it to pin 9
}

void loop(){
  nh.spinOnce();
  delay(100);
}
