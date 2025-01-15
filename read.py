import cv2 as cv

# Reading Images
'''
img = cv.imread('Resources/Photos/cat_large.jpg') # Devuelve la imagen como una matriz de pixeles

cv.imshow('Cat', img) #Muestra la imagen. Params:(nombre de la ventana, imagen a mostrar)

cv.waitKey(0) #Delay hasta que se presione una letra
'''



# Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4') #El argumento 0 es la webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

cv.waitKey(0)