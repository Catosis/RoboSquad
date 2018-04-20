;; Auto-generated. Do not edit!


(when (boundp 'squad::robot_position_msg)
  (if (not (find-package "SQUAD"))
    (make-package "SQUAD"))
  (shadow 'robot_position_msg (find-package "SQUAD")))
(unless (find-package "SQUAD::ROBOT_POSITION_MSG")
  (make-package "SQUAD::ROBOT_POSITION_MSG"))

(in-package "ROS")
;;//! \htmlinclude robot_position_msg.msg.html


(defclass squad::robot_position_msg
  :super ros::object
  :slots (_x _y _angle ))

(defmethod squad::robot_position_msg
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:angle __angle) 0.0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _angle (float __angle))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:serialization-length
   ()
   (+
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; float32 _angle
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get squad::robot_position_msg :md5sum-) "269c87d34c95513f467e300b14f117c0")
(setf (get squad::robot_position_msg :datatype-) "squad/robot_position_msg")
(setf (get squad::robot_position_msg :definition-)
      "int32 x
int32 y
float32 angle

")



(provide :squad/robot_position_msg "269c87d34c95513f467e300b14f117c0")


