import unittest
from backend.src.api.patient_record_manage import add_record, delete_record, update_record

class TestPatientRecordManage(unittest.TestCase):
    
    def setUp(self):
        # 设置一些初始数据，用于测试
        self.patient_data = {'id': 1, 'name': 'John Doe', 'age': 30, 'medical_history': 'None'}
        self.new_patient_data = {'name': 'John Doe', 'age': 31, 'medical_history': 'Flu'}
    
    def test_add_record(self):
        # 测试添加患者记录功能
        result = add_record(self.patient_data)
        self.assertTrue(result)  # 假设添加成功返回True
    
    def test_delete_record(self):
        # 测试删除患者记录功能
        result = delete_record(self.patient_data['id'])
        self.assertTrue(result)  # 假设删除成功返回True
    
    def test_update_record(self):
        # 测试更新患者记录功能
        result = update_record(self.patient_data['id'], self.new_patient_data)
        self.assertTrue(result)  # 假设更新成功返回True

if __name__ == '__main__':
    unittest.main()
