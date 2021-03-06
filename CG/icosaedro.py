from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

a = 0.5
b = 0.1591

def Icosaedro():
    glBegin(GL_TRIANGLES)
    glColor(0,0.2,0.6)
    glVertex3f(0,0.1591,-0.5)
    glVertex3f(0.1591,0.5,0)
    glVertex3f(-0.1591,0.5,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,1.0,0.6)
    glVertex3f(0,0.1591,0.5)
    glVertex3f(-0.1591,0.5,0)
    glVertex3f(0.1591,0.5,0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0,1.0,0.2)
    glVertex3f(0,b,a)
    glVertex3f(0,-b,a)
    glVertex3f(-a,0,b)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.4,0,0.9)
    glVertex3f(0,b,a)
    glVertex3f(a,0,b)
    glVertex3f(0,-b,a)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.2,1.0)
    glVertex3f(0,b,-a)
    glVertex3f(0,-b,-a)
    glVertex3f(a,0,-b)
    glEnd()

    #6
    glBegin(GL_TRIANGLES)
    glColor(0,0.8,0.111)
    glVertex3f(0,b,-a)
    glVertex3f(-a,0,-b)
    glVertex3f(0,-b,-a)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.3,1.0)
    glVertex3f(0,-b,a)
    glVertex3f(b,-a,0)
    glVertex3f(-b,-a,0)
    glEnd()

	#8
    glBegin(GL_TRIANGLES)
    glColor(0,0.8,0.9)
    glVertex3f(0,-b,-a)
    glVertex3f(-b,-a,0)
    glVertex3f(b,-a,0)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(0.3,0.8,0)
    glVertex3f(-b,a,0)
    glVertex3f(-a,0,b)
    glVertex3f(-a,0,-b)
    glEnd()    

	#10
    glBegin(GL_TRIANGLES)
    glColor(0,1.0,0.3)
    glVertex3f(-b,-a,0)
    glVertex3f(-a,0,-b)
    glVertex3f(-a,0,b)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(1,0.2,0.2)
    glVertex3f(b,a,0)
    glVertex3f(a,0,-b)
    glVertex3f(a,0,b)
    glEnd()    

	#12
    glBegin(GL_TRIANGLES)
    glColor(0,0.2,0.9)
    glVertex3f(b,-a,0)
    glVertex3f(a,0,b)
    glVertex3f(a,0,-b)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(1,0,0)
    glVertex3f(0,b,a)
    glVertex3f(-a,0,b)
    glVertex3f(-b,a,0)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(1,0,1.0)
    glVertex3f(0,b,a)
    glVertex3f(b,a,0)
    glVertex3f(a,0,b)
    glEnd()    

	#15
    glBegin(GL_TRIANGLES)
    glColor(0,0.5,0)
    glVertex3f(0,b,-a)
    glVertex3f(-b,a,0)
    glVertex3f(-a,0,-b)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(1,0,0.6)
    glVertex3f(0,b,-a)
    glVertex3f(a,0,-b)
    glVertex3f(b,a,0)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(1,0.2,0)
    glVertex3f(0,-b,-a)
    glVertex3f(-a,0,-b)
    glVertex3f(-b,-a,0)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(1,0.3,0.5)
    glVertex3f(0,-b,-a)
    glVertex3f(b,-a,0)
    glVertex3f(a,0,-b)
    glEnd()    

    glBegin(GL_TRIANGLES)
    glColor(0.1,0,1.0)
    glVertex3f(0,-b,a)
    glVertex3f(-b,-a,0)
    glVertex3f(-a,0,b)
    glEnd() 
 
    glBegin(GL_TRIANGLES)
    glColor(1,1,0)
    glVertex3f(0,-b,a)
    glVertex3f(a,0,b)
    glVertex3f(b,-a,0)
    glEnd()  

def abc():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,2,2,2)
    Icosaedro()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600) 
glutCreateWindow("ICOSAEDRO")    
glutDisplayFunc(abc)  
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.) 
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-3)
glRotatef(45,10,10,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



