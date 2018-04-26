from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


D = 0.5

x0=-10
xf=10
z0=-10
zf=10


def f(x,z):
    return x**2 + z**2

def fpc():
    z=z0
    while z<zf:
	x=x0
	glBegin(GL_QUAD_STRIP)
	while x<xf:	    
	    glVertex3f(x,f(x,z),z)
	    glVertex3f(x,f(x,z+D),z+D)
	    x = x+D
	glEnd()
	z = z+D

   


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(9,6,10,0)
    fpc()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)





#def GerenciaMouse(button, state,x, y):

#   if button == GLUT_LEFT_BUTTON:
#       if state == GLUT_DOWN:
#             glutDisplayFunc(abacaxi)         
#         glutPostRedisplay()






# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PARABOLA CIRCULOIDE")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
#glutMouseFunc(GerenciaMouse);
glutMainLoop()


