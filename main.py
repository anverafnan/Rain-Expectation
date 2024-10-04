import scipy.stats as stats

prob1=stats.poisson.pmf(6,10)
print("probablity of raining of exactly 6 days: ",prob1)

prob2=stats.poisson.pmf(12,10) + stats.poisson.pmf(13,10) + stats.poisson.pmf(14,10)
print("probablity of rainning for 12-14 days:",prob2)