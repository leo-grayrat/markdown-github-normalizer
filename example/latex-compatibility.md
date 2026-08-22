# GitHub LaTeX / MathJax 兼容性示例

**中文** | [English](latex-compatibility.en.md)

这个页面用来直接观察 GitHub 当前的数学公式渲染能力。A 组是基础语法，B 组是常见 AMS 语法，C 组测试宏定义，D 组放已知对照项。

明确依赖额外扩展包的命令不作为本项目的 GitHub 兼容性问题。

---

# A. 基础语法

## A01 — 分式、根式、多层上下标

```math
\frac{a+b}{c+d}
+\sqrt{x}
+\sqrt[3]{x^2+y^2}
+x_{i_j}^{n+1}
+\frac{1}{1+\frac{1}{x}}
```

## A02 — 自动伸缩定界符与 `\middle`

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

## A03 — 重音、横线与箭头

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

## A04 — 上下括号

```math
\overbrace{a+b+c}^{\text{three terms}}
\qquad
\underbrace{x_1+x_2+\cdots+x_n}_{n\text{ terms}}
```

## A05 — 数学字体

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

## A06 — 间距命令

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

## A07 — 文本与盒子

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

## A08 — phantom 系列

```math
a+\phantom{x^2+y^2}+b
\qquad
a+\hphantom{x^2+y^2}+b
\qquad
a+\vphantom{\frac{x}{y}}+b
```

## A09 — 常见函数与极限

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

## A10 — 大型运算符

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

## A11 — 上下叠放

```math
\overset{!}{=}
\qquad
\underset{x\to 0}{\lim}
\qquad
\stackrel{\mathrm{def}}{=}
```

## A12 — Plain TeX 分式 / 组合式

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

# B. AMS 常见语法

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

## B03 — AMS 分式与组合数

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

## B05 — 长箭头

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

## B06 — AMS 关系与符号

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

## B07 — 矩阵家族

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

## B08 — 其他矩阵定界符

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

# C. 宏定义

## C01 — `\newcommand`

```math
\newcommand{\RR}{\mathbb{R}}
\RR^n
```

## C02 — 带参数的 `\newcommand`

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

# D. 已知对照项

## D01 — `\makebox`（此前实测失败）

```math
A \qquad \makebox[4em][r]{hello} \qquad B
```

## D02 — `\mbox`（此前实测正常）

```math
A \qquad \mbox{hello} \qquad B
```

## D03 — `\boxed` / `\fbox`（此前实测正常）

```math
\boxed{x+y}
\qquad
\fbox{hello}
```

---

## 本轮不判定的额外扩展

`physics`、`mathtools`、`cancel`、`mhchem`、`bbox`、`braket`、`amscd`、`bussproofs`、`html`、`gensymb`、`textcomp` 等额外扩展不纳入本页的 GitHub 基础兼容性判定。
