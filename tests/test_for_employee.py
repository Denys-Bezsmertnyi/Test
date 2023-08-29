import unittest
from first_test import Employee
from unittest.mock import patch
from exceptions import EmailAlreadyExistsException
import os
import datetime

csv_file_path = os.path.join(os.path.dirname(__file__), 'pythonProject1', 'emails.csv')
candidates_csv_path = os.path.join(os.path.dirname(__file__), 'candidates.csv')

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Denys", 999, 'gerbyboyz@gmail.com')

    def test_is_email_valid(self):
        self.assertEqual(self.employee.email, 'gerbyboyz@gmail.com')

    @patch('first_test.Employee.validate')
    @patch('first_test.Employee.save_email')
    @patch('first_test.Employee.log_exception')
    def test_is_email_invalid(self, mock_log_exception, mock_save_email, mock_validate):
        mock_validate.side_effect = EmailAlreadyExistsException("Email already exists!")
        self.employee1 = Employee("Anatoliy", 111, 'anatiloy@gmail.com')
        self.employee2 = Employee("Anatoliy", 111, 'anatiloy@gmail.com')
        self.assertTrue(mock_log_exception.called)

    @patch('first_test.dt')
    @patch('first_test.traceback')
    @patch('first_test.logging')
    def test_log_exception(self, mock_logging, mock_traceback, mock_dt):
        mock_dt.now.return_value.strftime.return_value = '2023-08-29 12:00:00'
        mock_traceback.format_exc.return_value = 'Traceback info'
        self.employee.log_exception()
        mock_logging.error.assert_called_once_with('2023-08-29 12:00:00 | Traceback info')

    def test_work(self):
        returned_value = "I come to the office"
        self.assertEqual(self.employee.work(),returned_value)

    def test_name(self):
        real_name = 'Employee Denys'
        self.assertEqual(self.employee.__str__(),real_name)

    @patch('first_test.datetime')
    def test_check_salary_default_days(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime.date(2023, 8, 29)
        result = self.employee.check_salary()
        expected_salary = self.employee.day_salary * 21
        self.assertEqual(result, expected_salary)

class TestEmployee_gt_lt_eq(unittest.TestCase):
    def test_gt(self):
        employee1 = Employee("Denys", 1000)
        employee2 = Employee("Mark", 1200)
        self.assertTrue(employee2 > employee1)
        self.assertFalse(employee1 > employee2)

    def test_lt(self):
        employee1 = Employee("Denys", 1000)
        employee2 = Employee("Mark", 1200)
        self.assertTrue(employee1 < employee2)
        self.assertFalse(employee2 < employee1)

    def test_eq(self):
        employee1 = Employee("Denys", 1000)
        employee2 = Employee("Mark", 1000)
        self.assertTrue(employee1 == employee2)
        self.assertFalse(employee1 != employee2)