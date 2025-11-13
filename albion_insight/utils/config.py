"""
Módulo de configuração centralizado para a aplicação Albion Insight.
Carrega variáveis de ambiente e fornece valores padrão.
"""

import os
from pathlib import Path
from typing import Optional


class Config:
    """Classe de configuração para a aplicação Albion Insight."""

    # Diretório base do projeto
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # Configurações de Debug
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Configurações de Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR = Path(os.getenv("LOG_DIR", BASE_DIR / "logs"))
    LOG_FILE = LOG_DIR / "app.log"

    # Configurações de Rede
    NETWORK_INTERFACE = os.getenv("NETWORK_INTERFACE", "eth0")
    ALBION_PORTS = [int(p) for p in os.getenv("ALBION_PORTS", "5055,5056,5058").split(",")]

    # Configurações de Sessão
    SESSION_DIR = Path(os.getenv("SESSION_DIR", BASE_DIR / "sessions"))

    # Configurações da Aplicação
    APP_NAME = "Albion Insight"
    APP_VERSION = "1.0.0"

    @classmethod
    def ensure_directories(cls) -> None:
        """Garante que todos os diretórios necessários existam."""
        cls.LOG_DIR.mkdir(parents=True, exist_ok=True)
        cls.SESSION_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_config(cls) -> dict:
        """Retorna um dicionário com todas as configurações."""
        return {
            "debug": cls.DEBUG,
            "log_level": cls.LOG_LEVEL,
            "log_dir": str(cls.LOG_DIR),
            "log_file": str(cls.LOG_FILE),
            "network_interface": cls.NETWORK_INTERFACE,
            "albion_ports": cls.ALBION_PORTS,
            "session_dir": str(cls.SESSION_DIR),
            "app_name": cls.APP_NAME,
            "app_version": cls.APP_VERSION,
        }
