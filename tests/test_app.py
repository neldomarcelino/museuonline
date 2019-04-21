import pytest


@pytest.fixture()
def soma():
    return 2 + 5


def test_adicionar(soma):
    ret = soma

    assert ret == 7
