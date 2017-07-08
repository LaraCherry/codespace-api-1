from base_test import BaseTestCase
import requests


class TestDeleteIssue(BaseTestCase):

    def test_delete_issue(self):
        issue_id = self.create_issue()
        url = self.base_url + '/issue/' + issue_id

        r = requests.delete(url, cookies=self.cookies)
        self.assertEqual(r.status_code, 200)

        r = requests.get(url, cookies=self.cookies)
        self.assertEqual(r.status_code, 404)

    def test_delete_unexisted_issue(self):
        url = self.base_url + '/issue/' + 'NON_EXISTED'

        r = requests.delete(url, cookies=self.cookies)
        self.assertEqual(r.status_code, 404)