# Import all test functions
from testing.test_scorer import *
from testing.test_simulation import *
from testing.test_generator import *


def run_all_tests():
    #start with generator tests
    print("Running generator tests:")
    test_output_length()
    test_output_values_valid()
    test_minimum_case()
    test_reproducibility()
    test_different_seeds()
    test_invalid_size_zero()
    test_invalid_size_negative()
    test_seed_none()
    test_empty_possible_answers()
    print("Generator tests passed.\n")

    # move on to scorer tests
    print("Running scorer tests:")
    test_all_correct()
    test_all_wrong()
    test_partial_correct()
    test_length_mismatch()
    test_invalid_model_answer()
    test_invalid_generated_answer()
    test_empty_inputs()
    print("Scorer tests passed.\n")

    #lastly run simulation tests
    print("Running simulation tests:")
    test_output_structure()
    test_output_lengths()
    test_score_bounds()
    test_weights_sum_to_questions()
    test_mean_close_to_expected()
    test_reproducibility()
    test_invalid_trials()
    test_invalid_questions()
    test_mismatched_model_length()
    test_empty_possible_answers()
    print("Simulation tests passed.\n")


    print("All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()