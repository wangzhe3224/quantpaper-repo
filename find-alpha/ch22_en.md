# Chapter 22: The Impact of News and Social Media on Stock Returns

**By Wancheng Zhang**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

## Introduction

Stock prices naturally respond to news. But in recent years, news and sentiment seen on social media have grown increasingly significant as potential predictors of stock prices. However, it is challenging to make alphas using news. As unstructured data that often includes text and multimedia content, news cannot be understood directly by a computer. We can use natural language processing (NLP) and machine learning methods to classify and score raw news content, and we can measure additional properties of the news, such as novelty, relevance, and category, to better describe the sentiment of the news. Similar techniques can be applied to social media data to generate alphas, though we should bear in mind that social media has much more volume and is much noisier than conventional news media. This chapter gives an overview of ways to find alphas using news and social media.

## News in Alphas

It is not easy for machines to accurately parse and interpret the meaning of news. As in other areas in statistical arbitrage, an algorithm has the advantages of fast response time and broad coverage, but at the expense of weaker accuracy than a human analyst. Nowadays, trading firms can analyze news within 1 millisecond and make trading decisions instantly. Big news usually causes large price movements instantly, often with a subsequent overshoot and reversal.

Since 2007, the application of sophisticated linguistic analysis of news and social media has grown from a highly speculative area of research into mature product solutions. Professional data vendors use sophisticated algorithms to analyze news and deliver the results in real time. News analytics and news sentiment are widely used by both buy-side and sell-side institutions in alpha generation, trading, and risk management. Increasingly, Big Data vendors offer packages, services, or data sources to help firms use news in the investment process.

## Academic Research

Since 2000, news on stock returns has become a popular topic. Some of the key research areas include the aggregation and dispersion of sentiment; beta calculations using news; leading news stocks; weighting schemes in textual analysis; news confirmation by day-return earnings announcements; the idea that no news is good news; the notion that stocks that are sensitive to news outperform the broader market; confirmation of news by trading volume; bias in the news coverage on stocks; momentum, overshoot, and reversal after news; and the relationship of news to analyst revisions. Related papers can be found by searching for "news" and "stock return" on the Social Science Research Network (SSRN).

The first research paper on using social media for stock prediction was "Twitter Mood Predicts the Stock Market," published by Johan Bollen, Huina Mao, and Xiao-Jun Zeng in *The Journal of Computational Science* in 2011. The paper argues that by analyzing Twitter texts the authors gained an accuracy of 87.6% in predicting daily up and down changes in the closing values of the Dow Jones Industrial Average (DJIA). Since then, key research areas include the prediction power of various forms of social media; social media applied to individual stocks; the discussion of noise in social media; finding valuable tweets by observing retweets and tweets from celebrities; and social media sentiment with long-term firm value.

## Sentiment

Simply speaking, sentiment measures the quality of news. The most basic definition of sentiment is the polarity of the news: good, bad, or neutral. Advanced sentiment analysis can express more sophisticated emotional details, such as "anger," "surprise," or "beyond expectations."

The construction of news sentiment usually involves natural language processing and statistical/machine learning algorithms (for example, naive Bayes and support vector machines). The recent explosion of deep learning techniques has enabled rapid progress in understanding news. Novel techniques like word2vec have achieved higher accuracy compared with classical NLP methods.

Sentiment is usually normalized into scores (for example, in the range 0–100) that are cross-sectionally comparable across assets. By convention, a higher score means the news is good, a lower score means the news is bad, and a score near 50 means the news is neutral.

Individual news sentiment may have exposure to market aggregate sentiment, seasonality, and other timing factors (for example, before or after the earning season). For a relative-value strategy, it is useful to compare the relative sentiment among similar stocks.

Sentiment is also useful in risk management. For example, a portfolio manager may cut the size of a stock holding because of unexpected news, or estimate the portfolio covariance matrix taking into account the news sentiment score or news frequency.

**Example**

A simple alpha could be to follow the sentiment directly:

```
If (stock A sentiment > 70) long stock A;
if (stock B sentiment < 30) short stock B;
use the no-news stocks in the same industry for neutralization.
```

## Novelty

Novelty measures whether the news is a brand-new story or an update to an old story. Vendors may split one long report into several parts. Sometimes a story is a follow-up report on previous news. In other cases, news may be revised several times after the initial report. Less novel news usually has less impact on the market because the information delivered in the previous news may already be reflected in the market. If we view news as events in a time series, novelty usually is inversely proportional to the time between the events.

**Example**

We could enhance the previous simple alpha by using novelty:

```
Score novelty from 0 to 1.
If (sentiment > 70) alpha = sentiment * novelty;
if (sentiment < 30) alpha = sentiment * novelty;
use the no-news stocks in the same industry for neutralization.
```

## Relevance

News can have an impact on multiple stocks. Relevance measures the focus of news on specific stocks. Some news, such as earnings or corporate actions, is company specific. The relevance of such news is usually high. One news story could talk about multiple companies in the supply chain of a product; in this case, the relevance of the news could be the highest for the company manufacturing the product and lower for other companies along the supply chain.

Industry or general macroeconomic news usually has lower relevance to individual stocks. A general news item about the banking industry may affect lots of banking stocks; a news story about Apple's new products may affect Apple and competitors like Samsung, with higher relevance to Apple and lower relevance to Samsung. In other words, relevance maps the news sentiment to individual stocks. It can be another factor to enhance news alphas.

**Example**

We could enhance the previous simple alpha by using relevance and ignore the news that affects too many stocks:

```
Score relevance from 0 to 1, get ns = number of stocks impacted by one news item.
If (sentiment > 70 and ns < 100) alpha = sentiment * novelty * relevance;
if (sentiment < 30 and ns < 100) alpha = sentiment * novelty * relevance;
use the no-news stocks in the same industry for neutralization.
```

## News Categories

Besides the simplistic classification of news into "good" or "bad," further classification into more detailed categories can enhance the analysis and use of news. A category can be as broad as "earnings," which may include all earnings-related reports, like earnings announcements, earnings forecasts, earnings revisions, earnings guidelines, earnings conference calls, and earnings calendars. Or it can be more specific, like "corporate legal issues."

There are several important aspects to consider when using news categories. First, different categories of news may have different response times in the market. Some categories have longer-term effects on company valuations; other categories can cause short-term price fluctuations. Second, markets have different flavors of news at different times. A category-rotation strategy can take advantage of these flavors of news styles. Third, some news categories are specific to certain industries and sectors, and may affect only those industries or sectors. Last, categories make different types of news easier to combine with other types of information to create alphas. For example, one can use earnings news together with analyst earnings revisions. News vendors like Bloomberg provide tags and categories for raw news, and automatic categorizations by advanced machine learning methods are becoming more common.

**Example**

Consider the earnings news example. We can drop "market reports" categories and use a simple "learning" method to further weight the news:

```
Ignore all news from the categories "market imbalance" and "market movements."
For each news category,
  Category_score = the average of relative stock returns after the news happened in the past two years
If (sentiment > 70 and ns < 100) alpha = sentiment * novelty * relevance * category_score;
if (sentiment < 30 and ns < 100) alpha = sentiment * novelty * relevance * category_score;
use the no-news stocks in the same industry for neutralization.
```

## Expected and Unexpected News

A seemingly good piece of news, if the information already is expected by the market and thus reflected in the price, will not cause a positive price movement. For example, a piece of news reads, "Earnings have large growth — 150% compared with last year." Analyzing this news usually gives positive sentiment. However, if the previous market consensus was that the company would grow 200%, the value in the news is below expectations and will cause the price to go down. Therefore, it can be helpful to use news data together with market consensus and market expectations. Textual analysis and calendar analysis can be useful in determining whether the news is a routine update or something different. Surprises and unexpected news and events usually result in larger price movements.

## Headlines and Full Text

Headlines usually contain the most important information and are well formatted, so they are easier to parse and analyze. Full text provides more detailed information, but it is harder to work with. One academic research paper shows an interesting result: most of the information in a paragraph is included in the first and last sentences. Similarly, we can focus more on the first and last paragraphs of an article, or the first and last few words. The paragraph structure and sentence structure also can contain valuable information.

## No News Is Good News?

There is an old saying: "No news is good news." This is true to some extent; news means change, events or something unusual happening, and markets hate uncertainty. News is also usually associated with higher volatility, higher volume, analyst revisions, and the expectation of more news. These aspects imply potential risks to the company. Because more and more firms are using news in their risk management models, institutional investors may reduce their holdings of companies that are frequently affected by news reports or even remove them from their portfolios. Because institutional investment flow tends to be positive for stock returns, this can lower returns.

**Example**

When there is an abnormal amount of news for a company, short the company.

## News Momentum

If the impact of news on a stock is not immediately and fully priced in by the market, the stock price may exhibit drift or momentum as the news becomes more widely known and understood. This effect is much stronger for smaller stocks because they are less closely observed, and for unexpected news. For large stocks and expected news, the price generally exhibits a reversal after an initial overshoot.

**Example**

For the first three days after the news release, hold a position in the same direction as the two-day stock returns for the two days prior to the news release; for the following five days, reverse the trade to capture the reversal.

## Social Media

In April 2013, a Twitter post by the Associated Press claimed there had been an explosion at the White House that injured President Obama. The tweet was false, but it caused a huge instant reaction in the market. From 1:08 p.m. to 1:10 p.m., the DJIA dropped more than 140 points. Though the index rebounded just as quickly, one fake Twitter event caused market losses of $136 billion. This case clearly shows the significant potential value of social media in algorithmic trading. Many data vendors are capturing this opportunity. Companies like Dataminr and PsychSignal provide millions of social data feeds on a daily basis. They also provide data to third-party vendors that create sentiment products used by many hedge funds.

The most popular social media platform for generating alphas is Twitter because it can be easily mapped to stocks (by checking the @ ticker symbol) and people (such as the CEOs of public companies). There is also increasing research based on online forums like Yahoo Finance message boards and StockTwits, blogs by professional investors and traders, Facebook, Glassdoor, and even Wikipedia.

Social media currently is a hot area in quant research. Essentially, social media can be viewed as news, but with much more volume and much more noise. Many of the ideas that work for news also can work for social media, but there are several challenges in applying sentiment analysis to the contents of social media. First, social media has a larger number of records and updates more quickly. Second, social media content usually is casual in format — a Twitter post, for instance, can contain a lot of abbreviations and poorly formatted words. This increases the difficulty of language processing. Third, how do we find original and important records? A lot of social media content is in response to news and has a smaller impact than more original social media content. Hence, there are many fake signals in social media, and that is why it is difficult to use social media for predictions.

**Example**

Use the frequency of tweets and the number of retweets to short companies being mentioned with increasing frequency (tweets about companies are mostly negative).

```
For each company, calculate the number of tweets that mentioned
the ticker symbol or company name on a particular day.
Get the number of retweets for each tweet and set it as t.
Set frequency = sum of log(t + 1).
Alpha = -time_series_rank(frequency, 1 month) ^ 0.5
```

## Conclusion

The quantity of news, social media content, and companies processing Big Data is increasing rapidly. More and more market participants are using automatic methods to analyze and trade this information. Therefore, the average impact of each piece of information on stock returns will likely decrease over time. To continue to find alphas in news, one will need to parse more news, find the most impactful news, filter noise, and adopt more advanced machine learning methods to learn and classify the news.
