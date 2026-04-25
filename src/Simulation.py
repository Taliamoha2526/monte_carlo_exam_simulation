from src.Generator import answer
from src.Scoring import check_answers
def simulation(trials:int, no_questions:int,model_answers:list[str], possible_answers:list[str]):
    """
    This function represents the core of the experiment. It returns the desired outcomes of the simulation.
    The for loop structure is based on the number of trials we want to produce, to reduce memory usage.
    For each trial, the generator function is first ran then the scoring function.
    The weights and scores are calculated for each trial.
    The list of dictionaries is used to store the weights of each choice in each trial.
    Takes as parameters:
    trials: the number of trials chosen.
    no_questions: the number of questions experimenting with.
    possible_answers: the list of possible answers chosen.
    model_answers: the list of the model answers to be used.
    Returns:
    results: dictionary with the data related to the experiment.
    results contains:scores, weights, expected mean, observed mean, number of successful attempt, and the total success rate
    """
    #input constraints
    if len(model_answers)!= no_questions:
        raise ValueError ("The answers do not match the number of questions")
    if trials <=0:
        raise ValueError ("The number of trials must be greater than 0")
    if no_questions <= 0:
        raise ValueError ("The number of questions must be greater than 0")

    #trial initialization
    scores_list=[]
    total_weights=[]
    for i in range(trials):
        #single trial logic
        answers= answer(i, size=no_questions, possible_answers=possible_answers).tolist()
        weight = {}
        for choice in possible_answers:
            weight[choice]= answers.count(choice)
        total_weights.append(weight)
        scores_list.append(check_answers(answers, model_answers, possible_answers).count('Correct'))
    assert len(scores_list)==len(total_weights)

    #calculations and data observed
    passed= [x for x in scores_list if x >= no_questions//2]
    expected_mean= no_questions/len(possible_answers)
    observed_mean= sum(scores_list)/len(scores_list)
    successful_attempts= len(passed)
    success_rate= len(passed)/ trials
    results={'scores':scores_list,'weights':total_weights, 'exp_mean':expected_mean,
             'obs_mean':observed_mean,'successful_attempts':successful_attempts,
             'success_rate':success_rate}

    return results





