from src.Scoring import check_answers
def test_all_correct():
    x = ["A", "B", "C"]
    model = ["A", "B", "C"]
    possible = ["A", "B", "C", "D"]

    result = check_answers(x, model, possible)

    assert result == ["Correct", "Correct", "Correct"]


def test_all_wrong():
    x = ["A", "A", "A"]
    model = ["B", "B", "B"]
    possible = ["A", "B", "C", "D"]

    result = check_answers(x, model, possible)

    assert result == ["Wrong", "Wrong", "Wrong"]


def test_partial_correct():
    x = ["A", "B", "C"]
    model = ["A", "D", "C"]
    possible = ["A", "B", "C", "D"]

    result = check_answers(x, model, possible)

    assert result == ["Correct", "Wrong", "Correct"]


def test_length_mismatch():
    try:
        check_answers(["A", "B"], ["A", "B", "C"], ["A", "B", "C"])
        assert False
    except ValueError:
        assert True


def test_invalid_model_answer():
    try:
        check_answers(
            ["A", "B", "C"],
            ["A", "X", "C"],  # invalid
            ["A", "B", "C"]
        )
        assert False
    except ValueError:
        assert True


def test_invalid_generated_answer():
    try:
        check_answers(
            ["A", "X", "C"],  # invalid
            ["A", "B", "C"],
            ["A", "B", "C"]
        )
        assert False
    except ValueError:
        assert True


def test_empty_inputs():
    result = check_answers([], [], ["A", "B"])
    assert result == []