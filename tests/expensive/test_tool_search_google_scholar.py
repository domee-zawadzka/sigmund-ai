from .expensive_test_utils import BaseExpensiveTest


class TestToolsGoogleScholar(BaseExpensiveTest):
    
    def _test_tool(self):
        query = 'Can you search Google Scholar for articles about pupillometry in psychology? What is the title of the review article by Mathôt?'
        for reply in self.sigmund.send_user_message(query):
            print(reply.msg)
        assert 'Pupillometry: Psychology, physiology, and function' in reply
