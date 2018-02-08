import unittest
import json
from request_maker import readInputUrls, write_json_to_file, retrieve_response_details, status_codes_report

class TestUrls(unittest.TestCase):


    def test_url_file_read(self):
        self.assertEqual(readInputUrls("urls_test"),["http://www.google.com"])


    def test_response_details(self):
        url = "https://www.yahoo.com"
        expected_status_code = 200
        expected_content_length = "12"
        expected_date = "figure this out"
        expected_response_details = {"URL": url, "Status_code": expected_status_code,
                                     "Content_length": expected_content_length, "Date": expected_date}
        actual_response_details = json.loads(retrieve_response_details(url)[0])
        self.assertEqual(expected_response_details["URL"], actual_response_details["URL"])
        self.assertEqual(expected_response_details["Status_code"], actual_response_details["Status_code"])
        self.assertEqual(expected_response_details["Content_length"], actual_response_details["Content_length"])



    def test_file_write(self):
        expected_json = ("{\"URL\": \"https://google.com\", \"Status_code\": 302, \"Content_length\": \"269\","
                     "\"Date\": \"Wed, 07 Feb 2018 19:13:16 GMT\"}")

        write_json_to_file(expected_json)
        with open("REPORT----google.txt") as file:
            content = file.read()

        self.assertEqual(content,expected_json)

    def test_all_status_records(self):
        status_codes = [200,302,200]

        with open("status_reports_test") as expected_report_file:
            expected_status_report = expected_report_file.readlines()
            expected_status_report = [x.strip() for x in expected_status_report]

        status_codes_report(status_codes)

        with open("Http-Status-Report.txt","r") as report_file:
            actual_status_codes_reports = report_file.readlines()
            actual_status_codes_reports = [x.strip() for x in actual_status_codes_reports]


        self.assertEqual(expected_status_report, actual_status_codes_reports)


def main():
    unittest.main()

if __name__ == '__main__':
    main()