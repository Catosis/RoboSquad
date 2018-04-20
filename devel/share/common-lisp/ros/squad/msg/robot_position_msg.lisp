; Auto-generated. Do not edit!


(cl:in-package squad-msg)


;//! \htmlinclude robot_position_msg.msg.html

(cl:defclass <robot_position_msg> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass robot_position_msg (<robot_position_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_position_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_position_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name squad-msg:<robot_position_msg> is deprecated: use squad-msg:robot_position_msg instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <robot_position_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader squad-msg:x-val is deprecated.  Use squad-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <robot_position_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader squad-msg:y-val is deprecated.  Use squad-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <robot_position_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader squad-msg:angle-val is deprecated.  Use squad-msg:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_position_msg>) ostream)
  "Serializes a message object of type '<robot_position_msg>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_position_msg>) istream)
  "Deserializes a message object of type '<robot_position_msg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_position_msg>)))
  "Returns string type for a message object of type '<robot_position_msg>"
  "squad/robot_position_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_position_msg)))
  "Returns string type for a message object of type 'robot_position_msg"
  "squad/robot_position_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_position_msg>)))
  "Returns md5sum for a message object of type '<robot_position_msg>"
  "269c87d34c95513f467e300b14f117c0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_position_msg)))
  "Returns md5sum for a message object of type 'robot_position_msg"
  "269c87d34c95513f467e300b14f117c0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_position_msg>)))
  "Returns full string definition for message of type '<robot_position_msg>"
  (cl:format cl:nil "int32 x~%int32 y~%float32 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_position_msg)))
  "Returns full string definition for message of type 'robot_position_msg"
  (cl:format cl:nil "int32 x~%int32 y~%float32 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_position_msg>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_position_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_position_msg
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':angle (angle msg))
))
