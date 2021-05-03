from unittest.mock import Mock
import pytest
from libpytools.spam.main import EnviadorDeSpam
from libpytools.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Marcelo', email='marcelo@marcelo.com.br'),
            Usuario(nome='Ferreira', email='ferreira@ferreira.com.br')
        ],
        [
            Usuario(nome='Luciano', email='luciano@luciano.com.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    # enviador = EnviadorMock()
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marcelo@ferreira.com.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    # assert len(usuarios) == enviador.qtde_email_enviados
    assert len(usuarios) == enviador.enviar.call_count


'''
Esta classe foi descontinuada após a utilização do Mock()
class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtde_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_email_enviados += 1
'''


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcelo', email='marcelo@marcelo.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@luciano.com.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
    # assert enviador.parametros_de_envio == (
    enviador.enviar.assert_called_with(
        'luciano@luciano.com.br',
        'marcelo@marcelo.com.br',
        'Curso Python Pro',
        'Confira os módulos'
    )
