
>[!CITE] **Algorithm 1 (single-sample random search)**
>
Let $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_u \rangle_{0 \leq u \leq t})$ be an optimization process. The process $\mathcal{D}$ continues via (single-sample) random search if $e$ is of the form 
>
$$e(⟨x_u⟩0≤u≤t,τ)=x_{t+1}=\underset{\,x\,\in\,\{x_{t},x_{t}'\}}{arg\;⁡min}\;\tau(x)$$
>
>where $x'_t \sim \mathcal{X}$ is drawn at random for each call to $e$.

### ELI5

It just tries out a **completely random new point** from the whole space, and picks it if it's better than the current one.

---

### Explanation

1. **Search Space**: $\mathcal{X}$ is the set of all possible solutions.
2. **Time-Steps**: $\mathcal{T} = \mathbb{N}$, representing iteration count (0, 1, 2, ...) for each step in the algorithm
3. **Heuristic Function**: $\tau(x)$ measures how "good" a solution $x$ is.
4. **Update Rule / Step Function** $e$:
   - $e$ takes the current trajectory (the past values of $x$) and the evaluation function $\tau$
   - and returns the next point $x_{t+1}$​
1. **Procedure**:
    - Draw a new candidate $x'_t$ uniformly from the entire space $\mathcal{X}$.
    - Compare it with the current state $x_t$ using $\tau$.
    - Select the better of the two (lower $\tau$ means better).
2. **Nature**: This is a **global**, uninformed search. It does not use local information.