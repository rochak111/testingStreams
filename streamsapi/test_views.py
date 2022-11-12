import json
from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_user_cannot_addStreams_with_no_data(self):
        res = self.client.post(self.matches_url)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,400)


