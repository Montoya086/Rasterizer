from gl import Renderer, V2,V3, color
import random, shaders
width = 1080
height = 720

rend = Renderer(width, height)

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

rend.glLookAt(camPos=(-3,10,-2),
              eyePos=(0,0,-5))

#Right: -90,0,90
#Back: -90,0,0
#Front: -90,0,-180
#Left: -90,0,-90

rend.glLoadModel(filename="./models/face/object.obj", 
                 textureName="./models/face/texture.bmp", 
                 translate=(0, 0, -5), 
                 scale=(1.5,1.5,1.5), 
                 rotate=(0,0,0))


rend.glRender() 

rend.glFinish("./renders/face/FaceCams.bmp") 