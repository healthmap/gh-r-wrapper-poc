# Taken from https://github.com/BDI-pathogens/EpiLine/tree/main?tab=readme-ov-file#example-results

library(EpiLine)
library(htmlwidgets)
set.seed(1)

# Run the EpiLine example
run <- function(t_rep, t_symptom_pre, t_symptom_post, plot_name) {
  t_max <- t_rep + t_symptom_post + t_symptom_pre

  # set up the variable r(t) and distribution
  symptom_0 <- 2                                # initial number of symptomatic people
  r         <- 0.1 - 0.13 * ( 1:t_max ) / t_max # r(t) in the simulation
  xi        <- -1 + 6 * ( t_max:1 ) / t_max          # xi parameter in the symptom-report dist
  lambda    <- 2 + ( t_max:1 ) / t_max         # lambda parameter in the symptom-report dist

  simulation <- symptom_report.simulator(
    t_rep          = t_rep,
    t_symptom_pre  = t_symptom_pre,
    t_symptom_post = t_symptom_post,
    symptom_0   = symptom_0,
    r           = r,
    dist_xi     = xi,
    dist_lambda = lambda
  )

  # data 
  reported    <- simulation$reported
  ll_report   <- simulation$linelist$report
  ll_symptom  <- simulation$linelist$symptom
  report_date <- as.Date("2022-04-01")

  # fit using model
  mcmc_n_samples <- 100
  mcmc_n_chains  <- 1
  fit <- symptom_report.fit(
    reported,
    ll_symptom,
    ll_report,
    
    report_date = report_date,
    mcmc_n_samples = mcmc_n_samples,
    mcmc_n_chains = mcmc_n_chains
  )
  
  plot_symptoms <- fit$plot.symptoms(show = FALSE, simulation = simulation)
  saveWidget(plot_symptoms, plot_name, selfcontained = FALSE)

  return(fit)
}
