> [!CITE] Definition 9 (optimization)  
> Let $\mathcal{X}$ be an arbitrary **state space**, $\mathcal{T}$ a **target space**, and $\leq$ a **total order** on $\mathcal{T}$. A total function $\tau : \mathcal{X} \to \mathcal{T}$ is called a **target function**. Optimization (minimization/maximization) means searching for an $x \in \mathcal{X}$ such that $\tau(x)$ is optimal. Unless stated otherwise, assume minimization.
> 
> An **optimization run** of length $g+1$ is a sequence of states $\langle x_t \rangle_{0 \leq t \leq g}$ with $x_t \in \mathcal{X}$ for all $t$.

---

## ELI5

This definition sets up the formal framework for understanding **optimization** — a process where we try to find the _best_ option from a set of possibilities, based on some measurement or **target function**.

---

### Components of the Definition

1. **State Space ($\mathcal{X}$):**  
    The set of all possible choices or solutions we could consider during optimization.
2. **Target Space ($\mathcal{T}$):**  
    The range of values we get when we evaluate a solution using the target function — often representing things like cost, error, or reward.
3. **Target Function ($\tau$):**  
    This is the measurement function. For each state $x \in \mathcal{X}$, it tells us how "good" that state is:  
    $\tau : \mathcal{X} \to \mathcal{T}$
    Lower values are better if we are minimizing.
4. **Optimization Run:**  
    A sequence of states:  
    $\langle x_t \rangle_{0 \leq t \leq g}$​  
    It shows how the optimizer moves through different solutions over time (from $t = 0$ to $t = g$).

---

### Terminology Introduced

- **Working to some extent:**  
    An optimization run is _working to some extent_ if, for time steps $t \leq t'$ in $[1, g]$, the function values $\tau(x_t)$ and $\tau(x_{t'})$ **correlate positively** — that means, roughly, that progress is being made on average, even if it's not guaranteed at every step.
    
- **Improving:**  
    A run is **improving** if for all $t \leq t'$:  
    $\tau(x_t) \geq \tau(x_{t'}))$  
    So, the target function value never gets worse — it's always improving or staying the same.
    
- **Found a global optimum:**  
    The optimization run has **found a global optimum** if:  
    $\tau(x) \geq \tau(x_g) \; \text{for all } x \in \mathcal{X}$
    This means that $x_g$ is at least as good as every possible state — it’s the best you can do.
    

---

### Summary

This definition gives a formal way to describe what it means for an optimization process to be:
- Making _some_ progress (`working to some extent`)
- _Strictly improving_ at every step
- Or having _found the best possible solution_

It does so by tracking how the values from the target function change over time in a run.

---

> [!CITE] Optimization Process & Evaluation  
> Let $e : \langle \mathcal{X} \rangle \times (\mathcal{X} \to \mathcal{T}) \to \mathcal{X}$ be a (possibly randomized) function that defines how new states in an optimization run $\langle x_t \rangle_{0 \leq t \leq g}$ are produced by calling $e$ repeatedly, i.e,. $x_{t+1} = e\left(\langle x_u \rangle_{0 \leq u \leq t}, \tau \right)$ fro all $t, 1 \leq t \leq g,$ where $x_o$ is given externally (e.g.; $x_0 = _{def}42$) or chosen randomly (e.g., $x_0 ~ \mathcal{X}$). An optimization process is a tuple $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_t \rangle_{0 \leq t \leq g})$

### ELI5

This definition explains **how an optimization algorithm works** and how to evaluate its performance.

The key idea is that the optimization process generates a sequence of states $x_t$ using a rule (called $e$) that can depend on previous states and the target function. This process can be deterministic or random.

---

### Components of the Optimization Process

1. **$e$: The next-step function**  
    Think of $e$ as the **brain** of the optimizer: it looks at the history so far (all $x_u$ up to time $t$) and the evaluation function $\tau$, and then decides what the next state $x_{t+1}$ should be.
2. **$\langle x_t \rangle_{0 \leq t \leq g}$: The run**  
    This is the **sequence of states** or solutions produced during optimization — starting from $x_0$ and ending at $x_g$.
3. **The process tuple**  
    The optimization process as a whole is:
    $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_t \rangle_{0 \leq t \leq g})$
    It includes everything: the search space, the target function, the rule to generate new states, and the actual run.

---

### Terminology Introduced

- **End Result ($x_g$):**  
    The last state in the optimization run. It’s the final solution the algorithm ended up with.
- __Best Result ($*_\mathcal{D}$):  
    The best state among all $x_t$ in the run:
    $*\mathcal{D} = \arg\min_{x_t,\, 0 \leq t \leq g} \tau(x_t)$
    It is the state with the best target value encountered during the run.
- **Best Target Value ($|\mathcal{D}|$):**  
    The value of $\tau$ at the best state:
    $|\mathcal{D}| = \tau(*\mathcal{D})$
- **Continuation ($\mathcal{D}'$):**  
    A longer version of the same run. $\mathcal{D}'$ is a continuation of $\mathcal{D}$ if it starts the same way (same $x_t$ for $t \leq g$), and continues up to some $g' \geq g$:
    $\mathcal{D}' = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x'_t \rangle_{0 \leq t \leq g'})$
- **$\ell(\mathcal{D})$ (Set of Continuations):**  
    The set of **all possible continuations** of $\mathcal{D}$ — important when $e$ is random, so there could be many ways to continue the run.
- **Elitist Optimization:**  
    The process $\mathcal{D}$ is **elitist** if, for all its continuations, the target value never gets worse:
    $\tau(x'_t) \geq \tau(x'_{t'}) \quad \text{for all } t \leq t'$
    That means the optimizer **keeps the best-so-far** and doesn't allow regression.

---

### Summary

This section formalizes how an optimization algorithm works — how it generates new solutions using a function $e$, how we evaluate its output, and how we define _the best result_. It also introduces the important idea of **elitism**, where optimizers are designed to never lose good solutions they've already found.