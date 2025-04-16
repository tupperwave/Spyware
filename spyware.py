import cv2
import time
from datetime import datetime
import os

# Configurações éticas do projeto
AVISO = """
=== Tentativa de Montar um SPyware ===
- principio do codigo é capturar imagens da webcam
- separr as imagens em uma pasta e enviar para um servidor
===========================
"""

def verificar_consentimento():
    print(AVISO)
    consentimento = input("gatilho de acesso deve ser misturado a outro programa  para mascarar (s/n): ").lower()
    if consentimento != 's':
        print("Abortando: Consentimento não fornecido")
        exit()

def webcam_demo():
    # Cria diretório para imagens (se não existir)
    if not os.path.exists('demo_images'):
        os.makedirs('demo_images')
    
    # Inicia a webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Erro: Webcam não encontrada")
        return
    
    print(" Pressione 'q' para encerrar")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Mostra o vídeo ao vivo (com aviso)
            cv2.putText(frame, "DEMONSTRACAO ", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.imshow('Webcam Demo ', frame)
            
            # Salva frame a cada 5 segundos (para demonstração)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if int(time.time()) % 5 == 0:
                filename = f"demo_images/webcam_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Frame salvo: {filename} (Simulacao)")
            
            # Encerra ao pressionar 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Demonstração encerrada")

if __name__ == "__main__":
    verificar_consentimento()
    webcam_demo()