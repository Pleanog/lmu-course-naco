
> [!CITE] **Algorithm 2 (stochastic hill climbing)**
>
> Let $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_u \rangle_{0 \leq u \leq t})$ be an optimization process.  
Let $\mathit{neighbors}: \mathcal{X} \rightarrow \mathcal{P}(\mathcal{X})$ be a function that returns a set of neighbors of a given state $x \in \mathcal{X}$. The process $\mathcal{D}$ continues via stochastic hill climbing if $e$ is of the form
>
>$$e(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} = \arg\min_{x \in \{x_t, x'_t\}} \tau(x)$$
>
where $x'_t \sim \mathit{neighbors}(x_t)$ is drawn at random for each call to $e$.

## Eli5

**Algorithm 2** is is a bit smarter than [[Algorithm 1 (Simgle-Sample Random Search)]]: it only tries **random neighbors** of the current point, not the whole space. It still picks whichever (current or new neighbor) is better, but stays more local—like climbing a hill one small step at a time.

---

### Explanation

1. **Search Space**: $\mathcal{X}$ is the set of all possible solutions.
2. **Heuristic Function**: $\tau(x)$ measures how "good" a solution $x$ is.
3. **Neighborhood Function**: $\mathit{neighbors}(x)$ returns nearby candidates of $x$.
4. **Procedure**:
    - Sample a neighbor $x'_t$ from $\mathit{neighbors}(x_t)$.
    - Compare it with $x_t$ using $\tau$.
    - Choose the better one for the next step.
5. **Nature**: This is a **local** search strategy. It improves by sampling small variations of the current state.