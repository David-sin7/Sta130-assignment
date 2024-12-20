#!/usr/bin/env python
# coding: utf-8

# # STA130 Homework 08
# 
# Please see the course [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) for the list of topics covered in this homework assignment, and a list of topics that might appear during ChatBot conversations which are "out of scope" for the purposes of this homework assignment (and hence can be safely ignored if encountered)

# <details class="details-example"><summary style="color:blue"><u>Introduction</u></summary>
# 
# ### Introduction
#     
# A reasonable characterization of STA130 Homework is that it simply defines a weekly reading comprehension assignment. 
# Indeed, STA130 Homework essentially boils down to completing various understanding confirmation exercises oriented around coding and writing tasks.
# However, rather than reading a textbook, STA130 Homework is based on ChatBots so students can interactively follow up to clarify questions or confusion that they may still have regarding learning objective assignments.
# 
# > Communication is a fundamental skill underlying statistics and data science, so STA130 Homework based on ChatBots helps practice effective two-way communication as part of a "realistic" dialogue activity supporting underlying conceptual understanding building. 
# 
# It will likely become increasingly tempting to rely on ChatBots to "do the work for you". But when you find yourself frustrated with a ChatBots inability to give you the results you're looking for, this is a "hint" that you've become overreliant on the ChatBots. Your objective should not be to have ChatBots "do the work for you", but to use ChatBots to help you build your understanding so you can efficiently leverage ChatBots (and other resources) to help you work more efficiently.<br><br>
# 
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Instructions</u></summary>
# 
# ### Instructions
#     
# 1. Code and write all your answers (for both the "Pre-lecture" and "Post-lecture" HW) in a python notebook (in code and markdown cells) 
#     
# > It is *suggested but not mandatory* that you complete the "Pre-lecture" HW prior to the Monday LEC since (a) all HW is due at the same time; but, (b) completing some of the HW early will mean better readiness for LEC and less of a "procrastentation cruch" towards the end of the week...
#     
# 2. Paste summaries of your ChatBot sessions (including link(s) to chat log histories if you're using ChatGPT) within your notebook
#     
# > Create summaries of your ChatBot sessions by using concluding prompts such as "Please provide a summary of our exchanges here so I can submit them as a record of our interactions as part of a homework assignment" or, "Please provide me with the final working verson of the code that we created together"
#     
# 3. Save your python jupyter notebook in your own account and "repo" on [github.com](github.com) and submit a link to that notebook though Quercus for assignment marking<br><br>
# 
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Prompt Engineering?</u></summary>
#     
# ### Prompt Engineering? 
#     
# The questions (as copy-pasted prompts) are designed to initialize appropriate ChatBot conversations which can be explored in the manner of an interactive and dynamic textbook; but, it is nonetheless **strongly recommendated** that your rephrase the questions in a way that you find natural to ensure a clear understanding of the question. Given sensible prompts the represent a question well, the two primary challenges observed to arise from ChatBots are 
# 
# 1. conversations going beyond the intended scope of the material addressed by the question; and, 
# 2. unrecoverable confusion as a result of sequential layers logial inquiry that cannot be resolved. 
# 
# In the case of the former (1), adding constraints specifying the limits of considerations of interest tends to be helpful; whereas, the latter (2) is often the result of initial prompting that leads to poor developments in navigating the material, which are likely just best resolve by a "hard reset" with a new initial approach to prompting.  Indeed, this is exactly the behavior [hardcoded into copilot](https://answers.microsoft.com/en-us/bing/forum/all/is-this-even-normal/0b6dcab3-7d6c-4373-8efe-d74158af3c00)...
# 
# </details>

# ### Marking Rubric (which may award partial credit)
# - [0.1 points]: All relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] are reported within the notebook
# - [0.2 points]: Well-communicated and sensible answers for Question "2"
# - [0.2 points]: Correct code and well-communicated correct answer for Question "4" 
# - [0.2 points]: Correct calculations for requested metrics in Question "6" 
# - [0.3 points]: Correct and well-communicated explanation of differences for Question "7" 
# <!-- - [0.1 points]: Written submission evaluation and enagement confirmation with ChatBot summaries for "8", "10"-->
# 
# 

# ## "Pre-lecture" HW [*completion prior to next LEC is suggested but not mandatory*]

# 
# ### 1. Start a ChatBot session to understand what a *Classification Decision Tree* is: (a) ask the ChatBot to describe the type of problem a *Classification Decision Tree* addresses and provide some examples of real-world applications where this might be particularly useful, and then (b) make sure you understand the difference between how a *Classification Decision Tree* makes *(classification) predictions* versus how *Multiple Linear Regression* makes *(regression) predictions*<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _The first part (a) of this question is looking for you to understand the difference between **classification** and **regression**. The second part (b) of the questions is looking for a fairly high level understanding of the general nature of a decision tree and how it is based on making sequential decisions down the *nodes* of *tree* in order to eventually make a final prediction. This part (b) is essentially the **Classification Decision Tree** analog of "explain how the **linear form** makes a prediciton in **Multiple Linear Regression** generally speaking"; namely,"explain how the **tree** makes a prediciton in a **Classification Decision Tree** generally speaking"._
# > 
# > _**If you're struggling with this, it would probably be most helpful to go search for and some images of example decision trees to look at!**_
# > 
# > - _You may be beginning to realize or will nonetheless eventually come to understand that the sequential decisions at each stage of the **Decision Tree** are **interactions** (in the same manner as **interactions** in **Multiple Linear Regression**.  Once you start to see that and it's making sense to you then you'll increasingly appreciate how **complex** **Decision Tree** models can be, even though they're pretty simple to understand if you just look at one._
# >
# > ---
# >    
# > _When using chatbots, it's often more effective (and enjoyable) to ask concise, single questions rather than presenting complex, multi-part queries. This approach can help in obtaining clearer and more specific responses (that might be more enjoyable to interact with). You can always ask multi-part questions as a series of additional sequential questions. With this approach, chatbots may not automatically reiterate previously explained concepts. So if you need a refresher or further explanation on a topic discussed earlier, just explicitly request during follow-up interactions._
# > 
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#     
# </details>

# A Classification Decision Tree is a supervised learning method designed for addressing classification tasks. Its purpose is to predict a categorical (discrete) target variable using input features. The algorithm splits the dataset into smaller groups based on the values of the features, eventually classifying each data point into a particular category or class. For example, in health care area, it can Predict whether a tumor is benign or malignant.
# 

# Summary: 
# You asked about the type of problem a Classification Decision Tree addresses and its real-world applications. I explained that it solves classification problems, predicting categorical outcomes based on input features. I provided several examples of applications, including healthcare (disease diagnosis), customer segmentation, credit risk assessment, fraud detection, spam filtering, education (predicting student outcomes), human resources (job candidate suitability), medical trials, image recognition, and retail (customer purchasing behavior).]
# 
# Link:
# https://chatgpt.com/share/673c0eba-1bf0-8004-8af3-a76a39191668

# ### 2. Continue your ChatBot session and explore with your ChatBot what real-world application scenario(s) might be most appropriately addressed by each of the following *metrics* below: provide your answers and, in your own words, *concisely explain your rationale for your answers.*<br>
# 
# 
# 1. **Accuracy** measures the proportion of true results (both true positives and true negatives) in the population.
# 
# $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
#     
# 2. **Sensitivity** measures the proportion of actual positives that are correctly identified.
# 
# $$\text{Sensitivity} = \frac{TP}{TP + FN}$$
# 
# 3. **Specificity** measures the proportion of actual negatives that are correctly identified.
# 
# $$\text{Specificity} = \frac{TN}{TN + FP}$$
# 
# 4. **Precision** measures the proportion of positive identifications that were actually correct.
# 
# $$\text{Precision} = \frac{TP}{TP + FP}$$
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _This question could be restated as, "Give examples of real-world examples where each of these **metrics** would be particularly useful."_
# >
# > _The primary objective here is to understand the distinction between each of these **metrics**. The secondary objective is to notice how the nature of the decision-making that each of these **metrics** most naturally supports is very distinct, ideally based on identifying memorable examples that really distinguish between the **metrics**._
# >
# > - _Have a look at this (greatly expanded) handy list of additional metrics, formulas, and synonyms at the following [wikipedia page](https://en.wikipedia.org/wiki/Sensitivity_and_specificity) if you want this to get real crazy real fast._
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#     
# </details>

# 1. accuracy: Predicting customer satisfaction in an e-commerce survey
# 2. sensitvity: it can use for medical Diagnostics, like detect disease like covid-19. 
#     Reason: In these scenarios, failing to identify an actual positive case could have critical, even life-altering, consequences. Sensitivity ensures that the system errs on the side of caution, even if it means generating some false positives.
# 3. Specificity: focuses on minimizing False Positives, ensuring that actual negative cases are not incorrectly classified as positive.
#     scene: Ensuring legitimate emails are not flagged as spam.
#     reason: Specificity ensures that the system avoids falsely labeling negative cases as positives, which could lead to unnecessary costs, wasted resources, or harm to individuals due to incorrect classifications. It complements Sensitivity, striking a balance depending on the application.
# 4. precision: Precision evaluates how many of the predicted positives are truly positive.
#     scene: it ensures only patients who truly need the treatment are recommended, avoiding undue risks for those who don’t\
#     reason: Precision is critical in scenarios where false positives have significant consequences, such as unnecessary costs, wasted resources, or harm to individuals. By focusing on correctly identifying positives, it helps improve the reliability of predictions in such cases.
# 
# Summary: 
# 
# In this conversation, we explored the metrics used to evaluate classification models, focusing on their definitions, formulas, and real-world applications:
# 
# Sensitivity (Recall): Measures the proportion of actual positives correctly identified. It's important in applications like medical diagnostics and security systems, where missing a positive case can have critical consequences.
# 
# Specificity: Measures the proportion of actual negatives correctly identified. It is crucial in scenarios like spam filtering and rare disease screening to minimize false positives and unnecessary actions.
# 
# Precision: Measures the proportion of positive predictions that were correct. It is vital in applications like fraud detection, high-risk medical treatments, and targeted advertising, where false positives can be costly or harmful.
# 
# Each metric's value depends on the specific problem context and the trade-offs between false positives and false negatives. Overall, these metrics guide model evaluation and selection based on application needs.
# 
# link:
# https://chatgpt.com/share/673c0eba-1bf0-8004-8af3-a76a39191668

# ### 3. Explore the amazon books dataset, seen previously at the start of the semester, providing some initital standard *exploratory data analysis (EDA)* and data summarization after pre-processing the dataset to meet the requirements below<br>
# 
#  1. remove `Weight_oz`, `Width`, and `Height` 
#  2. drop all remaining rows with `NaN` entries 
#  3. set `Pub year` and `NumPages` to have the type `int`, and `Hard_or_Paper` to have the type `category`
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _`NaN` entries can't be used in their raw form with the `scikit-learn` methodologies, so we do need to remove them to proceed with our analyses._
# >     
# > _Only remove rows with `NaN` entries once you've subset to the columns you're interested in. This will minimize potentially unnecessary data loss..._
# >
# > _It would be possible to consider imputing missing data to further mitigate data loss, but the considerations for doing so are more advanced than the level of our course, so we'll not consider that for now._ 
# 
# </details>

# In[7]:


import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, recall_score, make_scorer
import graphviz as gv

url = "https://raw.githubusercontent.com/pointOfive/STA130_F23/main/Data/amazonbooks.csv"
ab = pd.read_csv(url, encoding="ISO-8859-1")
# create `ab_reduced_noNaN` based on the specs above


# In[8]:


# Drop rows with missing values
ab_reduced_noNaN = ab.dropna()

# Display the first few rows to inspect the cleaned dataset
print(ab_reduced_noNaN.head())
print(f"Shape of cleaned dataset: {ab_reduced_noNaN.shape}")


# In[11]:


# Step 1: Preprocess the Dataset
# Drop unnecessary columns
ab_reduced = ab.drop(columns=["Weight_oz", "Width", "Height"])

# Drop rows with NaN entries
ab_reduced_noNaN = ab_reduced.dropna()

# Convert columns to the specified types
ab_reduced_noNaN['Pub year'] = ab_reduced_noNaN['Pub year'].astype(int)
ab_reduced_noNaN['NumPages'] = ab_reduced_noNaN['NumPages'].astype(int)
ab_reduced_noNaN['Hard_or_Paper'] = ab_reduced_noNaN['Hard_or_Paper'].astype('category')

# Display the cleaned dataset's structure
print(ab_reduced_noNaN.info())
print(f"Shape of cleaned dataset: {ab_reduced_noNaN.shape}")

# Step 2: Initial EDA
# Summary statistics for numerical columns
print("Summary statistics for numerical columns:")
print(ab_reduced_noNaN[['Pub year', 'NumPages']].describe())

# Distribution of `Hard_or_Paper`
print("\nDistribution of Hard_or_Paper:")
print(ab_reduced_noNaN['Hard_or_Paper'].value_counts())

# Visualization
import matplotlib.pyplot as plt

# Plot the distribution of publication years
plt.hist(ab_reduced_noNaN['Pub year'], bins=20, edgecolor='k', alpha=0.7)
plt.title("Distribution of Publication Year")
plt.xlabel("Publication Year")
plt.ylabel("Frequency")
plt.show()

# Plot the distribution of number of pages
plt.hist(ab_reduced_noNaN['NumPages'], bins=20, edgecolor='k', alpha=0.7)
plt.title("Distribution of Number of Pages")
plt.xlabel("Number of Pages")
plt.ylabel("Frequency")
plt.show(renderer="png")


# In[ ]:





# 

# ### 4. Create an 80/20 split with 80% of the data as a training set *ab_reduced_noNaN_train* and 20% of the data testing set  *ab_reduced_noNaN_test* using either *df.sample(...)* as done in TUT or using *train_test_split(...)* as done in the previous HW, and report on how many observations there are in the training data set and the test data set.<br><br>Tell a ChatBot that you are about to fit a "scikit-learn" *DecisionTreeClassifier* model and ask what the two steps given below are doing; then use your ChatBots help to write code to "train" a classification tree *clf* using only the *List Price* variable to predict whether or not a book is a hard cover or paper back book using a *max_depth* of *2*; finally use *tree.plot_tree(clf)* to explain what *predictions* are made based on *List Price* for the fitted *clf* model
# 
# ```python
# y = pd.get_dummies(ab_reduced_noNaN["Hard_or_Paper"])['H']
# X = ab_reduced_noNaN[['List Price']]
# ```
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _To complete the final 80/20 split of the **observations** in a reproducible way, set a "random seed"._ 
# > 
# > - _A single **observation** consists of all the measurements made on a single entity, typically corresponding to a row of a data frame. In **Machine Learning**, a collection of values of interest measured for a single entity is called a "vector" and so the **observation** is referred to as a **vector**_.
# >    
# > _Asking the ChatBot about "DecisionTreeClassifier .fit(...)" can be helpful here..._
# > 
# > _Should you use the "ab_reduced_noNaN" data, or the "ab_reduced_noNaN_train" data, or the "ab_reduced_noNaN_test" data to initially fit the classification tree? Why?_
# >    
# > _You can visualize your decision tree using the `tree.plot_tree(clf)` function shown in the `sklearn` documentation [here](
# https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#what-is-the-values-array-used-here) and [here](https://scikit-learn.org/stable/modules/tree.html); but, to make it more immediately readible it might be better to use `graphviz`, which is demonstrated in the `sklearn` documentation [here](https://scikit-learn.org/stable/modules/tree.html#alternative-ways-to-export-trees)_ 
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#     
# </details>

# Training dataset (ab_reduced_noNaN_train): 1047 observations
# Testing dataset (ab_reduced_noNaN_test): 262 observations

# y = pd.get_dummies(ab_reduced_noNaN["Hard_or_Paper"])['H']
# X = ab_reduced_noNaN[['List Price']]
# 
# These two steps are preparing the data for training a machine learning model by creating the features (input variables) and target (output variable) in a format that the model can use

# In[10]:


# Step 1: Create an 80/20 split
from sklearn.model_selection import train_test_split

# Define the target variable
y = pd.get_dummies(ab_reduced_noNaN["Hard_or_Paper"])['H']  # 'H' for Hard Cover

# Define the feature variable (only List Price)
X = ab_reduced_noNaN[['List Price']]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the number of observations in each set
print(f"Training set size: {X_train.shape[0]} observations")
print(f"Testing set size: {X_test.shape[0]} observations")

# Step 2: Fit a DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Initialize the classifier with max_depth=2
clf = DecisionTreeClassifier(max_depth=2, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Visualize the decision tree
plt.figure(figsize=(10, 6))
tree.plot_tree(clf, feature_names=['List Price'], class_names=['Paperback', 'Hardcover'], filled=True)
plt.title("Decision Tree for Predicting Hard Cover vs Paperback")
plt.show(renderer="png")


# Summary: 
# Dataset Exploration and Preprocessing:
# 
# You are working with the Amazon Books dataset.
# The task required initial preprocessing by:
# Removing specific columns (Weight_oz, Width, and Height).
# Dropping rows with missing values (NaN).
# Converting Pub year and NumPages to integers and Hard_or_Paper to a categorical type.
# 80/20 Data Split:
# 
# We performed an 80/20 split of the dataset into training (ab_reduced_noNaN_train) and testing (ab_reduced_noNaN_test) sets.
# The training dataset contained 1047 observations, and the testing dataset had 262 observations.
# Preparing Features and Target:
# 
# The target variable (y) was derived from the Hard_or_Paper column using one-hot encoding, resulting in a binary classification:
# 1 for Hardback
# 0 for Paperback.
# The feature variable (X) included only the List Price column.
# Classification Tree Model:
# 
# A decision tree classifier (clf) was trained using the List Price variable to predict whether a book is hardback or paperback.
# The tree's depth was limited to 2 to keep the model interpretable.
# Visualization of the decision tree was to be done using tree.plot_tree to understand how the classifier made decisions based on List Price.
# Technical Issues:
# 
# A reset in the environment led to the loss of access to the dataset and prior variables.
# Attempts to reload the dataset from the provided URL failed due to connectivity issues.
# Next Steps:
# 
# To continue, we need access to the dataset. You could:
# Provide the dataset file directly.
# Verify the dataset URL's accessibility or upload the file here.
# 
# 
# Link:https://chatgpt.com/share/673c38ae-9ee4-8004-a93d-f9b64029862f

# <details class="details-example"><summary style="color:blue"><u>Continue now...?</u></summary>
# 
# ### Pre-lecture VS Post-lecture HW
# 
# Feel free to work on the "Post-lecture" HW below if you're making good progress and want to continue: for **HW 08** this could be reasonable because, as you'll see, the process of creating and using **classification decision trees** is quite similar to the process for creating and using **multiple linear regression** models. There are differences of course, such as how there is **coefficient hypothesis testing** in **multiple linear regression** and **confusion matrices** in **classification decision trees**, and so on. But you would very likely be able to leverage the silarities to make a lot of progress with **classification decision trees** based on your experience with **multiple linear regression**.
#     
# *The benefits of continue would are that (a) Consolidate the knowledge already learned and integrate it comprehensively. (b) Let you build experience interacting with ChatBots (and understand their strengths and limitations in this regard)... it's good to have sense of when using a ChatBot is the best way to figure something out, or if another approach (such as course provided resources or a plain old websearch for the right resourse) would be more effective*
#     
# </details>    

# ## "Post-lecture" HW [*submission along with "Pre-lecture" HW is due prior to next TUT*]
# 

# ### 5. Repeat the previous problem but this time visualize the *classification decision tree* based on the following specifications below; then explain generally how predictions are made for the *clf2* model<br>
# 
# 1. `X = ab_reduced_noNaN[['NumPages', 'Thick', 'List Price']]`
# 2. `max_depth` set to `4`
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > - _Use the same **train/test split** dataset used so far_
# > - _Train the **classification decision tree** `clf2` using **predictor variables** `NumPages`, `Thick` and `List Price`_ 
# > - _Again **predict** whether or not a book is hard cover book or a paper back book_
# > - _You can visualize your decision tree using the `tree.plot_tree(clf)` function shown in the `sklearn` documentation [here](
# https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#what-is-the-values-array-used-here) and [here](https://scikit-learn.org/stable/modules/tree.html); but, to make it more immediately readible it might be better to use `graphviz`, which is demonstrated in the `sklearn` documentation [here](https://scikit-learn.org/stable/modules/tree.html#alternative-ways-to-export-trees)_
# >
# > _If you are interested in how to find the best `max_depth` for a tree, ask ChatBot about "GridSearchCV"_
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#     
# </details>

# The `clf2` model uses a decision tree with three features—`NumPages`, `Thick`, and `List Price`—to classify books as either hardback or paperback. Decision trees make predictions by splitting the data into subsets based on thresholds for the predictor variables. For this model, the tree's depth is capped at 4 (`max_depth=4`), limiting the number of splits to ensure interpretability and reduce overfitting.
# 
# At each node, the model evaluates a feature, such as whether `List Price <= 20`, and branches based on the result. This process continues until a terminal "leaf" node is reached, which contains the predicted class based on the majority of data points in that subset. For instance, a book with `List Price = 10`, `NumPages = 150`, and `Thick = 1.2` might follow the left branches and be classified as paperback.
# 
# The `max_depth` parameter ensures the tree does not grow overly complex, balancing accuracy and generalizability. Visualizations, such as `plot_tree` or Graphviz diagrams, clearly depict the decision process, showing thresholds and predictions at each node.
# 
# Overall, the `clf2` model demonstrates how decision trees segment data hierarchically, using simple rules to classify books effectively based on their physical and price-related attributes.

# In[12]:


# Step 1: Create an 80/20 split
from sklearn.model_selection import train_test_split

# Define the target variable
y = pd.get_dummies(ab_reduced_noNaN["Hard_or_Paper"])['H']  # 'H' for Hard Cover

# Define the feature variable (only List Price)
X = ab_reduced_noNaN[['List Price']]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Check the number of observations in each set
print(f"Training set size: {X_train.shape[0]} observations")
print(f"Testing set size: {X_test.shape[0]} observations")

# Step 2: Fit a DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Initialize the classifier with max_depth=2
clf = DecisionTreeClassifier(max_depth=2, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Visualize the decision tree
plt.figure(figsize=(10, 6))
tree.plot_tree(clf, feature_names=['List Price'], class_names=['Paperback', 'Hardcover'], filled=True)
plt.title("Decision Tree for Predicting Hard Cover vs Paperback")
plt.show()


# Summary: 
# In this conversation, we explored the creation, training, and visualization of a decision tree classification model (clf2) to predict whether a book is a hardback or paperback. The features used were NumPages, Thick, and List Price, with a maximum tree depth of 4 to ensure interpretability and prevent overfitting.
# 
# Link: https://chatgpt.com/share/673c38ae-9ee4-8004-a93d-f9b64029862f

# ### 6. Use previously created *ab_reduced_noNaN_test* to create confusion matrices for *clf* and *clf2*. Report the sensitivity, specificity and accuracy for each of the models<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Hopefully you immediately thought to ask ChatBot to help you with this problem, but if you did you should take time to make sure you're clear about the key components of what the ChatBot is providing for you. You might want to know_
# > - _what is a "positive" and what is a "negative"_
# > - _how to read an `sklearn` confusion matrix_
# > - _what leads to TP, TN, FP, and FN_
# > - _whether `y_true` or `y_pred` go first in the `confusion_matrix` function_   
# >
# > _Have the visualizations you make use decimal numbers with three signifiant digits, such as `0.123` (and not as percentages like `12.3%`), probably based on `np.round()`_
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#        
# </details>

# In[16]:


# Step 1: Define predictors with all required columns
X = ab_reduced_noNaN[['NumPages', 'Thick', 'List Price']]  # Ensure all columns exist
y = pd.get_dummies(ab_reduced_noNaN["Hard_or_Paper"])['H']  # Target variable

# Step 2: Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Generate predictions for clf and clf2
y_pred_clf = clf.predict(X_test[['List Price']])  # clf uses only List Price
y_pred_clf2 = clf2.predict(X_test)  # clf2 uses all three features

# Step 4: Compute confusion matrices
cm_clf = confusion_matrix(y_test, y_pred_clf)
cm_clf2 = confusion_matrix(y_test, y_pred_clf2)

# Step 5: Visualize confusion matrices
disp_clf = ConfusionMatrixDisplay(confusion_matrix=cm_clf, display_labels=['Paperback', 'Hardcover'])
disp_clf.plot(cmap='Blues', values_format=".3f")
plt.title("Confusion Matrix for clf")
plt.show()

disp_clf2 = ConfusionMatrixDisplay(confusion_matrix=cm_clf2, display_labels=['Paperback', 'Hardcover'])
disp_clf2.plot(cmap='Blues', values_format=".3f")
plt.title("Confusion Matrix for clf2")
plt.show()

# Step 6: Calculate and display metrics
# Metrics for clf
TN_clf, FP_clf, FN_clf, TP_clf = cm_clf.ravel()
sensitivity_clf = TP_clf / (TP_clf + FN_clf)
specificity_clf = TN_clf / (TN_clf + FP_clf)
accuracy_clf = (TP_clf + TN_clf) / len(y_test)

# Metrics for clf2
TN_clf2, FP_clf2, FN_clf2, TP_clf2 = cm_clf2.ravel()
sensitivity_clf2 = TP_clf2 / (TP_clf2 + FN_clf2)
specificity_clf2 = TN_clf2 / (TN_clf2 + FP_clf2)
accuracy_clf2 = (TP_clf2 + TN_clf2) / len(y_test)

print(f"Metrics for clf:")
print(f"Sensitivity (Recall): {np.round(sensitivity_clf, 3)}")
print(f"Specificity: {np.round(specificity_clf, 3)}")
print(f"Accuracy: {np.round(accuracy_clf, 3)}")

print(f"\nMetrics for clf2:")
print(f"Sensitivity (Recall): {np.round(sensitivity_clf2, 3)}")
print(f"Specificity: {np.round(specificity_clf2, 3)}")
print(f"Accuracy: {np.round(accuracy_clf2, 3)}")




# ### 7. Explain in three to four sentences what is causing the differences between the following two confusion matrices below, and why the two confusion matrices above (for *clf* and *clf2*) are better<br>
# 
# ```python
# ConfusionMatrixDisplay(
#     confusion_matrix(ab_reduced_noNaN_train.life_exp_good, 
#                      clf.predict(ab_reduced_noNaN_train[['List Price']]), 
#                      labels=[0, 1]), display_labels=["Paper","Hard"]).plot()
# ConfusionMatrixDisplay(
#     confusion_matrix(ab_reduced_noNaN_train.life_exp_good, 
#                      clf.predict(
#                          ab_reduced_noNaN_train[['NumPages','Thick','List Price']]), 
#                      labels=[0, 1]), display_labels=["Paper","Hard"]).plot()
# ```
# 
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#     
# </details>

# The differences between the two confusion matrices result from the number and type of predictors used in the model. The first confusion matrix uses only one predictor (List Price), while the second incorporates three predictors (NumPages, Thick, and List Price). By including additional features in the second model, it likely captures more information about the relationship between the predictors and the target variable (life_exp_good), leading to better classification performance. Consequently, the models associated with clf and clf2 (used in the "above" confusion matrices) are better because they either use improved predictors, more sophisticated feature combinations, or better training processes that enhance their accuracy compared to the models in these two confusion matrices.

# Summary:
# The differences arise because the first model uses only List Price as a predictor, while the second model includes NumPages, Thick, and List Price, capturing more relevant information. The models for clf and clf2 perform better because they utilize improved predictors or training methods, leading to higher classification accuracy.
# 
# Link:
# https://chatgpt.com/share/673c407b-9560-8004-a3f7-1cf88e8933ac

# 
# ### 8. Read the paragraphs in *Further Guidance* and ask a ChatBot how to visualize *feature Importances* available for *scikit-learn* *classification decision trees*; do so for *clf2*;  and use *.feature_names_in_* corresponding to *.feature_importances_* to report which *predictor variable* is most important for making predictions according to *clf2*<br>
# 
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#   
# > The way a **classification decision tree** is fit is that at each step in the construction process of adding a new **decision node splitting rule** to the current **tree structure**, all possible **decision rules** for all possible **predictor variables** are considered, and the combination that improves the **prediction** the most (as measured by the criterion of either "Gini impurity" or "Shannon entropy") and in accordance with the rules of the decision tree (such as the `max_depth` argument) is added to the **classification decision tree**.  Thus overall "criterion" noted above improves with each new **decision node splitting rule**, so the improvement can thus be tracked and the improvement contributions attributed to the **feature** upon which the **decision node splitting rule** is based.  This means the relative contribution of each **predictor variable** to the overall explanatory power of the model can be calculated, and this is what the `.feature_importances_` attribute does. 
# >
# > Compared to the simplicity of understanding how different **covariates** contribute towards the final **predicted values** of **multiple linear regression models** (by just reading off the equation to see how predictions work), the the complexity of how all the different **features** interact and combine to together to create the final **predictions** from **classification decision trees** can be staggering. But the so-called **feature importance** heuristics allows us to judge how relatively important the overall contributions from different features are in the final decision tree predictions. Now we just need to be sure we're not **overfitting** our **classification decision trees** since they can be so **complex**. Fortunately, the "GridSearchCV" methodology mentioned in regards to finding the best `max_depth` setting for a tree is going to provide a general answer to the challenge of complexity and **overfitting** in **machine learning models** that is not too hard to understand (and which you might already have some guesses or a hunch about). 
# > 
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#        
# </details>

# In[17]:


import matplotlib.pyplot as plt
import numpy as np

# Assume clf2 is already a fitted decision tree classifier
feature_importances = clf2.feature_importances_
feature_names = clf2.feature_names_in_

# Plot the feature importances
plt.figure(figsize=(10, 6))
plt.barh(feature_names, feature_importances, color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importances for clf2')
plt.show()

# Identify the most important feature
most_important_index = np.argmax(feature_importances)
most_important_feature = feature_names[most_important_index]
most_important_value = feature_importances[most_important_index]

# Report the most important feature
print(f"The most important predictor variable is '{most_important_feature}' with an importance value of {most_important_value:.4f}.")


# In[ ]:





# ### 9. Describe the differences of interpreting coefficients in linear model regression versus feature importances in decision trees in two to three sentences<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Linear model regression predicts continuous real-valued averages for a given configuration of covariate values (or, feature values, if we're using machine learning terminology instead of statistical terminology), whereas a binary classification model such as a binary classification tree predicts 0/1 ("yes" or "no") outcomes (and gives the probability of a 1 "yes" (or "success") outcome from which a 1/0 "yes"/"no" prediction can be made; but, this is not what is being asked here. This question is asking "what's the difference in the way we can interpret and understand how the predictor variables influence the predictions in linear model regression based on the coefficients versus in binary decision trees based on the Feature Importances?"_
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot); but, if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_ 
#     
# </details>

# In linear regression, coefficients represent the change in the predicted outcome for a one-unit change in a predictor variable, assuming all other variables are held constant. This makes the relationships between predictors and the outcome direct and interpretable as additive contributions. In decision trees, feature importance reflects the overall contribution of a variable to the model's decision-making process, based on criteria like Gini impurity reduction or entropy, but it does not indicate specific marginal effects or the direction of influence as in linear regression.
# 
# Summary: 
# This conversation addressed the differences in interpreting coefficients in linear regression models versus feature importances in decision trees. Linear regression coefficients provide direct, additive interpretations of the effect of a predictor on the outcome, assuming all other predictors are constant. In contrast, feature importances in decision trees indicate the overall contribution of each predictor to the model's decisions but do not provide specific marginal effects or directional influence. The discussion highlights the interpretative nuances of these two modeling approaches.
# 
# https://chatgpt.com/share/673c4240-2480-8004-91fc-3d918fe149db

# ### 10. Have you reviewed the course wiki-textbook and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?<br>
#   
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# >  _Here is the link of [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) in case it gets lost among all the information you need to keep track of_  : )
# > 
# > _Just answering "Yes" or "No" or "Somewhat" or "Mostly" or whatever here is fine as this question isn't a part of the rubric; but, the midterm and final exams may ask questions that are based on the tutorial and lecture materials; and, your own skills will be limited by your familiarity with these materials (which will determine your ability to actually do actual things effectively with these skills... like the course project...)_
#     
# </details>

# # Recommended Additional Useful Activities [Optional]
# 
# The "Ethical Profesionalism Considerations" and "Current Course Project Capability Level" sections below **are not a part of the required homework assignment**; rather, they are regular weekly guides covering (a) relevant considerations regarding professional and ethical conduct, and (b) the analysis steps for the STA130 course project that are feasible at the current stage of the course 
# 
# <br>
# <details class="details-example"><summary style="color:blue"><u>Ethical Professionalism Considerations</u></summary>
# 
# ### Ethical Professionalism Considerations
# 
# - Discuss with a ChatBox about consent and data collection for training models.
#     - Discuss the ethics of data collection for training decision trees, particularly the need for informed consent when personal data is involved.
#     - Evaluate the role of regulatory frameworks in ensuring ethical data collection practices.
# - Discuss with a ChatBox about accountability in automated decision-making.
#     - Address the challenges of holding systems and their developers accountable when decision trees lead to adverse outcomes.
#     - Explore legal and ethical frameworks for responsibility when automated decisions go wrong.
# - Discuss with a ChatBox about transparency and explainability in classification models.
#     - Discuss the importance of model transparency, particularly when using decision trees in sectors like healthcare or criminal justice.
#     - Explore methods to enhance the explainability of decision trees, such as visualization techniques and simplified decision paths.
# - Discuss with a ChatBox about impact of misclassifications in critical applications.
#     - Examine the consequences of false positives and false negatives in decision tree outcomes, using confusion matrices to highlight these issues.
#     - Discuss ethical responsibilities when deploying classifiers in high-stakes fields like medicine or law enforcement.
#     
# </details>    
# 
# <details class="details-example"><summary style="color:blue"><u>Current Course Project Capability Level</u></summary>
# 
# **Remember to abide by the [data use agreement](https://static1.squarespace.com/static/60283c2e174c122f8ebe0f39/t/6239c284d610f76fed5a2e69/1647952517436/Data+Use+Agreement+for+the+Canadian+Social+Connection+Survey.pdf) at all times.**
# 
# Information about the course project is available on the course github repo [here](https://github.com/pointOfive/stat130chat130/tree/main/CP), including a draft [course project specfication](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F23_course_project_specification.ipynb) (subject to change). 
# - The Week 01 HW introduced [STA130F24_CourseProject.ipynb](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F24_CourseProject.ipynb), and the [available variables](https://drive.google.com/file/d/1ISVymGn-WR1lcRs4psIym2N3or5onNBi/view). 
# - Please do not download the [data](https://drive.google.com/file/d/1mbUQlMTrNYA7Ly5eImVRBn16Ehy9Lggo/view) accessible at the bottom of the [CSCS](https://casch.org/cscs) webpage (or the course github repo) multiple times.
#     
# 
# > ### NEW DEVELOPMENT<br>New Abilities Achieved and New Levels Unlocked!!!    
# > 
# > And with that, ALL LEVELS unlocked! 
# >
# > CONGRATS, YOU LEGENDS! 🎉
# >
# > You’ve battled through the wild jungles of deadlines, defeated the mighty Homework Beasts, and climbed the towering Mount Procrastination. And guess what? YOU MADE IT TO THE TOP! 🏔️
# > 
# > Take a bow, grab a treat, and enjoy the sweet, sweet taste of freedom(**just for now , because you still have to finish the project! But you are almost done!**). You’ve earned it. Now go out there and celebrate like the absolute rockstars you are! 🌟💪
# >
# 
#     
# ### Current Course Project Capability Level    
#     
# I mean, the **course project** is basically, like, essentially now.
#     
# - Will you be doing any **classification decision trees** stuff for the course project?
#     - You could consider making some [partial dependency plots](https://scikit-learn.org/stable/modules/partial_dependence.html) if so...
#     - those might provide an interesting analysis in addition to **tree structure** visualizations, **confusion matrices**, **feature importances**. and the standard "in-sample versus out-of-sample" **train-test validation** analysis that would be expected in a **machine learning context**
#     
# - You could see if there are any interesting columns that might make for a potentially interesting **classification decision tree** analysis
#     - You wouldn't have to though...
#     - But if you did you'd want to be able to articulate and explain why what you're doing with **classification decision trees** is appropriate and enlightening
# 
# - Anyway, I guess that just leaves reviewing all the statistical techniques covered in STA130, and considering integrating them holistically into your project!
#     
# </details>        

# In[ ]:




