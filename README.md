# gh-r-wrapper-poc
Contains a proof-of-concepts for wrapping R scripts with Python.

## Running

Install R packages
```
Rscript -e 'install.packages("jsonlite", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("arrow", repos="https://cloud.r-project.org")'
```

Run python script
```
python <SCRIPT>
```

## Scripts 

- `log.py` - structured logging
- `error.py` - error handling and exiting
- `data.py` - loading data into memory and using it between processes

