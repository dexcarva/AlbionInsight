"""
Testes unitários para as funções auxiliares do Albion Insight.
"""

import pytest

from albion_insight.utils.helpers import (format_duration, format_number,
                                          retry, safe_get)


class TestFormatNumber:
    """Testes para a função format_number."""

    def test_format_number_thousands(self):
        """Testa a formatação de números com milhares."""
        assert format_number(1000) == "1,000"
        assert format_number(1000000) == "1,000,000"
        assert format_number(1000000000) == "1,000,000,000"

    def test_format_number_small(self):
        """Testa a formatação de números pequenos."""
        assert format_number(0) == "0"
        assert format_number(100) == "100"
        assert format_number(999) == "999"


class TestFormatDuration:
    """Testes para a função format_duration."""

    def test_format_duration_seconds(self):
        """Testa a formatação de durações em segundos."""
        assert format_duration(45) == "45s"
        assert format_duration(0) == "0s"

    def test_format_duration_minutes(self):
        """Testa a formatação de durações em minutos."""
        assert format_duration(60) == "1m"
        assert format_duration(90) == "1m 30s"

    def test_format_duration_hours(self):
        """Testa a formatação de durações em horas."""
        assert format_duration(3600) == "1h"
        assert format_duration(5445) == "1h 30m 45s"


class TestSafeGet:
    """Testes para a função safe_get."""

    def test_safe_get_existing_key(self):
        """Testa a obtenção de uma chave existente."""
        data = {"name": "John", "age": 30}
        assert safe_get(data, "name") == "John"
        assert safe_get(data, "age") == 30

    def test_safe_get_missing_key(self):
        """Testa a obtenção de uma chave inexistente."""
        data = {"name": "John"}
        assert safe_get(data, "age") is None
        assert safe_get(data, "age", 0) == 0

    def test_safe_get_empty_dict(self):
        """Testa a obtenção de chave em dicionário vazio."""
        data = {}
        assert safe_get(data, "key") is None
        assert safe_get(data, "key", "default") == "default"


class TestRetry:
    """Testes para o decorador retry."""

    def test_retry_success_first_attempt(self):
        """Testa a execução bem-sucedida na primeira tentativa."""

        @retry(max_attempts=3, delay=0.1)
        def successful_function():
            return "success"

        assert successful_function() == "success"

    def test_retry_success_after_failures(self):
        """Testa a execução bem-sucedida após falhas."""
        attempts = {"count": 0}

        @retry(max_attempts=3, delay=0.1)
        def eventually_successful():
            attempts["count"] += 1
            if attempts["count"] < 3:
                raise ValueError("Not yet")
            return "success"

        assert eventually_successful() == "success"
        assert attempts["count"] == 3

    def test_retry_max_attempts_exceeded(self):
        """Testa a falha após exceder o número máximo de tentativas."""

        @retry(max_attempts=2, delay=0.1)
        def always_fails():
            raise ValueError("Always fails")

        with pytest.raises(ValueError):
            always_fails()
