;; Auto-generated. Do not edit!


(when (boundp 'squad::Kiwi)
  (if (not (find-package "SQUAD"))
    (make-package "SQUAD"))
  (shadow 'Kiwi (find-package "SQUAD")))
(unless (find-package "SQUAD::KIWI")
  (make-package "SQUAD::KIWI"))

(in-package "ROS")
;;//! \htmlinclude Kiwi.msg.html


(defclass squad::Kiwi
  :super ros::object
  :slots (_w1 _w2 _w3 ))

(defmethod squad::Kiwi
  (:init
   (&key
    ((:w1 __w1) 0.0)
    ((:w2 __w2) 0.0)
    ((:w3 __w3) 0.0)
    )
   (send-super :init)
   (setq _w1 (float __w1))
   (setq _w2 (float __w2))
   (setq _w3 (float __w3))
   self)
  (:w1
   (&optional __w1)
   (if __w1 (setq _w1 __w1)) _w1)
  (:w2
   (&optional __w2)
   (if __w2 (setq _w2 __w2)) _w2)
  (:w3
   (&optional __w3)
   (if __w3 (setq _w3 __w3)) _w3)
  (:serialization-length
   ()
   (+
    ;; float32 _w1
    4
    ;; float32 _w2
    4
    ;; float32 _w3
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _w1
       (sys::poke _w1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _w2
       (sys::poke _w2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _w3
       (sys::poke _w3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _w1
     (setq _w1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _w2
     (setq _w2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _w3
     (setq _w3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get squad::Kiwi :md5sum-) "bd82aec785cf5731a7d25a0042e76809")
(setf (get squad::Kiwi :datatype-) "squad/Kiwi")
(setf (get squad::Kiwi :definition-)
      "float32 w1
float32 w2
float32 w3

")



(provide :squad/Kiwi "bd82aec785cf5731a7d25a0042e76809")


