from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


def Prisma():
    glBegin(GL_QUADS)
    glColor(1,0,0)
    glVertex3f(1,-1,0)
    glVertex3f(1,-1,-4)
    glVertex3f(-1,-1,-4)
    glVertex3f(-1,-1,0)
    glVertex3f(1,-1,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor(0,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,1,-4)
    glVertex3f(-1,1,-4)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glEnd()
 
    glBegin(GL_QUADS)
    glColor(0,0,1)
    glVertex3f(1,1,0)
    glVertex3f(1,1,-4)
    glVertex3f(1,-1,-4)
    glVertex3f(1,-1,0)
    glVertex3f(1,1,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor(0,1,1)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,-1,-4)
    glVertex3f(-1,1,-4)
    glVertex3f(-1,1,0)
    glVertex3f(-1,-1,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,0,1)
    glVertex3f(-1,1,0)
    glVertex3f(-1,-1,-0)
    glVertex3f(1,-1,-0)
    glVertex3f(1,1,0)
    glVertex3f(-1,1,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,1,0)
    glVertex3f(-1,1,-4)
    glVertex3f(-1,-1,-4)
    glVertex3f(1,-1,-4)
    glVertex3f(1,1,-4)
    glVertex3f(-1,1,-4)
    glEnd()


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(5,1,0,1)
    Prisma()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600) 
glutCreateWindow("PRISMA")    
glutDisplayFunc(abacaxi)  
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.) 
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,10,10,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



