> [!CITE] **Algorithm 5 (Simulated Annealing with Local Gradient Descent)**  
> Let $n \in \mathbb{N}$ , $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e_{\mathcal{D}}, \langle x_u \rangle_{0 \leq u \leq t})$  be an optimization process. This process continues via **simulated annealing with $n$ steps of local gradient descent** if $e_{\mathcal{D}}$ has the form:
>
$$e_{\mathcal{D}}(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} = \begin{cases} \ast \mathcal{E}(x_t') & \text{if } \tau(\ast \mathcal{E}(x_t')) \leq \tau(x_t) \\ & \quad \text{or } r \leq A(\tau(x_t), \tau(\ast \mathcal{E}(x_t')), \kappa(t)) \\ x_t & \text{otherwise} \end{cases}$$​
>
> where $x_t', r, A, kappa$: are given as in [[Algorithm 3 (Simulated Annealing)]] and where $\mathcal{E}(x_t') = (\mathcal{X}, \mathcal{T}, \tau, e_{\mathcal{E}}, \langle x_{t+v}' \rangle_{0 \leq v \leq n})$ is an optimization process that continues via gradien descent [[Algorithm 4 (Gradient Descent)]] so that:
> $$\ast \mathcal{E}(x_t') = \arg \min_{x_{t+v}' \; , \; 0 \leq v \leq n} \tau(x_{t+v}')$$
is the best solution found by $\mathcal{E}$ when starting at $x_t'$

---

## ELI5

This algorithm combines two powerful ideas: **Simulated Annealing (SA)** and **Gradient Descent (GD)**.
1. It starts like simulated annealing:  
    You randomly try a new point near your current one (called $x_t'$). Then you explore from there using a few steps of gradient descent to find an improved version of that point (called $\ast \mathcal{E}(x_t')$ — the best one after descent).
2. Then it decides:
    - **If this new point is better** (lower cost), we **take it**.
    - **If it’s worse**, we **might still take it** with a probability (like in simulated annealing) depending on how bad it is and the current “temperature” $\kappa(t)$.
    - If not accepted, we stay at the current point.
3. Over time, the algorithm becomes stricter about accepting worse points, thanks to the **cooling schedule** $\kappa(t)$.

---

## Summary

Simulated Annealing with Local Gradient Descent lets you:
- Escape local minima like SA (thanks to randomness),
- Quickly refine candidates using GD (by descending locally),
- Balance exploration and exploitation smartly,
- And ultimately find better solutions than using just SA or GD alone.

This method is especially useful when you want the broad search power of simulated annealing _and_ the fine-tuning precision of gradient descent.