
(cl:in-package :asdf)

(defsystem "squad-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Kiwi" :depends-on ("_package_Kiwi"))
    (:file "_package_Kiwi" :depends-on ("_package"))
  ))