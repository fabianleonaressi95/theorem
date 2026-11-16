# MQM-1 — Discriminant analysis of Q6 morphodynamic configurations

**Classification:** [M] statistical method adapted from the supplied lecture; [N] numerical implementation and unit tests; [C] proposed data protocol; [O] physical interpretation and empirical regime discovery.

## 1. Purpose and evidence boundary

The supplied Italian lecture defines discriminant analysis as a supervised method: observations are assigned to groups a priori by a qualitative response variable, while quantitative explanatory variables assess separation and classify new observations. Its descriptive objective compares the prior partition with the partition induced by explanatory variables; its decision objective classifies a new observation while controlling classification error.

For MQM-1, this method tests whether independently defined dynamical regimes can be distinguished from finite Q6 configurations. It does not discover physically meaningful labels automatically. Regime labels must be defined before fitting, from separately documented dynamical criteria, and must not be generated from the same feature matrix being evaluated.

This is a statistical analysis layer. It does not change the MQM-1 evolution equations or establish a new physical law.

## 2. MQM-1 state and feature descriptor

The finite model has 64 Q6 vertices, 192 edges, logarithmic conductances x in R^192, a normalized state psi in C^64, and a fixed reference vector x_* in R^192. The Hamiltonian is H(x)=gamma B diag(exp(x)) B^T.

For one observation, the implementation constructs the real descriptor
[
Phi(x,\psi;x_*)=
(x-x_*,\ |\psi|^2,\ e^x\odot|B^T\psi|^2,\ \operatorname{eigvalsh}(H(x))).
]
An optional six-entry ternary descriptor s in {-1,0,+1}^6 can be appended. The default descriptor has 512 components; including the ternary block gives 518.

- x-x_* preserves deviations from the actual reference configuration.
- |psi_v|^2 gives vertex probabilities and is invariant under global phase.
- exp(x_e)|(B^T psi)_e|^2 is the edge response density in the geometry gradient.
- eigvalsh(H(x)) records the sorted Hamiltonian spectrum.
- The optional ternary block is not identified with the 64 binary Q6 vertices. No canonical map between 729 ternary six-tuples and Q6 is assumed.

This descriptor is a proposed starting choice. Feature ablation and redundancy analysis are required before interpretation.

## 3. A priori labels and sampling unit

Each row is one sampled configuration (x(t), psi(t)). The label y in {1,...,k} must be assigned by a separately documented rule. Candidate names such as stationary, transient, oscillatory, or unstable are not assumed to be established regimes; they become usable only after precise operational definitions are supplied.

The independent sampling unit is the trajectory, not an individual time sample. Nearby samples from one trajectory are dependent. Random row-wise train/test splitting is therefore not an acceptable primary validation procedure. The implementation provides leave-one-trajectory/group-out validation.

## 4. Factorial discriminant analysis

For n observations with feature vectors z_i in R^p, group means g_r, and global mean g, define
[
W=\frac{1}{n-k}\sum_r\sum_{i:y_i=r}(z_i-g_r)(z_i-g_r)^T,
\quad
B=\frac1n\sum_r n_r(g_r-g)(g_r-g)^T.
]
Fisher directions maximize
[
J(u)=\frac{u^TBu}{u^TWu},\qquad Bu=\lambda Wu.
]
There are at most k-1 nonzero discriminant directions. Eigenvalues quantify separation under this criterion; they are not physical frequencies or energies.

The feature dimension (512 by default) can exceed the number of independent trajectories. Explicit isotropic covariance shrinkage is therefore used before whitening. Report the shrinkage value and sensitivity to it.

## 5. Decision rules: pooled versus class-specific dispersion

The lecture presents the pooled Mahalanobis rule, based on a common within-class covariance, and the Sebestyen principle, which uses one inverse within-class covariance per group. The implementation exposes both:

- pooled: squared Mahalanobis distance using regularized pooled within-class covariance;
- Sebestyen-type: squared distance using the regularized covariance of each candidate class.

These are distance rules. Prior probabilities and Gaussian log-determinant terms are not silently added. Posterior-probability classification, if later required, must be implemented as a distinct model.

## 6. Anisotropy: what is and is not assumed

The current MQM-1 energy contains
[
\frac{\kappa}{2}\|x-x_*\|^2.
]
A nonuniform x_* is an anisotropic reference configuration, and x-x_* preserves it. However, this term has isotropic Hessian kappa I in x-coordinates. It does not define a general anisotropic metric tensor G_*.

Accordingly, this implementation does not invent an anisotropic metric or arbitrary edge weights. A separate positive-definite metric may be introduced only after derivation from an explicit RGS/PSU action or another independently justified geometric construction. Class-specific covariance distances are statistical dispersion metrics, not physical metrics.

## 7. Validation and reporting

The implementation includes leave-one-group-out validation. Every fold holds out all samples from one trajectory and trains on the remaining trajectories. Report at minimum:

1. number of independent trajectories and observations per class;
2. feature blocks and ablation results;
3. shrinkage parameter and sensitivity;
4. discriminant eigenvalues;
5. confusion matrix, per-class recall, balanced accuracy and overall accuracy;
6. results for pooled and Sebestyen-type distances;
7. held-out-trajectory results and, where possible, a separately generated parameter regime.

The lecture also describes hold-out, leave-one-out, and repeated resampling. For time-dependent MQM trajectories, leave-one-observation-out can leak information from adjacent samples. Grouped hold-out or grouped cross-validation is preferred.

## 8. Ternary representation

A six-entry ternary vector has 3^6=729 possible values. It is included only as an optional explanatory block when a well-defined mapping from the MQM configuration to six ternary line states is supplied. The 729 ternary states must not be conflated with the 64 vertices of binary Q6. The mapping, symmetry action, and physical meaning remain open proof obligations.

## 9. Reproducibility

Implementation: audits/morphodynamics/q6_discriminant.py.  
Tests: tests/test_mqm1_q6_discriminant.py.

Tests cover global-phase invariance, descriptor dimensions, ternary validation, the k-1 bound, separated synthetic classes, confusion-matrix orientation, and trajectory-grouped validation. Synthetic tests verify software behavior only; they are not evidence that MQM-1 has the proposed physical regimes.

## 10. Status and next proof obligations

- [N] A reusable finite-dimensional discriminant-analysis implementation is provided.
- [N] Synthetic unit tests verify basic numerical behavior.
- [O] No MQM-1 trajectory dataset with independently labelled regimes has yet been analysed.
- [O] The ternary-to-MQM state map is not defined here.
- [O] A physical anisotropic metric G_* has not been derived.
- [O] Statistical separability does not prove dynamical stability, causality, or a physical phase transition.

**Conclusion.** Discriminant analysis is formulated as a supervised diagnostic layer for MQM-1. It tests whether independently specified dynamical classes are distinguishable in Q6 state space; it cannot by itself define those classes or establish their physical interpretation.
