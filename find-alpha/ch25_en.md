# Chapter 25: Event-Driven Investing

**By Prateek Srivastava**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

Joseph Nicholas defines event-driven strategies in his book *Hedge Fund of Funds Investing* (2004) as "strategies that are based on investments in opportunities created by significant transactional events, such as spin-offs, mergers and acquisitions, industry consolidations, liquidations, reorganizations, bankruptcies, recapitalizations, share buybacks, and other extraordinary corporate transactions. The uncertainty about the outcome of these events creates investment opportunities for managers who can correctly anticipate them and the success or failure usually depends on whether the manager accurately predicts the outcome and timing of a concrete event."

Event-driven investment strategies attempt to take advantage of price inefficiencies around company-specific (and sometimes market-wide) events. The most popular event-driven strategies include actions taken in response to corporate actions:

- **Mergers and acquisitions**, which give rise to a trading strategy known as merger arbitrage or risk arbitrage.
- **Spin-offs, split-offs, and carve-outs.**
- **Distressed securities.**
- **Index rebalancing.**
- **Capital restructuring events**, such as share buybacks, debt exchanges, and security issuances.

Event-driven strategies are important because their distribution of returns is significantly different from that of the market, providing diversification to a typical hedge fund's overall portfolio. A corporate event is generally unique to the specific organization and unrelated to broad market events, helping to reduce a portfolio's market dependency.

Another important advantage of an event-driven strategy is that it is an all-season strategy. In every phase of the business and economic cycle, companies are pursuing ways to unlock shareholder value, so there is always some type of corporate event happening. Merger arbitrage events are quite frequent when the economy expands, for example, and distressed-strategy events are more common when the economy contracts. Figure 25.1 lists corporate events that are more frequent in various phases of the business cycle.

<!-- Figure 25.1: Corporate events during phases of the business cycle. Recovery: management change, mergers & acquisitions, post-bankruptcy reorganization. Expansion: capital restructuring, corporate refinancing, management change, mergers & acquisitions. Peak: capital restructuring, corporate refinancing, deleveraging, mergers & acquisitions, spin-offs & split-offs, shareholder activism. Recession: capital restructuring, corporate refinancing, distressed asset. -->

## Merger Arbitrage

Merger, or risk, arbitrage is probably the best-known event-driven investment strategy. In a merger, two companies mutually agree to join together, which often involves an exchange of shares. In an acquisition, there is a clear-cut buyer (the acquirer) and seller (the target). Often, M&A begins as an acquisition, perhaps unfriendly, but eventually the target succumbs and agrees to a merger. Merger arbitrage is a bet that the deal will or will not close. Some of the major reasons companies make acquisitions are listed in Table 25.1.

Since hedge funds began to proliferate in the 1990s, merger arbitrage has been a classic market-neutral strategy. However, the activity goes back to the 1940s, when Gustave Levy created the first arbitrage desk on Wall Street at investment bank Goldman, Sachs & Co. Goldman has been a valuable training ground for hedge fund managers, including Daniel Och, Richard Perry, and Tom Steyer, who came out of its risk arbitrage group in the 1980s to start their own firms. In fact, merger arbitrage was never more powerful than during the buyout boom of the 1980s, when arbitrageurs provided the leverage in many of that era's hostile deals.

The merger arbitrage process typically begins when the acquirer approaches the target company with the proposal of a merger or acquisition. This discussion happens at the board of directors level and is kept confidential. If the companies agree on a deal, a press release discloses the important terms of the merger, such as the offer price for the target company (or the exchange ratio of the shares in the case of a merger) and whether the deal will be paid for in cash or in stock.

As its name implies, a cash merger is paid for in cash; in an all-stock deal, the merger is paid for in shares of the acquiring company at a certain exchange ratio. (Many deals involve a combination of cash and shares.) Following the news of the merger, the stock price of the target company typically jumps, but it generally does not reach the merger price because the deal carries the risk of not being completed. This is the point where the merger arbitrageur steps in. The difference between the target company's stock price and the merger price is known as the deal spread:

<!-- Formula: Deal Spread = (Offer Price - Target Stock Price) / Target Stock Price -->

This is the return (excluding dividend payments before the merger date and transaction costs) that the merger arbitrageur will earn if the deal goes through.

Within a few days of the official deal announcement, the full merger agreement is released by the two companies. The agreement contains all the details of the merger, including the conditions necessary for the deal to close, the required government approvals, and, most important, the material adverse change (MAC) clause. The MAC clause lists the conditions, mostly financial, under which either party can walk away from the deal.

An M&A fund manager will thoroughly analyze the deal agreement, conduct a detailed financial analysis of the transaction, participate in management conference calls, and check filings of both companies with the Securities and Exchange Commission to predict the likelihood of the merger's completion and whether the expected returns from the deal are high enough to justify the risk involved. If he likes the trade, the fund manager will decide on the position size and hedge the risks. For example, in the case of an all-stock merger, the fund manager will buy stock in the target company and short the stock in the acquirer to hedge the risk that the latter's stock price will drop before the deal concludes.

The fund manager would diversify across many deals to ensure that no single failed merger causes an unacceptably large drawdown to the portfolio. Since 1985, more than 300,000 M&A deals, with an estimated combined value of $33.2 trillion, have been announced in the US alone, according to the Institute for Mergers, Acquisitions and Alliances. In terms of total transaction value, 2015 was historic: $2.4 trillion, from roughly 13,000 deals. The record number of deals took place in 2017, when there were 15,558 transactions. All this activity gives fund managers a sufficient breadth of events to diversify their portfolios.

Many conditions affect the completion of a merger. Friendly mergers, where the deal is backed by the target company's management, have a higher probability of completion than hostile takeovers. Some deals may not get the required approvals because of antitrust concerns or other regulatory issues. A deal also may fail because of overall market conditions. For example, if the plan is to use external financing to pay for the merger and a credit crunch hits the market, the acquirer may not be able to arrange financing. Likewise, if the target company's stock price falls below the merger offer price because of a market decline, the acquirer may believe it is overpaying for the stock and the deal may not go through at the original price.

Merger arbitrage strategies are generally uncorrelated to market movements, but they are not immune to market risk. The returns on M&A strategies are uncorrelated during bull and mild bear markets, but in significant downturns they show higher correlation to the market because factors like uncertainty of completion, regulatory problems, or inability to get financing increase the risk of deal failure.

## Spin-Offs, Split-Offs, and Carve-Outs

A spin-off is the opposite of a merger: a divestiture in which a company separates a portion of its business (a division or a subsidiary) and organizes it as an independent company that is often publicly traded. This generally is done to unlock overall shareholder value (Table 25.2). A company may want to sell its noncore or nonessential businesses to focus on its core operations and competencies. For instance, General Electric sold 15% of its noncore financing arm Synchrony Financial in a 2014 initial public offering and completed the separation the next year by offering GE shareholders the opportunity to exchange their shares for shares in the 85% of Synchrony GE still owned. (For more examples of spin-offs, see Table 25.3.)

<!-- Table 25.3: Examples of notable spin-offs -->
<!-- 2015: eBay spins off PayPal, an online payment platform. -->
<!-- 2012: Kraft Foods splits off its snack business as Mondelez International. -->
<!-- 2011: Travel website Expedia spins off its review site TripAdvisor. -->
<!-- 2006: McDonald's spins off popular Mexican-food chain Chipotle. -->
<!-- 1999: Hewlett-Packard spins off its measurement business as Agilent Technologies. -->

Split-offs and carve-outs are similar to spin-offs. In a spin-off, shareholders of the parent company receive shares in the subsidiary on a pro rata basis. In the case of a split-off, shareholders of the parent company decide whether to tender shares in the parent in exchange for shares in the subsidiary. In an equity carve-out, the parent sells some shares of the subsidiary while retaining a fractional stake in the business.

Spin-offs are quite common; there typically are about 50 a year in the US alone. Many studies have found that both spun-off companies and their parents outperform the market in the years immediately after the split. Spin-offs generally outperform for a few reasons. Because the businesses are more focused on their core products, they run more efficiently and the profitability of each unit tends to grow. Also, the market starts valuing each business unit more accurately: analysts can assign each unit the price-earnings value of the individual industry to which it belongs rather than having to rely on a broader sector or on market values.

Even though these companies often outperform in the long run, they sometimes experience short-term price weakness. This may happen because shares of the spun-off unit may not fit the investment criteria of shareholders of the parent company. For instance, the spun-off company will have a smaller capitalization, and some shareholders might have limitations on their exposure to small-cap stocks, in their own right or because they typically have higher beta to the market. Generally, it is reasonable to invest in both the parent and the spun-off company, but it is important to carefully examine the particulars of any spin-off before making a decision on whether to keep, sell, or buy companies that are planning to spin off or already have done so.

## Distressed-Asset Investing

Distressed assets are the securities of companies or government entities that are experiencing financial or operational distress, default, or bankruptcy. Companies can become distressed for various reasons, including:

- Highly leveraged balance sheets
- Liquidity problems
- Credit downgrades
- Accounting irregularities
- Inadequate cash flows
- Poor operating performance

When an asset is distressed, it may trade far below its intrinsic value because of pessimistic investor sentiment. When this happens, investors whose mandates do not permit them to hold distressed securities, such as most mutual funds, are forced to sell them. This can cause huge differences between the assets' intrinsic value and the prevailing market price, and thus can present sizable potential profit opportunities. Investing in these assets to trade on the arbitrage between the intrinsic value and the prevailing market price of the security is known as distressed-asset investing. Warren Buffett fans might remember this strategy as the "cigar butt investing" approach:

> "If you buy a stock at a sufficiently low price, there will usually be some hiccup in the fortunes of the business that gives you a chance to unload at a decent profit, even though the long-term performance of the business may be terrible. I call this the 'cigar butt' approach to investing. A cigar butt found on the street that has only one puff left in it may not offer much of a smoke, but the 'bargain purchase' will make that puff all profit."
>
> — Warren Buffett, Berkshire Hathaway 1989 shareholder letter

The distressed-asset universe is huge and spans all kinds of below-investment-grade debt securities. These investments may include high-yield bonds, below-par distressed bank loans, debtor-in-possession loans, credit default swaps, preferred stock, common stock, warrants, and real estate assets. Distressed-asset investing tends to perform best during bull markets, when investors make money on the turnaround on investments made during the preceding economic downturn. A downturn provides a large number of opportunities for this form of investing. However, one can find good bargains even in a good economy: the US auto and airline sectors offered ample opportunities in the 2004–2006 period even though the economy was strong. The returns from distressed investing largely depend on company- and sector-specific factors rather than on overall business and credit cycles.

Hedge fund managers focusing on distressed securities can be categorized as active or passive. Active managers get involved in the daily business of the target company and work closely with its management to turn it around. Passive managers, meanwhile, are more oriented toward trading; they buy undervalued distressed securities and sell them when they revert to their fair value. Active managers who may have access to inside information are restricted in their trading until corporate information becomes public or immaterial. This is particularly a limitation in the event that a turnaround fails and the company files for bankruptcy. Active managers can sell their positions only after the bankruptcy process is complete, as opposed to passive managers, who, because they rely on public information, are not restricted.

## Index-Rebalancing Arbitrage

In this investment strategy, the arbitrageur bets on which stocks will be included in or excluded from an index. Some of the most popular indices for rebalancing arbitrage are managed by the London Stock Exchange Group's FTSE Russell business. A big reason for this is that Russell indices are rebalanced once a year, in June, whereas other major indices, such as the S&P 500 and the Dow Jones Industrial Average, are adjusted on an irregular basis. Among the Russell family of indices, the Russell Microcap Index is the most popular among these arbitrageurs because the companies that constitute it are very small and may not be well known. After they join the index, these companies often see a jump in participation by funds benchmarked to it. Stocks that move from the Russell 2000 to the large-cap Russell 1000 Index do not see a comparable jump in interest because they were already within the broad universe of index investments and simply moved from one basket to another.

Index rebalancing (or index reconstitution) arbitrage is a play on identifying additions and deletions to the index before they actually are added and deleted. If an investor can buy and sell the stocks ahead of institutional investors, they can generate profits after the announcement as the institutions buy and sell them. Historically, added and deleted stocks have significantly outperformed and underperformed the index, respectively, in the 2–3 months after the announcements were made.

## Capital Structure Arbitrage

A company's capital structure comprises the shares, debts, and other financial instruments it uses to finance its operations. In capital structure arbitrage, one security of a company is traded against another security of the same company — for example, buying the company's bonds and shorting its stock, or trading its credit default swaps (CDSs) against its stock. Another play could be on the arbitrage between listings of the same security on different exchanges; such mispricings may happen because of liquidity or other factors. Another type of capital arbitrage is to trade on changes in the company's capital structure, such as share buybacks, share issuances, debt issuances, or debt exchanges. These trades do not express a view on the overall quality of the company but on relative mispricings or shifts in value among different forms of capital.

One of the most popular capital structure arbitrage plays is to profit from mispricings between a company's equity and its bonds or credit default swaps. This strategy has gained a lot of popularity with the growth of the CDS market. Consider, for example, what happens when extremely bad news hits a company. This will cause both its bonds and its stocks to fall, though the stock prices will likely decline further, for several reasons. Stockholders will absorb a greater loss than bondholders if the company is liquidated, because bondholders have a priority claim on the assets of the company; the dividend might be reduced or dropped altogether, whereas annual bond payments are fixed, and the stock market is usually more liquid and so reacts to news more dramatically. In the case of bad news, if a mispricing is detected, the fund manager can go long the equity and short the bond. Another way to play the same trade is to use CDSs instead of bonds: the fund manager can go long equity and buy undervalued CDS protection. There are many ways to construct the same trade, and it is up to the fund manager to conduct due diligence to find the one with the best risk-return profile.

A second type of capital structure arbitrage involves finding mispricings between different categories of debt (for example, senior versus junior, secured versus unsecured, and bank loans versus bonds). During periods of stress or financial distress for the issuer company, discrepancies will occur in the relative prices of these debt instruments. The fund manager can play on the convergence of the spread between these instruments to the equilibrium level. Another example of capital structure arbitrage is convertible bond arbitrage, based on bonds that can be exchanged for company stock. The spread between standard bonds and convertible bonds should be fairly consistent, but variances in the company's stock price and dividend levels can give rise to mispricings between these two categories of bonds.

## Conclusion

Event-driven strategies capitalize on mispricings in securities linked to specific corporate events, such as mergers, acquisitions, spin-offs, bankruptcies, and restructurings. They have been among the best-performing hedge fund strategies historically and have gained a lot of traction over the past two decades. M&A strategies in particular have shown the best performance on a risk-adjusted basis, indicating why they are so popular among managers of event-driven funds. Those who incorporate multi-event strategies into a diversified hedge fund portfolio have the ability to potentially capture meaningful upside returns that are independent of broad market moves. Successful event-driven managers must possess vast deal experience, deep industry knowledge, and strong legal capabilities to assess the probable outcomes of a wide range of corporate events.
