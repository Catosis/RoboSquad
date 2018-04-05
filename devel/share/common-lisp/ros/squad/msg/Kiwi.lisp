; Auto-generated. Do not edit!


(cl:in-package squad-msg)


;//! \htmlinclude Kiwi.msg.html

(cl:defclass <Kiwi> (roslisp-msg-protocol:ros-message)
  ((w1
    :reader w1
    :initarg :w1
    :type cl:float
    :initform 0.0)
   (w2
    :reader w2
    :initarg :w2
    :type cl:float
    :initform 0.0)
   (w3
    :reader w3
    :initarg :w3
    :type cl:float
    :initform 0.0))
)

(cl:defclass Kiwi (<Kiwi>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Kiwi>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Kiwi)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name squad-msg:<Kiwi> is deprecated: use squad-msg:Kiwi instead.")))

(cl:ensure-generic-function 'w1-val :lambda-list '(m))
(cl:defmethod w1-val ((m <Kiwi>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader squad-msg:w1-val is deprecated.  Use squad-msg:w1 instead.")
  (w1 m))

(cl:ensure-generic-function 'w2-val :lambda-list '(m))
(cl:defmethod w2-val ((m <Kiwi>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader squad-msg:w2-val is deprecated.  Use squad-msg:w2 instead.")
  (w2 m))

(cl:ensure-generic-function 'w3-val :lambda-list '(m))
(cl:defmethod w3-val ((m <Kiwi>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader squad-msg:w3-val is deprecated.  Use squad-msg:w3 instead.")
  (w3 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Kiwi>) ostream)
  "Serializes a message object of type '<Kiwi>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'w1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'w2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'w3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Kiwi>) istream)
  "Deserializes a message object of type '<Kiwi>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'w1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'w2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'w3) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Kiwi>)))
  "Returns string type for a message object of type '<Kiwi>"
  "squad/Kiwi")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Kiwi)))
  "Returns string type for a message object of type 'Kiwi"
  "squad/Kiwi")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Kiwi>)))
  "Returns md5sum for a message object of type '<Kiwi>"
  "bd82aec785cf5731a7d25a0042e76809")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Kiwi)))
  "Returns md5sum for a message object of type 'Kiwi"
  "bd82aec785cf5731a7d25a0042e76809")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Kiwi>)))
  "Returns full string definition for message of type '<Kiwi>"
  (cl:format cl:nil "float32 w1~%float32 w2~%float32 w3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Kiwi)))
  "Returns full string definition for message of type 'Kiwi"
  (cl:format cl:nil "float32 w1~%float32 w2~%float32 w3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Kiwi>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Kiwi>))
  "Converts a ROS message object to a list"
  (cl:list 'Kiwi
    (cl:cons ':w1 (w1 msg))
    (cl:cons ':w2 (w2 msg))
    (cl:cons ':w3 (w3 msg))
))
