
To determine whether the quantum state of the example $|b⟩ = \frac{1}{\sqrt{3}} |00⟩ + \frac{1}{\sqrt{3}} |01⟩ + \frac{1}{\sqrt{3}} |10⟩$ is **entangled** or **separable**, we check if it can be written as a **tensor product** of two single-qubit states:

$|b⟩ = |\psi⟩ \otimes |\phi⟩$

---
### Step 1

it is a two-qubit system, with basis:

$|00⟩, |01⟩, |10⟩, |11⟩$ (this is allways the same)

example: $|b⟩ = \frac{1}{\sqrt{3}} |00⟩ + \frac{1}{\sqrt{3}} |01⟩ + \frac{1}{\sqrt{3}} |10⟩$

Note: There is **no component of** $∣11⟩$⟩, i.e., its amplitude is 0.

---

### Step 2

Assume:
$$|\psi⟩ = a|0⟩ + b|1⟩, \quad |\phi⟩ = c|0⟩ + d|1⟩$$
Then the product is:
$$|\psi⟩ \otimes |\phi⟩ = ac |00⟩ + ad |01⟩ + bc |10⟩ + bd |11⟩$$
Compare to:
$$|b⟩ = \frac{1}{\sqrt{3}} |00⟩ + \frac{1}{\sqrt{3}} |01⟩ + \frac{1}{\sqrt{3}} |10⟩ + 0 \cdot |11⟩$$
This matches to:
- $ac= \frac{1}{\sqrt{3}}​$
- $ad= \frac{1}{\sqrt{3}}$
- $bc= \frac{1}{\sqrt{3}}$
- $bd=0$

Since $b\times d=0$ it means, that,
	either $b = 0$
	or $d=0$

if $b=0$:
	$b\times c=0$, but $bc = \frac{1}{\sqrt{3}} \neq 0$  → contradiction.
If $d=0$:
	$a\times d=0$, but $ad= \frac{1}{\sqrt{3}}​$ → contradiction

**No solution** exists:
⇒ **cannot be written as a product state**.
⇒ The state **cannot** be separated into two independent qubits
⇒ the state is **entangled**

---

## Schmidt Decomposition

**Schmidt decomposition**:

$|\psi⟩ = \alpha|00⟩ + \beta|01⟩ + \gamma|10⟩ + \delta|11⟩$

Form a 2×2 matrix:

$M = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}$

Compute the **determinant**:

$\text{det}(M) = \alpha\delta - \beta\gamma$
- If $\text{det}(M) = 0$, the state is **not entangled** (separable).
- If $\text{det}(M) \neq 0$, the state **is entangled**.
