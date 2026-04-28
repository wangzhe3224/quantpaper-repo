# Chapter 27: Intraday Trading

**By Rohit Kumar Jha**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

Intraday trading, also known as day trading, is speculation in securities — specifically, buying and selling financial instruments within the same trading day. Some of the more commonly day-traded financial instruments are stocks, options, currencies, and a host of futures contracts, such as equity index futures, interest rate futures, currency futures, and commodity futures. Strictly defined, all day-trading positions are closed before the market closes. Many traders, however, include day trading as one component of an overall strategy. Traders who trade intraday with the motive of profit are considered speculators rather than hedgers or liquidity traders. The methods of quick trading contrast with the long-term methods underlying buy-and-hold and value investing strategies.

It may seem quite unremarkable that a trader can buy and sell an instrument on the same day, but day trading is a relatively new concept. Although the practice can be traced back to 1867 and the creation of the first ticker tape, there were significant barriers to entry at that time, and as a result this type of trading was not popular among the general population. Day trading began to gain in popularity with the creation of electronic communication networks like Instinet in 1969 and the National Association of Securities Dealers Automated Quotation System, or Nasdaq, in 1971, as well as the abolishment of fixed commission rates in 1975.

An intraday alpha tries to time the entry and exit points of trades to make money on intraday price fluctuations. The switch from daily alpha research to intraday alpha research requires certain changes in style and approach. This chapter presents different styles of making intraday alphas, beginning with some fundamental differences in intraday alpha construction. Then we look into the pros and cons of day trading over daily trading. After that, we consider some different ways of making intraday alphas, followed by a few examples.

## Daily Trading versus Intraday Trading

A wide variety of information is available for making daily alphas, from sources ranging from corporate balance sheets to social media to weather data. Most of the information sources used in making daily alphas are useless in intraday research because their horizons are too long to be helpful. However, other information sources, including bid-and-ask snapshot prices, detailed order-book data, and other microstructure data, have predictive power for much shorter time horizons and thus are much more helpful for intraday research.

In general, as the analyst moves toward higher-frequency research, he has less diverse sources of information and data at his disposal. When doing daily research, an analyst is not that concerned about the performance of individual alphas in relation to cost because it is possible to cross many different alphas. But in intraday research, cost becomes a concern at the alpha level, owing to the lack of sufficiently diverse sources of information and the lower ability to net out different alphas. This will be touched upon below when the process of making an intraday alpha is explained.

Intraday research offers some significant advantages over daily research. Because it is possible to trade at much finer timescales, the performance and returns of intraday alphas are generally much higher. The statistical significance of intraday alphas for even shorter backtesting periods is much higher for intraday alphas than for daily alphas. As a result, the out-of-sample performance of the alphas is very similar to the performance in the backtesting period.

When making daily alphas, the analyst tries to keep the alphas neutral to all possible overnight risks, like dollar delta exposure, sector exposure, and similar risk factors. When we are working on intraday alphas, however, most of these risk factors are acceptable beneath a certain threshold, as it is possible to get out of those positions immediately if they go against the alpha. This provides an opportunity to use these risk factors to try to improve returns.

Liquidity is defined as the availability of an asset to the market. At any particular time, there is only so much volume being traded. In other words, there is limited liquidity at any time. If someone trades a significant fraction of the volume being traded at a given time, she runs the risk of moving the price herself, making it more difficult to execute the trade. Most tradable instruments don't have sufficient liquidity during the day to trade them frequently throughout the day. This restricts intraday trading to the most-liquid instruments in any region. In the US, for example, it's difficult to trade anything except the top 200–500 most liquid instruments. This, in turn, leads to smaller possible capital allocations on intraday strategies.

## Different Types of Intraday Alphas

There are different styles of intraday alphas. The classical definition of intraday alphas is that the alphas do not hold any overnight positions. Such alphas are called overnight-0 alphas. Similarly, overnight-1 alphas are those that hold positions overnight as well. In general, such alphas either hold unliquidated positions overnight or take the form of intraday overlays on overnight positions. In both overnight-0 and overnight-1 alphas, the alpha can either allocate positions continuously across different instruments or have a more discrete entry- or exit-based signal. In entry- or exit-based signals, the trade is entered based on an indicator or abnormal change in some derived statistics (called events) and the position is held until some exit triggers are met. These exit triggers can be a change in derived statistics or some stop-loss or profit-booking conditions.

When designing intraday alphas, an analyst needs to keep several constraints in mind. For one thing, liquidity is not the same throughout the day. It typically looks like Figure 27.1, with most trading happening at the start and the end of the day. Some stocks have very large slippage at the beginning of the trading day — for example, Microsoft Corp. (MSFT), as shown in Figure 27.2 — and in such cases it is generally a good idea to get into or out of positions in these securities when there is less slippage. Also, remember that not all financial instruments behave similarly, especially when we are working on intraday alphas for exchange-traded funds and futures. For many categories of ideas, the instruments need to be treated separately or in small groups of similar instruments.

<!-- Figure 27.1: Daily trading volume for Microsoft Corp. (MSFT) -->
<!-- Figure 27.2: Intraday spread profile for Microsoft Corp. (MSFT) -->

## Making an Intraday Alpha

The following is an example of a simple mean-reversion alpha. The analyst wants to capture the reverting nature of financial instruments. The alpha is defined as:

<!-- Formula: alpha = second_last_interval_close − last_interval_close -->

This is an overnight-0 continuous alpha on the top 500 liquid instruments. The positions are then neutralized by subtracting the cross-sectional mean, keeping each interval dollar neutral (equal long and short positions).

This idea can be improved by understanding it more deeply. This is a mean-reversion idea, and the analyst is trying to capture the tendency of instruments to revert to their mean positions. The instruments that are more volatile should have a higher tendency to revert. We can capture that in multiple ways. One way is presented below. Simply take the standard deviation of returns or price for the past 30–40 intervals and multiply the alpha value by the standard deviation:

<!-- Formula: alpha = (second_last_interval_close − last_interval_close) × std_close -->

This improves the margins, but it decreases the Sharpe ratio. It is important to understand why. Introducing the multiplying factor increases both the returns and the volatility of the alpha, but the volatility is in the denominator of the Sharpe ratio, and the net effect of these opposite forces is to lower the overall Sharpe.

An analyst could try to lower the volatility of the alpha as a whole as follows:

<!-- Formula: alpha = (second_last_interval_close − last_interval_close) / std_close -->

This lowers the volatility of the alpha and hence raises the Sharpe ratio, but it also significantly cuts the returns and margins.

The alpha design choices depend on the trader's requirements. The former version, with higher margins, would perform better after applying transaction costs. One can try variants of the same by using the cross-section rank of std(close) instead of the absolute values.

## Conclusion

Intraday trading is significantly different from daily trading, in which an analyst can gather information from a wide variety of sources. At the same time, certain pieces of information with short-term predictive power, such as bid-ask and other order-book-level information, which are mostly useless in daily trading, have significant potential value in intraday trading.

Intraday trading is hampered by the limited liquidity of most financial instruments, which restricts day traders generally to the most liquid of instruments. But the limited trading-book size is compensated for by the higher potential returns generated in intraday trading. Intraday alphas can be of different types, varying from pure intraday alphas that hold no overnight positions to hybrid daily-intraday alphas that hold overnight positions but boost returns with an intraday overlay.
