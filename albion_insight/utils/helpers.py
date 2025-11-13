"""
Módulo de funções auxiliares para a aplicação Albion Insight.
Contém funções utilitárias reutilizáveis em toda a aplicação.
"""

from typing import Any, Callable, Optional
from functools import wraps
import time


def format_number(value: int) -> str:
    """
    Formata um número com separadores de milhares.

    Args:
        value (int): O número a ser formatado.

    Returns:
        str: O número formatado com separadores de milhares.

    Example:
        >>> format_number(1000000)
        '1,000,000'
    """
    return f"{value:,}"


def format_duration(seconds: float) -> str:
    """
    Formata uma duração em segundos para um formato legível.

    Args:
        seconds (float): A duração em segundos.

    Returns:
        str: A duração formatada (ex: "1h 30m 45s").

    Example:
        >>> format_duration(5445)
        '1h 30m 45s'
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")

    return " ".join(parts)


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    Decorador para tentar executar uma função múltiplas vezes em caso de falha.

    Args:
        max_attempts (int): Número máximo de tentativas. Padrão: 3.
        delay (float): Atraso em segundos entre tentativas. Padrão: 1.0.

    Returns:
        Callable: A função decorada.

    Example:
        >>> @retry(max_attempts=3, delay=1.0)
        ... def unstable_function():
        ...     pass
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator


def safe_get(data: dict, key: str, default: Any = None) -> Any:
    """
    Obtém um valor de um dicionário de forma segura.

    Args:
        data (dict): O dicionário.
        key (str): A chave a ser buscada.
        default (Any): O valor padrão se a chave não existir. Padrão: None.

    Returns:
        Any: O valor encontrado ou o valor padrão.

    Example:
        >>> data = {"name": "John"}
        >>> safe_get(data, "age", 0)
        0
    """
    return data.get(key, default)
