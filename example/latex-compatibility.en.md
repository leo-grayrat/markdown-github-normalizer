# GitHub LaTeX / MathJax Compatibility Example

[中文](latex-compatibility.md) | **English**

This page is for directly observing GitHub's current math-rendering capabilities. Group A covers base syntax, Group B common AMS syntax, Group C macro definitions, and Group D known controls.

Commands that clearly depend on extra extensions are not treated as GitHub compatibility issues for this project.

---

# A. Base syntax

## A01 — Fractions, roots, nested scripts

```math
\frac{a+b}{c+d}
+\sqrt{x}
+\sqrt[3]{x^2+y^2}
+x_{i_j}^{n+1}
+\frac{1}{1+\frac{1}{x}}
```

## A02 — Auto-sized delimiters and `\middle`

```math
\left(
\frac{a}{b}
\right)
\qquad
\left[
\frac{x+1}{x-1}
\right]
\qquad
\left\{
x \,\middle|\, x>0
\right\}
```

## A03 — Accents, bars, arrows

```math
\hat{x}
\quad
\widehat{ABC}
\quad
\bar{x}
\quad
\overline{AB}
\quad
\vec{v}
\quad
\overrightarrow{AB}
\quad
\widetilde{f}
```

## A04 — Overbrace / underbrace

```math
\overbrace{a+b+c}^{\text{three terms}}
\qquad
\underbrace{x_1+x_2+\cdots+x_n}_{n\text{ terms}}
```

## A05 — Math fonts

```math
\mathrm{ABC}
\quad
\mathbf{ABC}
\quad
\mathit{ABC}
\quad
\mathsf{ABC}
\quad
\mathtt{ABC}
\quad
\mathcal{ABC}
\quad
\mathbb{R}
\quad
\mathfrak{g}
\quad
\mathscr{F}
```

## A06 — Spacing commands

```math
a\,b
\quad
a\;b
\quad
a\:b
\quad
a\!b
\quad
a\quad b
\quad
a\qquad b
\quad
a\enspace b
\quad
a\hspace{1em}b
\quad
a\mkern3mu b
```

## A07 — Text and boxes

```math
\text{plain text}
\qquad
\mbox{mbox text}
\qquad
\fbox{fbox text}
\qquad
\framebox{framebox text}
\qquad
\boxed{x+y}
```

## A08 — Phantom commands

```math
a+\phantom{x^2+y^2}+b
\qquad
a+\hphantom{x^2+y^2}+b
\qquad
a+\vphantom{\frac{x}{y}}+b
```

## A09 — Common functions and limits

```math
\sin x
+\cos x
+\tan x
+\log x
+\ln x
+\exp x
+\det A
+\gcd(a,b)
+\lim_{x\to 0}\frac{\sin x}{x}
```

## A10 — Large operators

```math
\sum_{i=1}^{n} i
\qquad
\prod_{k=1}^{n} k
\qquad
\coprod_{i\in I} A_i
\qquad
\int_0^1 x^2\,dx
\qquad
\iint_D f(x,y)\,dx\,dy
\qquad
\iiint_V f\,dV
\qquad
\oint_C \mathbf{F}\cdot d\mathbf{r}
```

## A11 — Over/under stacking

```math
\overset{!}{=}
\qquad
\underset{x\to 0}{\lim}
\qquad
\stackrel{\mathrm{def}}{=}
```

## A12 — Plain TeX fraction / combination forms

```math
{a+b \over c+d}
\qquad
{n \choose k}
\qquad
{a \atop b}
```

## A13 — `array`

```math
\begin{array}{c|cc}
 & x & y\\
\hline
A & 1 & 2\\
B & 3 & 4
\end{array}
```

## A14 — `equation`

```math
\begin{equation}
E = mc^2
\end{equation}
```

## A15 — `eqnarray`

```math
\begin{eqnarray}
a & = & b+c\\
  & = & d+e
\end{eqnarray}
```

---

# B. Common AMS syntax

## B01 — `\operatorname`

```math
\operatorname{rank}(A)
\qquad
\operatorname{span}(v_1,\dots,v_n)
\qquad
\operatorname{diag}(a_1,\dots,a_n)
```

## B02 — `\DeclareMathOperator`

```math
\DeclareMathOperator{\rank}{rank}
\rank(A)
```

## B03 — AMS fractions and binomials

```math
\dfrac{a}{b}
\qquad
\tfrac{a}{b}
\qquad
\binom{n}{k}
\qquad
\dbinom{n}{k}
\qquad
\tbinom{n}{k}
\qquad
\cfrac{1}{1+\cfrac{1}{x}}
```

## B04 — `\genfrac`

```math
\genfrac{(}{)}{0pt}{}{n}{k}
\qquad
\genfrac{[}{]}{0pt}{1}{a+b}{c+d}
```

## B05 — Extensible arrows

```math
A \xrightarrow{f} B
\qquad
C \xleftarrow{g} D
\qquad
P \implies Q
\qquad
Q \impliedby P
\qquad
P \iff Q
```

## B06 — AMS relations and symbols

```math
a \because b
\qquad
a \therefore b
\qquad
x \nexists A
\qquad
A \subsetneq B
\qquad
B \supsetneq A
\qquad
x \lesssim y
\qquad
y \gtrsim x
```

## B07 — Matrix family

```math
\begin{matrix}
a & b\\
c & d
\end{matrix}
\qquad
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\qquad
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
```

## B08 — Other matrix delimiters

```math
\begin{Bmatrix}
a & b\\
c & d
\end{Bmatrix}
\qquad
\begin{vmatrix}
a & b\\
c & d
\end{vmatrix}
\qquad
\begin{Vmatrix}
a & b\\
c & d
\end{Vmatrix}
```

## B09 — `aligned`

```math
\begin{aligned}
f(x)
&= x^2+2x+1\\
&= (x+1)^2
\end{aligned}
```

## B10 — `cases`

```math
f(x)=
\begin{cases}
x^2, & x\ge 0\\
-x,  & x<0
\end{cases}
```

## B11 — `gathered`

```math
\begin{gathered}
a+b=c\\
d+e=f\\
g+h=i
\end{gathered}
```

## B12 — `split`

```math
\begin{split}
(a+b)^2
&= a^2+2ab+b^2\\
&= a(a+2b)+b^2
\end{split}
```

## B13 — `smallmatrix`

```math
A=
\left(
\begin{smallmatrix}
a & b\\
c & d
\end{smallmatrix}
\right)
```

## B14 — `substack`

```math
\sum_{\substack{1\le i\le n\\ i\text{ odd}}} i
```

## B15 — `tag`

```math
E = mc^2 \tag{mass-energy}
```

## B16 — `align`

```math
\begin{align}
a+b &= c\\
d+e &= f
\end{align}
```

## B17 — `gather`

```math
\begin{gather}
a+b=c\\
d+e=f
\end{gather}
```

## B18 — `multline`

```math
\begin{multline}
a+b+c+d+e+f+g+h+i+j\\
= k+l+m+n+o+p+q+r+s+t
\end{multline}
```

---

# C. Macro definitions

## C01 — `\newcommand`

```math
\newcommand{\RR}{\mathbb{R}}
\RR^n
```

## C02 — Parameterized `\newcommand`

```math
\newcommand{\vect}[1]{\mathbf{#1}}
\vect{x}+\vect{y}
```

## C03 — `\def`

```math
\def\foo#1{#1^2+1}
\foo{x}
```

## C04 — `\renewcommand`

```math
\newcommand{\mysym}{A}
\renewcommand{\mysym}{B}
\mysym
```

---

# D. Known controls

## D01 — `\makebox` (previously observed to fail)

```math
A \qquad \makebox[4em][r]{hello} \qquad B
```

## D02 — `\mbox` (previously observed to work)

```math
A \qquad \mbox{hello} \qquad B
```

## D03 — `\boxed` / `\fbox` (previously observed to work)

```math
\boxed{x+y}
\qquad
\fbox{hello}
```

---

## Extra extensions not judged here

Extra extensions such as `physics`, `mathtools`, `cancel`, `mhchem`, `bbox`, `braket`, `amscd`, `bussproofs`, `html`, `gensymb`, and `textcomp` are outside this page's baseline GitHub compatibility check.

---

# E. Additional controls

## E01 — `array` without `\hline`

```math
\begin{array}{c|cc}
 & x & y\\
A & 1 & 2\\
B & 3 & 4
\end{array}
```

## E02 — `array` + `\hline`

```math
\begin{array}{c|cc}
 & x & y\\
\hline
A & 1 & 2\\
B & 3 & 4
\end{array}
```

## E03 — Spacing commands: fenced `math`

```math
a\,b\;c
```

## E04 — Spacing commands: ordinary inline math

$a\,b\;c$

## E05 — Spacing commands: GitHub protected inline math

$`a\,b\;c`$

## E06 — `\operatorname`: fenced `math`

```math
\operatorname{rank}(A)
```

## E07 — `\operatorname`: ordinary inline math

$\operatorname{rank}(A)$

## E08 — `\operatorname`: GitHub protected inline math

$`\operatorname{rank}(A)`$
