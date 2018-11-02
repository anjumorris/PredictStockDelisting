# Predict Stock Market Delisting in India 

### Project McNulty

> #### Datasets
> Financial Statement data from Prowess Dx, India
>
> Stock Market data from Prowess Dx, India
>
> Company Identity data from Prowess Dx, India 
>
>  1.  4770 data point (class 0 = 4295, class 1 = 475 )
>  2.  92 features



> #### Tools
>
> 1. Numpy
> 2. Pandas
> 3. Matplotlib
> 4. Seaborn
> 5. Flask
> 6. Javascript
> 7. HTML
> 8. Tableau
> 9. Statsmodel
> 10. Sklearn
> 11. Powerpoint
> 12. Typora
> 13. Jupyter Notebooks



> #### Algorithms
>
> 1. K- nearest neighbors
> 2. Logistic Regression
> 3. Support Vector Machine
> 4. Decision Trees
> 5. Random Forest
> 6. Gradient Boosting
> 7. Principle Component Analysis



> #### Modules 
>
> 1. **clean_restructure** - contains notebooks for cleaning data and restructuring for modeling
>
>    1. **identity_clean_data.ipynb** 
>
>       Notebook to clean the list of company identities and find out which ones were listed and which ones were delisted
>
>    2. **financial_statements_clean.ipynb**
>
>       Notebook to clean the financial statements for our companies of interest. These are financial statement data ie information from balance sheets, income statement etc. for different years for all companies 
>
>    3. **market_data_clean.ipynb**
>
>       Clean stock market data and aggregate at annual level for each company
>
>    4. **make_model_data**
>
>       Notebook to combine financial data, market data, and setup features which will be used by the model. We will be setting our target 'delisted' as 0 - company is still listed 1 - company delisted
>       Listed Companies - We take data from 2017 Delisted Companies - Companies that were delisted from 2015 onwards we look at their last available information.
>
> 2. **model** - notebooks for data_cleaning and encoding
>
>    1. **model.ipynb**
>
>       Notebook for trying out various modeling algorithmns
>
>    2. **use_final_model.ipynb**
>
>       This is a notebook that loads the final pickled model and uses it with data from 2018 to predict which companies may delist and which companies are safe. 
>
> 3. **model**
>
>    1. **explore_correlations.ipynb**
>
>       Explore  the data, look at correlations and try feature engineering
>
>    2. **model_1_linear_regression.ipynb**
>
>       Prepare multiple linear regression models and figure out which feature to remove / transform.
>
>    3. **model_2_final.ipynb**
>
>       Lasso and Ridege crossvalidation, compare several models and select best model. Test the model.
>
> 4. **data** - all csv files
>
>    1. model_data_india.csv - data ready for modeling
>    2. crystal_ball_web_ready.csv - data from 2018 to be used in the app for predicting future outcomes
>
> 5. **templates**
>
>    1. Index.html - landing page for flask app
>
> 6. **app.py** 
>
>    1. Flask app for predicting delisting
>
> 7. **docs** - documents 
>
>    1. Proposal - Proposal_McNulty.pdf
>
>    2. Presentation - PredictDelisting.pdf
>
>    3. Summary - Summary_Predict_Delisting.pdf
>
>



> #### How to run ?
>
> 1. Run only the Module - "model" as the other modules/notebooks are related to web scrapping and cleaning of the data. 
> 2. Run flask app -> python app.py

