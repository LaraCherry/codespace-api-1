import requests
from base_test import BaseTestCase


class TestCreateNewIssue(BaseTestCase):

    def test_create_issue(self):
        url = self.base_url + '/issue/'

        params = {
            'project': 'API',
            'summary': 'Awesome summary',
            'description': 'created by autotests'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        self.assertEquals(r.status_code, 201)

        location = r.headers['Location']
        r = requests.get(location)
        self.assertEquals(r.status_code, 200)