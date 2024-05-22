# gh-r-wrapper-poc
Contains a proof-of-concepts for wrapping R scripts with Python.

## Running

### Install R packages
```
Rscript -e 'install.packages("jsonlite", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("arrow", repos="https://cloud.r-project.org")'
```

### Install EpiLine
Follow instructions [here](https://github.com/BDI-pathogens/EpiLine/tree/main?tab=readme-ov-file#installation)

### Install Python virtual environment
Using Python 3.12:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Alternatively, use `poetry` with the included `pyproject.toml`

### Run Python script
```
python <SCRIPT>
```

## Scripts 

- `log.py` - structured logging
- `error.py` - error handling and exiting
- `data.py` - loading data into memory and using it between processes
- `epiline_example.py` - runs model on simulated data, generates plot, returns data