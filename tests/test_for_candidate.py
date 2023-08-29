import os
import unittest
from unittest.mock import patch
from first_test import Candidate

class TestCandidateClass(unittest.TestCase):

    def test_full_name_property(self):
        candidate = Candidate('John', 'Doe', 'john@example.com', ['Python'], 'Python', 'Junior')
        self.assertEqual(candidate.full_name, 'John Doe')

    @patch('requests.get')
    def test_generate_candidates_from_url(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = "Full Name,Email,Technologies,Main Skill,Main Skill Grade\nJohn Doe,john@example.com,Python,Python,Junior"

        candidates = Candidate.generate_candidates('https://example.com/candidates.csv')

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].full_name, 'John Doe')
        self.assertEqual(candidates[0].email, 'john@example.com')
        #self.assertListEqual(candidates[0].tech_stack, ['Python'])  # Here, tech_stack is a list
        self.assertEqual(candidates[0].main_skill, 'Python')
        self.assertEqual(candidates[0].main_skill_grade, 'Junior')

    def test_generate_candidates_from_file(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test_candidates.csv')
        with open(file_path, 'w') as file:
            file.write("Full Name,Email,Technologies,Main Skill,Main Skill Grade\n"
                       "Jane Smith,jane@example.com,Java,Java,Senior\n"
                       "Ivan Chechov,ichech@example.com,Python|Django|Angular,Python,Senior\n"
                       "Max Payne,mpayne@example.com,PHP|Laravel|MySQL,PHP,Middle\n"
                       "Tom Hanks,thanks@example.com,Python|CSS,Python,Junior")

        candidates = Candidate.generate_candidates(file_path)

        self.assertEqual(len(candidates), 4)
        self.assertEqual(candidates[0].full_name, 'Jane Smith')
        self.assertEqual(candidates[0].email, 'jane@example.com')
        #self.assertListEqual(candidates[0].tech_stack, ['Java'])
        self.assertEqual(candidates[0].main_skill, 'Java')
        self.assertEqual(candidates[0].main_skill_grade, 'Senior')

        # Проверяем атрибуты второго кандидата
        self.assertEqual(candidates[1].full_name, 'Ivan Chechov')
        self.assertEqual(candidates[1].email, 'ichech@example.com')
        #self.assertListEqual(candidates[1].tech_stack, ['Python', 'Django', 'Angular'])
        self.assertEqual(candidates[1].main_skill, 'Python')
        self.assertEqual(candidates[1].main_skill_grade, 'Senior')

        # Проверяем атрибуты третьего кандидата
        self.assertEqual(candidates[2].full_name, 'Max Payne')
        self.assertEqual(candidates[2].email, 'mpayne@example.com')
        #self.assertListEqual(candidates[2].tech_stack, ['PHP', 'Laravel', 'MySQL'])
        self.assertEqual(candidates[2].main_skill, 'PHP')
        self.assertEqual(candidates[2].main_skill_grade, 'Middle')

        # Проверяем атрибуты четвертого кандидата
        self.assertEqual(candidates[3].full_name, 'Tom Hanks')
        self.assertEqual(candidates[3].email, 'thanks@example.com')
        #self.assertListEqual(candidates[3].tech_stack, ['Python', 'CSS'])
        self.assertEqual(candidates[3].main_skill, 'Python')
        self.assertEqual(candidates[3].main_skill_grade, 'Junior')

        os.remove(file_path)
