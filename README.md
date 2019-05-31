# OKCupid_EDA
This project is the first part of the Capstone Project from [Galvanize Data Science Immersive](https://www.galvanize.com). 

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is using different tools to clean the dataset, do the exploratory data analysis, and do the hypothesis testing based on the findings during the EDA.

### Methods Used
* Natural Language Processing
* Inferential Statistics
* Data Visualization

### Technologies
* Python
* Pandas, numpy, jupyter
* scipy

## Project Description
The OKCupid user profile dataset contains 31 columns with over 50,000 entries collected in 2012 in San Francisco area. You can find the dataset from here: [Albert Y. Kim's github](https://github.com/rudeboybert/JSE_OkCupid). 
The analysis focused on the demographic info of the single male and the single female, feature distribution of smokes, drugs usage, drinks, diet and body type, income disparities, etc. 

The 10 essay columns with self-introductory sentences are process with NLP tools to remove signs and stop words, so word use frequencies are calculated. 

The hypothesis test is based on the findings from smoke data, aiming to prove the different smoking habbit between single men and single women. 


## Data Pipeline
1. Download the dataset from [Albert Y. Kim's github](https://github.com/rudeboybert/JSE_OkCupid).
2. Quickly check the dataset info. 
3. Check the missing values, duplicated rows, etc. 
4. Since we are going to focus on the text columns so the text columns are processed with nltk. 


## Data Visualizations




## Hypothesis Tests and results
$H_0$: The single male and the single female who are dating have the same probability to smoke.

$H_1$: The single male are more likely to smoke than the single female.


$$ p_m = P(\text{the male smoke}) $$
$$ p_f = P(\text{the female smoke}) $$


$$ H_0: \ p_m - p_f = 0 $$

$$ H_1: \ p_m - p_f > 0$$


## Contact
* Feel free to contact me if you think I'm doing something too stupid. 