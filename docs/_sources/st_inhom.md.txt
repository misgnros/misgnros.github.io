---
blogpost: true
date: 2024-04-14 # YYYY-MM-DD
category: math
tags: stochastic process
language: en
--- 

# Existence of a unique stationary distribution for a time-inhomogeneous Markov process
A unique stationary distribution exists for a Markov process under some conditions.

Time-homogeneous Markov processes have time-independent transition probabilities(or rates). Although many textbooks discuss proofs that time-homogeneous Markov processes have unique stationary distributions, that of time-**inhomogeneous** ones are not so common(as far as I know, information on web is kind rather than textbooks)[^wiki][^mathoverflow].

In the following, we discuss a proof for time-inhomogeneous Markov processes. This problem is significant for some MCMC algorithms utilizing time-inhomogeneity.

```{Attention}
The following discussion is not rigorous in mathematical sense. I tried to describe as far as intuitive. However I assumed basics of the probability theory, such as the terms conditional probability, joint probability, and so on. 
```

## Notations and setup
Consider a random variable $X$. $x$ is a some value that random variable $X$ can take. Probability of $X=x$ is expressed $p_X(x)$. In the same way, a capital letter indicates a random variable and small letter indicates a some value. 

A stochastic process $\{X_t\}_t$ is defined by a sequence of random variables $X_1, X_2, \ldots ,X_T$ , where $T$ is a positive inetger. $\{X_t\}_t$ is called Markov process when $X_{t+1}$ is affected only $X_t$, a variable at the previous time step. Thus, joint probability is,

$$
p_{X_{1:T}}(x_{1:T}) = \prod_{t=1}^{T-1} p_{X_{t+1}|X_t} (x_{t+1}|x_t) p_{X_1}(x_1).
$$

In this article, discrete-time Markov processes for discrete variables is only considered. Extending the following discussion to continuous-time cases is not so difficult.

## Time-homogeneous Markov processes
Time-homogeneous Markov processes are defined by time-independent transition probabilities(or rates). Thus,

$$
p_{X_2|X_1} (x'|x) = \cdots = p_{X_T|X_{T-1}} (x'|x).
$$

In the following, I use $T(x'|x)$ for  $p_{X_{t+1}|X_t} (x'|x) (t=1,\ldots,T-1)$ in time-homogeneous Markov processes.

In contrast, time-**inhomogeneous**(or non-homogeneous) Markov processes have time-dependent transition probabilities.

A stationary distribution of $\{X_t\}_t$, denoted by $p^{\mathrm{st}}(x)$, is defined as follows.

```{math}
p^{\mathrm{st}} (x) &= p_{X_t} (x) \quad (t=1,\ldots,T-1) \\
\sum_{x'} p_{X_{t+1}|X_t} (x|x')p_{X_t} (x') &= 1 \cdot p_{X_t} (x) \\
\sum_{x'} p_{X_{t+1}|X_t} (x|x')p_{X_t} (x') &= \sum_{x'} p_{X_{t+1}|X_t} (x'|x){X_t} (x)
```

The last equation is called the balance condition, which means the probability flows between $x$ and $x'$ is balancing.

$$
\sum_{x'} [p_{X_{t+1}|X_t} (x|x')p_{X_t} (x') - p_{X_{t+1}|X_t} (x'|x)p_{X_t} (x)] = 0
$$

## Existence of $p^{\mathrm{st}}$ for time-homogeneous cases in a nutshell
For a time-homogeneous Markov process, there exists a unique stationary distribution under the following conditions.
- Finiteness: The size of state space(set of the values that random variable can be) is finite.
- Aperiodicity: GCD of step numbers, that probability of returning the state $i$ from the same $i$, is 1.
- Irreducibility: For any $(i,j)$ in state space, 
  - starting from state $j$, probability of state $i$ after some steps is positive and,
  - starting from state $i$, probability of state $j$ after some steps is positive.
See standard textbooks for details.
## Mapping inhomogeneous to homogeneous
Time-inhomogeneous Markov processes can be mapped to time-homogeneous Markov processes. Some properties of time-homogeneous ones can be obtained when considering time-inhomogeneous cases[^serfozo2009].

Let $\{X_t\}_t (t=1,2,\ldots)$  is a time-inhomogeneous Markov process. Then, the two-dimensional random variable $Y_{t} = (X_t, t)$ obeys a time-homogeneous process.

Here, we introduce a parameter $\tau := t$, which means time for a process $\{ Y_{\tau} \}_{\tau}=\{ X_{\tau}, t_{\tau} \}_{\tau}$ (where $p(t_{\tau})=\delta_{t,\tau}$), because regarding $t$ like an independent random variable makes the discussion clear.

Starting from one-step evolution,  we show the transition probabiliy for $\{ Y_{\tau} \}_{\tau}$ is independent of time $\tau$ as follows.

```{math}
p_{Y_{\tau+1}, Y_{\tau}}(y_{\tau+1}, y_{\tau}) &= p_{Y_{\tau+1}|Y_{\tau}}(y_{\tau+1}|y_{\tau}) p_{Y_{\tau}}(y_{\tau}) \\
&= p_{X_{\tau+1},t+1|X_{\tau},t}(x_{\tau+1},t+1|x_{\tau},t) p_{X_{\tau},t}(x_{\tau},t) \\
&= p_{X_{\tau+1}|t+1,(X_{\tau},t)}(x_{\tau+1}|t+1,x_{\tau},t) p_{t+1|X_{\tau},t}(t+1|x_{\tau},t) p_{X_{\tau},t}(x_{\tau},t) \\
&= p_{X_{\tau+1}|X_{\tau}}(x_{\tau+1}|x_{\tau}) p_{X_{\tau},t}(x_{\tau},t) \\
&= p_{X_{\tau+1}|X_{\tau}}(x_{\tau+1}|x_{\tau}) p_{X_{\tau}}(x_{\tau}) \delta_{\tau,t} \\
&= p_{X_{t+1}|X_{t}}(x_{t+1}|x_{t}) p_{X_{\tau},t}(x_{\tau},t) \\
\rightarrow p_{Y_{\tau+1}|Y_{\tau}}(y_{\tau+1}|y_{\tau})&= p_{X_{t+1}|X_{t}}(x_{t+1}|x_{t})
```

Assuming the conditions finiteness, aperiodicity, and irreducibility for time-homogeneous process $\{ Y_{\tau} \}_{\tau}$,  it has a unique stationary distribution $p^{\mathrm{st}}_Y$. We obtain a unique stationary distribution for $\{ X_t \}_t$ by margnalizing $t$ of $p^{\mathrm{st}}_Y$.

```{math}
\sum_t p^{\mathrm{st}}_Y = p^{\mathrm{st}}_X
```

Finally we get our target $p^{\mathrm{st}}_X$,  a unique stationary distribution for time-**inhomogeneous** Markov process.

[^wiki]: [https://en.wikipedia.org/wiki/Discrete-time_Markov_chain#Steady-state_analysis_and_the_time-inhomogeneous_Markov_chain](https://en.wikipedia.org/wiki/Discrete-time_Markov_chain#Steady-state_analysis_and_the_time-inhomogeneous_Markov_chain)

[^mathoverflow]: [https://mathoverflow.net/questions/209907/stationary-distribution-for-time-inhomogeneous-markov-process](https://mathoverflow.net/questions/209907/stationary-distribution-for-time-inhomogeneous-markov-process)

[^serfozo2009]: Serfozo, R. (2009). Basics of applied stochastic processes. Springer.
