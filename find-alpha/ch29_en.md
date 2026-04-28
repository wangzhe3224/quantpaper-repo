# Chapter 29: ETFs and Alpha Research

**By Mark YikChun Chan**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

Exchange-traded funds (ETFs) are investment funds that are traded on stock exchanges. Most of them track an index, such as a stock or bond index; the first such fund, SPDR S&P 500 ETF Trust (SPY), was created in 1993 to track the S&P 500 index. Since then, the ETF universe has expanded rapidly. Today the underlying assets held by ETFs span a broad spectrum that includes not only equities but also bonds, commodities, currencies, and more.

According to research firm ETFGI, as of the end of October 2018 there were 5,785 ETFs and 7,616 exchange-traded products (ETPs) globally, with assets under management (AUM) of $4.78 trillion and $4.94 trillion, respectively (see Figure 29.1). Although the US market has dominated these vehicles -- with 1,966 ETFs and 2,210 ETPs, and assets of $3.42 trillion and $3.50 trillion, respectively -- the ETF markets in Europe, Asia, and Canada also have experienced steady growth. The huge rise in assets has come with proliferating liquidity, making the instruments more attractive to investors.

<!-- Figure 29.1: Global ETF growth, 2008-2018. Source: ETFGI. ETFGI, based in London, is a leading independent research and consultancy firm covering trends in the global ETF/ETP ecosystem. -->

Undoubtedly, ETFs are an emerging asset class, but the more intriguing questions are, first, whether they can become a new source of alphas, and, second, how we can seize the opportunity to seek profits. This chapter will start with a review of the basics, highlighting some benefits and risks of trading these instruments. Next, it will shed light on some of the possibilities in the ETF space and examine some examples of alphas or market phenomena that have been suggested by other analysts in their publications. Last but not least, it will discuss some unique potential challenges in ETF alpha research.

## Merits of Investing in ETFs

ETFs are traded by different kinds of investors in the markets. Some investors are relatively long term, using the funds simply for index investing; others are more active traders, seeking alphas or profits over a shorter term. ETFs have demonstrated remarkable attractiveness to all, as evidenced by their growing popularity and increasing trading volume. Some of their chief advantages for investors are:

- **Exchange trading:** Unlike mutual funds, which can be bought or sold only at the end of each trading day at their net asset value (NAV), ETFs experience price changes throughout the day and can be traded as long as the market is open. This allows active traders to implement intraday strategies or even exploit arbitrage opportunities. ETFs enjoy other stocklike features, such as short-selling, the use of limit orders and stop-loss orders, and buying on margin.

- **Low costs:** In general, ETFs incur lower costs (expense ratio < 1%) compared with traditional mutual funds (1--3%), benefiting all investors. For instance, SPY's expense ratio is 0.09%, and those of some others, such as Schwab US Broad Market ETF (SCHB), are as low as 0.03%. One reason for such low expense ratios is that many ETFs are index funds that are not actively managed -- hence they are relatively simple to run. Also, ETFs do not need to maintain a cash reserve for redemptions.

- **Tax efficiency:** Taxable capital gains are created when a mutual fund or ETF sells securities that have appreciated in value. However, as most ETFs are passive index funds with very low turnover of the portfolio securities (most trading happens only for index rebalancing), they are highly tax efficient. More notably, ETFs have a unique creation and redemption mechanism: only authorized participants (APs) -- large, specialized financial institutions -- can create or redeem ETF shares. When a holder wants to sell an ETF, he just sells it to other investors, like a stock. Even when an AP redeems shares of an ETF with the issuer, the issuer simply pays the AP "in kind" by delivering the underlying holdings of the ETF. In either case, there is no capital gains transaction for the ETF.

- **Transparency:** The underlying holdings of each ETF are disclosed to the public daily. In contrast, mutual funds need to make such disclosures on a quarterly basis only.

- **Market exposure and diversification:** The wide range of available ETFs enables investors to easily achieve their desired market exposures -- for example, to the broad market, specific sectors, markets in foreign countries, bond indexes, commodities, and currencies. Such variety makes it possible for short-term alpha traders to do statistical arbitrage across instruments. At the same time, a broad-based index ETF itself can be considered a well-diversified investment for some longer-term investors.

## Risks Behind These Instruments

Risk is always a big topic in investment, and it is hard to give an exhaustive list of the risks behind the diverse ETF instruments. The following section will seek to shed light on some notable examples of the risks, as well as other interesting features that may complicate risk evaluation. These risks include:

- **Tracking errors:** Sometimes ETF providers may not be able to fully replicate the performance of the underlying index, giving rise to tracking errors. (This term should not be confused with the premium/discount, which is defined as the difference between an ETF's market price and its NAV.) Such errors often adversely affect long-term index tracking but may potentially give rise to alpha or even arbitrage opportunities for active traders. In general, liquid broad-market equity ETFs like SPY have few tracking errors because they hold a large number of underlying stocks, each of which is liquid. The tracking error issue tends to be more substantial for some futures-based ETFs (which can suffer from negative roll yields) and commodity ETFs, as well as their inverse and/or leveraged counterparts.

- **Inverse or leveraged ETFs:** By using various derivatives and financial engineering techniques, some ETFs are constructed to achieve returns that are opposite and/or more sensitive to the price movements of the underlying securities. The common types of these ETFs are leveraged (2x), triple leveraged (3x), inverse (-1), double inverse (-2x), and triple inverse (-3x). Under volatile market conditions, the rebalancing of these leveraged ETFs may incur significant costs. Also, these instruments are by nature more volatile than nonleveraged ETFs and therefore must be handled with care in a multi-instrument (long-short) portfolio.

- **Factor risk heterogeneity:** ETFs of various asset classes innately take different types of exposure and hence have different factor risks. Equity ETFs generally have considerable market beta. Meanwhile, sector-, country-, or region-specific equity ETFs have risk exposure to their corresponding sectors, countries, or regions. Some ETFs designed for volatility trading are also usually classified as equity ETFs, but they have unique behaviors or characteristics because of their exposure to the CBOE Volatility Index (VIX) or, more precisely, the S&P 500 VIX Futures indices. Bond ETFs make up the second-largest group of ETFs in the US markets. They essentially hold a portfolio of debt securities ranging from Treasury bonds to high-yield corporate bonds, thereby bearing the respective dollar duration or interest rate risks. Commodity ETFs and currency ETFs face corresponding factor risks based on their underlying securities; those can be driven by numerous macro factors.

- **Capacity constraints:** As the ETF industry is booming, with ever-greater AUM, the capacity of an ETF should not be overlooked. This issue is particularly noteworthy for popular equity ETFs targeting niche areas. In April 2017, VanEck Vectors Junior Gold Miners ETF (GDXJ), which focuses on small- and midcap companies in the gold and silver mining industries, attracted so much capital inflow that it ended up suspending creation orders (and later altering the composition of the underlying index) because the ownership in some of its underlying securities was reaching the 20% threshold, beyond which automatic takeover laws would be triggered. In other words, an ETF can grow too big for its index and, consequently, fail to hold the underlying securities according to its investment mandate, resulting in a suspension of share creation and/or significant tracking errors.

- **Separation from underlying markets:** As mentioned above, an ETF can be bought or sold at its market price throughout the trading day. Many US-listed ETFs track foreign stock markets, but what would happen if the underlying markets closed? Chances are the ETFs could still trade on their own exchanges, not being directly affected. Such incidents happen not only when the underlying local markets have holidays but also occasionally because of trading halts, as experienced by VanEck Vectors Egypt Index ETF (EGPT) in January 2011 and iShares MSCI Brazil Capped ETF (EWZ) in May 2017. One could reasonably argue, however, that such ETFs became useful price discovery tools when the local markets were halted.

## Alpha Opportunities

The huge number and wide variety of ETF instruments, together with the availability of different datasets, make it possible to find alphas and take statistical arbitrage in a manner similar to equities: coming up with an idea, designing a numerical alpha formula, assigning alpha values to the ETF instruments, and then performing neutralization across the market or certain instrument groups. In addition, with ETFs tracking the performance of specific sectors, countries, and regions -- as well as bond indices and commodities -- ETF alphas can achieve better utilization of many macro indicators and data.

As with equities, the possible alpha ideas for ETFs span an array of categories. Among the most commonly discussed concepts are price momentum and seasonality. The following is a review of some examples from the literature.

### 1. US Sector Momentum Strategy

Samuel Lee proposed this idea in a Morningstar ETFInvestor newsletter (2012). It starts by defining a universe of 10 sector ETFs (Table 29.1).

<!-- Table 29.1: Sector ETFs. XLY - Consumer Discretionary Select Sector SPDR Fund; XLP - Consumer Staples Select Sector SPDR Fund; XLE - Energy Select Sector SPDR Fund; XLF - Financial Select Sector SPDR Fund; XLV - Health Care Select Sector SPDR Fund; XLI - Industrial Select Sector SPDR Fund; XLB - Materials Select Sector SPDR Fund; XLK - Technology Select Sector SPDR Fund; XLU - Utilities Select Sector SPDR Fund; IJR - iShares Core S&P Small-Cap ETF. -->

Comparing the last close price of each ETF against its 12-month simple moving average (SMA), the momentum strategy considers only those funds that are trading above their SMAs. It then holds equal positions on as many as three ETFs with the best 12-month returns. If fewer than three ETFs meet the criterion, the missing positions are replaced with cash. A comparison between the historical PnLs of this strategy and those of holding S&P 500 is shown in Figure 29.2.

<!-- Figure 29.2: US sector momentum strategy versus S&P 500. Source: Seeking Alpha. -->

To capture the "alpha," we can take an equal-sized short position on SPY, which will give us a long-short-balanced market-neutral (and dollar-neutral) alpha. The alpha's backtested performance for the 10 years from 2004 through 2013 is shown in Figure 29.3.

<!-- Figure 29.3: Simulation result of the sector momentum alpha from January 2004 to December 2013. -->

Interestingly, the alpha performed best around the 2008 financial crisis because the sectors selected outperformed the broad market. Yet without the market beta, the returns have become much less seductive -- only about 2.92% per annum; at this stage, the Sharpe ratio of this alpha is only about 0.38. Enhancing the signal would require further research effort. As Lee noted, this simple strategy was not well diversified and therefore should be used only as part of a broader portfolio.

### 2. Seasonality

Seasonality is a well-known phenomenon in the global securities markets. In US equities, there is a "sell in May and go away" theory that has worked well over many years. In essence, it tells us that US stock markets historically have tended to underperform in the period from May to October relative to the period from November to April.

Some examples in the literature also illustrate such seasonal patterns in equities in other regions. In an article on the Seeking Alpha website, Fred Piard (2016) suggested that the stock markets in Germany, Singapore, and Brazil were good examples of this phenomenon and that the corresponding country ETFs -- namely, iShares MSCI Germany ETF (EWG), iShares MSCI Singapore ETF (EWS), and iShares MSCI Brazil ETF (EWZ) -- could be used to take advantage of the seasonal tendencies.

To better explain the idea, we simulate and compare two long-only portfolios (see Figure 29.4):

1. Long equities only, holding equal long positions in SPY, EWG, EWS, and EWZ all the time.
2. Equity and bond rotations, holding equal long positions in SPY, EWG, EWS, and EWZ from November to April and equal long positions in popular bond ETFs -- say, iShares Barclays 20+ Year Treasury Bond ETF (TLT) and iShares iBoxx $ High Yield Corporate Bond ETF (HYG) -- from May to October.

<!-- Figure 29.4: Simulation results of two long-only portfolios from January 2006 through June 2017. Long equities only vs. Equity and bond rotations. -->

By staying away from equities from May to October, the equity-and-bond-rotation portfolio outperformed the long-equities-only portfolio. Most notably, the Sharpe ratio almost doubled, from 0.40 to 0.77, while the maximum drawdown was reduced by half.

Seasonal trends appear not only in equities but also in various commodities. Investopedia (Picardo 2018) describes the tendency of gold to gain in September and October, which can be captured by using gold ETFs. On his website, financial engineer Perry Kaufman (2016) has delineated several classic seasonality examples in agricultural products and their related ETFs.

Frankly, the seasonality phenomena discussed so far are more like market-timing tricks than practical hedged alpha ideas. Nonetheless, by studying such patterns one may come up with interesting technical or macro indicators, which, in turn, can be implemented as alphas to capture statistical arbitrage across some correlated instruments.

## Challenges in ETF Alpha Research

From the diverse pool of ETF instruments, researchers can apply their quantitative techniques to different datasets and make use of their creativity to test ideas and seek more alphas. Yet the emerging opportunities in this space come with many new challenges.

Among other factors, the liquidity of the instruments should be of particular concern. In the US markets, the aggregate average daily trading volume (ADV) in dollar terms of all ETFs was about $93 billion as of November 2018, accounting for almost 30% of all trading on the exchanges. Nonetheless, the actual liquidity may not be as good as it sounds because of the highly skewed distribution of the ADV values. Taking a closer look, SPY alone represented about 25% of the aggregate trading volume of all US ETFs, and the top 10 liquid ETFs (including SPY) represented about 50% of that. In other words, the actual tradable universe for a robust alpha is likely only a small subset of the thousands of ETFs in the markets.

After filtering based on liquidity, another tricky issue in defining an ETF universe is that many of the funds have highly similar counterparts. For instance, apart from SPY, ETFs like iShares Core S&P 500 ETF (IVV) and Vanguard S&P 500 ETF (VOO) also track the S&P 500. It does not make much sense for a daily or even an intraday (e.g. based on five-minute intervals) alpha to assign opposite values to these almost identical instruments because the room for arbitrage, if any, at such frequencies is not likely to cover the transaction costs.

A further complication is the presence of many inverse or leveraged ETFs. Imagine an extreme scenario in which an alpha has a long position in SPY and a short position in ProShares Short S&P 500 (SH), which gives the opposite of the daily performance of the S&P 500. Though the alpha may be dollar-neutral (long-short balanced), it essentially is taking two long positions in the S&P 500 simultaneously, resulting in pure market beta exposure. As such, the "dollar-neutral" alpha may not be as hedged as it ought to be if such inverse or leveraged instruments are not handled properly.

Eventually, the actual universe for alpha research in ETFs may be much smaller when compared with that of equities, thereby increasing the ease of overfitting and the risk of finding "fake" alphas. Consistent exposure to certain risk factors may generate high Sharpe performance. One example would be a purely short VIX strategy, such as taking a short position in iPATH S&P 500 VIX Short-Term Futures ETN (VXX) since its inception, which could achieve a Sharpe ratio of about 1.1 (see Figure 29.5).

<!-- Figure 29.5: Simulation result of the short VXX example from April 2009 to September 2018. -->

Exchange-traded funds have undergone rapid development over the past several years, with more-novel ETFs entering the universe of tradable liquid products. These instruments may exist only in the later part of the backtested period and hence adversely affect the reliability of the simulated in-sample performance. This is not a unique issue for ETFs, but it is a substantial one in this drastically growing investment area.

## Conclusion

The ETF is a rapidly developing investment vehicle whose rising popularity has been driven by the array of advantages it offers investors. However, the risk profile of strategies and portfolios trading ETFs can be very different from that of other asset classes, especially pure equities. The wide range of ETF instruments makes finding alphas a challenging yet appealing task. With the myriad possibilities, one has to be creative in generating trading ideas, while being cautious at every step of the alpha research process. However, many successful portfolio managers have shown strategies constructed with ETF alphas have the potential to generate PnLs with good Sharpe ratios and very low correlations with other strategies, and thus may add value to overall portfolios.
