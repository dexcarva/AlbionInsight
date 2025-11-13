"""
Módulo de exceções customizadas para a aplicação Albion Insight.
Define exceções específicas para diferentes cenários da aplicação.
"""


class AlbionInsightException(Exception):
    """Exceção base para todas as exceções do Albion Insight."""

    pass


class NetworkTrackerException(AlbionInsightException):
    """Exceção levantada quando há um erro no rastreamento de rede."""

    pass


class PacketParsingException(AlbionInsightException):
    """Exceção levantada quando há um erro ao analisar um pacote."""

    pass


class PhotonDecodingException(AlbionInsightException):
    """Exceção levantada quando há um erro ao decodificar o protocolo Photon."""

    pass


class SessionException(AlbionInsightException):
    """Exceção levantada quando há um erro no gerenciamento de sessão."""

    pass


class ConfigurationException(AlbionInsightException):
    """Exceção levantada quando há um erro de configuração."""

    pass


class PermissionException(AlbionInsightException):
    """Exceção levantada quando há falta de permissões necessárias."""

    pass
