import unittest
from datetime import datetime
from io import StringIO
from unittest.mock import patch

import patient_choose_visit_time


class TestPatientChooseVisitTime(unittest.TestCase):

    def setUp(self):
        # 设置固定的日期时间，以便测试结果的一致性
        self.fixed_date = datetime(2024, 10, 26, 10, 0)
        self.expected_slots = [
            '2024-10-27 10:00',
            '2024-10-28 10:00',
            '2024-10-29 10:00',
            '2024-10-30 10:00',
            '2024-10-31 10:00'
        ]

    @patch('datetime.datetime')
    def test_show_available_slots(self, mock_datetime):
        # 模拟当前时间为fixed_date
        mock_datetime.now.return_value = self.fixed_date

        # 使用StringIO来捕获输出
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # 模拟用户输入
            with patch('builtins.input', return_value='1'):
                patient_choose_visit_time.choose_time()

        # 获取输出流的内容
        output = fake_out.getvalue().strip()

        # 验证输出包含所有的可预约时间段
        for i, slot in enumerate(self.expected_slots, start=1):
            self.assertIn(f"{i}. {slot}", output)

        # 验证选择了第一个时间段
        self.assertIn("You have chosen: 2024-10-27 10:00", output)


if __name__ == '__main__':
    unittest.main()