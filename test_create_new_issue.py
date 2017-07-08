import unittest
import requests
import xmltodict


class TestCreateNewIssue(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c00desp1ce')

    def test_create_new_issue(self):
        issue_id = 'API-1'
        url = self.base_url + '/issue/' + issue_id
        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEqual(response.status_code, 200)

        self.assertAlmostEqual(
            response_dict['issue']['@id'],
            issue_id
        )

    def test_invalid_issue(self):
        issue_id = 'IAMINVALID'
        url = self.base_url + '/issue/' + issue_id
        response = requests.get(url, auth=self.creds)

        self.assertEqual(response.status_code, 404)


