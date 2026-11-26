# TSMR-C-I — I Ching / golden Q6 audit

This audit uses exact arithmetic in Z[lambda], lambda^2=1-lambda.

## Finite exact checks

- Trigram bits are read bottom-to-top; 1=yang and 0=yin.
- 100 is Zhen (Thunder); 011 is Xun (Wind/Wood).
- Their golden evaluations coincide: 1 = lambda + lambda^2.
- The eight trigram states yield seven scalar values.
- Six line states are the 64 hexagrams; single-line changes give Q6, degree 6 and 192 edges.
- The six-line golden evaluation yields 33 distinct scalar values.
- The partition into those 33 values is not equitable for Q6: 21 scalar classes contain states with different one-step transition profiles.

## What this does not establish

The finite collision count does not prove singularity or full support of an infinite measure. The 33 scalar values do not form a valid Markov quotient of Q6. Keep the 64-state Markov lift unless a smaller state representation is proved to preserve transition profiles.

The graph-directed measure built from the Q6 random walk is not the i.i.d. Erdős Bernoulli convolution. Its atomlessness, support, Fourier behavior, and multifractal spectrum remain open analytical questions.
