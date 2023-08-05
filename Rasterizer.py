from gl import Renderer, V2,V3, color
import random, shaders
width = 1080
height = 720

rend = Renderer(width, height)

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

#rend.glLookAt(camPos=(0,-3,0),
#             eyePos=(0,-2,-3))
rend.glCameraMatrix(translate=(0,-2,0),
                    rotate=(0,0,15))

#Right: -90,0,90
#Back: -90,0,0
#Front: -90,0,-180
#Left: -90,0,-90

rend.glLoadModel(filename="./models/cone/object.obj", 
                 textureName="./models/cone/texture.bmp", 
                 translate=(0, -3, -3), 
                 scale=(4,4,4), 
                 rotate=(0,0,0))


rend.glRender() 

rend.glFinish("./renders/cone/DutchAngle.bmp") 