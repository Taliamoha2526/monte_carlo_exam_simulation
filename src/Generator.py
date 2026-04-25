import numpy as np
def answer(seed:int, size:int, possible_answers:list[str]):
    """ Chooses a random answer from the list of possible mcq answers based on a random seed.
    params:
    seed: random seed for each answer.
    size: size of the list of answers to be generated.
    possible_answers: list of possible answers to generate from.
    returns list of generated answers.
    """

    #input constraints.
    if seed is None:
        raise ValueError("Seed cannot be None.")
    if size is None:
        raise ValueError("Size cannot be None.")
    if size <=0:
        raise ValueError("Size must be greater than one.")
    if not possible_answers:
        raise ValueError("Possible answers cannot be empty.")

    #core logic.
    np.random.seed(seed)
    return np.random.choice(possible_answers, size= size)