from PyQt4 import QtGui
import pygame
import sys

class ImageWidget(QtGui.QWidget):
    def __init__(self,surface,parent=None):
        super(ImageWidget,self).__init__(parent)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image=QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)
        image = QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)
        l = QtGui.QLabel()
        l.setPixmap(QtGui.QPixmap(self.image))

        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(l)

    def handleButton(self):
    	print("test successful")

    def paintEvent(self,event):
        qp=QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()


class MainWindow(QtGui.QMainWindow):
    def __init__(self,surface,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface))

class Ship(object):
    def __init__(self):
        self.x, self.y = (0, 0)
        self.set_target((0, 0))
        self.speed = 0.7

    @property
    def pos(self):
        return self.x, self.y

    # for drawing, we need the position as tuple of ints
    # so lets create a helper property
    @property
    def int_pos(self):
        return map(int, self.pos)

    @property
    def target(self):
        return self.t_x, self.t_y

    @property
    def int_target(self):
        return map(int, self.target)   

    def set_target(self, pos):
        self.t_x, self.t_y = pos

    def update(self):
        # if we won't move, don't calculate new vectors
        if self.int_pos == self.int_target:
            return 

        target_vector = sub(self.target, self.pos) 

        # a threshold to stop moving if the distance is to small.
        # it prevents a 'flickering' between two points
        if magnitude(target_vector) < 2: 
            return

        # apply the ship's speed to the vector
        move_vector = [c * self.speed for c in normalize(target_vector)]

        # update position
        self.x, self.y = add(self.pos, move_vector)

    def draw(self, s):
        pygame.draw.circle(s, (255, 0 ,0), self.int_pos, 2)

pygame.init()
s=pygame.Surface((640,480))
s.fill((64,128,192,224))
#pygame.draw.circle(s,(255,255,255,255),(100,100),50)



app=QtGui.QApplication(sys.argv)
w=MainWindow(s)
w.show()
app.exec_()