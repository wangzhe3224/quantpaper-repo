# Chapter 23: Stock Returns Information from the Stock Options Market

**By Swastik Tiwari and Hardik Agarwal**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

In finance, an option is a financial derivative that represents a contract sold by one party (the option writer) to another party (the option holder), giving the buyer the right, but not the obligation, to buy or sell an underlying asset or instrument at a specified "strike price" on or before a certain date. The seller has the corresponding obligation to fulfill the transaction -- that is, to sell or buy -- if the option holder exercises the option. The buyer pays a premium to the seller for this right. Because call options give the option to buy at a certain price, the buyer wants the underlying asset or instrument to go up in price. And because put options give the option to sell at a certain price, the buyer wants the underlying asset or instrument to go down in price. Speculators use options to make leveraged bets on the underlying assets, while hedgers use options to reduce the risk of holding them.

The equity options market provides a lot of useful information for seeking to predict stock returns. Equity options contribute to price discovery because they allow traders to align their strategies more precisely with the sign and magnitude of their information. The leverage in equity options, combined with this alignment, creates an additional incentive for traders to invest time and money in research to generate private information. In this way, trades in equity options may provide more refined and precise signals of an underlying asset's value than trades in the asset itself. Understanding how and why equity options affect price discovery is therefore vital to understanding how information is incorporated in asset prices.

Equity options are becoming increasingly popular with both retail and institutional investors. There are currently 15 options markets in the US, run by BOX Holdings Group, Cboe Group, Miami International Holdings, Nasdaq, and the Intercontinental Exchange's NYSE.

In its 2014 annual report, Options Clearing Corp. (OCC) presented the statistics and charts shown in Figures 23.1--23.3.

<!-- Figure 23.1: Options cleared and daily contract volumes 2010-2014. Source: © 2018, The Options Clearing Corporation. Used with permission. All rights reserved. -->

<!-- Figure 23.2: Options daily call and put volumes 2010-2014. Source: © 2018, The Options Clearing Corporation. Used with permission. All rights reserved. -->

<!-- Figure 23.3: Options open interest and contracts exercised 2010-2014. Source: © 2018, The Options Clearing Corporation. Used with permission. All rights reserved. -->

## Volatility Skew

A useful source of information on the direction of the options market is the implied volatility of stock options. This is the value for the volatility of the underlying instrument such that, when the value is input in an option pricing model (such as Black--Scholes), the model will return a theoretical value equal to the current market price of the option. In the case of equity options, a plot of the implied volatility against the strike price gives a skewed surface. The volatility skew is the difference in implied volatility between out-of-the-money, at-the-money, and in-the-money options. The volatility skew is affected by sentiment and supply--demand relationships, and provides information on whether fund managers prefer to write calls or puts. In equity options markets, a skew generally occurs because money managers, on the whole, would rather write call options than put options, as can be seen in Figure 23.4.

<!-- Figure 23.4: Sample volatility skew in equity options markets -->

In their paper "Option Prices Leading Equity Prices: Do Option Traders Have an Information Advantage?" Jin et al. (2012) survey the existing literature on the information advantage, including Bollen and Whaley (2004), Bradshaw et al. (2010), Garleanu et al. (2009), Van Buskirk (2011), and Xing et al. (2010). Bollen and Whaley and Garleanu et al. attribute the "shape of observed volatility skew and its predictive ability to the buying pressure due to the information possessed by option traders." Bollen and Whaley find that "contemporaneous changes in daily implied volatilities are driven by changes in net buying pressure." Options traders with expectations of positive news create an excess of buy-call trades and/or sell-put trades, which causes prices and implied volatilities of call options, relative to put options, to rise. Similarly, options traders with expectations of negative news create an excess of sell-call trades and/or buy-put trades, which causes the prices and implied volatilities of put options, relative to call options, to rise. Thus, when options traders expect information about the probability of a negative event, the demand for out-of-the-money put options increases relative to the demand for at-the-money call options, thereby increasing the volatility skew.

Researchers have shown that there is a negative association between volatility skews and individual stock returns at the company level. This finding is consistent with the hypothesis that volatility skews reflect negative information. Xing et al. (2010) state that the "greater the volatility skew in the traded options of the stock, [the] higher the underperformance." They calculate the underperformance of the underlying stocks of options with higher skews relative to the underlying stocks of options with lower skews as 10.9% per year on a risk-adjusted basis. In a long--short equity alpha, this implies taking a long position on stocks whose options have lower volatility skews and a short position on stocks whose options have higher volatility skews. A few recent studies have examined the predictive ability of volatility skews for extreme negative events. Van Buskirk (2011) finds that high volatility skews predict negative jumps over short windows containing earnings announcements and over longer windows containing no earnings announcements, but do not predict negative jumps around management earnings forecasts or dividend declarations. Bradshaw et al. (2010) show that the "predictive abilities of volatility skews and accounting opacity for crash risks are incremental to each other." According to the authors, although the information advantage as reflected in the predictive ability of volatility skews is greater for negative news than for positive news, the predictive ability of the options market applies to news surprises of a range of magnitudes. This phenomenon can be used to find stocks to short long--short equity alphas on longer and shorter time scales.

<!-- Figure 23.5: Performance of alpha on the Russell 1000 stock universe using volatility skew (2012-2017) -->

Alpha = -(change in slope of the implied volatility curve).

Figure 23.5 shows the performance of an alpha on the Russell 1000 universe of stocks. The alpha uses the slope of the implied volatility curve to measure the skew. The idea is to buy stocks that have shown a decrease in the slope of the implied volatility curve (or decrease in volatility skew), and vice versa.

## Volatility Spread

The put-call parity relation states that in perfect markets, the following equality holds for European options on non-dividend-paying stocks:

<!-- Formula: C - P = S - D·K -->

where C and P are the current call and put prices, respectively; D is the discount factor; K is the strike price; and S is the spot price. For US options, which allow early exercise, the equation takes the form of an inequality: S - D·K ≤ C - P. From these relations, it can be shown that European call and put options with the same strike price and maturity date should have the same implied volatilities, while the US call and put options should have a spread in the implied volatilities ("volatility spread") attributable to the early-exercise premium (Hull 2008).

However, Ofek et al. (2004) show that the volatility spread cannot be entirely explained by the early-exercise premium. Ofek et al. and Cremers and Weinbaum (2010) demonstrate that this volatility spread implies future stock returns. For example, Cremers and Weinbaum find that stocks with high volatility spreads outperform those with low volatility spreads by 50 basis points per week, on average. Bollen and Whaley (2004) and Garleanu et al. (2009) attribute the "predictive ability of volatility spreads to the demand-based option models." Higher volatility spreads indicate greater excess demand for call options than for put options, suggesting that options traders may possess expectations about positive news. Thus, the volatility spread can be considered as indicative of the nature (positive or negative) and potential impact of the news expected by the options traders, by measuring the overall net buying pressure in the options market. This phenomenon can be used in an equity alpha to go long stocks with high volatility spreads and short those with low volatility spreads.

<!-- Figure 23.6: Performance of an alpha on the Russell 3000 stock universe using volatility spread (2010-2016) -->

Alpha = implied volatility of at-the-money (call options - put options).

Figure 23.6 shows the performance of an alpha on the Russell 3000 universe of stocks. The alpha uses implied volatility information of at-the-money call and put options. The idea is to buy stocks with higher call-implied volatility than put-implied volatility, and vice versa.

## Options Trading Volume

The trading volumes of stock options can also carry useful information about future stock returns. In their paper "The Option to Stock Volume Ratio and Future Returns" Johnson and So (2011) focus on the inferences that can be drawn from the trading volumes of options and their underlying stocks. The authors provide theoretical and empirical evidence that O/S -- the ratio of the total option market volume (aggregated across calls and puts) to the total equity market volume -- is indicative of the private information available to informed traders. The O/S measure was first coined and studied by Roll et al. (2009), whose findings state that "cross-sectional and time-series variation in O/S may be driven by the trades of informed traders in possession of private information." As an extension of these findings, Johnson and So examine the relationship between O/S and future returns, and find outperformance of low O/S companies over high O/S companies. Their methodology involves sorting companies by O/S at the end of each month and computing the average return of a portfolio consisting of a short position in high O/S stocks and a long position in low O/S stocks, holding this portfolio for one month. This portfolio provides an average risk-adjusted monthly hedged return of 1.47%. The authors attribute the negative relationship between O/S and future equity returns to short-sale costs in the underlying equity markets: because of capital constraints and equity short-sale costs, informed traders prefer to trade options more frequently when they expect negative news than when they expect positive news.

According to Johnson and So (2011), "O/S predicts earnings surprises, standardized unexplained earnings, and abnormal returns at quarterly earnings announcements in the following month." The same O/S-measure-based portfolio construction methodology also contains information about future earnings announcements that occur in the month subsequent to the "holding month." They contend that this is consistent with the hypothesis that O/S reflects private information that is incorporated into equity prices when the news becomes public. Furthermore, they state that their model "also predicts that O/S is a stronger signal when short-sale costs are high or option leverage is low" and confirm this in the data. These ideas can be used to go long low O/S companies and short high O/S companies in a long--short equity alpha.

<!-- Figure 23.7: Performance of an alpha on Russell 1000 stock universe using option-to-stock-volume ratio (2011-2017) -->

Alpha = stock trading volume / (call + put option trading volume).

Figure 23.7 shows the performance of an alpha on the Russell 1000 universe of stocks. The alpha uses option volume information from Nasdaq OMX PHLX and compares it with average daily stock volume. The idea is to buy stocks that have a high ratio of stock volume to option volume, and vice versa.

## Option Open Interest

Open interest is the number of outstanding options contracts on a given underlying asset. In their paper "Do Option Open-Interest Changes Foreshadow Future Equity Returns?" Fodor et al. (2010) examine the relationship between option open-interest changes and future returns. They show that options traders buy relatively more (fewer) call (put) options when they are near-term bullish on the underlying asset. Similarly, options traders buy relatively more (fewer) put (call) options when they are near-term bearish on the underlying asset. Because of this behavior, changes in aggregate open interest contain information about future equity returns. The authors assert that informed investors leverage their bullish (bearish) views through increased long call (put) positions.

In their empirical investigation, the authors demonstrate a strong negative relationship between recent changes in aggregate put open-interest levels and future underlying equity returns. Companies with increases in recent put open interest significantly underperformed companies with decreases in put open interest. The authors find that an opposite but much weaker relationship exists for the call open-interest changes. They note that the ratio of the recent changes in call open interest to put open interest is the most effective predictor of future equity returns and that this relationship is positive in the sense that large increases in the ratio tend to be followed by relatively strong future equity returns.

Fodor et al. demonstrate the documented preference of informed traders, as first discussed by Black (1975), to leverage their views through options (bullish views through long call positions and bearish views through long put positions) because of the relatively small initial outlay requirements. Fodor et al. present further evidence that real-world informational differences between the options and equity markets result in differences in the rates at which information gets incorporated into prices in the respective markets. The open interest in equity call and put options can thus be used to select long and short stocks in a long--short equity alpha.

<!-- Figure 23.8: Performance of alpha on the Russell 3000 stock universe using call and put open interest (2010-2016) -->

Alpha = open interest of call options / open interest of put options.

Figure 23.8 shows the performance of an alpha on the Russell 3000 universe of stocks. The alpha uses call and put option open-interest information from PHLX. The idea is to buy stocks with higher call open interest compared with put open interest, and vice versa.

## Conclusion

As shown in the extensive research literature, equity options markets contain useful information to seek to predict stock movements. The shape of the volatility skew, the volatility spread, the options trading volume, and the options open interest are all useful tools for predicting near-term performance of the underlying stock.
