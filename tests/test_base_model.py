from unittest import TestCase

from models import CAMEL_TO_LOWER_CASE_SNAKE


class TestBaseModel(TestCase):
    
    def setUp(self) -> None:
        return super().setUp()
    
    def test_camel_to_lower_case_snake_case_1(self):
        self.assertEqual(CAMEL_TO_LOWER_CASE_SNAKE('ItIsACamelCase'), 'it_is_a_camel_case')

    def test_camel_to_lower_case_snake_case_2(self):
        self.assertEqual(CAMEL_TO_LOWER_CASE_SNAKE('itIsACamelCase'), 'it_is_a_camel_case')