import package_a.module_1 as mod_1


def test_my_function():
    assert mod_1.function_1(2) == 5
    assert mod_1.function_multiply_by_3(0) == 0
    assert mod_1.function_multiply_by_3(5) == 15
    assert mod_1.function_add_5(10) == 15
