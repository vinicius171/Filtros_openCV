import cv2
import numpy as np

def edge_detection(input_image_path, output_image_path, low_threshold, high_threshold):
    # Carregar a imagem em tons de cinza
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Aplicar o detector de bordas Canny
    edges = cv2.Canny(image, low_threshold, high_threshold)

    # Salvar a imagem resultante
    cv2.imwrite(output_image_path, edges)

if __name__ == "__main__":
    input_image = "img/a1.jpg"
    output_image = "edges_detected.jpg"
    low_threshold = 50
    high_threshold = 150
    edge_detection(input_image, output_image, low_threshold, high_threshold)
