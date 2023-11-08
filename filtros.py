import cv2
import os

# Função para criar um diretório se ele não existir
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Função para aplicar o detector de bordas Canny
def edge_detection_canny(image_path, output_path, low_threshold, high_threshold):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Carregar a imagem em tons de cinza
    edges = cv2.Canny(image, low_threshold, high_threshold)  # Aplicar o detector de bordas Canny
    cv2.imwrite(output_path, edges)  # Salvar a imagem resultante

# Função para aplicar o detector de bordas Laplaciano
def edge_detection_laplacian(image_path, output_path):
    image = cv2.imread(image_path)  # Carregar a imagem colorida
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converter a imagem para tons de cinza
    edges = cv2.Laplacian(gray, cv2.CV_8U)  # Aplicar o filtro Laplaciano
    cv2.imwrite(output_path, edges)  # Salvar a imagem resultante

if __name__ == "__main__":
    input_image = input("Digite o nome da imagem de entrada: ")

    create_directory_if_not_exists("canny_results")  # Criar diretório para resultados do Canny
    create_directory_if_not_exists("laplacian_results")  # Criar diretório para resultados do Laplaciano

    while True:
        print("Escolha uma opção:")
        print("1 - Detector de bordas Canny")
        print("2 - Detector de bordas Laplaciano")
        print("0 - Sair")
        
        choice = input("Digite o número da opção desejada: ")

        if choice == '0':
            break
        elif choice == '1':
            low_threshold = int(input("Digite o limite inferior: "))
            high_threshold = int(input("Digite o limite superior: "))
            output_image = "canny_results/canny_edges.jpg"
            edge_detection_canny(input_image, output_image, low_threshold, high_threshold)
            print(f"Detector de bordas Canny aplicado. Resultado salvo em {output_image}")
        elif choice == '2':
            output_image = "laplacian_results/laplacian_edges.jpg"
            edge_detection_laplacian(input_image, output_image)
            print(f"Detector de bordas Laplaciano aplicado. Resultado salvo em {output_image}")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
