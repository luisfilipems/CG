from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

phi = (1+math.sqrt(5))/2
r = 2
k = r/math.sqrt(15)
A = (k*(phi+1),0,k*phi)
B = (k*(-phi-1),0,k*phi)
C = (k*(-phi-1),0,k*(-phi))
D = (k*(phi+1),0,k*(-phi))
E = (0,k*phi,k*(phi+1))
F = (0,k*phi,k*(-phi-1))
G = (0,k*(-phi),k*(-phi-1))
H = (0,k*(-phi),k*(phi+1))
I = (k*phi,k*(phi+1),0)
J = (k*phi,k*(-phi-1),0)
L = (k*(-phi),k*(-phi-1),0)
M = (k*(-phi),k*(phi+1),0)


def Icosaedro():

    #verde
    glBegin(GL_POINTS)
    glColor(0,1,0)
    glVertex(A)
    glEnd()

    #azul
    glBegin(GL_POINTS)
    glColor(0,0,1)
    glVertex(B)
    glEnd()
    
    #vermelho
    glBegin(GL_POINTS)
    glColor(1,0,0)
    glVertex(C)
    glEnd()
    
    #amarelo
    glBegin(GL_POINTS)
    glColor(1,1,0)
    glVertex(D)
    glEnd()

    #branco
    glBegin(GL_POINTS)
    glColor(1,1,1)
    glVertex(E)
    glEnd()

    #roxo
    glBegin(GL_POINTS)
    glColor(0.7,0,0.7)
    glVertex(F)
    glEnd()

    #cinza
    glBegin(GL_POINTS)
    glColor(0.7,0.7,0.6)
    glVertex(G)
    glEnd()

    #laranja
    glBegin(GL_POINTS)
    glColor(1, 0.7, 0.1)
    glVertex(H)
    glEnd()

    #marrom
    glBegin(GL_POINTS)
    glColor(0.7,0.4,0.1)
    glVertex(I)
    glEnd()

    #vinho
    glBegin(GL_POINTS)
    glColor(0.7,0.1,0.1)
    glVertex(J)
    glEnd()

    #verde claro
    glBegin(GL_POINTS)
    glColor(0.7,1,0.7)
    glVertex(L)
    glEnd()

    #azul claro
    glBegin(GL_POINTS)
    glColor(0,1,1)
    glVertex(M)
    glEnd()
	
    glBegin(GL_TRIANGLES)
    glColor(1,1,1)#BRANCO
    glVertex(D)
    glVertex(F)    
    glVertex(G)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.5,1)#ROSA
    glVertex(D)
    glVertex(G)    
    glVertex(J)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,1,0.5)#AMARELO CLARO
    glVertex(C)
    glVertex(F)    
    glVertex(G)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.5,1,1)#AZUL CLARO
    glVertex(D)
    glVertex(F)    
    glVertex(I)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.5,0.5,1)#AZUL ESCURO
    glVertex(A)
    glVertex(J)    
    glVertex(D)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.5,0.5)#VERMELHO CLARO
    glVertex(A)
    glVertex(D)    
    glVertex(I)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.5,0.5,0.5)#CINZA
    glVertex(A)
    glVertex(E)    
    glVertex(I)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.5,0)#LARANJA
    glVertex(A)
    glVertex(E)    
    glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0,0)#VERMELHO
    glVertex(A)
    glVertex(J)    
    glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0,1,0)#VERDE
    glVertex(F)
    glVertex(I)    
    glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0,0,1)#AZUL
    glVertex(C)
    glVertex(F)    
    glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.5,0)#LARANJA
    glVertex(A)
    glVertex(E)    
    glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,0.1)#MARROM
    glVertex(E)
    glVertex(I)    
    glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0,0.7)#ROXO
    glVertex(B)
    glVertex(E)    
    glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,1,0)#AMARELO
    glVertex(B)
    glVertex(E)    
    glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.1,0,0.3)#AZUL MARINHO
    glVertex(B)
    glVertex(C)    
    glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,0.1)#MARROM
    glVertex(B)
    glVertex(C)    
    glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,1)
    glVertex(C)
    glVertex(G)    
    glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,1,0.3)
    glVertex(B)
    glVertex(H)    
    glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,0.1)
    glVertex(H)
    glVertex(J)    
    glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0,0.1)
    glVertex(G)
    glVertex(J)    
    glVertex(L)
    glEnd()

def abc():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,3,0,1)
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
glPointSize(5)    
glutDisplayFunc(abc)  
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.) 
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-15)
glRotatef(45,10,10,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



