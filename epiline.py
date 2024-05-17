import rpy2.robjects as robjects

# Import an R file
r_source = robjects.r["source"]
r_source("epiline.R")

# Get the R function
run_epiline = robjects.r["run"]

r_result = run_epiline()

print(f"Result: {r_result}")
