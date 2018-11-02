# Predicted Pre-owned Car Prices

### Project Luther

> #### Datasets
> Web scrapping from www.carmax.com
>  1.  1700 + webscraped data points
>  2.  30+ parameters



> #### Tools
>
> 1. Numpy
> 2. Pandas
> 3. Matplotlib
> 4. Seaborn
> 5. Selenium
> 6. Statsmodel
> 7. Sklearn
> 8. Powerpoint
> 9. Typora
> 10. Jupyter Notebooks



> #### Algorithms
>
> 1. Simple linear regression
> 2. Lasso and Ridge Regression
> 3. Cross-validation



> #### Modules 
>
> 1. **data_collection** - contains notebooks for web scrapping 
>
>    1. **grab_links.ipynb** 
>
>       This notebook goes to the carmax website and grabs basic information on the cars from their banners. We typically have 50 banners per page after which it goes to the next button to keep pulling 50 banners at a time automatically. Most importantly it grabs the stockno (viz the unique identifier for a car).  Using this stockno we can generate links to the car's individual page. 
>
>    2. **page_scrap.ipynb**
>
>       This notebook creates go to a car's individual page by generating the link "https://www.carmax.com/car/"+ str (stock_num). It goes to this page and scraps the key details such as miles, color and then clicks on "see all  specifications" which takes us to a detailed description of the car.
>
> 2. **data_cleaning** - notebooks for data_cleaning and encoding
>
>    1. clean_data.ipynb
>
>       Notebook that cleans all my data and outputs to final_data.csv
>
>    2. encoding_data.ipynb
>
>       This notebook reads the final_data.csv and prepares model_data.csv which can be used to run models. The notebook encodes categorical features such as 
>
>       - brand - luxury or not 
>       - interior_color - black or not
>       - exterior_color - dark colors (black, brown ..), light colors (white, silver ..), prime colors (red, gold,blue ..
>       - engine_type (normal, turbo or alternate)
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
>    1. final_data.csv - cleaned final data
>    2. model_data.csv - data ready for modelling
>
> 5. **docs** - documents 
>
>    1. Proposal - Proposal.pages / Proposal.pdf
>    2. Presentation - PREDICTING USED CAR PRICES.pdf
>    3. Summary - Summary.pages / Summary.pdf
>



> #### How to run ?
>
> 1. Run only the Module - "model" as the other modules/notebooks are related to web scrapping and
>     cleaning of the data. Their ouput is stored in the data files - final_data.csv and model_data.csv 

