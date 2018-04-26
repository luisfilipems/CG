from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

verticesTF = (
	(  0 , 1 , 0),
	( 1 , -1 ,-1),
	(-1 ,-1 , -1),
	(-1 , -1 , 1),
	(1 , -1 , 1 ),
	(  0 , 1 , 0),
)	
	
verticesQ = (
	(1 ,-1, -1),
	(-1 ,-1,-1),
	(-1 ,-1, 1),
	(1 , -1 ,1),
)

arestasT = (
	(  0 , 1 , 0),
	(1 ,-1, -1),
	(-1 ,-1,-1),
	(-1 ,-1, 1),
)

def Piramide():
    glBegin(GL_TRIANGLE_FAN)
    t = 0.2
    for i in verticesTF:
	glColor(t , 0, 0)
	glVertex3fv(i); 
	t = t + 0.2
    glEnd()		


    glBegin(GL_QUADS)
    for i in verticesQ:    
	glVertex3fv(i);
    glEnd()

    glBegin(GL_LINES)
    for i in arestasT:
	glVertex3fv(i);
    glEnd()


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,5,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600) 
glutCreateWindow("PIRAMIDE")    
glutDisplayFunc(abacaxi)  
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.) 
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



