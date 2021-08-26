from user import check_password


def test_check_password_true():
    assert check_password('123123abc')


def test_check_password_false():
    assert check_password('wrong password')


def test_it_returns_false_if_invalid_password():
    assert not check_password('wrong password')
