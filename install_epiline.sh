#!/bin/bash

set -eoxu pipefail

Rscript -e 'install.packages("rstan", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("rstantools", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("StanHeaders", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("BH", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("RcppEigen", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("data.table", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("plotly", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("moments", repos="https://cloud.r-project.org")'
Rscript -e 'install.packages("matrixStats", repos="https://cloud.r-project.org")'

git clone git@github.com:BDI-pathogens/EpiLine.git

# fails due to fatal error: 'tbb/tbb_stddef.h' file not found
# see README for more info
R CMD INSTALL --no-multiarch --with-keep.source EpiLine
