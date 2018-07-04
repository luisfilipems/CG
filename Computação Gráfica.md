---


---

<h1 id="introdução">Introdução</h1>
<p>Neste artigo, apresentarei como desenvolver um sólido platônico (<em>icosaedro</em>) e posteriormente, a aplicação de uma textura.<br>
O desenvolvimento será feito em <strong>python</strong> juntamente da API <strong>openGL</strong>.<br>
Portanto, para que o código funcione, é necessário que ambos estejam instalados.</p>
<h1 id="primeiros-passos">Primeiros passos</h1>
<p>O primeiro passo a se pensar seria os vértices deste icosaedro.</p>
<p><img src="http://www.uff.br/cdme/platonicos/platonicos-html/figuras/icosaedro/icosaedro-pg-01.gif" alt="Coordenadas do icosaedro"><br>
<strong>Observação: Perceba que trabalhamos com proporção áurea nos cálculos.</strong></p>
<h2 id="identificando-os-pontos">Identificando os pontos</h2>
<p>Definiremos no escopo do programa os pontos de **A** até **L** e demais valores do seguinte modo:
</p><pre><code>phi = (1+math.sqrt(5))/2
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
M = (k*(-phi),k*(phi+1),0)</code><pre></pre></pre><p></p>
Dessa forma, agora temos as coordenadas do nosso icosaedro definidas.
<h2 id="desenhando-os-pontos">Desenhando os pontos</h2>
<p>O OpenGL fornece ferramentas para desenhar pontos, linhas e polígonos, que são formados por um ou mais vértices. Neste caso, é necessário passar uma lista de vértices, o que pode ser feito entre duas chamadas de funções:</p>
<p>-&gt; <em>glBegin()</em><br>
-&gt; <em>glEnd()</em></p>
<p>O argumento passado para <em>glBegin()</em> determina qual objeto será desenhado.<br>
No momento, passaremos o argumento <strong>GL_POINTS</strong> para mostrar os pontos dos vértices.<br>
Utilizaremos <em>glColor()</em> para definirmos cores diferentes pra cada ponto. Mais para frente isso irá nos facilitar para formas as faces do icosaedro.</p>
<p>
	<code>
</code></p><pre><code>#verde
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
</code></pre>
<p></p>
O resultado será algo semelhante à imagem abaixo:
<p><img src="https://raw.githubusercontent.com/luisfilipems/CG/master/PONTOS.PNG" alt="Pontos do icosaedro"></p>
<h2 id="desenhando-as-faces">Desenhando as faces</h2>
<p>Uma vez que desenhamos os pontos na tela e conseguimos identificar cada um (através das cores), poderemos agora formar as faces do icosaedro utilizando GL_TRIANGLES.<br>
Novamente, utilizaremos uma cor para cada face.</p>
<p>
	<code>
</code></p><pre><code>glBegin(GL_TRIANGLES)
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
</code></pre>
<p></p><p>Agora temos nosso icosaedro devidamente formado, com suas faces coloridas:</p>
<p><img src="https://raw.githubusercontent.com/luisfilipems/CG/master/FACES.PNG" alt="Faces"></p>
<h2 id="textura">Textura</h2>
<p>Utilizaremos a textura disponibilizada no site da [UFF]. (<a href="http://www.uff.br/cdme/platonicos/platonicos-html/icosaedro-br.html">http://www.uff.br/cdme/platonicos/platonicos-html/icosaedro-br.html</a>)</p>
<p>A textura se trata de um mapa mundi:<br>
<img src="https://raw.githubusercontent.com/luisfilipems/CG/master/mundo.png" alt="mundo"></p>
<p>Para podermos colocar a textura sobre o nosso icosaedro, é necessário calcular as proporções de distância de cada ponto da textura, para que fique alinhado com nosso vértices.<br>
Para isso, foi utilizado o <strong>GIMP</strong> a fim de obter essas medidas.</p>
<h2 id="posicionando-a-textura">Posicionando a textura</h2>
<p>Uma vez medido as posições, é hora de usar a função <em>glTexCoord2f()</em>. Ela associa as coordenadas da textura em png com os nossos vértices.<br>
O código fica assim :</p>
<p>
	<code>
</code></p><pre><code>glBegin(GL_TRIANGLES)
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
</code></pre>
<p></p><h1 id="resultado">Resultado</h1>
<p>O resultado final de nosso icosaedro está demonstrado abaixo :</p>
<p><img src="https://raw.githubusercontent.com/luisfilipems/CG/master/completo.PNG" alt="completo"></p>
<h2 id="mais-informações">Mais informações</h2>
<p>O código completa está disponível no <a href="https://github.com/luisfilipems/CG/blob/master/icosaedro.py">link</a>.</p>

