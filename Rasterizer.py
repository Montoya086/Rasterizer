from gl import Renderer, V2,V3, color
import random, shaders
width = 700
height = 500

rend = Renderer(width, height)
rend.glClearColor(0.5,0.5,0.5)
rend.glBackgroundTexture('./backgrounds/texture.bmp')
rend.clearBackground()
rend.vertexShader=shaders.vertexShader
#rend.fragmentShader=shaders.celShader
#rend.fragmentShader=shaders.negativeShader
#rend.fragmentShader=shaders.embossShader
#rend.fragmentShader=shaders.pixelationShader
#rend.fragmentShader=shaders.noiseShader
rend.fragmentShader=shaders.gouradShader

#Camera
rend.glLookAt(camPos=(0,-1.5,-0.6),
             eyePos=(0,-2,-3))


#Skull
#rend.fragmentShader=shaders.celShader
rend.glDirectionalLight(1,-0.6,0)
rend.glLoadModel(filename="./models/skull/object.obj", 
                 textureName="./models/skull/texture.bmp", 
                 translate=(0.5, -2, -2.5), 
                 scale=(0.01,0.01,0.01), 
                 rotate=(-90,0,-20))
rend.glRender()

#Desk
#rend.fragmentShader=shaders.pixelationShader
rend.glDirectionalLight(0,-1,0)
rend.glLoadModel(filename="./models/desk/object.obj", 
                 textureName="./models/desk/texture.bmp", 
                 translate=(0, -3, -3), 
                 scale=(0.1,0.1,0.1), 
                 rotate=(0,0,0))
rend.glRender()

#Candle
#rend.fragmentShader=shaders.brighterColorsShader
rend.glDirectionalLight(0,-1,0)
rend.glLoadModel(filename="./models/candle/object.obj", 
                 textureName="./models/candle/texture.bmp", 
                 translate=(0, -2, -2.55), 
                 scale=(0.006,0.006,0.006), 
                 rotate=(10,0,0))
rend.glRender()

#Books
#rend.fragmentShader=shaders.negativeShader
rend.glDirectionalLight(-1,-0.6,0)
rend.glLoadModel(filename="./models/books/object.obj", 
                 textureName="./models/books/texture.bmp", 
                 translate=(-0.7, -2, -2.55), 
                 scale=(0.008,0.008,0.008), 
                 rotate=(10,-20,0))
rend.glRender()

#Generate render
rend.glFinish("./scenes/MedievalDeskScene.bmp")
