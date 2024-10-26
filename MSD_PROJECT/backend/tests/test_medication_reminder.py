# 创建 test_medication_reminder.py 的内容，用于测试 medication_reminder.py

test_content = """
import medication_reminder
from datetime import datetime

def test_check_reminders_for_today(monkeypatch, capsys):
    # 设置日期为 2024-10-28
    fake_today = "2024-10-28"
    monkeypatch.setattr(medication_reminder, 'datetime', FakeDateTime(fake_today))

    # 检查 patient_123 的提醒信息
    medication_reminder.check_reminders("patient_123")
    captured = capsys.readouterr()
    assert "Reminder: Medication for Patient patient_123 is scheduled for today." in captured.out

def test_no_reminders_for_patient(capsys):
    # 使用不存在的病人ID
    medication_reminder.check_reminders("nonexistent_patient")
    captured = capsys.readouterr()
    assert "No reminders available for this patient." in captured.out

class FakeDateTime:
    def __init__(self, fake_today):
        self.fake_today = fake_today

    def now(self):
        # 返回假日期
        return datetime.strptime(self.fake_today, "%Y-%m-%d")

    def strftime(self, format):
        return self.fake_today

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_medication_reminder.py"])
"""

# 将测试文件写入 backend/tests/test_medication_reminder.py
with open("/mnt/data/test_medication_reminder.py", "w", encoding="utf-8") as f:
    f.write(test_content)

"/mnt/data/test_medication_reminder.py"
