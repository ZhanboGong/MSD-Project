import patient_check_expenses

def test_view_expenses_for_existing_patient(capsys):
    # 测试查看已有病人的费用信息
    patient_check_expenses.view_expenses("patient_123")
    captured = capsys.readouterr()

    # 验证输出是否包含病人的费用详情
    assert "Expenses for Patient patient_123:" in captured.out
    assert "2024-10-20: Room Charge - $100" in captured.out
    assert "2024-10-21: Medication - $50" in captured.out

def test_view_expenses_for_nonexistent_patient(capsys):
    # 测试查看不存在的病人
    patient_check_expenses.view_expenses("nonexistent_patient")
    captured = capsys.readouterr()

    # 验证是否输出正确的错误信息
    assert "No expenses available." in captured.out

def test_view_expenses_for_another_existing_patient(capsys):
    # 测试查看另一个已有病人的费用信息
    patient_check_expenses.view_expenses("patient_456")
    captured = capsys.readouterr()

    # 验证输出是否包含正确的费用信息
    assert "Expenses for Patient patient_456:" in captured.out
    assert "2024-10-20: Consultation Fee - $200" in captured.out

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_patient_check_expenses.py"])
