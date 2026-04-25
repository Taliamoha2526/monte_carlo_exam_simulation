def check_answers(x:list[str], model:list[str], possible_answers:list[str]):
    """ Checks whether the answer is similar to the corresponding question in the model answers list.
    params:
    x: The list of the answers chosen by the algorithm.
    model: The list of model answers.
    Returns the list results, which contains the string 'Correct' or 'Wrong' for each question.
    """

    #input constraints
    if len(x) != len(model):
        raise ValueError("Provided answers and model answers must be the same length.")
    if not possible_answers:
        raise ValueError("Possible answers must not be empty.")

    result=[]
    for answer in range(len(model)):

        #logical constraints
        if model[answer] not in possible_answers:
            raise ValueError(f"The model answer to the {answer+1}th question is invalid.")
        if x[answer] not in possible_answers:
            raise ValueError(f"The generated answer to the {answer+1}th question is invalid.")

        #core logic.
        if x[answer] == model[answer]:
            result.append('Correct')
        else:
            result.append('Wrong')
    return result