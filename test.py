import unittest
from io import StringIO
import sys
from main import main

class TestMain(unittest.TestCase):

    def test_main_exemplo1(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set up sys.argv
        sys.argv = ['main.py', 'topologia1.txt', 'exec1.txt']

        # Run the main function
        try:
            main()
        except SystemExit:
            pass  # Ignore the sys.exit() call

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Read the expected output from a file
        with open('resultado1.txt', 'r') as file:
            expected_output = file.read()
            
        # Check the output
        self.assertIn(expected_output.strip(), captured_output.getvalue().strip())
    
    def test_main_exemplo2(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set up sys.argv
        sys.argv = ['main.py', 'topologia2.txt', 'exec2.txt']

        # Run the main function
        try:
            main()
        except SystemExit:
            pass  # Ignore the sys.exit() call

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Read the expected output from a file
        with open('resultado2.txt', 'r') as file:
            expected_output = file.read()
            
        # Check the output
        self.assertIn(expected_output.strip(), captured_output.getvalue().strip())
        
    def test_main_exemplo3(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set up sys.argv
        sys.argv = ['main.py', 'topologia3.txt', 'exec3.txt']

        # Run the main function
        try:
            main()
        except SystemExit:
            pass  # Ignore the sys.exit() call

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Read the expected output from a file
        with open('resultado3.txt', 'r') as file:
            expected_output = file.read()
            
        # Check the output
        self.assertIn(expected_output.strip(), captured_output.getvalue().strip())
        
    def test_main_exemplo4(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set up sys.argv
        sys.argv = ['main.py', 'topologia4.txt', 'exec4.txt']

        # Run the main function
        try:
            main()
        except SystemExit:
            pass  # Ignore the sys.exit() call

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Read the expected output from a file
        with open('resultado4.txt', 'r') as file:
            expected_output = file.read()
            
        # Check the output
        self.assertIn(expected_output.strip(), captured_output.getvalue().strip())

    def test_main_with_insufficient_arguments(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set up sys.argv with insufficient arguments
        sys.argv = ['main.py']

        # Run the main function
        with self.assertRaises(SystemExit) as cm:
            main()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Expected output for insufficient arguments
        expected_output = 'Usage: python main.py <topologia.txt> <exec.txt>'

        # Check the output
        self.assertIn(expected_output.strip(), captured_output.getvalue().strip())
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
