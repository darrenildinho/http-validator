import unittest
from request_maker import readInputUrls, write_json_to_file

class TestUrls(unittest.TestCase):


    def test_url_file_read(self):
        self.assertEqual(readInputUrls("urls.txt"),"http://www.google.com")


    def test_response_details(self):
        url = "http://www.google.com"
        expected_status_code = 200
        expected_content_length = 5398
        expected_date = "figure this out"
        expected_response_details = {"URL": url, "Status_code": expected_status_code,
                                     "Content_length": expected_content_length, "Date": expected_date}


    def test_file_write(self):
        expected_json = ("{\"URL\": \"https://google.com\", \"Status_code\": 302, \"Content_length\": \"269\","
                     "\"Date\": \"Wed, 07 Feb 2018 19:13:16 GMT\"}")
        write_json_to_file("https://google.com")
        with open("REPORT----google.txt") as file:
            content = file.read()

        self.assertEqual(content,expected_json)


def main():
    unittest.main()

if __name__ == '__main__':
    main()