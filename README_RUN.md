# How to Run the Simulation

Follow these steps to set up the environment and execute the Monte Carlo simulation.

1. Prerequisites
Ensure you have **Python 3.14+** installed. You can check your version with:
```bash
python --version
```

2. Environment Setup
It is recommended to use a virtual environment to manage dependencies and keep your global Python installation clean:

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install Dependencies
Install the required scientific computing libraries (such as NumPy and Matplotlib) using the provided requirements file:

```bash
pip install -r requirements.txt
```

4. Running the Simulation
The project uses a main execution pipeline. Run the script to start the Monte Carlo trials:

Standard Run:
```bash
python run.py
```

5. Running Tests
To ensure the mathematical logic and generator functions are working correctly, execute the test suite:

```bash
python run_tests.py
```

6. Viewing Results
Once the simulation completes, the outputs are organized in the results/ directory:

results/plots/: PNG files showing the score distribution, convergence toward the theoretical mean, and random seed behavior.

results/data/: A summary.json file containing the precise numerical statistics (mean, success rate, etc.) for deeper analysis.

