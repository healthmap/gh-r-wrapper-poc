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
- `epiline.py` - wrapping a script


## EpiLine

The team selected the [EpiLine](https://github.com/BDI-pathogens/EpiLine) package for testing an integration beyond spikes. Installation using the included `install_epiline.sh` script currently fails at the last step, due to an outstanding issue with three files. See [this issue](https://github.com/BDI-pathogens/EpiLine/issues/7) for a description and workaround.

