# test_password_reset.py
import password_reset


def test_reset_password_success(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "newpassword123")


    assert password_reset.users["user123"] == "oldpassword"


    password_reset.reset_password("user123")


    assert password_reset.users["user123"] == "newpassword123"


def test_reset_password_user_not_found(capsys):

    password_reset.reset_password("nonexistent_user")


    captured = capsys.readouterr()
    assert "Username not found." in captured.out


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", "test_password_reset.py"])
