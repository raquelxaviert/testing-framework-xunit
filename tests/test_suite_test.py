from framework.test_case import TestCase
from framework.test_suite import TestSuite
from framework.test_result import TestResult
from tests.test_case_test import TestStub

class TestSuiteTest(TestCase):

    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))
        assert len(suite.tests) == 3

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.run(result)
        assert result.summary() == "1 run, 0 failed, 0 error"

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))
        suite.run(result)
        assert result.summary() == "3 run, 1 failed, 1 error"
