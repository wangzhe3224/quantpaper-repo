# Chapter 28: Finding an Index Alpha

**By Glenn DeSouza**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

Alpha discovery is not limited to single-company equity instruments. With the dramatic rise of passive investing in the past two decades, exchange-traded funds (ETFs) and related index products have fostered the growth of various index-based alpha strategies. Historically based in large investment banks because of their reliance on technology investment, balance sheet usage, and cheap funding, these strategies have become more popular among buy-side firms in recent years, including large quant- and arbitrage-focused hedge funds and market-making firms.

## Index Arbitrage in Practice

Index arbitrage is an alpha strategy that attempts to profit from differences between the actual and theoretical futures prices of a stock index, adjusted for the trader's unique costs, including cost of capital and borrowing costs (or stock rebate). The theoretical value, or the fair value in industry parlance, of an index futures contract can be described by the following top-down adjustment formula:

<!-- Formula: Fair value of future = Cash value of index + Interest – Dividends -->

Holding a futures contract instead of directly investing in the underlying companies of a stock index frees up additional capital for investment (because futures have a much lower margin requirement than stock investments, particularly in the US), but it forces contract holders to forgo dividends, thus making interest rates and dividends the two primary differences affecting futures index arbitrage.

How can such strategies prosper in an increasingly computerized and automated world? A practical example from investment bank trading desks in the past can be illuminating in this context. In the mid-2000s, some banks operated as follows:

- The bank's index arbitrage desk would calculate its own fair value using one or more of the following methods: top-down (by adjusting variables in the formula above based on macroeconomic forecasts), bottom-up (estimating and aggregating individual stock dividend forecasts), or option-implied information. The bottom-up method typically was the most reliable for generating profits, but it was also the most time consuming.
- After calculating the fair value and other product-specific costs, desks could compare multiple index-based products for arbitrage opportunities, in addition to the typical futures-versus-underlying-stocks arbitrage. These trades included arbitrage among futures, over-the-counter (OTC) index swaps, and index options.
- Some bank trading desks had a funding advantage — a lower cost of capital — which implied that the fair value of an index future was lower for them than for other firms. This offered more opportunities to short futures because the actual futures prices often appeared "rich" (expensive) compared with their own fair values. On the other side of these trades, typically, were institutional accounts that often paid a slight premium for the cheap access to leverage and liquidity afforded by futures.
- The desks would hedge their short futures exposure by simultaneously purchasing the underlying stocks. In effect, banks were sellers of balance sheet and institutional investors were buyers of it because of the banks' funding and balance sheet advantages.

Such a strategy at this stage might earn a small (less than 1%) return annually because the funding advantages typically were only a few basis points. So some banks became more creative in their inventory usage:

- Long positions from the acquired (and other bank) inventory could be converted into ETFs because many of the banks were ETF-authorized participants (APs), which allowed them to create and redeem ETF shares.
- For ETFs that were popular to short (and thus had higher than average borrowing costs), such as the Russell 2000 ETF (IWM), desks could now lend out their newly created ETFs and earn a higher stock-lending rate (sometimes 1% or more annually for certain highly sought-after funds).
- In other cases, inventory could be combined with options positions to create options reversals and conversions, which had their own OTC market and allowed inventory holders to provide liquidity in hard-to-borrow names to counterparties such as M&A arbitrageurs.
- Last, any remaining stock positions were examined for alpha-generating events such as tender offers or index changes. Stock risk could then be taken opportunistically in single names around those event dates.

In some cases, multiple overlays to a seemingly simple index arbitrage strategy could increase the overall returns of an index arbitrage desk from less than 1% to 5% or more.

How easy would this implementation be for buy-side firms? The answer depends partly on the size and pricing power of firms to lower trading and borrowing costs as much as possible to mimic the investment bank setup. Typically, only the largest hedge fund firms or active managers with related broker-dealer entities had the potential ability to negotiate such advantageous deals.

Some segments of the overall index arbitrage strategy, however, such as predicting market impact for certain indices, can be implemented by active managers without necessarily requiring a large balance sheet.

## Market Impact from Index Changes

Besides being a popular ETF to short, the IWM fund is reconstituted annually, causing some market impact on its constituents and former constituents compared with other sought-after ETFs. FTSE Russell's published research has noted that the impact of buying newly added companies and selling deleted companies on the reconstitution date affected Russell 2000 index returns by an estimated 28 basis points (bps) a year for the period 2007–2015, although with large annual deviations (Figure 28.1).

<!-- Figure 28.1: Average negative impact on Russell 2000 index returns from rebalancing (2007–2015). Source: London Stock Exchange Group plc and its group undertakings (collectively, the "LSE Group"). © LSE Group 2019. FTSE Russell is a trading name of certain of the LSE Group companies. "FTSE Russell®" is a trademark of the relevant LSE Group companies and is used by any other LSE Group company under license. -->

This would imply that arbitrageurs could short the added names and buy the deleted ones on the effective date of the reconstitution to earn a positive return. Such reversion could be expected to occur if the affected stocks had dislocated from fundamental and peer values in the months before the reconstitution and pairs- and sector-based relative-value traders were now pushing the stocks back toward their previous valuations. These large dislocations combine to imply that the true cost of owning the Russell 2000 IWM ETF is much higher than its 20 bps expense ratio would suggest.

In contrast to the Russell 2000, large-cap and total-market-tracking products typically do not suffer as much of a rebalancing drag on their portfolios. The S&P 500, for example, tends not to see as much reversion in added stocks, perhaps owing to their higher liquidity or late purchases by closet trackers, who cannot predict S&P additions as easily. Meanwhile, the CRSP US Total Market Index, which is tracked by Vanguard Group's largest index funds, encompasses the entire US market, from large caps to microcaps, and accordingly does not trigger any trading requirements when cap-size migrations occur. (However, funds benchmarked to the individual capitalization ranges would still need to trade and thus potentially would impact market prices for some illiquid stocks.)

## Other Index Anomalies

### Captive Capital-Raising by Newly Indexed Companies

Index changes can lead to other market anomalies. For example, when stocks are added to major blue-chip indices, such as the S&P 500, a few of the added companies occasionally engage in opportunistic capital-raising without the usual offering discount, as index funds are forced buyers of stock around that time. Real estate companies are the most notable offenders: more than a quarter of real estate investment trusts (REITs) added to the S&P 500 since 2005 have engaged in this behavior.

Deal pricings around S&P 500 REIT additions since 2008 show an average placing discount of only 17 bps to the previous close for these captive capital raises (and 26 bps for all added companies' offerings), compared with an average discount of 2.8% for all other share offerings by stocks in the same index since 2008 (Figure 28.2).

<!-- Figure 28.2: Average offering price discounts. S&P 500 REIT companies (2008–2017) versus S&P 500 companies (2008–2017). REIT offerings during S&P inclusion week: 0.17%; All REIT offerings: 0.26%; All offerings during S&P inclusion week: 0.26%; All S&P 500 offerings: 2.82%. Source: S&P® and S&P 500® are registered trademarks of Standard & Poor's Financial Services LLC, and Dow Jones® is a registered trademark of Dow Jones Trademark Holdings LLC. © 2019 S&P Dow Jones Indices LLC, its affiliates, and/or its licensors. -->

Thus, syndicate desks can raise capital much more cheaply for the issuer than historical fundamentals would indicate. In essence, the participating index fund becomes a captive buyer that is not being incentivized for the immediate share dilution and potential EPS dilution of the share offering. However, bypassing the offering might result in an even higher purchase cost on the upcoming rebalance date.

Event-driven traders constructing alphas around corporate events therefore should take note of the unique nature of these offerings. The combination of smaller pricing discounts, more placement to passive funds, and follow-on buying from the upcoming index additions could lead to unusual effects on alphas that might otherwise expect strong selling activity immediately after the offering.

### Valuation Distortions in Index Versus Nonindex Stocks

The Russell 2000 also suffers from a persistent valuation distortion, perhaps resulting from a premium placed on index versus nonindex stocks. Russell 2000 index members were valued at a premium to nonindex members across every sector as of September 2017 (Figure 28.3), and broadly every year since 2008, even though more than 30% of stocks in the index had negative earnings (compared with less than 5% in the S&P 500). Communications stocks, for example, had a median trailing price-earnings ratio (P/E) of 30 times in the Russell 2000, while non-Russell sector peers were priced at only 19 times trailing earnings. A similar but smaller disparity is seen in the other nine major sectors. One possible reason is that ETFs constitute a higher percentage of small caps' average daily volume traded than they do of large caps' — often more than double the percentage of volume, as of mid-2017.

<!-- Figure 28.3: Excess (deficit) of index P/E over non-index P/E. Median trailing P/E of Russell 2000 small-cap sectors versus non-Russell stocks (September 2017). Source: London Stock Exchange Group plc and its group undertakings (collectively, the "LSE Group"). © LSE Group 2019. FTSE Russell is a trading name of certain of the LSE Group companies. -->

Interestingly, in the US large-cap universe, the effect of index membership is reversed. S&P 500 members trade at a discount to nonmember peers, as measured by year-end median trailing P/E over the past 10 years (Figure 28.4). This may be due not only to the lower proportion of ETF trading but also to the smaller eligible universe of available companies, as well as different factor exposures. Whereas Russell 2000 candidates include rising microcaps as well as declining large caps, the S&P 500 index already is at the top of the market capitalization range and can only add either new large- or megacap IPOs or rising small- and midcap names that have outperformed recently, thus exposing the index to long momentum factor risk.

<!-- Figure 28.4: Year-end median P/E disparity between index and nonindex stocks. R2 median P/E excess (deficit) vs non-R2 US SC; S&P 500 median P/E excess (deficit) vs non-S&P 500 LC (2005–2016). Sources: London Stock Exchange Group plc and its group undertakings (collectively, the "LSE Group"); S&P® and S&P 500® are registered trademarks of Standard & Poor's Financial Services LLC. © LSE Group 2019. © 2019 S&P Dow Jones Indices LLC, its affiliates, and/or its licensors. -->

## Conclusion

The rise of index products has created not only a new benefit for the average investor in the form of inexpensive portfolio management, but also new inefficiencies and arbitrage opportunities for many active managers. An extended period of low interest rates has allowed the proliferation of cheaply financed strategies, while the rise of passive investing has created market microstructure distortions, in part as a result of rising ownership concentration.

Fortunately, new index constructions (and associated funds) also have proliferated in recent years, allowing investors to slice and dice passive portfolios in myriad ways that avoid several index drawbacks, including market impact and valuation distortions.

But with legacy index products continuing to reap liquidity and some market inefficiencies persisting, both passive products and the active ones that arbitrage them may prosper for a while longer, implying that perhaps the investment allocation debate is not simply a choice between active and passive but rather the creation of a combined model of active overlays to passive core portfolios to take advantage of the best aspects of both worlds.
