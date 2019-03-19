import cv2

#lê a imagem
imagem = cv2.imread("messi.jpg")

#mostra a imagem
cv2.imshow("janela",imagem)

#dimensões da imagem
print(imagem.shape)

#padrão RGB trocado (BGR)
print(imagem[100,200])

#troca a cor de um intervalo de pixels
imagem[100:200,200:500] = (0,0,255)

#salvando imagem
cv2.imwrite("novaimagem.jpg",imagem)

imagem = cv2.imread("novaimagem.jpg")

cv2.imshow("janela2",imagem)

#convertendo cores
imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("janela3",imagem)


