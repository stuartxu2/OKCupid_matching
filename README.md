# OKCupid_matching
This is the capstone project from [Galvanize Data Science Immersive](https://www.galvanize.com). 


#### -- Project Status: [Done]

## Project Intro/Objective
1. EDA on the OKCupid datasets, hypothesis testing to identify if gender is related to somking or not. 
2. Based on the essays of each user's profile, identify the MBTI personality of the user, and make the match for his/her ideal matches with the right personalities. 

### Methods Used
* Data Visualization
* Natural Language Processing
* Inferential Statistics
* Vectorization
* Logistic Regression, Random Forest, XG Boosting, Stochastic Gradient Descent Classifier, SVC Classifier

### Technologies
* Python
* pandas, numpy
* Scipy
* Scikit-learn
* NLTK
* matplotlib, seaborn

## Project Description

The OKCupid user profile dataset contains 31 columns with over 50,000 entries collected in 2012 in San Francisco area. You can find the dataset from here: [Albert Y. Kim's github](https://github.com/rudeboybert/JSE_OkCupid). 
The analysis focused on the demographic info of the single male and the single female, feature distribution of smokes, drugs usage, drinks, diet and body type, income disparities, etc. 

The 10 essay columns with self-introductory sentences are process with NLP tools to remove signs and stop words, so word use frequencies are calculated. 

The hypothesis test is based on the findings from smoke data, aiming to prove the different smoking habbit between single men and single women. 

The (MBTI) Myers-Briggs Personality Type Dataset includes a large number of people's MBTI type and content written by them. Since this is a labeled dataset, we can use it to train the model, and then apply the models to the OKCupid datasets to get the users' personalities. 


## Data Pipeline

1. Download the OKCupid dataset from [Albert Y. Kim's github](https://github.com/rudeboybert/JSE_OkCupid) and (MBTI) Myers-Briggs Personality Type Dataset from [Kaggle.com](https://www.kaggle.com/datasnaek/mbti-type)
2. remove the columns we do not need and clean the text.
3. Build up the model pipelines to train the model using the MBTI dataset. 
4. Choose the best performance model to apply to the OKCupid dataset, and get the personality for each user.
5. Get the matches for each user based on a preset matching rule. 


## Data Visualizations

Please see the notebook.


## Hypothesis Tests and results
H0: The single male and the single female who are dating have the same probability to smoke.

H1: The single male are more likely to smoke than the single female.


H0: p_m - p_f = 0

H1: p_m - p_f > 0

## Conclusion
EDA on OKCupid Dataset: 
1. There is difference in many aspects between the single male and single female. 🤪
2. A lot of single men are good at frisbee... (really?) 😆
3. Both of them think they are good at cooking. 🤨
4. Gay men have a much higher percentage of drug users than lesbians. 😱
5. Since we rejected the H0, we can say the single male are more likely to smoke than the single female. 🤔


## Next Step
1. include more features to make the matching system more comprehensive.
2. web app to apply the model to a production


## Contact
* Feel free to contact me if you think I'm doing something too stupid. 
