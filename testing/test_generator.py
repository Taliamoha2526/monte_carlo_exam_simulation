from src.Generator import answer
import numpy as np
def test_output_length():
    result = answer(seed=42, size=10, possible_answers=["A", "B", "C", "D"])
    assert len(result) == 10


def test_output_values_valid():
    choices = ["A", "B", "C", "D"]
    result = answer(seed=42, size=50, possible_answers=choices)

    assert all(r in choices for r in result)


def test_minimum_case():
    result = answer(seed=1, size=1, possible_answers=["A", "B"])
    assert len(result) == 1
    assert result[0] in ["A", "B"]


def test_reproducibility():
    result1 = answer(seed=42, size=10, possible_answers=["A", "B", "C"])
    result2 = answer(seed=42, size=10, possible_answers=["A", "B", "C"])

    assert np.array_equal(result1, result2)


def test_different_seeds():
    result1 = answer(seed=1, size=10, possible_answers=["A", "B", "C"])
    result2 = answer(seed=2, size=10, possible_answers=["A", "B", "C"])

    assert not np.array_equal(result1, result2)


def test_invalid_size_zero():
    try:
        answer(seed=1, size=0, possible_answers=["A", "B"])
        assert False
    except ValueError:
        assert True


def test_invalid_size_negative():
    try:
        answer(seed=1, size=-5, possible_answers=["A", "B"])
        assert False
    except ValueError:
        assert True


def test_seed_none():
    try:
        answer(seed=None, size=10, possible_answers=["A", "B"])
        assert False
    except ValueError:
        assert True

def test_empty_possible_answers():
    try:
        answer(seed=1, size=10, possible_answers=[])
        assert False
    except ValueError:
        assert True