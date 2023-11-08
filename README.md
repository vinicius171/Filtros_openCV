# openCV
alguns programas que criei enquanto estudo a biblioteca openCV

(1- Detector de arestas)
  O código a seguir é um programa simples em Python que permite aos usuários escolher entre dois filtros de detecção de bordas em uma imagem: o filtro Canny e o filtro Laplaciano.
O que são os filtros Canny e Laplaciano?

  Filtro Canny:
  
O filtro Canny é um algoritmo de detecção de bordas que realça as transições de intensidade nas imagens. Ele é amplamente utilizado devido à sua precisão e capacidade de reduzir o ruído na imagem. O processo envolve a aplicação de um gradiente de intensidade à imagem, seguida pela supressão de não-máximos para destacar as bordas finas e a vinculação de bordas para conectar os pixels de borda.

  Filtro Laplaciano:
  
O filtro Laplaciano é um operador que enfatiza as regiões de alta variação de intensidade nas imagens. Ele é usado para detectar bordas e realçar características de detalhes, como linhas e contornos. O filtro Laplaciano calcula a segunda derivada da imagem em relação às coordenadas espaciais, destacando as mudanças abruptas na intensidade da imagem.
  Ambos os filtros são utilizados para destacar bordas e características importantes em uma imagem, mas eles usam abordagens diferentes para alcançar esse objetivo. O filtro Canny é especialmente conhecido por sua capacidade de reduzir o ruído, enquanto o filtro Laplaciano realça áreas de alta variação de intensidade.

A função create_directory_if_not_exists é definida para criar um diretório (pasta) se ele não existir. Isso é usado para organizar os resultados dos filtros.

Duas funções são definidas: edge_detection_canny e edge_detection_laplacian, que aplicam os filtros Canny e Laplaciano, respectivamente, às imagens.

A variável input_image é definida com o nome da imagem de entrada que você deseja processar.

Em seguida, o programa verifica se as pastas "canny_results" e "laplacian_results" existem e as cria se ainda não existirem. Essas pastas serão usadas para armazenar os resultados dos filtros.

O programa entra em um loop que permite ao usuário escolher entre as seguintes opções:

Digitar '1' para aplicar o filtro Canny.
Digitar '2' para aplicar o filtro Laplaciano.
Digitar '0' para sair do programa.
Se o usuário escolher o filtro Canny (opção '1'), ele será solicitado a inserir limites inferiores e superiores para a detecção de bordas. A imagem resultante será salva na pasta "canny_results".

Se o usuário escolher o filtro Laplaciano (opção '2'), a detecção de bordas Laplaciano será aplicada, e a imagem resultante será salva na pasta "laplacian_results".

Se o usuário escolher '0', o programa encerra.

O programa exibe mensagens informativas durante o processo, como o caminho do arquivo onde o resultado foi salvo.
