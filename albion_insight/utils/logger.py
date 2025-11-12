import logging
from pathlib import Path



def setup_logger(name, log_file=None):
    """
    Configura um logger centralizado para a aplicação.

    Args:
        name (str): Nome do logger (geralmente o nome do módulo).
        log_file (str, optional): Caminho para o arquivo de log. Defaults to None.

    Returns:
        logging.Logger: O objeto logger configurado.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Evita adicionar handlers duplicados se o logger já foi configurado
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # File handler (opcional)
        if log_file:
            # Garante que o diretório do log exista
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)
            logger.addHandler(fh)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    
    return logger

# Configuração inicial do logger principal
logger = setup_logger("AlbionInsight", log_file="logs/app.log")
