import unittest
import requests
import xmltodict
from base_test import BaseTestCase


class TestGetIssue(BaseTestCase):

    def test_get_issue(self):
        issue_id = 'API-1'
        url = self.base_url + '/issue/' + issue_id
        response = requests.get(url)
        response_dict = xmltodict.parse(response.text)

        self.assertEqual(response.status_code, 200)

        self.assertAlmostEqual(
            response_dict['issue']['@id'],
            issue_id
        )


    def test_get_invalid_issue(self):
        issue_id = 'IAMINVALID'
        url = self.base_url + '/issue/' + issue_id
        response = requests.get(url, auth=self.creds)

        self.assertEqual(response.status_code, 404)


