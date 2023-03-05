# ConsciousCapital

#### ConsciousCapital aims to help beginner investors curate portfolios that align with their values.

_THIS PROJECT WAS A PART OF HACKTJ2023_

## Inspiration 🔮 
Being an new investor can be difficult, especially when you're told to conduct extensive research on the income statements, news releases, and values of hundreds of companies. We aimed to make an easy tool that makes your own stock basket based on conscious values. These include environment, social, governance, controversy, gender, and racial diversity. *This makes the barrier to entry for people much lower.*

## What it does ⭐
Our website gather user data through a questionaire which asks client preferences regarding their values in environment, social good, governance, controversy, gender diversity, and racial diversity. We then match these values to companies listed on the Standard and Poor's 500 Index by minizming euclidean distance between vectors (similar to how the KNN model works).

We then filter the stocks based on which perform better, choosing stocks that have higher alpha metrics than the average, and lower beta metrics than the average. This means we aim to select stocks that have higher yield and lower risk than their counterpart stocks. 

Finally, we utilize award-winning Markowitzian portfolio theory, more specifically, the Mean-Variance theorem. This combined with L2 regularization allows us to calculate the asset/weight allocation for each stock in the portfolio, aiming to maximize the sharpe ratio (a measure of return compared to risk). 

## What's in this Repo? 📑

1. static - Folder of CSS formatting and background images
2. templates - Folder of HTML web development files
3. doctorReturn.py - Returns a list of doctors and medical specialists for a specific disease
4. doctorOutput.py - Returns the type of doctor that would treat a given disease with an input of its symptoms
5. finalized_modevl.sav - The trained SVC model
6. main.py - The FLASK file which connects all components of this project

## What's next for Doctor Direct 🏆
Currently, we recognize 42 medical conditions and 132 symptoms. We plan to expand the symptoms and medical conditions to cover a greater range including physical injuries and mental illnesses. Additionally, we can continue to expand onto our website, linking APIs from hospitals directly to our services. This would allow for a more ubiquitous and thorough service. 
