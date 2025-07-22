

>[!CITE] **Algorithm 5 (gradient descent)**
>Let $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_u \rangle_{0 \leq u \leq t})$ be an optimization process. Let $\mathcal{T}$ be continuous ($\mathcal{T} = \mathbb{R}$, e.g.) and let $\tau': \mathcal{X} \to \mathcal{T}$ be the first derivative of $\tau$. The process $\mathcal{D}$ continues via gradient descent (with update rate $\alpha \in \mathbb{R}^+$) if $e$ is of the form
>
$$e(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} = x_t - \alpha \cdot \tau'(x_t).$$
>
The learning rate $\alpha$ can also be given as a function, usually $\alpha: \mathbb{N} \to \mathbb{R}$, so that $e(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} = x_t - \alpha(t) \cdot \tau'(x_t).$
>
If $\tau$ is stochastic, this process is called stochastic gradient descent $(SGD)$.


## ELI5

**Gradient Descent** is like walking downhill to reach the bottom of a valley (the minimum). You look at how steep the hill is at your current spot (that’s the _gradient_) and take a small step _in the opposite direction_ of the slope — downhill. The size of the step is controlled by something called the _learning rate_.

If the hill is steep, the gradient is large, and you might take a bigger step. As you get closer to the bottom, the hill flattens out, and your steps get smaller and smaller.

This method ensures that you get closer and closer to the lowest point of your cost function — ideally the best solution.

---

### Components of the Definition

1. **Optimization Process ($\mathcal{D}$):**  
    The general framework that defines how optimization steps evolve over time.
2. **Target Function ($\tau$):**  
    The function we want to minimize. For example, this might be the error or loss in a machine learning model.
3. **Gradient ($\tau'(x_t)$):**  
    The slope of the function at the current point. It tells us the direction and rate of the steepest increase. Since we want to minimize, we _go the other way_.
4. **Learning Rate ($\alpha$):**  
    A positive value that determines how big our step is at each iteration. It can be constant or decrease over time.
5. **Update Rule ($e$):**  
    The formula $x_{t+1} = x_t - \alpha \cdot \tau'(x_t)$ updates the current state by taking a step in the direction of the negative gradient.

---

### The Graph

![[Pasted image 20250716222200.png]]

![[Pasted image 20250716222312.png]]

The graph visualizes a function with a U-curve — the kind gradient descent loves.
- The **x-axis** shows the current state or position ($x_t$).
- The **y-axis** shows the value of the target function $\tau(x)$ — this is what we’re trying to minimize.
- Each **step** is a position that the algorithm visits.
- **Arrows** between the steps show the update steps — moving from one $x_t$ to $x_{t+1}$.
- The size of the step shrinks as we get closer to the bottom, since the slope (gradient) becomes smaller.

---

### Summary

Gradient descent is a simple but powerful method for minimizing functions. It follows the steepest descent direction based on the function’s slope and gradually converges to a minimum. The size of the step is critical — too big and you overshoot, too small and it takes forever. If the function is noisy (as in SGD), you still follow the general trend of going downhill, but with some random jitters.