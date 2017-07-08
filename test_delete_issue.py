from base_test import BaseTestCase
import requests


class TestDeleteIssue(BaseTestCase):

    def test_delete_issue(self):
        issue_id = 'API-1139'
        url = self.base_url + '/issue/' + issue_id

        r = requests.delete(url, cookies=self.cookies)

        self.assertEqual(r.status_code, 200)

        r = requests.get(url, cookies=self.cookies)
        self.assertEqual(r.status_code, 404)
