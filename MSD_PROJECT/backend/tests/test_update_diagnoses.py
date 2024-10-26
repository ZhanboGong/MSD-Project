# 创建 test_update_diagnoses.py 的内容，用于测试 update_diagnoses.py

import update_diagnoses

def test_update_diagnosis(capsys):
    # 更新病人的诊断和治疗计划
    update_diagnoses.update_diagnosis("patient_001", "Flu", "Rest and hydration")

    # 验证是否输出正确的提示信息
    captured = capsys.readouterr()
    assert "Updated record for Patient patient_001." in captured.out

    # 检查病历是否正确更新
    assert "patient_001" in update_diagnoses.medical_records
    assert update_diagnoses.medical_records["patient_001"]["diagnosis"] == "Flu"
    assert update_diagnoses.medical_records["patient_001"]["treatment"] == "Rest and hydration"

def test_update_diagnosis_overwrite():
    # 更新已有病人的病历信息，覆盖旧数据
    update_diagnoses.update_diagnosis("patient_001", "Cold", "Medication and rest")

    # 验证新的病历是否正确覆盖
    assert update_diagnoses.medical_records["patient_001"]["diagnosis"] == "Cold"
    assert update_diagnoses.medical_records["patient_001"]["treatment"] == "Medication and rest"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "test_update_diagnoses.py"])
