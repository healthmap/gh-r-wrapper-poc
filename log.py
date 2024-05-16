from rpy2.robjects.packages import importr
import rpy2.robjects as robjects


# Needed for `toJSON` call
_ = importr("jsonlite")

# Create an R logging function
structured_logging_function = """
log_message <- function(level, message) {
  # Get current timestamp
  timestamp <- Sys.time()

  # Create log object
  log <- list(
    timestamp = timestamp,
    level = level,
    message = message
  )

  # Convert log object to JSON
  log_json <- toJSON(log, pretty = TRUE)

  # Print JSON log
  cat(log_json, "\n")
}
"""

# Execute the R logging function
robjects.r(structured_logging_function)

# Call the R logging function from Python
level = "INFO"
message = "Hello!"
robjects.r["log_message"](level, message)

level = "CRITICAL"
message = "Uh oh!"
robjects.r["log_message"](level, message)
