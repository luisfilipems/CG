from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

a = 0.3535
b = 0.5

def Octaedro():
    glBegin(GL_TRIANGLES)
    glColor(0,0.2,0.6)
    glVertex3f(-a,0,a)
    glVertex3f(-a,0,-a)
    glVertex3f(0,b,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,1.0,0.6)
    glVertex3f(-a,0,-a)
    glVertex3f(a,0,-a)
    glVertex3f(0,b,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0,1.0,0.2)
    glVertex3f(a,0,-a)
    glVertex3f(a,0,a)
    glVertex3f(0,b,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.4,0,0.9)
    glVertex3f(a,0,a)
    glVertex3f(-a,0,a)
    glVertex3f(0,b,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.2,1.0)
    glVertex3f(a,0,-a)
    glVertex3f(-a,0,-a)
    glVertex3f(0,-b,0)
    glEnd()

    #6
    glBegin(GL_TRIANGLES)
    glColor(0.4,0.9,0.1)
    glVertex3f(-a,0,-a)
    glVertex3f(-a,0,a)
    glVertex3f(0,-b,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.3,1.0)
    glVertex3f(a,0,a)
    glVertex3f(a,0,-a)
    glVertex3f(0,-b,0)
    glEnd()

	#8
    glBegin(GL_TRIANGLES)
    glColor(0,0.8,0.9)
    glVertex3f(-a,0,a)
    glVertex3f(a,0,a)
    glVertex3f(0,-b,0)
    glEnd()    


def abc():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,2,0,1)
    Octaedro()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600) 
glutCreateWindow("OCTAEDRO")    
glutDisplayFunc(abc)  
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.) 
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-3)
glRotatef(45,10,10,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



