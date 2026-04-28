# Chapter 24: Institutional Research 101: Analyst Reports

**By Benjamin Ee, Hardik Agarwal, Shubham Goyal, Abhishek Panigrahy, and Anant Pushkar**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

This chapter is a general overview of analyst research reports and stock recommendations that alpha researchers may encounter in financial media sources. We will discuss the best ways to access analyst recommendations, and address the all-important question of how these reports can help inspire systematic trading ideas.

Sell-side analysts' recommendations, ratings, and price-target changes -- on companies and entire industries -- are featured prominently in financial newspapers, conferences, blogs, and databases, which often cite these reports to explain major stock price movements. Indeed, numerous studies by industry associations and academics have found that analyst research contains valuable information.

Nevertheless, the phrase "stock analyst" conjures up images of sophisticated researchers from Goldman Sachs or J.P. Morgan who conduct high-powered earnings calls with Fortune 500 CEOs to gather information and present their findings to multibillion-dollar institutional funds. How can you, a new alpha researcher (with something less than a few billion dollars at your disposal), access this valuable body of analysis? Just as important, why should an alpha researcher, who is interested in constructing systematic market strategies, pay attention to what are typically company-specific analyses?

## Accessing Analyst Research (For Free, of Course)

An analyst report generally contains the following:

- A detailed description of a company and its industry.
- Estimates for relevant financial numbers, such as earnings and revenue.
- A price target.
- A buy, hold, or sell recommendation based on the analyst's research.
- A thesis explaining the recommendation.

Sell-side analysts often perform research that is costly, sophisticated, and time consuming; naturally, they want to provide first access to their valued clients. To be sure, you will not be able to access all (or even most) analyst research on a company via public sources. Nevertheless, the portion of analyst research that finds its way to publicly accessible media can be a valuable learning tool for new alpha researchers.

In fact, some analyst research is surprisingly accessible, with the financial media acting as an intermediary. In this case, the term "financial media" includes not only traditional sources like The Wall Street Journal and Bloomberg, but also aggregator websites such as Yahoo Finance and Google Finance. The latter are particularly useful sources of analyst analysis, estimates, and questions posed to corporate management during earnings calls. Pulling up mentions of analyst research on a company is often as easy as entering that company's stock ticker into your favorite finance portal. For instance, typing Apple's stock ticker (AAPL) into Yahoo Finance's portal turns up the headlines in Figure 24.1, from November 2018.

The left-hand side of the screenshot shows headlines and links to articles that sometimes draw upon analyst research. On the right side, Yahoo Finance has helpfully summarized the analyst recommendations (strong buy, sell, and so forth), price targets, upgrades, and downgrades. Clicking on Upgrades & Downgrades will lead to a detailed table with earnings and revenue estimates for AAPL, as well as EPS trend and revisions for the company.

<!-- Figure 24.1: Screenshot of search result for "AAPL" on Yahoo Finance. Source: Yahoo Finance. https://finance.yahoo.com/ -->

You may wish to try out this process on other portals, such as Google Finance or Bloomberg.com, before picking the one that works best for you. If these don't provide what you're looking for, try using search engines directly (Google "AAPL analyst reports," for instance).

As with analyst research, finance portals often provide transcripts of companies' earnings calls, as well as stock analysts' questions during the calls and management's responses. In the next example, we use another finance portal, Seeking Alpha (https://seekingalpha.com). There are many places on the internet where you can find such information. Other examples: the Motley Fool website (www.fool.com), stock exchange websites (such as www.nasdaq.com), and the investor relations section of company websites. Some of these sources also contain a fair amount of discussion by nonbank market commentators on specific industries as well as individual stocks. The discussion on these sites can be similar to research from stock analysts, touching on points such as firm-specific fundamentals, macroeconomics, geopolitics, and market conditions. Table 24.1 provides additional examples of such market commentary sites and finance blogs.

<!-- Table 24.1: Market commentary sites and finance blogs -->

| Market commentary sites | Link |
|---|---|
| Bloomberg | http://www.bloomberg.com |
| The Wall Street Journal | http://www.wsj.com |
| Seeking Alpha | http://www.seekingalpha.com |
| Morningstar | http://www.morningstar.com |
| TheStreet | http://www.thestreet.com |

| Finance blogs | Link |
|---|---|
| Econbrowser | http://econbrowser.com/ |
| Free Exchange | http://www.economist.com/blogs/freeexchange |
| ZeroHedge | http://www.zerohedge.com/ |
| CXO Advisory Group | http://www.cxoadvisory.com/blog/ |
| Freakonomics | http://freakonomics.com/ |
| Marginal Revolution | http://marginalrevolution.com/ |

*Note: In many places, our listing coincides with a ranking compiled by Time magazine.*

<!-- Figure 24.2: Screenshot of Apple Q3 2018 earnings call transcript on Seeking Alpha. Source: Seeking Alpha. http://seekingalpha.com. -->

See if you can find Apple's third-quarter 2018 earnings-call transcript and analyst Q&A on the Seeking Alpha website.

## So Far, So Good. But Why Should You Care?

Good question. Most analyst reports (and market commentaries) focus on a single stock or industry, whereas you, as an alpha researcher, are looking for systematic market strategies that trade tens of thousands of stocks each day. So what if some analyst from Bank XYZ likes a particular company? How do we go from this to trading thousands of companies on 20 different stock exchanges around the world?

You can combine information from analyst reports for various stocks to construct an alpha that trades a more diversified set of stocks.

### 1. Recommendations

Useful information from analyst reports includes buy and sell recommendations. We can use the average recommendation rating for stocks to make an alpha. Figure 24.3 shows the performance of an alpha that uses buy and sell recommendations from analyst reports for the Russell 3000 universe of stocks. The idea is to go long stocks with buy recommendations and short stocks with sell recommendations.

<!-- Figure 24.3: Performance of alpha using buy and sell recommendations. Alpha = average buy recommendation - average sell recommendation. -->

### 2. Price Targets

Analysts calculate the projected price levels of stocks. Figure 24.4 shows the performance of an alpha using the Russell 3000 universe that compares the analyst price target with the present stock price. The idea is to buy the stock if the projected price target is above the current stock price and sell it short if the price target is below the current price.

<!-- Figure 24.4: Performance of alpha using price target. Alpha = analyst price target - stock price. Currency in USD. -->

### 3. Earnings Estimates

Analysts provide estimates for various fundamentals of a company, such as earnings, dividends, and cash flow. Figure 24.5 is a snapshot of summarized statistics for earnings estimates of AAPL from Yahoo Finance.

<!-- Figure 24.5: Screenshot of earnings estimates results for AAPL on Yahoo Finance. Source: Yahoo Finance. https://finance.yahoo.com/. Table includes columns for No. of Analysts, Avg. Estimate, Low Estimate, High Estimate, and Year Ago EPS across Current Qtr. (Dec 2018), Next Qtr. (Mar 2019), Current Year (2019), and Next Year (2020). -->

Figure 24.6 shows the performance of an alpha based on the Russell 3000 universe of stocks, using the growth in earnings estimates. The alpha buys stocks with positive growth and sells short stocks with negative growth.

<!-- Figure 24.6: Performance of alpha using earnings estimates. Alpha = change in analyst's earnings estimate for next fiscal period. -->

### 4. Earnings Surprises

When a company releases its earnings for the quarter or year, the actual earnings number can be compared with the earnings estimated by analysts for that period. A higher than expected earnings number is generally taken as a positive indicator, and vice versa.

Figure 24.7 shows the performance of an alpha, based on the Russell 3000 universe of stocks, that uses the earnings surprise. The idea is to buy the stock if the company's earnings consistently outperform analyst estimates and sell it short if the earnings underperform estimates.

<!-- Figure 24.7: Performance of alpha using earnings surprise. Alpha = actual earnings reported - analyst earnings estimate. -->

Researchers looking for systematic market strategies can develop unique or less-known alpha ideas from reading stock analyst reports. The following points may be worth considering:

- **The analyst's thought process is far more important than any specific buy or sell recommendation.** Did she decide to upgrade AAPL for industry-specific reasons (the market for smartphones has been growing at double-digit rates), for company-specific reasons (net margins have been increasing over the past four quarters), or for a more general reason, such as AAPL's low price-earnings ratio compared with the rest of the industry? Regardless of the reason, an interesting question is: can I apply this to other companies? For instance, if the analyst says she likes AAPL because the CEO has been buying stock in the company, should this logic be applied only to AAPL or to publicly listed companies in general? This line of reasoning has been known to yield new strategy ideas. Figure 24.8 shows an alpha developed using this hypothesis (go long if there is a share buyback and short otherwise) for the Russell 3000 universe of stocks.

<!-- Figure 24.8: Performance of an alpha using share buybacks. Alpha = if shares bought back by company's board executive then buy; otherwise sell. -->

- **Analysts usually ask good questions during earnings calls.** They should, because they are highly paid to do so. And for a new researcher trying to figure out how to make sense of the dense numbers that are a modern corporation's financials, these questions can be a lifesaver. More information is not always better, especially if you have 20 pages of numbers per company and need to separate signal from noise. How can you understand which accounting item is important? One clue is to think about the numbers or trends analysts focus on and the logic that motivates their questions. Are they puzzled by an extremely large and unseasonal change in inventory from one quarter to the next? Why is this important? As always, we should ask if it is something that is generally important beyond the company under discussion.

One way to extract trading signals from earnings calls is to focus on the collective sentiment of the company's management and the analysts and reporters present during such calls. The questions of analysts and the answers provided by management can be a measure of overall market sentiment about a company's quality of earnings and hence the future price of its stock.

Text-parsing algorithms can use this information to derive a net sentiment score (positive or negative) for the stock and decide to buy or sell accordingly. Figure 24.9 shows an alpha using this idea on the Russell 3000 universe.

<!-- Figure 24.9: Performance of alpha using earnings-call data. Alpha = average positive sentiment - average negative sentiment. -->

- **Analysts have detailed industry knowledge.** As Larrabee (2014) points out, industry-specific expertise has been cited as one of the most important attributes (and competitive advantages) of stock analysts. The best sell-side analysts are able to move stock prices with their ratings and forecasts, and this effect is stronger for analysts with industry experience. Alpha researchers can learn a lot about methodology from analysts' work. For instance:
  - Valuation methodologies vary across industries. Constructing a discounted cash flow model may be very different for the manufacturing sector compared with consumer cyclical firms, noncyclicals, and other sectors. Analysts may focus on different valuation metrics, such as the price-earnings ratio for one industry and the price-book ratio for another. For the alpha researcher, it is important to understand the underlying reasons for these differences in order to normalize and compare data appropriately for the universe of tradable stocks.
  - Each industry may have its own unique driver or measure of operational performance, which usually features prominently in analyst reports. Dot-coms used to look at "eyeballs" back in the late 1990s (perhaps they still do), and airlines think about "passenger miles," whereas biotech companies may focus on drug trials or drugs in the pipeline. Understanding the key drivers of operational performance in each industry may help the alpha researcher figure out interindustry variations in her strategy's performance.

- **Analyst research can provide valid trading signals.** On occasion, analyst research can directly move stock prices. You may have seen headlines attributing a large price bump or fall for a specific ticker to an analyst upgrade or downgrade, or to an increase in price targets. An extensive body of academic research shows a link between analyst research and stock returns; you can find it on Google Scholar under "stock analyst research." A better understanding of analyst recommendations may help you make better use of this information in constructing strategies.

## Things to Watch Out For in Reading Analyst Reports

Whether you are reading analyst research to look for inspiration on new market strategies or want to use its recommendations and targets directly in strategy construction, it may help to keep in mind some of the pros, cons, and idiosyncrasies of this research.

- **Positive bias.** While different banks have different approaches, academic researchers contend that stock analysts as a group exhibit positive bias. One implication is that the distribution of analyst recommendations is skewed. For example, if we are counting buy, hold, and sell recommendations, there are far more buy than sell recommendations. Academic researchers have debated the reasons for this; Michaely and Womack (1999) and Lin and McNichols (1998) have questioned whether banks are inclined to issue optimistic recommendations for companies with which they have relationships.

- **Herding.** Herding refers to the theory that analysts try not to be too different from one another in their public recommendations and targets. Part of the reason for this may be behavioral: making public stock price predictions (or "targets," in analyst-speak) is a risky endeavor with career implications. All else being equal, there may be some safety in numbers from going with the crowd. A corollary to this is that analysts who are more confident or have established reputations are usually willing to deviate more from the consensus. Behavioral reasons aside, there may be sound reasons for analysts to arrive at similar conclusions -- for example, most might be working off the same sources of information. Hence, it might be interesting to understand major analyst deviations from the consensus, what is unique about their methods or data source, and whether this can be systematized.

- **Coverage drop.** Analysts have a greater tendency to issue buy (or at least slightly positive) ratings than sell ratings. The reason for this is ingrained in how the financial industry works. The desire of analysts to please their potential investment banking clients can create a conflict of interest. Issuing negative research on the stocks of their own corporate clients (or potential clients) may cost brokerages profitable business. In other words, a brokerage firm would rather be wrong on any buy or sell recommendation than be right and lose a corporate client.

In some cases -- especially large-cap stocks -- an analyst may rather drop coverage of the stock than give a sell signal on it and be proved wrong later. Therefore, a drop in coverage of a stock, especially a large cap, may be a red flag. Issuing a sell rating on a small company may have fewer repercussions for an analyst than issuing a sell rating on a big company.

Figure 24.10 shows the performance of an alpha that compares short-term and long-term analyst coverage. The idea is that if the number of analysts covering the stock has decreased significantly with respect to its long-term coverage, then we short the stock; we go long the stock if the short-term analyst coverage has increased.

<!-- Figure 24.10: Performance of an alpha using coverage drop. Alpha = short-term analyst coverage / long-term analyst coverage. -->

## Why Do Stock Analysts Talk to the Financial Media?

If you were to invest significant time and energy in detailed analysis that produced wonderful trading ideas, your first impulse might not be to pick up the phone and tell a bunch of reporters about it. After all, many ideas are capacity limited -- only so many people can trade them before the price starts to move significantly and the chance for profit disappears.

Yet we find mentions of analyst research in media reports all the time. In fact, we may even rely on this because it allows us to peek into the world of analyst research at little or no cost. What explains this accessibility? Some possible reasons:

- Many meetings between stock analysts and the companies they cover are open to members of the public and therefore to the financial press. One example of this is earnings calls, which are available through publicly accessible transcripts. In the US, the Securities and Exchange Commission's Regulation Fair Disclosure, known as Reg FD, mandates that nonpublic information disclosed by issuers to investment professionals must also be made available to all market participants. This includes both analysts working for multibillion-dollar banks and members of the investing public.

- A certain amount of publicity probably doesn't hurt a stock analyst's career. Media mentions and interviews may increase demand for an analyst's research among investor clients, and high-profile recommendations that are proved right (such as calling the market bottom in 2009) may fast-track an analyst's career. These benefits are possible only if analysts go public with some of their research.

## Conclusion

- Analyst research may be accessible via the financial media.
- Analyst recommendations and price targets may be trading signals in their own right.
- Fundamental estimates provided by analysts provide an outlook for a company and can be used to make alphas.
- Stock prices may respond to surprises resulting from a difference between reported fundamentals and their corresponding consensus values.
- The methodologies and reasoning processes analysts use to arrive at their recommendations may be a source of ideas for alpha researchers.
- Earnings-call transcripts can be analyzed to gain insight into the collective sentiment of a company's management, stock analysts, and reporters.
- Watch out for caveats, such as positive bias, analyst herding, and coverage drops.
