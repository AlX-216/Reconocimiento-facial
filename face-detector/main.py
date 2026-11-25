import cv2
image = cv2.imread("image.jpg")
if image is None:
    print("Error: imagen no encontrada")
else:
    print("Imagen cargada correctamente")