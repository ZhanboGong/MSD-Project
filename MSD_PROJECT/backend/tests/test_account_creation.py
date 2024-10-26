# test_patient_account_creation.py
import pytest
from patient_account_creation import create_account

def test_create_account():
    # 清除初始状态
    global patients
    patients.clear()

    # 给定的输入数据
    record_number = '12345'
    patient_id = '67890'

    # 调用函数
    create_account(record_number, patient_id)

    # 验证结果
    expected_username = f"user_{record_number}_{patient_id}"
    assert expected_username in patients
    assert patients[expected_username] == "default_password"

    # 再次创建账户，验证是否覆盖或提示已存在
    create_account(record_number, patient_id)
    assert len(patients) == 1  # 只有一个用户被创建