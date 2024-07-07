# ConsciousCapital

ConsciousCapital aims to help beginner investors curate portfolios that align with their ESG values.

*This project was a part of HackTJ 2023 (Best Web Hack, 1x Sponsor Prize)(

## Inspiration 🔮 
Being an new investor can be difficult, especially when you're told to conduct extensive research on the income statements, news releases, and values of hundreds of companies. We aimed to make an easy tool that makes your own stock basket based on conscious values. These include environment, social, governance, controversy, gender, and racial diversity. *This makes the barrier to entry for people much lower.*

## What it does ⭐
Our website gather user data through a questionaire which asks client preferences regarding their values in environment, social good, governance, controversy, gender diversity, and racial diversity. We then match these values to companies listed on the Standard and Poor's 500 Index by minizming euclidean distance between vectors (similar to how the KNN model works).

We then filter the stocks based on which perform better, choosing stocks that have higher alpha metrics than the average, and lower beta metrics than the average. This means we aim to select stocks that have higher yield and lower risk than their counterpart stocks. 

Finally, we utilize award-winning Markowitzian portfolio theory, more specifically, the Mean-Variance theorem. This combined with L2 regularization allows us to calculate the asset/weight allocation for each stock in the portfolio, aiming to maximize the sharpe ratio (a measure of return compared to risk). 

## What's next for Conscious Capital 🏆
We want to explore different Markowitzian portfolio algorithms. Additionally, we want to extend the dataset and perhaps include more metrics to evaluate companies by.
