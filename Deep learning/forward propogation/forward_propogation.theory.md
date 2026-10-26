# Forward Propagation — Theory


## 1. Forward Propagation kya hai?

**Forward Propagation** neural network ka woh process hai jisme input data network ke through:

**Input Layer → Hidden Layers → Output Layer**

ki direction mein move karta hai aur final mein **prediction** generate hoti hai.

### Basic Flow

```text
Input
  ↓
Hidden Layer 1
  ↓
Hidden Layer 2
  ↓
Hidden Layer 3
  ↓
Output Layer
  ↓
Prediction
```

> **Key Point:** Forward propagation mein information **input se output ki taraf** flow karti hai.

---

# 2. Basic Neuron Flow

Ek neuron previous layer se values receive karta hai. Phir un values par weights apply hote hain, bias add hota hai aur activation function output generate karta hai.

```text
Previous Layer Values
          ↓
   Weighted Sum
          ↓
       + Bias
          ↓
          Z
          ↓
 Activation Function
          ↓
          A
```

## Mathematical Form

Weighted sum:

$$
Z = \sum_{i=1}^{n} w_i x_i + b
$$

Activation ke baad:

$$
A = g(Z)
$$

### Symbols

| Symbol | Meaning |
|:---:|:---|
| **xᵢ** | Input value |
| **wᵢ** | Weight |
| **b** | Bias |
| **Z** | Pre-activation value |
| **g** | Activation function |
| **A** | Activated output |

---

# 3. Layer-wise Forward Propagation

Neural network ki kisi bhi layer l ke liye forward propagation ko do main equations se represent kiya jata hai.

### Step 1 — Weighted Sum

$$
\boxed{
Z^{[l]} = W^{[l]}A^{[l-1]} + b^{[l]}
}
$$

### Step 2 — Activation

$$
\boxed{
A^{[l]} = g^{[l]}(Z^{[l]})
}
$$

### Meaning

- W⁽ˡ⁾ → current layer ke weights
- A⁽ˡ⁻¹⁾ → previous layer ka output
- b⁽ˡ⁾ → current layer ka bias
- Z⁽ˡ⁾ → activation se pehle ki value
- A⁽ˡ⁾ → activation ke baad ki value
- g⁽ˡ⁾ → activation function

> **Important:** Har layer ka output next layer ka input ban jata hai.

---

# 4. Z aur A ka Concept

Neural network mein **Z** aur **A** ko clearly distinguish karna important hai.

## Z — Pre-activation Value

Z activation function apply hone se **pehle** ki value hai.

$$
Z = WA + b
$$

## A — Activation Value

A activation function apply hone ke **baad** ki value hai.

$$
A = g(Z)
$$

### Complete Flow

```text
Previous Layer
      ↓
    W × A
      ↓
   + Bias
      ↓
      Z
      ↓
Activation Function
      ↓
      A
```

### Short Form

$$
\boxed{A = g(WA_{\text{previous}} + b)}
$$

---

# 5. Weights ka Role

**Weight decide karta hai ki kisi input ka contribution kitna important hoga.**

Conceptually:

```text
Input
  │
  ×
Weight
  │
  ↓
Contribution
```

Agar kisi connection ka weight comparatively bada hai, toh us connection ke through aane wale input ka contribution bhi comparatively zyada ho sakta hai.

### Important Points

- Har connection ke saath ek weight associated hota hai.
- Weights training ke dauraan learn hote hain.
- Weights network ko different inputs ki importance learn karne mein help karte hain.

---

# 6. Bias ka Role

**Bias neuron ko additional flexibility provide karta hai.**

Basic neuron:

$$
Z = WX + b
$$

Bias ke bina:

$$
Z = WX
$$

Bias add karne se neuron ki decision boundary ko shift karne ki flexibility milti hai.

### Conceptual Flow

```text
Weighted Inputs
      +
    Bias
      ↓
      Z
```

> **Remember:** Weight input ke contribution ko control karta hai, jabki bias neuron ke overall activation ko shift karne mein help karta hai.

---

# 7. Activation Function ka Role

Activation function neuron ke output ko transform karta hai:

$$
\boxed{
A = g(Z)
}
$$

Activation function ka sabse important role neural network mein **non-linearity introduce karna** hai.

Agar network mein activation functions na hon, toh multiple linear layers combine hone ke baad bhi overall network effectively ek linear transformation ki tarah behave kar sakta hai.

Isliye deep neural networks mein activation functions important hain.

---

# 8. ReLU Activation

Hidden layers mein commonly used activation functions mein **ReLU (Rectified Linear Unit)** important hai.

## Formula

$$
\boxed{
ReLU(z) = \max(0,z)
}
$$

### Concept

```text
z < 0  →  0

z > 0  →  z
```

### ReLU ka Basic Behavior

```text
Output
  ↑
  │        /
  │       /
  │      /
  │     /
──┼────/────────→ Input
  │
  │
```

### Main Idea

ReLU negative values ko zero side par le jata hai aur positive values ko pass through karta hai.

> **Use:** Hidden layers mein non-linearity introduce karne ke liye ReLU widely used hai.

---

# 9. Sigmoid Activation

**Sigmoid** especially binary classification ke output layer mein commonly use hota hai.

## Formula

$$
\boxed{
\sigma(z) = \frac{1}{1+e^{-z}}
}
$$

Sigmoid ka output:

$$
0 < \sigma(z) < 1
$$

Isliye sigmoid output ko probability-like value ke form mein interpret kiya ja sakta hai.

### Conceptual Behavior

```text
Output
  1 │             ______
    │          __/
    │        _/
0.5 │───────
    │     _/
    │   _/
  0 │___/______________→ z
```

### Interpretation

```text
Output ≈ 0  → Class 0 ke closer
Output ≈ 1  → Class 1 ke closer
```

---

# 10. Hidden Layers ka Role

Hidden layer previous layer se information leti hai aur us information ko transform karke **new representation** create karti hai.

### Basic Hidden-Layer Flow

```text
Previous Layer
      ↓
Weighted Sum
      ↓
     Bias
      ↓
      Z
      ↓
Activation
      ↓
      A
      ↓
Next Layer
```

Har hidden layer ka output next layer ke liye input ban jata hai.

---

# 11. Multiple Hidden Layers

Agar neural network mein multiple hidden layers hain, toh forward propagation layer-by-layer perform hota hai.

```text
Input
  ↓
Hidden Layer 1
  ↓
Hidden Layer 2
  ↓
Hidden Layer 3
  ↓
Output
```

Har layer previous layer ka output receive karti hai.

### Layer 1

$$
A^{[1]}
=
g^{[1]}
\left(
W^{[1]}X+b^{[1]}
\right)
$$

### Layer 2

$$
A^{[2]}
=
g^{[2]}
\left(
W^{[2]}A^{[1]}+b^{[2]}
\right)
$$

### Layer 3

$$
A^{[3]}
=
g^{[3]}
\left(
W^{[3]}A^{[2]}+b^{[3]}
\right)
$$

### Output Layer

$$
\hat{Y}
=
g^{[4]}
\left(
W^{[4]}A^{[3]}+b^{[4]}
\right)
$$

> Yahi **layer-by-layer forward propagation** hai.

---

# 12. Complete Architecture

Yahan hum ek **4 → 3 → 2 → 1 → 1** neural-network architecture ko conceptually dekh rahe hain.

![Complete Architecture](architecture.png)

### Information Flow

$$
\boxed{
X
\rightarrow
A^{[1]}
\rightarrow
A^{[2]}
\rightarrow
A^{[3]}
\rightarrow
\hat{Y}
}
$$


---

# 13. Matrix Form

Forward propagation ko neural networks mein matrix form mein efficiently represent kiya jata hai.

## General Formula

$$
\boxed{
Z^{[l]} = W^{[l]}A^{[l-1]} + b^{[l]}
}
$$

Then:

$$
\boxed{
A^{[l]} = g^{[l]}(Z^{[l]})
}
$$

### Complete Flow

$$
X
\rightarrow
Z^{[1]}
\rightarrow
A^{[1]}
\rightarrow
Z^{[2]}
\rightarrow
A^{[2]}
\rightarrow
\cdots
\rightarrow
Z^{[L]}
\rightarrow
\hat{Y}
$$

---

# 14. Dimensions ka Concept

Matrix multiplication ke liye dimensions compatible honi chahiye.

Agar previous layer mein **n neurons** aur current layer mein **m neurons** hain:

### Previous Layer Output

$$
A^{[l-1]} \in \mathbb{R}^{n\times1}
$$

### Weight Matrix

$$
W^{[l]} \in \mathbb{R}^{m\times n}
$$

### Bias

$$
b^{[l]} \in \mathbb{R}^{m\times1}
$$

### Result

$$
Z^{[l]} \in \mathbb{R}^{m\times1}
$$

### Weight Matrix ka General Shape

$$
\boxed{
(\text{Current Layer Neurons})
\times
(\text{Previous Layer Neurons})
}
$$

> **Shortcut:** Weight matrix ka **rows = current layer neurons** aur **columns = previous layer neurons**.

---

# 15. Fully Connected Layer

Fully connected layer mein current layer ka **har neuron previous layer ke har neuron se connected** hota hai.

### Concept

![Layer](layer1.png)


Isliye agar previous layer mein n neurons aur current layer mein m neurons hain, toh total weighted connections:

$$
\boxed{
n\times m
}
$$

---

# 16. Important Notation

| Symbol | Meaning |
|:---:|:---|
| X | Input |
| W | Weight matrix |
| **b** | Bias |
| Z | Pre-activation / weighted sum + bias |
| **g** | Activation function |
| **A** | Activated output |
| Ŷ | Predicted output |
| l | Layer number |
| L | Final layer |

## ⭐ Most Important Formulas

### Linear Transformation

$$
\boxed{
Z^{[l]}=W^{[l]}A^{[l-1]}+b^{[l]}
}
$$

### Activation

$$
\boxed{
A^{[l]}=g^{[l]}(Z^{[l]})
}
$$

### Final Prediction

$$
\boxed{
\hat{Y}=A^{[L]}
}
$$

---

# 17. Final Mental Model

Forward Propagation ko ek simple chain ki tarah yaad rakho:

```text
INPUT
  ↓
Weights se multiply
  ↓
Bias add
  ↓
  Z
  ↓
Activation Function
  ↓
  A
  ↓
Next Layer
  ↓
Repeat
  ↓
OUTPUT
  ↓
PREDICTION
```

### One-Line Formula

Har layer ke liye:

$$
\boxed{
A^{[l]}
=
g^{[l]}
\left(
W^{[l]}A^{[l-1]}+b^{[l]}
\right)
}
$$

### Final Takeaway

> **Forward Propagation = Input ko layer-by-layer process karke final prediction tak pahunchana.**

