import sys
import time
import os
from datetime import datetime

# Este módulo deve ser executado com privilégios de root/administrador
# para usar Scapy e capturar pacotes de rede.

def run_sniffer():
    """
    Função que simula a inicialização do sniffer de pacotes.
    Em uma implementação real, esta função conteria a lógica do Scapy.
    """
    if os.geteuid() != 0:
        # Em um ambiente real, isso seria um erro, mas aqui é apenas um aviso.
        # A UI deve garantir que este processo seja iniciado com sudo.
        print("AVISO: O sniffer não está sendo executado como root. A captura de pacotes pode falhar.", file=sys.stderr)

    print(f"Sniffer iniciado com PID: {os.getpid()} em {datetime.now().isoformat()}")
    sys.stdout.flush()

    # Simulação de captura de dados e envio para a UI via stdout
    try:
        count = 0
        while True:
            # Simula a decodificação de um evento (ex: UpdateMoney)
            simulated_event = f"EVENT:UpdateMoney|Silver:{1000 + count * 10}"
            print(simulated_event)
            sys.stdout.flush()
            count += 1
            time.sleep(5) # Simula o intervalo entre eventos
    except KeyboardInterrupt:
        print("Sniffer encerrado.")
        sys.stdout.flush()
        sys.exit(0)

if __name__ == "__main__":
    run_sniffer()
