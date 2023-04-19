import unittest
from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(translator.english_to_french(''), '')
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

    def test_f2e(self):
        self.assertEqual(translator.french_to_english(''), '')
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
