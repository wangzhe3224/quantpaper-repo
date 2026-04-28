# Chapter 8: Alpha Correlation

**By Chinh Dang and Crispin Bui**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

Alphas are evaluated by many different metrics, such as the information ratio, return, drawdown, turnover, and margin. These metrics are derived mainly from the alpha's profit and loss (PnL). For example, the information ratio is just the average returns divided by the standard deviation of returns. Another key quality of an alpha is its uniqueness, which is evaluated by the correlation coefficient between a given alpha and other existing alphas. An alpha with a lower correlation coefficient normally is considered to be adding more value to the pool of existing alphas.

If the number of alphas in the pool is small, the importance of correlation is low. As the number of alphas increases, however, different techniques to measure the correlation coefficient among them become more important in helping the investor diversify his or her portfolio. Portfolio managers will want to include relatively uncorrelated alphas in their portfolios because a diversified portfolio helps to reduce risk. A good correlation measure needs to identify the uniqueness of one alpha with respect to other alphas in the pool (a smaller value indicates a good uniqueness). In addition, a good correlation measure has the ability to predict the trend of movement of two alpha PnL vectors (time-series vectors). The correlation among alphas can be computed based on alpha PnL correlation or alpha value correlation.

## Alpha PnL Correlation

Given two alpha PnL vectors (we use bold letters for vectors):

**P**ᵢ = [ Pᵢ₁, Pᵢ₂, …, Pᵢₙ ] ∈ ℝⁿ

**P**ⱼ = [ Pⱼ₁, Pⱼ₂, …, Pⱼₙ ] ∈ ℝⁿ                                       (1)

where Pᵢₜ and Pⱼₜ denote the PnLs of the *i*th and *j*th alphas on the *t*th day, *n* is the number of days used to measure correlation, and superscript *T* denotes the matrix transposition. Note: tests usually select the number of days for correlation as two or four years instead of a full history, to save computational resources.

### Pearson Correlation Coefficient

The Pearson correlation coefficient, also known as the Pearson product-moment correlation coefficient, has no units and can take values from −1 to 1. The mathematical formula was first developed by Karl Pearson in 1895:

> r = cov(**P**ᵢ, **P**ⱼ) / (σ_Pᵢ · σ_Pⱼ)                              (2)

where cov(**P**ᵢ, **P**ⱼ) = E[**P**ᵢ · **P**ⱼ] − E[**P**ᵢ] · E[**P**ⱼ] is the covariance and σ_Pᵢ and σ_Pⱼ are the standard deviations of **P**ᵢ and **P**ⱼ, respectively. For two vectors of PnLs, the coefficient is computed by using the sample covariance and variances. In particular,

> r = Σₜ₌₁ⁿ (Pᵢₜ − P̄ᵢ)(Pⱼₜ − P̄ⱼ) / √[Σₜ₌₁ⁿ (Pᵢₜ − P̄ᵢ)² · Σₜ₌₁ⁿ (Pⱼₜ − P̄ⱼ)²]   (3)

The coefficient is invariant to linear transformations of either variable. If the sign of the correlation coefficient is positive, it means that the PnLs of the two alphas tend to move in the same direction. When the return on Pᵢ is positive (negative), the return on Pⱼ has a tendency to be positive (negative) as well. Conversely, a negative correlation coefficient shows that the PnLs of the two alphas tend to move in opposite directions. A zero correlation implies that there is no relationship between two PnL vectors. Figure 8.1 shows the variation of maximum correlation as a function of trading signals, using two years' worth of data.

<!-- Figure 8.1: Variation of maximum correlation as a function of trading signals. Scatter plot showing MaxCorr decreasing as the number of trading signals increases. -->

Alphas seek to make predictions about the future movements of various financial instruments. As a result, the analysis needs to be extended into a time series, which includes a sequence of random variables with the time index. In the case of an alpha PnL vector, the observation is the profit (+) or loss (−) of the alpha in one day. Below we briefly review the dot product, then discuss the temporal-based correlation.

### Temporal-Based Correlation

The dot (inner) product is defined as the sum of the products of the corresponding entries of the two sequences of numbers:

> **P**ᵢ · **P**ⱼ = |**P**ᵢ| · |**P**ⱼ| · cos(θ)                         (4)

where |**P**| is the modulus, or magnitude, of the PnL vector and θ is the angle between the two vectors. One important application of the dot product is to find the angle between two vectors because the angle can be found via:

> cos(θ) = **P**ᵢ · **P**ⱼ / (|**P**ᵢ| · |**P**ⱼ|) = Σₜ₌₁ⁿ Pᵢₜ · Pⱼₜ / √[Σₜ₌₁ⁿ Pᵢₜ² · Σₜ₌₁ⁿ Pⱼₜ²]   (5)

When the angle is zero, the two PnL vectors fall on the same line and cos(θ) = 1. When the angle is π/2, the vectors are orthogonal and cos(θ) = 0.

The temporal-based correlation considers each alpha's PnL vector as a time-series sequence and assigns weight to the values on each day. The correlation between two PnL vectors is thus defined as:

> r = Σₜ₌₁ⁿ wₜ · Pᵢₜ · Pⱼₜ / √[Σₜ₌₁ⁿ wₜ · Pᵢₜ² · Σₜ₌₁ⁿ wₜ · Pⱼₜ²]      (6)

Naturally, larger weights are assigned to recent PnL values (wₜ ≥ wₜ₊₁, t = 1, 2, …, n). For example, wₜ = 1/n, which is inversely proportional to the time index t. The formula transforms input pairs of vectors (**P**ᵢ, **P**ⱼ) into time-scaled vectors and then computes the angle between the two scaled vectors:

**P**'ᵢ = [ w₁Pᵢ₁, w₂Pᵢ₂, …, wₙPᵢₙ ] ∈ ℝⁿ

**P**'ⱼ = [ w₁Pⱼ₁, w₂Pⱼ₂, …, wₙPⱼₙ ] ∈ ℝⁿ.                       (7)

As a result, the temporal-based correlation still preserves many desirable aspects of the traditional dot product, such as commutative, distributive, and bilinear properties.

The Pearson correlation coefficient can be computed here for the two scaled vectors in Equation 7. We can see that the centered variables have zero correlation or are uncorrelated in the sense of the Pearson correlation coefficient (i.e. the mean of each vector is subtracted from the elements of that vector), while orthogonality is a property of the raw variables. Zero correlation implies that the two demeaned vectors are orthogonal. The demeaning process often changes the angle of each vector and the angle between two vectors. Therefore, two vectors could be uncorrelated but not orthogonal, and vice versa. For further information about linear independent, orthogonal, and uncorrelated variables, see Joseph Rodgers et al. (1984).

### Generalized Correlation

Data transformation can be an important tool for proper data analysis. There are two kinds of transformations: linear and nonlinear. A linear transformation (such as multiplication or addition of a constant) preserves the linear relationships among the variables, so it does not change the correlation among the variables. Below we will consider nonlinear transformations, which typically modify the correlation between two variables.

The two correlation formulas above compute correlation coefficients using daily PnL values. The generalized correlation creates a matrix **M**ₖₓₙ, then transforms the two PnL vectors to a different Euclidean space:

**Q**ᵢ = **M**ₖₓₙ · **P**ᵢ ∈ ℝᵏ

**Q**ⱼ = **M**ₖₓₙ · **P**ⱼ ∈ ℝᵏ.                                      (8)

The regular correlation now is computed in the transformed domain, with some additional features added by the transformed matrix **M**ₖₓₙ. If **M**ₖₓₙ = **I** (the identity matrix), we obtain the regular correlation scheme. Here we take a look at some other particularly useful transformations.

The weekly PnL correlation is computed for weekly instead of daily PnL vectors. In this case, *k* = *n*/5 and the transformation matrix becomes:

> **M**ₖₓₙ = (mᵢ,ⱼ), where mᵢ,ᵢ = 1 × 5 and *t* = 1, 5 and all other elements are zero.     (9)

The weekly correlation is usually higher than daily values, but it is another way to understand alphas. The monthly PnL correlation is computed using a similar approach.

The temporal-based correlation is another form of generalized correlation, corresponding to the square diagonal transformation matrix:

> **M**ₖₓₙ = (mᵢ,ⱼ), where mᵢ,ⱼ = wᵢ if i = j, and mᵢ,ⱼ = 0 otherwise.   (10)

Under this transformation, the input PnL vectors are transformed into time-scaled vectors, as in Equation 7.

The sign PnL correlation is another form of PnL vector correlation, in which the correlation is computed over the signs of the PnL values instead of the values themselves. The transformation matrix now is a data-dependent diagonal matrix and its element values depend on input PnL vectors. As a result, the input pairs (**P**ᵢ, **P**ⱼ) are transformed into the following form:

**Q**'ᵢ = [ sgn(Pᵢ₁), sgn(Pᵢ₂), …, sgn(Pᵢₙ) ] ∈ ℝⁿ

**Q**'ⱼ = [ sgn(Pⱼ₁), sgn(Pⱼ₂), …, sgn(Pⱼₙ) ] ∈ ℝⁿ                (11)

where sgn(*x*) is the sign (or signum) function and takes the values {−1, 0, 1}, corresponding to (negative, zero, positive) values of *x*.

## Alpha Value Correlation

Denote the alpha position vector on the *t*th day by:

> **α**ᵢ(*t*) = [ αᵢ₁(*t*), αᵢ₂(*t*), …, αᵢₘ(*t*) ] ∈ ℝᵐ          (12)

where *m* is the number of instruments, αᵢₖ(*t*) is (or is proportional to) the amount of money invested in the *k*th instrument, and Σₖ₌₁ᵐ αᵢₖ(*t*) is (or is proportional to) the total amount of money invested in the portfolio. It is sometimes useful to consider the alpha position vectors as well as the PnL vectors. In particular, portfolio managers often consider two correlation measures based on positions: the position correlation and the trading correlation.

The position correlation between two alphas over a period of *d* days is computed by forming the following two vectors:

> **α**ᵢ = [ **α**ᵢ(1), **α**ᵢ(2), …, **α**ᵢ(*d*) ] ∈ ℝ⁽ᵐˣᵈ⁾       (13)

> **α**ⱼ = [ **α**ⱼ(1), **α**ⱼ(2), …, **α**ⱼ(*d*) ] ∈ ℝ⁽ᵐˣᵈ⁾.

The trading correlation between two alphas over a period of *d* days is computed by forming the two difference vectors:

> Δ**α**ᵢ = [ **α**ᵢ(1) − **α**ᵢ(2), **α**ᵢ(2) − **α**ᵢ(3), …, **α**ᵢ(*d*) − **α**ᵢ(*d*+1) ] ∈ ℝ⁽ᵐˣᵈ⁾    (14)

> Δ**α**ⱼ = [ **α**ⱼ(1) − **α**ⱼ(2), **α**ⱼ(2) − **α**ⱼ(3), …, **α**ⱼ(*d*) − **α**ⱼ(*d*+1) ] ∈ ℝ⁽ᵐˣᵈ⁾.

Normally, it is enough to take *d* = 20 days, so the alpha vector is of dimension 20 × the number of instruments in the universe. If two alphas take positions on different universes of instruments, the intersection of the two universes is used for the calculations.

## Correlation with Alpha Pool

The above correlation methods are used for checking the correlation between two individual alphas. Naturally, given a pool of alphas, the maximum correlation has been used as a measure of the value added by a given alpha. As the number of alphas increases, the average correlation becomes more important than a single max correlation.

T-corr is defined as the sum of the correlations of the given alpha with all other alphas. The average correlation and T-corr provide additional powerful measures of alpha value addition, along with the max correlation.

A correlation density distribution is more important than a singular maximum value or even the average correlation value. Table 8.1 shows a sample histogram of correlation density (20 bins of size 0.1).

**Table 8.1: A histogram of correlation**

| Bins | cnt(%) | count_in_number |
|------|--------|-----------------|
| 0.9  | c9     | 0               |
| 0.8  | c8     | 0               |
| 0.7  | c7     | 0               |
| 0.6  | c6     | 0               |
| 0.5  | c5     | 0               |
| 0.4  | c4     | 167             |
| 0.3  | c3     | 5,102           |
| 0.2  | c2     | 70,294          |
| 0.1  | c1     | 283,436         |
| 0    | c0     | 438,720         |
| −0.1 | c_1    | 286,478         |
| −0.2 | c_2    | 36,889          |
| −0.3 | c_3    | 1,293           |
| −0.4 | c_4    | 59              |
| −0.5 | c_5    | 0               |
| −0.6 | c_6    | 0               |
| −0.7 | c_7    | 0               |
| −0.8 | c_8    | 0               |
| −0.9 | c_9    | 0               |
| −1   | c_10   | 0               |

Numerous features can be extracted from the histogram in addition to the maximum correlation and the average correlation. For example, the scaled average score of one alpha with the pool could be defined as:

> Score = Σⱼ₌₋₉⁹ cⱼ × j / 10                                              (where cⱼ is taken from Table 8.1)

The score ranges in [−1, 1], which increases if the number of alphas with positive correlation increases or the number of alphas with negative correlation decreases.

## Conclusion

We have surveyed several different approaches to evaluating the correlations between the PnLs and positions of alphas and pools of alphas. There are, of course, more statistical and less algebraic approaches to evaluate correlation, such as Spearman's rank correlation and the Kendall rank correlation. Within the scope of this chapter, we have covered only some of the most common methods for evaluating alpha correlation. PnL correlation can be evaluated over a longer period of time (2–4 years or longer) in comparison with alpha value correlation (which requires a short, recent period of time) because of the limitations of computational resources.

One reasonable idea often can be used to develop numerous alphas, depending on different techniques and datasets. Because they are developed using a single idea, these alphas have a tendency to be highly correlated. Sometimes there are instances when it is beneficial to combine some or all of these highly correlated alphas instead of selecting only one alpha and removing all others. Two alphas may have highly correlated historical performance, but the future is uncertain and it is not always clear which one may add more value in the future. Therefore, in terms of resource allocation for two high-correlation alphas (e.g. A and B), one can divide resources (not necessarily equally) between A and B instead of allocating all of the resources to a single alpha. A single alpha cannot fully describe every aspect of one idea, but each alpha represents that idea in a different way; hence, using all these alphas at once may provide a more complete view of the idea and make the overall strategy more robust.

The ultimate objective of alpha correlation is to find the true value of adding one new alpha, given a pool of existing alphas, which becomes increasingly important as the number of alphas grows toward the sky. Using multiple correlation approaches leads to a better understanding of the alpha signals in recent history as well as over a longer past period. An alpha based on a completely novel trading idea is generally unique and adds the most value to the alpha pool.
