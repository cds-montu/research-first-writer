#!/usr/bin/env python3
"""Small regression tests for language-neutral article checks."""
import unittest

from check_article import non_latin_script, words


class UnicodeChecksTest(unittest.TestCase):
    def test_hindi_words_are_counted(self):
        self.assertGreaterEqual(len(words("छोटे व्यवसाय के लिए काम व्यवस्थित करें")), 6)

    def test_english_words_still_work(self):
        self.assertEqual(words("Choose a tool for a small business."),
                         ["Choose", "a", "tool", "for", "a", "small", "business"])

    def test_script_detection_distinguishes_hindi(self):
        self.assertTrue(non_latin_script("छोटे व्यवसाय के लिए काम व्यवस्थित करें"))
        self.assertFalse(non_latin_script("Choose a project management tool"))


if __name__ == "__main__":
    unittest.main()
