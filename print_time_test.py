"""Testing."""
import datetime
import unittest
from io import StringIO
from unittest.mock import patch

from print_time import current_time

import coverage
cov = coverage.Coverage()
cov.start()

class CurrentTimeTestCase(unittest.TestCase):
    """Unittest.

    Args:
        unittest: unittest.TestCase
    """
    @patch('sys.stdout', new_callable=StringIO)
    def test_current_time_prints_correct_time(self, mock_stdout: str) -> None:
        """Unittest.

        Args:
            mock_stdout: unittest.TestCase
        """
        current_time()
        expected_output = F"Es ist {datetime.datetime.now().strftime('%H:%M:%S')} Uhr\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == "__main__":
    cov.stop()
    cov.save()
    cov.report()
    unittest.main()
