from framework.test_suite import TestSuite

class TestLoader:
    TEST_METHOD_PREFIX = "test"

    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        return [m for m in methods if m.startswith(self.TEST_METHOD_PREFIX)]

    def make_suite(self, test_case_class):
        suite = TestSuite()
        for method_name in self.get_test_case_names(test_case_class):
            suite.add_test(test_case_class(method_name))
        return suite
