from .test_result import TestResult

class TestCase:

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result: TestResult):
        result.test_started()
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError:
            result.add_failure(self.test_method_name)
        except Exception:
            result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self): pass
    def tear_down(self): pass

    # --- NOVOS ASSERTS ---
    def assert_equal(self, first, second):
        if first != second:
            raise AssertionError(f"{first} != {second}")

    def assert_true(self, expr):
        if not expr:
            raise AssertionError(f"{expr} is not true")

    def assert_false(self, expr):
        if expr:
            raise AssertionError(f"{expr} is not false")

    def assert_in(self, member, container):
        if member not in container:
            raise AssertionError(f"{member} not found in {container}")
