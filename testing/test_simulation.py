# Base valid config
from src.Simulation import *
trials = 100
no_questions = 20
model_answers = ["A"] * no_questions
possible_answers = ["A", "B", "C", "D"]

def test_output_structure():
    result = simulation(trials, no_questions, model_answers, possible_answers)

    assert "scores" in result
    assert "weights" in result


def test_output_lengths():
    result = simulation(trials, no_questions, model_answers, possible_answers)

    assert len(result["scores"]) == trials
    assert len(result["weights"]) == trials


def test_score_bounds():
    result = simulation(trials, no_questions, model_answers, possible_answers)

    scores = result["scores"]
    assert all(0 <= s <= no_questions for s in scores)


def test_weights_sum_to_questions():
    result = simulation(trials, no_questions, model_answers, possible_answers)

    for weight_dict in result["weights"]:
        assert sum(weight_dict.values()) == no_questions


def test_mean_close_to_expected():
    result = simulation(trials, no_questions, model_answers, possible_answers)

    scores = result["scores"]
    mean_score = sum(scores) / len(scores)

    expected = no_questions / len(possible_answers)

    assert abs(mean_score - expected) < 1.0


def test_reproducibility():
    result1 = simulation(10, no_questions, model_answers, possible_answers)
    result2 = simulation(10, no_questions, model_answers, possible_answers)

    # Because seeds are deterministic (i), these should match
    assert result1["scores"] == result2["scores"]


def test_invalid_trials():
    try:
        simulation(0, no_questions, model_answers, possible_answers)
        assert False
    except ValueError:
        assert True


def test_invalid_questions():
    try:
        simulation(trials, 0, model_answers, possible_answers)
        assert False
    except ValueError:
        assert True


def test_mismatched_model_length():
    try:
        simulation(trials, no_questions, ["A"] * (no_questions - 1), possible_answers)
        assert False
    except ValueError:
        assert True


def test_empty_possible_answers():
    try:
        simulation(trials, no_questions, model_answers, [])
        assert False
    except ValueError:
        assert True