from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import png

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

xrot = yrot = zrot = 1
dx = 0
dy = 0.1
dz = 0


def LoadTextures():
    global texture
    texture = glGenTextures(1)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture)
    reader = png.Reader(filename='mundo.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def Icosaedro():

    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,0.0,-7.0)            

    glRotatef(xrot,0.3,0.0,0.0)          
    glRotatef(yrot,0.0,0.3,0.0)           
    glRotatef(zrot,0.0,0.0,0.3) 
    

    glDisable(GL_TEXTURE_2D)
    
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
	

    glEnable(GL_TEXTURE_2D)

    glBegin(GL_TRIANGLES)
    glColor(1,1,1)#BRANCO
    glTexCoord2f(0.00094,0.9); glVertex(D)
    glTexCoord2f(0.2687,0.8); glVertex(F)    
    glTexCoord2f(0.2687,0.987); glVertex(G)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.5,1,1)#AZUL CLARO
    glTexCoord2f(0,0.7188); glVertex(D)
    glTexCoord2f(0.2687,0.8); glVertex(F)    
    glTexCoord2f(0.2687,0.629); glVertex(I)
    glEnd()


    glBegin(GL_TRIANGLES)
    glColor(1,0.5,0.5)#VERMELHO CLARO
    glTexCoord2f(0.2687,0.45); glVertex(A)
    glTexCoord2f(0,0.54); glVertex(D)    
    glTexCoord2f(0.2687,0.629); glVertex(I)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.5,0.5,1)#AZUL ESCURO
    glTexCoord2f(0.2687,0.45); glVertex(A)
    glTexCoord2f(0.2671,0.27); glVertex(J)    
    glTexCoord2f(0,0.36); glVertex(D)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.5,1)#ROSA
    glTexCoord2f(0,0.182); glVertex(D)
    glTexCoord2f(0.2671,0.092);glVertex(G)    
    glTexCoord2f(0.2671,0.27); glVertex(J)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,1,0.5)#AMARELO CLARO
    glTexCoord2f(0.538,0.8981);glVertex(C)
    glTexCoord2f(0.2687,0.8); glVertex(F)    
    glTexCoord2f(0.2671,0.987); glVertex(G)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0,0,1)#AZUL
    glTexCoord2f(0.538,0.8981); glVertex(C)
    glTexCoord2f(0.2687,0.8); glVertex(F)    
    glTexCoord2f(0.538,0.7188) ;glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0,1,0)#VERDE
    glTexCoord2f(0.2687,0.8); glVertex(F)
    glTexCoord2f(0.2687,0.629); glVertex(I)    
    glTexCoord2f(0.544,0.7188); glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,0.1)#MARROM
    glTexCoord2f(0.544,0.5357); glVertex(E)
    glTexCoord2f(0.2687,0.629); glVertex(I)    
    glTexCoord2f(0.544,0.7188); glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.5,0.5,0.5)#CINZA
    glTexCoord2f(0.2687,0.45); glVertex(A)
    glTexCoord2f(0.544,0.5357); glVertex(E)    
    glTexCoord2f(0.2687,0.629); glVertex(I)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0.5,0)#LARANJA
    glTexCoord2f(0.2687,0.45); glVertex(A)
    glTexCoord2f(0.544,0.5357); glVertex(E)    
    glTexCoord2f(0.544,0.36); glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0,0)#VERMELHO
    glTexCoord2f(0.2687,0.45); glVertex(A)
    glTexCoord2f(0.2671,0.27); glVertex(J)    
    glTexCoord2f(0.544,0.36); glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,0,0.1)
    glTexCoord2f(0.2671,0.092); glVertex(G)
    glTexCoord2f(0.2671,0.27); glVertex(J)    
    glTexCoord2f(0.544,0.182); glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,1)
    glTexCoord2f(0.544,0); glVertex(C)
    glTexCoord2f(0.2671,0.092); glVertex(G)    
    glTexCoord2f(0.544,0.182); glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,0.1)#MARROM
    glTexCoord2f(0.807,0.092); glVertex(B)
    glTexCoord2f(0.544,0); glVertex(C)    
    glTexCoord2f(0.544,0.182); glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,1,0.3)
    glTexCoord2f(0.807,0.27); glVertex(B)
    glTexCoord2f(0.544,0.36); glVertex(H)    
    glTexCoord2f(0.544,0.182); glVertex(L)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0,0.7)#ROXO
    glTexCoord2f(0.807,0.45); glVertex(B)
    glTexCoord2f(0.544,0.5357); glVertex(E)    
    glTexCoord2f(0.544,0.36); glVertex(H)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1,1,0)#AMARELO
    glTexCoord2f(0.807,0.629); glVertex(B)
    glTexCoord2f(0.544,0.5357); glVertex(E)    
    glTexCoord2f(0.544,0.7188); glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.1,0,0.3)#AZUL MARINHO
    glTexCoord2f(0.807,0.8); glVertex(B)
    glTexCoord2f(0.538,0.8981); glVertex(C)    
    glTexCoord2f(0.544,0.7188); glVertex(M)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(0.7,0.4,0.1)
    glTexCoord2f(0.544,0.36); glVertex(H)
    glTexCoord2f(0.2671,0.27); glVertex(J)    
    glTexCoord2f(0.544,0.182); glVertex(L)
    glEnd()

    glDisable(GL_TEXTURE_2D)


    xrot += 0.3
    yrot += 0.5
    zrot += 0.3

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 0.5
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 0.5
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 0.5


def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    glutInitWindowSize(640, 480)
    
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("icosaedro")

    glutDisplayFunc(Icosaedro)
    glutIdleFunc(Icosaedro)

    glutReshapeFunc(ReSizeGLScene)

    InitGL(640, 480)

    glutMainLoop()

if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()
