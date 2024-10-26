
import notification_system

def test_add_notification(capsys):
    # 测试添加通知
    notification_system.add_notification("patient_001", "Your test results are ready.")
    captured = capsys.readouterr()

    # 验证输出和通知是否正确
    assert "Notification added for Patient patient_001." in captured.out
    assert notification_system.notifications["patient_001"] == "Your test results are ready."

def test_view_existing_notification(capsys):
    # 添加通知并查看
    notification_system.add_notification("patient_002", "Your appointment is confirmed.")
    notification_system.view_notification("patient_002")
    captured = capsys.readouterr()

    # 验证输出是否包含正确的通知
    assert "Patient patient_002 Notification: Your appointment is confirmed." in captured.out

def test_view_nonexistent_notification(capsys):
    # 查看不存在的通知
    notification_system.view_notification("nonexistent_patient")
    captured = capsys.readouterr()

    # 验证是否输出正确的错误信息
    assert "No new notifications." in captured.out

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_notification_system.py"])
