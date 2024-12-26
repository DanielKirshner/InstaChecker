from instachecker import extract_usernames
from collections import Counter
import unittest
import os

class TestInstaChecker(unittest.TestCase):

    def test_extract_usernames(self):
        os.makedirs('mock_data', exist_ok=True)
        
        mock_html = '''
        <html>
            <body>
                <a href="https://instagram.com/user1">user1</a>
                <a href="https://instagram.com/user2">user2</a>
                <a href="https://instagram.com/user1">user1</a>
            </body>
        </html>
        '''
        
        # Write the mock HTML content to the followers.html file
        with open('mock_data/followers.html', 'w') as file:
            file.write(mock_html)
        
        result = extract_usernames('mock_data/followers.html')
        
        expected = Counter({'user1': 2, 'user2': 1})
        
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
