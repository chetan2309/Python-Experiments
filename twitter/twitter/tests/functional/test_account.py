from twitter.tests import *

class TestAccountController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='account'))
        # Test response...
