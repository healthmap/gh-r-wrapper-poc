library(arrow)


# Print each row in an input Apache Arrow table
print_arrow_table <- function(arrow_table) {
  # Get the number of rows in the table
  num_rows <- length(arrow_table[[1]])

  # Get the column names
  col_names <- names(arrow_table)

  # Print column names
  cat(paste(col_names, collapse = "\t"), "\n")

  # Iterate over rows and print each row
  for (i in 1:num_rows) {
    row <- lapply(arrow_table, function(x) x[[i]])
    cat(paste(row, collapse = "\t"), "\n")
  }

  # Return an arrow array 
  ret <- Array$create(c(42))
  return(ret)
}
