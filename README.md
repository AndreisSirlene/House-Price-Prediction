
# 🏠 House-Price-Prediction 🧮

> “Experience is the name everyone gives to their mistakes.” – Oscar Wilde


# :pushpin: Table of Contents

* [Introduction](#memo-introduction)
* [Exploratory Data Analysis ](#rocket-exploratory-data-analysis)
* [Summary Statistics](#runner-summary-statistics)
* [Exploratory Visualizations](#tada-exploratory-visualizations)
* [Model Analysis](#construction_worker-model-analysis)
* [License](#closed_book-license)

# :memo: Introduction

Houses price is one of the criteria used to determine the country wealth or state of development, as average houses price differ from country to another, even differ from one area to another, so in our project we are trying to understand the houses market and determine the factors that affect the market and main while make the prices go up or down, also predict houses price by analysing our data set using regression model and other models.
Data is available here https://www.kaggle.com/swathiachath/kc-housesales-data

# :rocket: Exploratory Data Analysis 

We dropped columns we deemed were not useful such as ID and Zipcode, then the mode and cardinality of all categorical variables were calculated. 
Feature engineering yr_renovated by creating binary-categories [0, 1]. 


# :runner: Summary Statistics
* Chi square results
* One-way ANOVA Test
From the results of the one-way ANOVA test, by evaluating price against the categorical variables of house dataset, taking alpha level 0.05 as a standard measure, the results on the table above are presented. We can reject the null hypothesis of the independent variables ‘view’, ‘grade’ and ‘waterfront’ as their P-values are less than 0.05 and do not have significant differences.

# :tada: Exploratory Visualizations
Visualization of the mean, median and minimum value for the variable price
The normal distributed curve of the dependent variable (price) should have a symmetric distribution, however our variable is a positive skewed (to the right) because it has a long right tail, and the mean is also represented in the right side as the plot below shows.


# :construction_worker: Model Analysis
*Ridge Regression
*Lasso Regression
*Linear Regression Model
*PCA- Principal Component Analysis
*Logistic Regression


# :closed_book: License

Released in 2021.
This project is under the [MIT license](https://github.com/AndreisSirlene/House-Price-Prediction/blob/master/LICENSE).

Made with love by [Sirlene Andreis](https://github.com/AndreisSirlene) 💚🚀
