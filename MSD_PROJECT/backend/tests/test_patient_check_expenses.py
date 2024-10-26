# 创建 test_patient_check_expenses.py 的内容，用于测试 patient_check_expenses.py


import patient_check_expenses

def test_view_expenses_for_existing_patient(capsys):
    # 测试已存在的病人费用
    patient_check_expenses.view_expenses("patient_123")
    captured = capsys.readouterr()

    # 验证输出内容是否包含病人的费用详情
    assert "Expenses for Patient patient_123:" in captured.out
    assert "2024-10-20: Room Charge - $100" in captured.out
    assert "2024-10-21: Medication - $50" in captured.out

def test_view_expenses_for_nonexistent_patient(capsys):
    # 测试不存在的病人ID
    patient_check_expenses.view_expenses("nonexistent_patient")
    captured = capsys.readouterr()

    # 验证是否输出正确的错误信息
    assert "No expenses available." in captured.out

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_patient_check_expenses.py"])
