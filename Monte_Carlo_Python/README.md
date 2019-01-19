# Monte-Carlo-Python
Monte Carlo Simulation and Black Scholes Model discussion and example using a brief dataset

> Note: **Please read .pdf document!**

## What is the Monte Carlo Simulation?

From Investopedia, 

"Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables.


## Where's the Formula?

Monte Carlo Simulation is a method, and goes by conditions of using **Black Scholes Model** and **Brownian Motion** (a type of stochiastic process). Below is a brief overview of the simulation:

1 Draw I (psuedo) random numbers $z(i), i \in \{1,2,...,I\}$ , from the standard normal distribution
2 Calculate all resulting index levels at maturity $S_T{(i)}$ for given $z(i)$ and the Black Scholes Model $S_T = S_0 \exp{( (r - \dfrac{1}{2} \sigma^2)T + \sigma \sqrt{T} z    )}$

3 Calculate all inner values of the option at maturity as $h_T (i) = \max{(S_T (i) K,0)}$ 
4 Estimate the option present value via Monte Carlo estimator below:

$$ C_0 = e^{-rT} \dfrac{1}{I} \underset{I}{\sum}{{h_T (i)}}$$


where:

- $S_t$ is the spot price of the underlying asset

- $S_0$ initial stock index

- $k$ is the strike price

- $h_T (i)$ is our option at maturity

## Resources

1. [Investopedia on Monte Carlo Simulation](http://www.investopedia.com/terms/m/montecarlosimulation.asp)
