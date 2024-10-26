# test_admin_log_view.py
import admin_log_view

def test_view_logs(capsys):

    admin_log_view.view_logs()


    captured = capsys.readouterr()
    expected_output = (
        "User Logs:\n"
        "User: staff1, Action: login, Status: success\n"
        "User: user123, Action: reset password, Status: failed\n"
    )

    assert captured.out == expected_output

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_admin_log_view.py"])
