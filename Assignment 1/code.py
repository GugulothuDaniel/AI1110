import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

#Simulating the probability using the binomial random variable

simlen = 100000

data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of a coin tossed 6 times and noting the number of heads

fav_count = np.count_nonzero(data_binom == 6)  #Finding the number of times all the outcomes of the 6 tosses is head

print(fav_count/simlen)  #printing the probability of all 6 tosses being heads
