import unittest
from unittest.mock import patch
from your_module import MyClass  # Replace 'your_module' with the actual module name

class TestMyClass(unittest.TestCase):

    @patch.object(MyClass, 'load_config', return_value=100)  # Mocking load_config to return 100
    def test_process_data_with_mocked_load_config(self, mock_load_config):
        # Instantiate the class
        obj = MyClass()

        # Call the method with some data
        result = obj.process_data(10)
        
        # Assert the results
        self.assertEqual(result, 1000)  # 10 * 100 = 1000
        
        # Assert that load_config was called
        mock_load_config.assert_called_once()

if __name__ == '__main__':
    unittest.main()