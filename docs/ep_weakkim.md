---
blogpost: true
date: 2025-03-02
category: physics
tags: statistical mechanics
language: en
--- 

# Entropy flow for kinetic Ising model under weak effective field limit

The transition probability $T$ and effective field $\boldsymbol{h}_t$ of kinetic Ising model (KIM) are as follows.

```{math}
T(\boldsymbol{s}'|\boldsymbol{s}) &= \exp [ \boldsymbol{s}^{'\top} \boldsymbol{h}_t(\boldsymbol{s}) - \psi_t(\boldsymbol{s})] \\
\boldsymbol{h}_t(\boldsymbol{s}) &= \boldsymbol{H}_t + \boldsymbol{J} \boldsymbol{s}
```

By definition, the entropy flow of KIM is calculated as,
```{math}
\sigma &=\mathbb{E}[
(\boldsymbol{s}_t - \boldsymbol{s}_{t-1}) ^{\top} \boldsymbol{H}_t 
+ \boldsymbol{s}_t ^{\top} \boldsymbol{J} \boldsymbol{s}_{t-1} - \boldsymbol{s}_{t-1} ^{\top} \boldsymbol{J} \boldsymbol{s}_t
-\psi_t(\boldsymbol{s}_{t-1}) + \psi_t(\boldsymbol{s}_t)
] \\
&=\mathbb{E}[
(\boldsymbol{s}_t - \boldsymbol{s}_{t-1}) ^{\top} \boldsymbol{H}_t 
+ \boldsymbol{s}_t ^{\top} (\boldsymbol{J} - \boldsymbol{J}^{\top}) \boldsymbol{s}_{t-1} 
-\psi_t(\boldsymbol{s}_{t-1}) + \psi_t(\boldsymbol{s}_t)
].
```

Difinition and different expression of $\psi_t$ is
```{math}
\psi_t(\boldsymbol{s}) : &= \log \sum_{\boldsymbol{s}'} \exp [ \boldsymbol{s}^{'\top} \boldsymbol{h}_t(\boldsymbol{s})] \\
&= \log \sum_{s'_1} \cdots \sum_{s'_N} \exp [
s'_1 h_{1,t}(\boldsymbol{s}) + \cdots + s'_N h_{N,t}(\boldsymbol{s})
] \\
&= \log \sum_{s'_1} e^{s'_1 h_{1,t}(\boldsymbol{s})} \cdots \sum_{s'_N} e^{s'_N h_{N,t}(\boldsymbol{s})} \\
&= \log 2\cosh(h_{1,t}(\boldsymbol{s})) \cdots 2\cosh(h_{N,t}(\boldsymbol{s})) \\
&= \sum_{i=1}^N \log 2\cosh(h_{i,t}(\boldsymbol{s})).
```

Here, $\cosh$ can be transformed as
```{math}
2\cosh(h_{i,t}(\boldsymbol{s})) = 2 \left( 1 + \frac{h_{i,t}^2}{2!} + \frac{h_{i,t}^4}{4!} + \cdots \right).
```

Assuming that the magnitude of the effective field and interaction parameters are appropriately adjusted so that $| h_{i,t} | < 1$. Thus, higher-order terms can be ignored.
```{math}
2\cosh(h_{i,t}(\boldsymbol{s})) \simeq 2 \left( 1 + \frac{h_{i,t}^2}{2!}\right)
```

Using above,
```{math}
\log 2\cosh (h_{i,t}(\boldsymbol{s})) &\simeq \log 2 \left( 1 + \frac{h_{i,t}^2}{2!}\right) \\
&= \log 2 + \log \left( 1 + \frac{h_{i,t}^2}{2!}\right).
```

By taking the Taylor expansion of the logarithm for $|X|<1$ up to the first order,
```{math}
\log (1+X) = X - \frac{X^2}{2!} + \frac{X^3}{3!} - \frac{X^4}{4!} + \cdots,
```

the following equation is obtained.
```{math}
\log 2\cosh (h_{i,t}(\boldsymbol{s})) &= \log 2 + \log \left( 1 + \frac{h_{i,t}^2}{2!}\right) \\
&\simeq \log 2 + \frac{h_{i,t}^2}{2}
```

Therefore, $\psi_t$ is
```{math}
\psi_t(\boldsymbol{s}) &= \sum_{i=1}^N \log 2\cosh(h_{i,t}(\boldsymbol{s})) \\
&= \sum_{i=1}^N \left[
\log 2 + \frac{h_{i,t}^2}{2}
\right] \\
&= N \log2 + \sum_{i=1}^N \frac{h_{i,t}^2}{2}.
```

Next, the second term $h_{i,t}^2$ is calculated as
```{math}
h_{i,t}^2 &= (H_{i,t} + \sum_j J_{ij} s_j)^2 \\
&= (H_{i,t} + J_{i1}s_1 + \cdots + J_{iN}s_N)^2 \\
&= H_{i,t}^2 + J_{i1}^2 + \cdots + J_{iN}^2 + 2 H_{i,t} (J_{i1}s_1 + \cdots + J_{iN}s_N) + 2 (J_{i1}J_{i2}s_1s_2 + \cdots) \\
&= H_{i,t}^2 + \sum_j J_{ij}^2 + 2 H_{i,t} \sum_j J_{ij}s_j + 2 \sum_{j<k} J_{ij}J_{ik}s_js_k.
```

Thus, $h_{i,t}^2$ can be expanded into the sum of constants, first-order and second-order terms of spins at the same time. The expectation value of these are
```{math}
\mathbb{E} \psi_t(\boldsymbol{s}) &= \mathbb{E} [
N\log 2 + \sum_i \frac{H_{i,t}^2}{2} + \sum_{ij} \frac{J_{ij}^2}{2} + \sum_{ij} H_{i,t}J_{ij}s_j + \sum_{i,j<k} J_{ij}J_{ik}s_js_k
] \\
&= N\log 2 + \sum_i \frac{H_{i,t}^2}{2} + \sum_{ij} \frac{J_{ij}^2}{2} + \sum_{ij} H_{i,t}J_{ij}m_j + \sum_{i,j<k} J_{ij}J_{ik}C_{jk}.
```

Here, we return to the entropy flow and obtain the following substituting above,
```{math}
\mathbb{E}\psi_{t}(\boldsymbol{s}_{t-1}) - \mathbb{E}\psi_{t-1}(\boldsymbol{s}_{t}) &= \frac{1}{2}\sum_{i} (H_{i,t}^2 - H_{i,t-1}^2) + \sum_{ij} J_{ij}(m_{j,t-1}H_{i,t} - m_{j,t}H_{i,t-1}) \\
&+ \sum_{i,j<k} J_{ij}J_{ik}(C_{jk,t-1} - C_{jk,t}).
```

Therefore, the entropy flow is
```{math}
\sigma &= \sum_i (m_{i,t} - m_{i,t-1}H_{i,t}) + \sum_{ij} J_{ij}(m_{j,t-1}H_{i,t} - m_{j,t}H_{i,t-1}) \\
&+ \sum_{i,j<k} J_{ij}J_{ik}(C_{jk,t-1} - C_{jk,t}) + \sum_{ij} (J_{ij} D_{ij,t} - J_{ji} D_{ij,t-1}) + \frac{1}{2}\sum_{i} (H_{i,t}^2 - H_{i,t-1}^2).
```

Among these, all terms can be calculated using the mean-field approximation, as they are described by expectations, correlations at the same time, and correlations over one time step and constans[^1].

[^1]: [Aguilera, M., Moosavi, S.A. & Shimazaki, H. A unifying framework for mean-field theories of asymmetric kinetic Ising systems. Nat Commun 12, 1197 (2021).](https://doi.org/10.1038/s41467-021-20890-5)
