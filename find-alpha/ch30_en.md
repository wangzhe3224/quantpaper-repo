# Chapter 30: Finding Alphas on Futures and Forwards

**By Rohit Agarwal, Rebecca Lehman, and Richard Williams**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

Finding alphas in the futures and currency forwards markets is an area of great practical interest. It also presents many challenges, some analogous to those in other markets, such as equities and exchange-traded funds, and some unique to these specific instruments. This chapter will discuss some of the techniques and ideas that have been useful in attacking these challenges over the past few years.

## Key Market Features

Futures are designed to give the trader exposure to price changes in an underlying asset without the cost of holding the equivalent position in that asset. Tradable futures markets include futures on equity indices, commodities, currencies, and bonds. In the context of alpha research, short-dated forwards on currencies provide a similar form of access to relative currency value exposures. This makes futures and forwards particularly convenient instruments for both hedgers and speculators, and gives rise to their most significant features.

## Underlying Factor Exposure

Because both futures and forwards give exposure equivalent to that of an underlying asset, it follows that the prices of the futures and forwards depend on the same factors that drive that asset. This simple observation has important implications. There are distinct groups of market traders who focus exclusively on particular sets of futures and currencies; the hedgers seek to control their exposure to the risks of particular factors.

Commodity futures provide a good example, as producers and consumers of physical commodities use futures to hedge their risk on specific commodities. Each group of traders can have its own characteristic risk limits, tolerances, and trading behavior, which in turn can give rise to qualitatively different market behavior. For example, the farmers and food-producing corporations that use the agricultural markets to control their risks have little in common with the airlines that employ energy futures to hedge their future fuel costs. As a result, in contrast to the equities universe, where the core liquid assets are all traded by the same population of investors for the same purposes, many properties are much less comparable across the entire universe of futures or forwards.

In recognition of the differences among market participants, many market-making and proprietary trading organizations have specialists managing the trading of different classes of futures and currencies, with the classes based on sets of similar underlying assets. This further reinforces the differences among "sectors," as different traders, desks, and business lines manage different futures and forwards. Because much of the correlation observed among assets in a common market is due to the common sentiment, behavioral biases, and practical constraints of the individuals and teams trading them, the correlations in the futures and forwards markets are generally much weaker than in the equities markets. It is interesting to note, however, that seemingly different asset classes become more correlated during periods of financial crisis.

## Consequences of Instrument Grouping

These instrument groups present both opportunities and challenges in seeking alphas. One of the most obvious challenges is that as we consider smaller groups of more closely connected instruments, we have fewer instruments that we can trade together in one alpha. All else being equal, the expected Sharpe ratio of an alpha is proportional to the square root of the breadth of the universe. The futures universe as a whole already contains many fewer instruments than the equity universe; when we segment the futures universe into relevant subsets, the universe for many alphas is even smaller — often between one and a few dozen instruments. Therefore, futures alphas require greater depth of information per instrument to achieve the same aggregate results than alphas on a larger instrument set. As the quality of the per-instrument alpha increases, it becomes more obvious to other market participants and its expected lifetime is reduced. Conversely, as we identify sets of more-similar instruments, we have higher expectations that any particular alpha should be present across the whole set. The cross-validation test of deleting each instrument in turn and retesting the identified relationship becomes more meaningful. Finding the right-size group on which to test our alpha candidates is therefore a key building block of alpha research.

Though generating alphas in these small and heterogeneous universes is definitely more difficult, the reward is the far greater liquidity in these markets. Robust alphas on liquid futures can be traded at large sizes without incurring the costs and regulatory risks of market impact.

## Basic Checklist for Alpha Testing

Starting from a core alpha idea, the first step is to identify the sectors where we expect it to appear and the timescales on which we expect it to manifest. As an example, consider the US energy market and an alpha based on the forecast of extreme weather in a major offshore US oil and gas field. Before we even look at the data, we can identify the instruments we expect will be relevant (oil, gas, and their products) and the timescale on which we expect the data to have an impact — in this case, the duration of a typical storm and the time it takes to stop and restart production. (There will be a range of views on both of these horizons, but we can still use the implied causal relationship between the extreme weather and the commodity supply to narrow the range of candidates.) We can now test our idea by gathering data on historical weather forecasts and price changes for the major energy contracts, and testing for association between the two datasets, using a partial in-sample historical dataset.

The next step is to fit a simple statistical model and test it for robustness, while varying the parameters in the fit. One good robustness test is to include a similar asset for comparison, where we expect the effect to be weaker. In the case of our weather alpha example, Brent crude oil would be a reasonable choice. Crude oil is a global market, so we would expect some spillover from a US supply disruption. However, oil delivered in Europe is not a perfect substitute for the US supply, so we would expect a diluted impact. Again, we can test this on in-sample data.

Having investigated the cases where we would expect the alpha to work, we can now test the converse: where do we expect there to be no relationship? In the case of our example, the core idea is quite closely targeted to one sector, so we would expect to detect no relationship if we retested it on other sectors, such as industrial metals or bond futures. This step is surprisingly good at finding incorrectly coded or specified statistical tests.

Depending on the results of our tests, we could now be in a position to test our idea on our out-of-sample dataset. With such a small set of instruments, the out-of-sample test becomes a crucial part of the process, helping to avoid unintentional overfitting.

The following phenomena and information sources are some of the most interesting and useful sources of alpha for futures traders.

## Follow the (Smart) Money

The Commitments of Traders (COT) report (Figure 30.1) is released every Friday by the Commodity Futures Trading Commission (CFTC). It can be extremely valuable to know what the "smart money" is betting on and then follow it. The report gives a breakdown of the open interest by different market participants, such as commercial traders (big businesses and producers), noncommercial traders (large speculators), and nonreportable traders (small speculators). More information on this report can be found at http://www.cftc.gov/marketreports/commitmentsoftraders/index.htm.

<!-- Figure 30.1: COT report on wheat as of November 13, 2018. Source: US Commodity Futures Trading Commission. -->

The value of the COT report is based on the premise that the trades of commercial traders tend to reflect their hedging needs, which may be uncorrelated or even negatively correlated with their views on the value of the assets, while speculators' trades express their views of the market. If speculators have access to relevant information, their trades may be predictive. When speculators exhibit trend-following and bandwagon effects, their trades may even be self-fulfilling. Consider the alpha idea to go long instruments with increasing open interest by speculators and short instruments with decreasing speculator open interest. This idea can be expected to work on assets in markets where speculators account for a significant proportion of the activity. It makes sense to compare speculator flow cross-sectionally across small groups of instruments — such as grain, energy, European currencies, or North American equity indices — that tend to be traded by the same speculators. The relevant time horizons for each asset group should be the most common time horizons for speculators in that group. This alpha should not work on groups of unrelated assets or assets with low speculator coverage. It also can be expected to fail if something unanticipated catches speculators by surprise; it may make sense to hedge or exit this alpha when a surprise is likely to happen — say, when a Federal Reserve meeting (for financial futures) or a crop report release (for agricultural futures) is scheduled.

## Seasonality in Markets

Seasonality is the tendency of markets to move in a given direction at certain times of the year. It is particularly prominent in the agricultural and energy commodity markets because of harvest patterns and heating and cooling cycles. But it is not restricted to agricultural and energy commodities; cyclical patterns in demand, consumption, inventory, or supply can give rise to similar behavior in other markets. A simple alpha can use the previous years' behavior to predict the current period. This alpha can be expected to work best on commodity futures and currencies, such as the Australian dollar (AUD), that are closely linked to commodities. It should also have some significance in equity markets that are driven by short-term consumer sentiment. It should be weakest on bonds and noncommodity currencies. The most likely time horizon is 1–3 months — short enough to pick up on the differences among seasons but long enough to average out the daily noise. Seasonal patterns can be expected to fail in the event of unusual shocks to supply or demand (such as unseasonable weather or a hurricane in the Gulf of Mexico for energy alphas) or to short-term sentiment (such as news).

<!-- Figure 30.2: Working gas in underground storage compared with the five-year maximum and minimum (as of November 2018). Source: US Energy Information Administration. -->

Figure 30.2 shows the seasonality in natural gas reserves. When winter approaches, the demand for natural gas increases as inventory is reduced because of its use in home heating.

## Risk-On and Risk-Off

There are times when market sentiment is generally positive and investors are optimistic and willing to take more risk to get better returns. Such an environment is called a risk-on market because market participants are seeking to take on more risk. On the other hand, there are times when investors are pessimistic and trying to cut risk by selling their positions in risky assets and moving money to cash positions or low-risk safe havens, like US Treasury bonds. These are called risk-off times (Figure 30.3).

<!-- Figure 30.3: Risk-on/risk-off regimes on the AUD/USD price curve. -->

This investor behavior — to flock to assets perceived as risky during risk-on times and to assets perceived as risk-free during risk-off times — increases the correlation among different asset classes.

To construct a risk-on/risk-off alpha, we must identify whether the market is in a risk-on or risk-off regime on a daily, weekly, monthly, and quarterly basis; categorize different assets as risk-on or risk-off assets (either absolutely or relative to other assets in the group); and assign them positions based on the current market state.

One popular indicator of market risk perception is the VIX, a volatility index constructed from the implied volatility of S&P 500 options. Traditionally, the correlation between price and volatility is negative for equities, which generally are a risk-on asset. Therefore, high or increasing VIX levels are associated with money moving out of equity markets into safer assets, indicating the arrival of a risk-off regime. The VIX itself is a tradable futures instrument that is used by many to benefit from falling markets. Other indicators include the yield curve (higher and steeper is risk-on; lower and flatter or inverted is risk-off); sector flows among risk-on sectors such as consumer discretionary and risk-off sectors such as utilities, or among emerging (risk-on) and developed (risk-off) markets; carry currency pairs, such as AUD/JPY; and the covariance structure of the market (the top eigenvector is usually risk-off).

Risk-on/risk-off alphas can be traded on the VIX and on broad cross-sectional markets because they are based on broad market correlations. They work better on longer time horizons of weeks to months.

## Carry and Contango/Backwardation

When near-month futures are cheaper than those at further expiries, the price curve slopes upward and the contract is said to be in contango (Figure 30.4). This is generally the case for commodities and can be attributed to the storage cost, or cost of carry.

<!-- Figure 30.4: Cocoa distribution in contango. -->

However, in some cases the near-month futures are more expensive than far-month futures, which creates a downward-sloping curve, and the contract is said to be in backwardation. Financial futures tend to be in backwardation because the underlying assets pay premiums or coupons and do not impose storage costs.

Some traders make money by selling contracts in contango and buying contracts in backwardation, which is known as a carry trade. The profit comes from two sources: the returns of the individual contracts as they approach expiration and the roll yield realized when the portfolio rolls from one contract to the next. This contango and backwardation alpha can be expected to work on commodities, equities, bonds, and currency pairs where at least one side has a significant nonzero interest rate. It does not work when the curves are all flat. The classic G-10 currency carry trade stopped working in the aftermath of the 2008–2009 global financial crisis, when many central banks lowered their lending rates to zero. Carry trades tend to make slow and steady profits when they are working, but they are vulnerable to sudden risk-off crashes.

For financial assets (equities, bonds, currencies, rates), the yield is supposed to be a return on risk. When the market enters a risk-off phase, investors pull out of the high-yield assets that they consider too risky.

## Conclusion

The grouping of instruments into sectors based on the underlying asset is an important aspect of futures and currency alpha research, as the behaviors of distinct groups of market actors within each sector and the common participants across all sectors give rise to the correlations among these instruments. Futures and currency traders are a relatively small group who follow particular assets and metrics, and respond in predictable and often self-fulfilling ways to common knowledge. Understanding the key ideas that drive human traders can be a fruitful source of alpha research ideas. If you take a moment to consider how the factor exposure of each sector should respond to the idea you are exploring, you may find a useful place to start testing your ideas.
