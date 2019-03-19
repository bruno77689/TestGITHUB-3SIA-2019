import cv2

imagem = cv2.imread("messi.jpg")

recorte = imagem[280:340, 330:390]

imagem[273:333, 100:160] = recorte

cv2.imshow("janela", imagem)



