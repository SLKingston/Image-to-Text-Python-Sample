import cv2
import pytesseract as pyt

imagem = cv2.imread("PROG.JPG")

caminho = r"C:\Program Files\Tesseract-OCR"
pyt.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pyt.image_to_string(imagem)

arquivo = open('arq01.txt','w')

arquivo.writelines(texto)
arquivo.close

print("Arquivo foi criado e salvo com o seguinte conteudo !!!\n")
print(texto)