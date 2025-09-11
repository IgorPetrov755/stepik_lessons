def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


if __name__ == '__main__':
    test_input_text(12, 12)
    #test_input_text(8, 12)
    #test_substring('fulltext', 'some_value')
    test_substring('1', '1')
    #test_substring('some_text', 'some')
    print("All tests passed!")

