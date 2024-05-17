import pyarrow as pa

import rpy2.robjects as robjects
from rpy2_arrow.pyarrow_rarrow import (
    rarrow_to_py_array,
    converter as arrowconverter
)
from rpy2.robjects.conversion import localconverter


# Import an R file
r_source = robjects.r["source"]
r_source("data.R")

# Get the R function
print_table = robjects.r["print_arrow_table"]

# Create a table
days = pa.array([1, 12, 17, 23, 28], type=pa.int8())
months = pa.array([1, 3, 5, 7, 1], type=pa.int8())
years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())
birthdays_table = pa.table([days, months, years], names=["days", "months", "years"])

# Call R function with table
with localconverter(arrowconverter):
    r_result = print_table(birthdays_table)

# The result of the R function will be an R Environment
# we can convert the Environment back to a pyarrow Array
# using the rarrow_to_py_array function
py_result = rarrow_to_py_array(r_result)
print(f"RESULT: {type(py_result)} {py_result}")
