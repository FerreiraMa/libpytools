from libpytools.spam.modelos import Usuario

# scope foi usado para abrir apenas uma vez a conexão


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Marcelo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Marcelo'), Usuario(nome='Ferreira')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
