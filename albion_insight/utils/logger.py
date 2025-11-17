"""
Módulo de configuração centralizado de logging para a aplicação Albion Insight.
Fornece um logger pré-configurado para uso em toda a aplicação.
"""

import logging
from pathlib import Path

from .config import Config


def setup_logger(name: str, log_file: str = None) -> logging.Logger:
    """
    Configura um logger centralizado para a aplicação.

    Args:
        name (str): Nome do logger (geralmente o nome do módulo).
        log_file (str, optional): Caminho para o arquivo de log. Defaults to None.

    Returns:
        logging.Logger: O objeto logger configurado.

    Example:
        >>> logger = setup_logger("albion_insight.core")
        >>> logger.info("Aplicação iniciada")
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Evita adicionar handlers duplicados se o logger já foi configurado
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, Config.LOG_LEVEL, logging.INFO))

        # File handler (opcional)
        if log_file is None:
            log_file = str(Config.LOG_FILE)

        # Garante que o diretório do log exista
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


# Configuração inicial do logger principal
Config.ensure_directories()
logger = setup_logger("AlbionInsight")
