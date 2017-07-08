from base_test import BaseTestCase
import requests


class TestUpdateIssue(BaseTestCase):

    def test_update_issue(self):
        issue_id = 'API-2'
        url = self.base_url + '/issue/' + issue_id

        params = {
            'summary': 'new summary',
            'description': 'new desc'
        }

        r = requests.post(url, params, cookies=self.cookies)
        self.assertEqual(r.status_code, 200)

