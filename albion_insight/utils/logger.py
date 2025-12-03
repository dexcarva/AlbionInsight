"""Módulo de configuração centralizado de logging para a aplicação Albion Insight."""

import logging
from pathlib import Path
from typing import Optional

from .config import Config


def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
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
    logger.setLevel(getattr(logging, Config.LOG_LEVEL, logging.INFO))

    # Evita adicionar handlers duplicados se o logger já foi configurado
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, Config.LOG_LEVEL, logging.INFO))
        logger.addHandler(ch)

        # File handler (opcional)
        if log_file is None:
            log_file = str(Config.LOG_FILE)

        # Garante que o diretório do log exista
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file)
        fh.setLevel(getattr(logging, Config.LOG_LEVEL, logging.INFO))
        logger.addHandler(fh)

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Aplica o formatter a todos os handlers
        for handler in logger.handlers:
            handler.setFormatter(formatter)

    return logger


# Configuração inicial do logger principal
Config.ensure_directories()
logger = setup_logger("AlbionInsight")
