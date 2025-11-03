
##  RNA Secondary Structure Prediction using the Nussinov–Jacobson Algorithm

###  Project Overview

This mini-project implements the **Nussinov–Jacobson dynamic programming algorithm** to predict the **secondary structure of RNA molecules**.
The algorithm maximizes the number of valid base pairs (A–U, G–C, and G–U wobble) without pseudoknots.

It serves as a simplified computational model to understand RNA folding and can be compared against experimental and energy-based results (such as **mfold** and **Vienna RNA**).

---

###  Objective

1. Implement the historical **Nussinov–Jacobson algorithm** for RNA folding prediction.
2. Predict the dot-bracket notation representing base pairings in an RNA sequence.
3. Compare the computational prediction with:

   * **mfold** prediction results
   * **Experimental (NMR) structure**
4. Evaluate how well the computational approach reflects the biological folding.

---

###  Algorithm Background

The **Nussinov–Jacobson algorithm** uses **dynamic programming** to find the RNA secondary structure with the **maximum number of base pairs**.

#### Recurrence relation:

For each subsequence *(i, j)*:

```
M[i, j] = max(
    M[i+1, j],
    M[i, j-1],
    M[i+1, j-1] + 1 if base[i] pairs with base[j],
    max(M[i, k] + M[k+1, j]) for i < k < j
)
```

The final result `M[0, n-1]` gives the maximum possible number of base pairs.
The corresponding **dot-bracket notation** is reconstructed by tracing back through the DP table.

---

###  Project Structure

```
RNA_Nussinov/
│
├── src/
│   ├── rna_sequence.py      # RNA sequence validation and base-pair checking
│   ├── nussinov_dp.py       # Dynamic programming implementation
│
├── main.py                  # Entry point: user interface and results printing
├── README.md                # Project documentation (this file)
└── .gitignore
```

---

###  Usage

Run the program:

```bash
python main.py
```

Then enter your RNA sequence, for example:

```
Enter RNA sequence (A,U,G,C only): GGCAGUACCAAGUCGCGAAAGCGAUGGCCUUGCAAAGGGUAUGGUAAUAAGCUGCC
```

Output:

```
==== RNA Folding with Nussinov-Jacobson Algorithm ====

--- Results ---
RNA Sequence:        GGCAGUACCAAGUCGCGAAAGCGAUGGCCUUGCAAAGGGUAUGGUAAUAAGCUGCC
Predicted Structure: (((.(((((((((((((....)).)))).)))(...)).)))(((...)..)))))
Max Base Pairs:      20

Compare this structure manually to:
 • mfold predicted structure
 • experimental (NMR) structure

You can visualize the structure at: https://rna.tbi.univie.ac.at/forna/
```

---

### 🔬 Comparison and Evaluation

* **mfold** and **Vienna RNA** predict folding using energy minimization.
* **Nussinov–Jacobson** maximizes base pairing count (simpler but less precise).

For comparison:

1. Generate mfold output at [mfold RNA server](http://www.unafold.org/mfold/applications/rna-folding-form.php).
2. Compare your dot-bracket structure manually or using the **RNAdistance** tool from the **Vienna RNA package**:

   ```bash
   RNAdistance mfold_structure.txt nussinov_structure.txt
   ```

---

###  Example Biological Sequence

The sequence used for validation:

```
GGCAGUACCAAGUCGCGAAAGCGAUGGCCUUGCAAAGGGUAUGGUAAUAAGCUGCC
```

Represents the **P5abc subdomain** of the *Tetrahymena thermophila* ribozyme.
The NMR reference structure is available in **Figure 2 (left)** of the provided paper.

---
