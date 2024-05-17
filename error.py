import logging

import rpy2.robjects as robjects


r_functions = """
exit_nonzero_on_error <- function(code, status_code) {
  tryCatch(code, error = function(c) {
    cat("Exiting from R", "\n")
    quit(status=status_code)
  })
  cat("No error to quit on", "\n")
}

exit <- function() {
  exit_nonzero_on_error(stop("!"), 42)
}

raise_on_error <- function(code) {
  tryCatch(code, error = function(c) {
    cat("Raising from R", "\n")
    stop("Problem in R function")
  })
  cat("No error to raise", "\n")
}

raise <- function() {
  raise_on_error(stop("!"))
}

run <- function() {
  raise_on_error(message("Hello"))
  exit_nonzero_on_error(message("Hello"), 0)
}
"""

# Execute the functions
robjects.r(r_functions)

# No errors
robjects.r["run"]()

# Error caught by Python for handling
try:
    robjects.r["raise"]()
except Exception:
    logging.exception("An error happened")

# Exit immediately from R
try:
    robjects.r["exit"]()
except Exception:
    logging.exception("This is unreachable!")
