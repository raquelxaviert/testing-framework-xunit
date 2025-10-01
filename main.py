from framework.test_loader import TestLoader
from framework.test_runner import TestRunner
from framework.test_suite import TestSuite
from tests.test_case_test import TestCaseTest
from tests.test_suite_test import TestSuiteTest
from tests.test_loader_test import TestLoaderTest

loader = TestLoader()
suite = TestSuite()
suite.add_test(loader.make_suite(TestCaseTest))
suite.add_test(loader.make_suite(TestSuiteTest))
suite.add_test(loader.make_suite(TestLoaderTest))

runner = TestRunner()
runner.run(suite)
