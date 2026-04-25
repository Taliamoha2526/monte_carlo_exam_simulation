from src.Simulation import simulation
from src.Visualization import *
from config import *
import json as json
def save_summary(results, path="results/data/summary.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    summary = {
        "exp_mean": results["exp_mean"],
        "obs_mean": results["obs_mean"],
        "successful_attempts": results["successful_attempts"],
        "success_rate": results["success_rate"]
    }

    with open(path, "w") as f:
        json.dump(summary, f, indent=2)


results= simulation(trials= trials, no_questions= no_questions,
                            possible_answers= possible_answers, model_answers= model_answers)
save_summary(results)

print(f"The expected mean for {trials} trials with {no_questions} questions with {len(possible_answers)} possible answers is {results['exp_mean']}.")
print(f"The observed mean for {trials} trials with {no_questions} questions with {len(possible_answers)} possible answers is {results['obs_mean']}.")
print(f"The number of successful attempts(passed trials) is: {results['successful_attempts']}.")
print(f"The success rate is: {results['success_rate']}.")

Scores= results['scores']
Weights= results['weights']

vis_scores(Scores, Weights, save_path="results/plots/score_distribution.png")
vis_weights(Scores, Weights, possible_answers= possible_answers, save_path="results/plots/weights_distribution.png")
vis_seeds(Scores, Weights, save_path="results/plots/trial.vs.seed.png")