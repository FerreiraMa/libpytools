from unittest.mock import Mock
import pytest

from libpytools import github_api

"""
Função utilizada antes de utilizar a fixture

def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "FerreiraMa", "id": 11910689,
        "avatar_url": "https://avatars.githubusercontent.com/u/11910689?v=4",
    }
    # A variável 'get_original' foi criada para isolar o teste
    get_original = github_api.request.get
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('FerreiraMa')
    assert 'https://avatars.githubusercontent.com/u/11910689?v=4' == url
    github_api.requests.get = get_original

# fixture utilizada antes de instalar o pytest-mock
@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/11910689?v=4'
    resp_mock.json.return_value = {
        'login': 'FerreiraMa', 'id': 11910689,
        'avatar_url': url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original
"""


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/11910689?v=4'
    resp_mock.json.return_value = {
        'login': 'FerreiraMa', 'id': 11910689,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpytools.github_api.requests.get')
    get_mock.requests.get = Mock(return_value=resp_mock)
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('FerreiraMa')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('FerreiraMa')
    assert 'https://avatars.githubusercontent.com/u/11910689?v=4' == url
