import numpy as np
import rpy2.robjects as robjects
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri


def run_example(t_rep, t_symptom_pre, t_symptom_post, plot_name):
    """Runs the EpiLine example code.

    Parameters
    __________
    t_rep : int
        length of time for which data is reported
    t_symptom_pre : int
        time before the reporting period to simulate
    t_symptom_post : int
        time after the reporting period to simulate
    plot_name : str
        output filename for symptoms plot. must end in .html

    Results
    _______
    fit : R Object
        object representing fitted model

    """
    # Import an R file
    r_source = robjects.r["source"]
    r_source("epiline.R")

    # Get the R function
    run_epiline = robjects.r["run"]
    fit = run_epiline(t_rep, t_symptom_pre, t_symptom_post, plot_name)
    return fit


if __name__ == "__main__":
    PLOT_HTML_FILENAME = "symptoms.html"
    SYMPTOMS_MATRIX_FILENAME = "symptoms.csv"
    result = run_example(50, 30, 5, "symptoms.html")
    symptoms_matrix_r = result["stan_extract"][0]
    with (ro.default_converter + pandas2ri.converter).context():
        symptoms_matrix_np = ro.conversion.get_conversion().rpy2py(symptoms_matrix_r)
    np.savetxt(SYMPTOMS_MATRIX_FILENAME, symptoms_matrix_np, delimiter=",")
    print("\n-----")
    print(f"Interactive plot saved at: {PLOT_HTML_FILENAME}")
    print(f"Symptoms matrix saved at: {SYMPTOMS_MATRIX_FILENAME}")
    print("-----\n\n")
