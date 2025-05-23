# test_login.py

def login(username, password):
    return username == "admin" and password == "1234"

def test_login_success():
    assert login("admin", "1234") == True

def test_login_fail():
    assert login("user", "wrongpass") == False
