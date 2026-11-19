from idade import idade_permitida


def test_aceita_idade_igual_ao_limite_minimo():
    # Preparar
    idade = 12
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is True


def test_rejeita_idade_abaixo_do_limite_minimo():
    # Preparar
    idade = 11
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is False


def test_rejeita_idade_acima_de_100():
    # Preparar
    idade = 101
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is False
