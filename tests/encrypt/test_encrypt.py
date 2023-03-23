from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("trybe", "4")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 4)

    expect = [
        encrypt_message("trybe", 2),
        encrypt_message("trybe", 4),
        encrypt_message("trybe", 10),
    ]

    response = ["eby_rt", "e_byrt", "ebyrt"]

    assert expect[0] == response[0]
    assert expect[1] == response[1]
    assert expect[2] == response[2]


# referencia
# https://www.educative.io/answers/how-to-check-if-an-exception-gets-raised-in-pytest
