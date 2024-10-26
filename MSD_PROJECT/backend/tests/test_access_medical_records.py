import access_medical_records

def test_create_record(capsys):
    # 测试创建病历记录
    access_medical_records.create_record("patient_001", "Flu, needs rest")
    captured = capsys.readouterr()

    # 验证输出和病历数据是否正确
    assert "Medical record created for Patient patient_001." in captured.out
    assert access_medical_records.medical_records["patient_001"] == "Flu, needs rest"

def test_view_existing_record(capsys):
    # 创建记录并查看是否正确显示
    access_medical_records.create_record("patient_002", "Cold, medication prescribed")
    access_medical_records.view_record("patient_002")
    captured = capsys.readouterr()

    # 验证输出是否包含正确的病历数据
    assert "Patient patient_002 Record: Cold, medication prescribed" in captured.out

def test_view_nonexistent_record(capsys):
    # 查看不存在的病历
    access_medical_records.view_record("nonexistent_patient")
    captured = capsys.readouterr()

    # 验证是否输出正确的错误信息
    assert "No record found for the given patient ID." in captured.out

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_access_medical_records.py"])
