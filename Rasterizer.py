from gl import Renderer, V2,V3, color
import random, shaders
width = 500
height = 500

rend = Renderer(width, height)
rend.glClearColor(0.5,0.5,0.5)
rend.glClear()
rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.pixelationShader

#MediumShot
rend.glLookAt(camPos=(0,-1.5,0.5),
             eyePos=(0,-2,-3))
rend.glLoadModel(filename="./models/skull/object.obj", 
                 textureName="./models/skull/texture.bmp", 
                 translate=(0, -2.8, -3), 
                 scale=(0.07,0.07,0.07), 
                 rotate=(-90,0,0))
rend.glRender() 
rend.glFinish("./renders/skull/Shaders/PixelationShader.bmp")
