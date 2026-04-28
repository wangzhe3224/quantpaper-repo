# Chapter 3: Cutting Losses

**By Igor Tulchinsky**

*Source: Finding Alphas: A Quantitative Approach to Building Trading Strategies, Second Edition. Edited by Igor Tulchinsky et al., WorldQuant Virtual Research Center. © 2020 Tulchinsky et al., WorldQuant Virtual Research Center. Published 2020 by John Wiley & Sons, Ltd.*

---

Man is a creature that became successful because he was able to make sense of his environment and develop rules more effectively than his natural competitors could. In hunting, agriculture, and, later, mathematics and physics, rules proliferated. Today, rules abound in every area of life, from finance to science, from relationships to self-improvement regimens. Man survives because of rules.

An infinite number of possible rules describe reality, and we are always struggling to discover and refine them. Yet, paradoxically, there is only one rule that governs them all. That rule is: no rule ever works perfectly. I call it the **UnRule**.

It's an accepted scientific principle that no rule can really be proved — it can only be disproved. Karl Popper, the great Austrian philosopher of science, pointed this out in 1934. He argued that although it is impossible to verify a universal truth, a single counterinstance can disprove it. Popper stressed that because pure facts don't exist, all observations and rules are subjective and theoretical.

There are good reasons for this uncertainty. Reality is complicated. People and their ideas are imperfect. Ideas are expressed as abstractions, in words or symbols. Rules are just metaphorical attempts to bring order to this complex reality. Thus, every rule is flawed and no rule works all the time. No single dogma fully describes the world, but every rule describes some aspect of the world. And every rule works sometimes.

We are like artists slowly painting images on canvases. Every stroke may bring an image closer to reality, but the painting will never become a perfect interpretation of reality. There are many examples of this. Newton's laws, which for centuries seemed to describe motion perfectly, turned out to be flawed, giving way to Einstein's theory of relativity. Man's attempts to explain his place in the universe have continually evolved, from the belief that the earth was at the center of the cosmos to the realization that we are tiny, fragile beings adrift in a vast universe that eludes our full comprehension. Likewise, various rules have been asserted that purport to describe, even predict, financial markets, from the belief in strongly efficient markets to the development of option-pricing models. All of these have proved flawed, usually after market meltdowns.

So you see the paradox: the only rule that works is the one that says no rule always works. Rules are specks of dust, fragments of a larger reality.

This is the reason it's so important to be able to cut your losses when riding the often turbulent seas of the markets, where the UnRule prevails. How can this turbulence and change be weathered? What is the best way to deal with myriad shifting rules, all of them imperfect, many of them conflicting, based on different sets of circumstances and assumptions?

Trading is a microcosm of reality, a dynamic environment of profound complexity in which millions of participants act and react based on rules and beliefs that in turn feed back into and affect the larger environment. The challenge in trading is to derive rules that describe and predict markets, then to use them successfully to earn profits, without changing those markets in ways that might result in the destruction of the rule itself.

We represent trading rules as alphas, algorithms that seek to predict the future of securities returns. Managing millions of alphas, each reflecting some hypothesis about the markets, is a complicated matter and a subject unto itself. In dealing with millions of alphas, certain regularities become apparent. The best, most universal way of dealing with this complexity (and the fact that all rules eventually break down) is knowing when to cut your losses.

The concept of cutting trading losses has been around for a long time. It originated in what may be the oldest type of trading, so-called trend following, in which a trader bets that a rising (or falling) security will continue to rise (or fall). In such a scenario, trades typically are entered when a new high is reached and exited when the accumulated profits exceed some preset limits.

In today's trading world, alphas and strategies are seldom as simple as that. Instead of following a particular security, we apply trend following to the accumulated profit and loss of a strategy as a whole, which may consist of many individual alphas on many securities.

To put it plainly: cutting losses means abandoning rules that no longer work.

Although the logic of cutting losses is easy to see in trading, the principle also holds true in other parts of life, including business, entrepreneurship, and even relationships. Sometimes you just have to admit that whatever you're doing is not working out and move on.

Cutting losses requires discipline and the subjugation of your ego. Typically, emotion plays a big role in any kind of thinking and decision making. Neuroscientists have studied patients suffering from damage to the areas of the brain involved in processing emotions, who are unable to make simple decisions like choosing which shirt to put on in the morning. In our work developing and deploying alphas, we often are driven by emotional confidence. When we are devising a strategy, the process starts with: "I understand how the world works. I believe in my rule. Here is my rule." Because ego and pride are intertwined with this confidence, it may be difficult to let go of the rule that you've come up with, even in the face of evidence that the rule no longer works.

Perhaps the practice of cutting losses is not followed more widely for ego reasons. Or it may be that people lack knowledge of alternative rules that might work. The often high cost of changing a strategy can contribute to resistance to letting go of rules that no longer work.

It's wise to refrain from believing exclusively in any particular theory or rule. You can believe them all, but don't embrace any of them completely. Sometimes they work; sometimes they don't. The best indicator of whether a rule is good is how well it's working at that moment. The rest is speculation. If a rule works, we invest in it; if it doesn't, we don't.

We collect all ideas and let time and performance show what works and what doesn't — and when it works and when it doesn't. When we postulate a new idea, rule, or alpha based on historical data and thorough statistical analysis (sometimes with a touch of fundamental wisdom), it then goes into our knowledge base. From this universe of ideas, we seek to construct the closest thing possible to a depiction of financial reality. But to do what we do, we have to be comfortable with the fact that we will never know everything there is to know.

The old saying is that in the land of the blind, the one-eyed man is king. We live in the land of the blind. Particularly in trading and financial markets, accepting that blindness and effectively using that one good eye is a big advantage.

## How to Apply the Principle of the UnRule to Cutting Losses

We acknowledge that the number of imperfect ideas is unbounded and that reality is unknown and unknowable. But each imperfect idea does describe reality a bit, so the more alphas we possess, the better we can describe an aspect of reality, and the closer we can come to having "one eye" with which we can seek to increase profits.

Because no rule is perfect, a combination of all rules may come as close to perfection as possible.

Applying all rules in tandem is a key to success. For example, to cross the street, you might have the following three rules in mind:

1. Look left, look right, look left again, then it is safe to cross.
2. If you hear a loud noise, turn in the direction of the noise.
3. If you see a car headed toward you, run!

You may start crossing the street believing in and comforted by Rule 1, then hear a horn honking, which triggers Rule 2. Rule 1 should be abandoned immediately because the safety conclusion has been challenged by the noise. Then you apply Rule 3.

This has the following implications:

- It is necessary to come up with as many good rules as possible.
- No single rule can ever be relied upon completely.
- It is necessary to develop a strategy for using rules simultaneously.

How do you know when an investment strategy isn't working? When the strategy performs outside its expected returns. This usually is accompanied by the following signals:

- A drawdown exceeds the typical drawdowns observed previously.
- The strategy's Sharpe ratio falls significantly.
- Rules that were initially observed in historical simulation are no longer valid in live trading.

It is important to pursue different strategies simultaneously and to shift your efforts into those that are working. Suppose you have a theory describing when gold prices will rise. The theory works 50% of the time. Suppose you have 10 other equally solid theories. A combination of theories should describe reality better than any one of them. And the best way to manage which one of them is most accurate is by observing which ones are working at the moment.

Then comes the discipline of cutting losses.

When a strategy stops working, determine the belief that initially motivated the activity. If the belief was obviously false, you are playing with dice. Best to terminate the activity and engage in more productive efforts.

Say you hire someone to renovate your house. They promise to do the job for $50,000, but less than halfway through the project they've already spent $45,000. At this point, you should cut that builder loose if switching to a new one can be done cheaply enough.

Suppose we are engaged in an activity — let's call it X — that starts to lose money. The activity can be anything, perhaps a trading strategy or a business. We need to ask the following questions:

- Am I losing money in activity X?
- What is the maximum acceptable loss? (Call the maximum acceptable loss Y.)
- What is the observed loss amount? (Call the observed loss Z.)

Before starting activity X, we should identify the maximum acceptable loss, Y. If the observed loss, Z, exceeds the maximum acceptable loss, Y, and the exit cost is not too high, cut the loss.

## Summary

Examine each potential action before embarking on it. Determine:

- What's the objective?
- What are the normal, expected difficulties?

Plan in advance how to get out of the strategy cheaply.

Pursue multiple strategies simultaneously.

Cut all strategies that fall outside expectations.
