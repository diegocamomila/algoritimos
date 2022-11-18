import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("AABBCC", 3) == "BAA_CCB"
    assert encrypt_message("AABBCC", -1) == "CCBBAA"
    assert encrypt_message("ABBCCA", 4) == "AC_CBBA"

    with pytest.raises(TypeError):
        encrypt_message("DIEGO", "A")

    with pytest.raises(TypeError):
        encrypt_message(["DIEGO"], 3)
