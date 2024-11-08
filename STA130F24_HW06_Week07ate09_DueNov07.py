#!/usr/bin/env python
# coding: utf-8

# # STA130 Homework 06
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
# 
# - [0.1 points]: All relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] are reported within the notebook
# - [0.2 points]: Evaluation of correctness and clarity in written communication for Question "3"
# - [0.2 points]: Evaluation of correctness and clarity in written communication for Question "4"
# - [0.2 points]: Evaluation of submitted work and conclusions for Question "9"
# - [0.3 points]: Evaluation of written communication of the "big picture" differences and correct evidence assessement for Question "11"
# 

# ## "Pre-lecture" versus "Post-lecture" HW? 
# 
# - _**Your HW submission is due prior to the Nov08 TUT on Friday after you return from Reading Week; however,**_
# - _**this homework assignment is longer since it covers material from both the Oct21 and Nov04 LEC (rather than a single LEC); so,**_
# - _**we'll brake the assignment into "Week of Oct21" and "Week of Nov04" HW and/but ALL of it will be DUE prior to the Nov08 TUT**_
# 

# ## "Week of Oct21" HW [*due prior to the Nov08 TUT*]

# ### 1. Explain the theoretical Simple Linear Regression model in your own words by describing its components (of predictor and outcome variables, slope and intercept coefficients, and an error term) and how they combine to form a sample from normal distribution; then, create *python* code explicitly demonstrating your explanation using *numpy* and *scipy.stats* <br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Your answer can be quite concise and will likely just address the "mathematical" and "statistical" aspects of the process of a **Simple Linear Model** specification, perhaps giving an intuitive interpretation summary of the result as a whole_
# >   
# > - _Your code could be based on values for `n`, `x`, `beta0`, `beta1`, and `sigma`; and, then create the `errors` and `Y`_
# > 
# > - _The predictors $x_i$ can be fixed arbitrarily to start the process (perhaps sampled using `stats.uniform`), and they are conceptually different from the creation of **error** (or **noise**) terms $\epsilon_i$ which are sampled from a **normal distribution** (with some aribtrarily *a priori* chosen **standard deviation** `scale` parameter $\sigma$) which are then combined with $x_i$ through the **Simple Linear Model** equation (based on aribtrarily *a priori* chosen **slope** and **intercept coefficients**) to produce the $Y_i$ outcomes_
# > 
# > - _It should be fairly easy to visualize the "a + bx" line defined by the **Simple Linear Model** equation, and some **simulated** data points around the line in a `plotly` figure using the help of a ChatBot_
# > 
# > _If you use a ChatBot (as expected for this problem), **don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)**_
# >
# > 
# > _**Question Scope Warning:** Be careful when using a ChatBot to help you with creating an example dataset and coding up a visualization though, **because it might suggest creating (and visualizing) a fitted model for to your data (rather than the theoretical model); but, this is not what this question is asking you to demonstrate**. This question is not asking about how to produce a fitted **Simple Linear Regression** model or explain how model **slope** and **intercept coefficients** are calculated (e.g., using "ordinary least squares" or analytical equations to estimate the **coefficients**  for an observed dataset)._
# > 
# > ```python
# > # There are two distinct ways to use `plotly` here
# >
# > import plotly.express as px
# > px.scatter(df, x='x',  y='Y', color='Data', 
# >            trendline='ols', title='Y vs. x')
# >        
# > import plotly.graph_objects as go
# > fig = go.Figure()
# > fig.add_trace(go.Scatter(x=x, y=Y, mode='markers', name='Data'))
# > 
# > # The latter is preferable since `trendline='ols'` in the former 
# > # creates a fitted model for the data and adds it to the figure
# > # and, again, THAT IS NOT what this problem is asking for right now
# > ```
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
# </details>
# 

# Predictor and Outcome: The predictor is the variable thought to influence the outcome, which is what we aim to predict. For example, if we're examining how study hours affect exam scores, "hours of study" is the predictor, and "exam score" is the outcome.
# 
# Intercept: This is the starting point of our line; it indicates the value of the outcome when the predictor is zero. In our example, it represents the exam score someone would get if they studied for zero hours.
# 
# Slope: The slope shows how much the outcome changes for each unit increase in the predictor. A positive slope means that as the predictor increases, the outcome tends to increase. In our example, a positive slope indicates that more hours of study generally lead to a higher exam score.
# 
# Error Term: Data points don't all fall perfectly on a straight line due to other factors causing variability around the line. This variation, or "noise," is captured by the error term. It accounts for random factors influencing the outcome but not included in the predictor.
# 
# how they combine to form a sample from normal distribution: 
# In simple linear regression, we create a model by combining a predictor variable with a slope, an intercept, and a normally distributed error term. The intercept and slope define the line that represents the predicted outcome based solely on the predictor. However, in real-world data, outcomes vary around this line due to random factors, which is where the error term comes in.
# 
# The error term is assumed to follow a normal distribution centered around zero, meaning errors are mostly small but can sometimes be larger. When we add this normally distributed error to each predicted outcome, the observed outcomes are spread around the prediction line. This distribution of outcomes at each predictor value resembles a bell curve or normal distribution around the line.
# 
# So, each observed outcome is effectively a sample from a normal distribution centered on the prediction line, with spread determined by the error’s standard deviation. If we repeated this sampling process for a given predictor value, we would get a normal distribution of outcomes around the predicted value. This is why the combination of the prediction and error term forms a sample that appears to follow a normal distribution around the regression line.

# In[1]:


import numpy as np
import plotly.graph_objs as go
from scipy.stats import norm, uniform

# Set theoretical model parameters
n = 100          # number of data points
beta_0 = 3       # intercept
beta_1 = 1.5     # slope
sigma = 1        # standard deviation of the error term

# Generate predictor values (X) from a uniform distribution
np.random.seed(0)  # for reproducibility
X = uniform.rvs(loc=0, scale=10, size=n)

# Generate error values (epsilon) from a normal distribution
epsilon = norm.rvs(loc=0, scale=sigma, size=n)

# Calculate outcome values (Y) using the theoretical model
Y = beta_0 + beta_1 * X + epsilon

# Define the "ideal" line without noise
Y_line = beta_0 + beta_1 * X

# Visualize the theoretical data and model line
scatter_data = go.Scatter(x=X, y=Y, mode='markers', name='Theoretical Data Points')
line_data = go.Scatter(x=X, y=Y_line, mode='lines', name='Theoretical Model Line')

layout = go.Layout(
    title="Theoretical Simple Linear Regression Model",
    xaxis=dict(title="Predictor (X)"),
    yaxis=dict(title="Outcome (Y)")
)

fig = go.Figure(data=[scatter_data, line_data], layout=layout)
fig.show()


# Summary
# In this conversation, we explored the theoretical concept of Simple Linear Regression (SLR) and how it generates data.
# 
# SLR Basics: We discussed SLR as a way to model the relationship between two variables—a predictor and an outcome—using a straight line defined by an intercept and slope. The intercept gives the outcome when the predictor is zero, while the slope indicates how the outcome changes with the predictor.
# 
# Role of Error Term: A normal error term is added to each predicted outcome to simulate random variation around the ideal line. This error term follows a normal distribution with a mean of zero, meaning most outcomes are close to the line, with fewer values farther away.
# 
# Normal Distribution of Outcomes: When the predictor effect (slope and intercept) is combined with the normally distributed error, it produces observed outcomes that are approximately normally distributed around the line.
# 
# Code Example: We created Python code that generates and visualizes this theoretical data using predefined parameters for slope, intercept, and error, illustrating how real-world data would scatter around a theoretical line without attempting to fit or estimate any parameters.
# 
# Link:
# https://chatgpt.com/share/672c3b0a-3e4c-8004-81ba-0601c96b2f79

# ### 2. Use a dataset simulated from your theoretical Simple Linear Regression model to demonstrate how to create and visualize a fitted Simple Linear Regression model using *pandas* and *import statsmodels.formula.api as smf*<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > - _Combine the **simulated** `x` and `Y` into a `pandas` data frame object named `df` with the column names "x" and "Y"_
# > 
# > - _Replace the inline question comments below with their answers (working with a ChatBot if needed)_
# >
# > ```python
# > import statsmodels.formula.api as smf  # what is this library for?
# > import plotly.express as px  # this is a ploting library
# >
# > # what are the following two steps doing?
# > model_data_specification = smf.ols("Y~x", data=df) 
# > fitted_model = model_data_specification.fit() 
# >
# > # what do each of the following provide?
# > fitted_model.summary()  # simple explanation? 
# > fitted_model.summary().tables[1]  # simple explanation?
# > fitted_model.params  # simple explanation?
# > fitted_model.params.values  # simple explanation?
# > fitted_model.rsquared  # simple explanation?
# >
# > # what two things does this add onto the figure?
# > df['Data'] = 'Data' # hack to add data to legend 
# > fig = px.scatter(df, x='x',  y='Y', color='Data', 
# >                  trendline='ols', title='Y vs. x')
# >
# > # This is essentially what above `trendline='ols'` does
# > fig.add_scatter(x=df['x'], y=fitted_model.fittedvalues,
# >                 line=dict(color='blue'), name="trendline='ols'")
# > 
# > fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS
# > ```
# >
# > _The plotting here uses the `plotly.express` form `fig.add_scatter(x=x, y=Y)` rather than the `plotly.graph_objects` form `fig.add_trace(go.Scatter(x=x, y=Y))`. The difference between these two was noted in the "Further Guidance" comments in the previous question; but, the preference for the former in this case is because `px` allows us to access `trendline='ols'` through `px.scatter(df, x='x',  y='Y', trendline='ols')`_
# >
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_      
# 
# </details>

# In[2]:


import statsmodels.formula.api as smf  # This library is used for fitting statistical models, like Ordinary Least Squares (OLS) regression.

import plotly.express as px  # This is a plotting library.

# The following two steps are doing:
model_data_specification = smf.ols("Y~x", data=df) 
# This specifies an Ordinary Least Squares (OLS) regression model, where Y is the dependent variable and x is the independent variable, using the dataframe df.

fitted_model = model_data_specification.fit() 
# This fits the specified model to the data and returns the fitted model object, which contains the regression results.

# Each of the following provides:
fitted_model.summary()  
# This provides a detailed summary of the fitted regression model, including R-squared, coefficients, standard errors, t-values, p-values, and more.

fitted_model.summary().tables[1]  
# This provides the regression coefficients table from the model summary, which includes details like standard errors, t-values, and p-values for each parameter.

fitted_model.params  
# This returns the estimated model parameters, including the intercept and the slope for x.

fitted_model.params.values  
# This returns the parameter values as a NumPy array.

fitted_model.rsquared  
# This returns the R-squared value, which represents the proportion of the variance in Y explained by x.

# The following two things are added onto the figure:
df['Data'] = 'Data'  # This line is used to add a categorical label for all the data points to create a legend entry in the plot.
fig = px.scatter(df, x='x', y='Y', color='Data', trendline='ols', title='Y vs. x')

# Adding a scatter plot with fitted line:
fig.add_scatter(x=df['x'], y=fitted_model.fittedvalues,
                line=dict(color='blue'), name="trendline='ols'")
# This manually adds the trendline for the fitted OLS regression model to the scatter plot, similar to what trendline='ols' does automatically.


# In[ ]:


Here’s a concise summary of what each part of your code does:

Imports:

statsmodels.formula.api (smf): Used to specify and fit statistical models, such as OLS regression.
plotly.express (px): Used for creating plots like scatter plots.
Model Specification and Fitting:

smf.ols("Y~x", data=df): Specifies an OLS regression model where Y is the dependent variable and x is the independent variable.
.fit(): Fits the model to the data, generating the fitted_model.
Model Information:

fitted_model.summary(): Provides a detailed summary of the regression (coefficients, R-squared, significance, etc.).
.tables[1]: Extracts the regression coefficients table.
.params: Returns the model's coefficients, including intercept and slope.
.params.values: Returns the coefficients as a NumPy array.
.rsquared: Provides the R-squared value, indicating the goodness of fit.
Plotting:

Adds a categorical label to the data ('Data') for legend purposes.
Uses Plotly to create a scatter plot and add an OLS trendline.
Manually adds the trendline using fittedvalues to represent the fitted model visually.

Link : https://chatgpt.com/share/672d3c66-1ed4-8004-8541-b5240fea866c


# ### 3. Add the line from Question 1 on the figure of Question 2 and explain the difference between the nature of the two lines in your own words; *but, hint though: simulation of random sampling variation*<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _This question is effectively asking you to explain what the combined code you produced for Questions 1 and 2 is trying to demonstrate overall. If you're working with a ChatBot (as expected), giving these two sets of code as context, and asking what the purpose of comparing these lines could be would be a way to get some help in formulating your answer_
# > 
# > _The graphical visualization aspect of this question could be accomplished by appending the following code to the code provided in Question 2._
# > 
# > ```python
# > # what does this add onto the figure in constrast to `trendline='ols'`?
# > x_range = np.array([df['x'].min(), df['x'].max()])
# > # beta0 and beta1 are assumed to be defined
# > y_line = beta0 + beta1 * x_range
# > fig.add_scatter(x=x_range, y=y_line, mode='lines',
# >                 name=str(beta0)+' + '+str(beta1)+' * x', 
# >                 line=dict(dash='dot', color='orange'))
# >
# > fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS
# > ```
# > 
# > _The right way to interactively "see" the answer to this question is to repeatedly create different dataset **simulations** using your theoretical model and the corresponding fitted models, and repeatedly visualize the data and the two lines over and over... this would be as easy as rerunning a single cell containing your simulation and visualization code..._
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
# </details>

# In[3]:


import numpy as np
import pandas as pd
from scipy.stats import norm
import plotly.graph_objects as go
import statsmodels.formula.api as smf  # what is this library for? It is for specifying and fitting statistical models using formulas, including linear regression.
import plotly.express as px  # this is a plotting library for creating a wide range of visualizations, including scatter plots.

# Parameters for the simple linear regression model
n = 100  # Number of data points
beta_0 = 2  # Intercept
beta_1 = 3  # Slope
sigma = 1  # Standard deviation of the error term

# Generate predictor variable x (fixed, can be arbitrary)
x = np.linspace(0, 10, n)  # Generating n values between 0 and 10

# Generate error terms from a normal distribution with mean 0 and standard deviation sigma
epsilon = norm.rvs(loc=0, scale=sigma, size=n)

# Calculate outcome variable Y based on the linear model
Y = beta_0 + beta_1 * x + epsilon

# Combine x and Y into a pandas data frame
df = pd.DataFrame({'x': x, 'Y': Y})

# what are the following two steps doing?
model_data_specification = smf.ols("Y~x", data=df)  # Specifying an ordinary least squares (OLS) regression model with Y as the outcome and x as the predictor.
fitted_model = model_data_specification.fit()  # Fitting the model to estimate the coefficients (intercept and slope).

# what do each of the following provide?
fitted_model.summary()  # simple explanation? Provides a detailed summary of the regression results, including coefficients, statistical significance, R-squared, and more.
fitted_model.summary().tables[1]  # simple explanation? Provides the table of estimated coefficients, their standard errors, t-values, and p-values.
fitted_model.params  # simple explanation? Provides the estimated values for the model's parameters (intercept and slope).
fitted_model.params.values  # simple explanation? Provides the parameter values as an array.
fitted_model.rsquared  # simple explanation? Provides the R-squared value, which indicates the proportion of variance in Y explained by x.

# Plotting the data points and the true regression line
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=Y, mode='markers', name='Data'))
fig.add_trace(go.Scatter(x=x, y=beta_0 + beta_1 * x, mode='lines', name='True Regression Line'))

# what two things does this add onto the figure?
df['Data'] = 'Data' # hack to add data to legend (adds a 'Data' label for points in the plot and makes it appear in the legend)
fig = px.scatter(df, x='x',  y='Y', color='Data', trendline='ols', title='Y vs. x')

# This is essentially what above `trendline='ols'` does
fig.add_scatter(x=df['x'], y=fitted_model.fittedvalues, line=dict(color='blue'), name="trendline='ols'")

# Adding the true line from Question 1
y_line = beta_0 + beta_1 * np.array([df['x'].min(), df['x'].max()])
fig.add_scatter(x=[df['x'].min(), df['x'].max()], y=y_line, mode='lines',
                name=str(beta_0)+' + '+str(beta_1)+' * x', 
                line=dict(dash='dot', color='orange'))

fig.show()  # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# Explanation of the difference between the two lines:
# The difference between the two lines is due to the random error added during the data generation process, which introduces variability in the observed data points. This demonstrates how random sampling variation affects the fitted model and causes it to differ from the true underlying relationship.

# Summary:
# This section summarizes the overall purpose of comparing the fitted regression line (blue) with the true underlying line (orange). It demonstrates the impact of random sampling variation on the observed data and how it affects the fitted model compared to the true relationship.
# Link:https://chatgpt.com/share/672d3e5e-f9a4-8004-8f5e-eda9a8659489

# ### 4. Explain how *fitted_model.fittedvalues* are derived on the basis of *fitted_model.summary().tables[1]* (or more specifically  *fitted_model.params* or *fitted_model.params.values*)<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _The previous questions used code to explore the distinction between theoretical (true) $Y_i = \beta_0 + \beta_1 x_i + \epsilon_i \;[\text{where } \epsilon_i \sim \mathcal{N}(0, \sigma)]\;$ and fitted (estimated) $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ **Simple Linear Regression** models_
# >
# > _This question asks you to explicitly illustrate how the the latter "in sample predictions" of the fitted **Simple Linear Regression** model $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ are made (in contrast to the linear equation of the theoretical model)_
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
# </details>

# The fitted_model.fittedvalues represent the predicted responses derived from the fitted Simple Linear Regression model. These values are calculated using the estimated parameters found in fitted_model.params, which are listed in fitted_model.summary().tables[]

# The `fitted_model.fittedvalues` are derived using the estimated coefficients found in `fitted_model.params`, which are detailed in `fitted_model.summary().tables[1]`. These coefficients (\( \hat{\beta}_0 \) and \( \hat{\beta}_1 \)) are obtained during model fitting. The fitted values (\( \hat{y}_i \)) are calculated using the equation:
# 
# \[
# \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
# \]
# 
# where \( x_i \) are the observed values. These fitted values represent the predictions made by the regression model based on the estimated parameters.
# 
# 
# Link: 
# https://chatgpt.com/share/672d46f5-7a00-8004-a4ae-13a84de9f8e4

# 5. Explain concisely in your own words what line is chosen for the fitted model based on observed data using the "ordinary least squares" method (as is done by *trendline='ols'* and *smf.ols(...).fit()*) and why it requires "squares"<br>
#     
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _This question addresses the use of **residuals** $\text{e}_i = \hat \epsilon_i = Y_i - \hat y_i$ (in contrast to the **error** terms $\epsilon_i$ of the theoretical model), and particularly, asks for an explanation based on the following visualization_
# >
# > ```python 
# > import scipy.stats as stats
# > import numpy as np
# > import pandas as pd
# > import statsmodels.formula.api as smf
# > import plotly.express as px
# > 
# > n,x_min,x_range,beta0,beta1,sigma = 20,5,5,2,3,5
# > x = stats.uniform(x_min, x_range).rvs(size=n)
# > errors = stats.norm(loc=0, scale=sigma).rvs(size=n)
# > Y = beta0 + beta1 * x + errors
# > 
# > df = pd.DataFrame({'x': x, 'y': Y})
# > model_data_specification = smf.ols("Y~x", data=df) 
# > fitted_model = model_data_specification.fit() 
# > 
# > df['Data'] = 'Data' # hack to add data to legend 
# > fig = px.scatter(df, x='x',  y='Y', color='Data', 
# >                  trendline='ols', title='Y vs. x')
# > 
# > # This is what `trendline='ols'` is
# > fig.add_scatter(x=df['x'], y=fitted_model.fittedvalues,
# >                 line=dict(color='blue'), name="trendline='ols'")
# > 
# > x_range = np.array([df['x'].min(), df['x'].max()])
# > y_line = beta0 + beta1 * x_range
# > fig.add_scatter(x=x_range, y=y_line, mode='lines',
# >                 name=str(beta0)+' + '+str(beta1)+' * x', 
# >                 line=dict(dash='dot', color='orange'))
# > 
# > # Add vertical lines for residuals
# > for i in range(len(df)):
# >     fig.add_scatter(x=[df['x'][i], df['x'][i]],
# >                     y=[fitted_model.fittedvalues[i], df['Y'][i]],
# >                     mode='lines',
# >                     line=dict(color='red', dash='dash'),
# >                     showlegend=False)
# >     
# > # Add horizontal line at y-bar
# > fig.add_scatter(x=x_range, y=[df['Y'].mean()]*2, mode='lines',
# >                 line=dict(color='black', dash='dot'), name='y-bar')
# > 
# > fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS
# > ```
# >
# > _**Question Scope Warning**: we are not looking for any explanation realted to the mathematical equations for the line chosen for the **Simple Linear Regression** model by the "ordinary least squares" method, which happen to be_
# > 
# > _$$\hat \beta_1 = r_{xy}\frac{s_y}{s_x} \quad \text{ and } \quad  \hat\beta_0 = \bar {y}-\hat \beta_1\bar {x}$$_
# >
# > _where $r_{xy}$ is the **correlation** between $x$ and $Y$ and $s_x$ and $s_Y$ are the **sample standard deviations** of $x$ and $y$_
# >
# > ---
# > 
# > ```python 
# > # Use this if you need it    
# > # https://stackoverflow.com/questions/52771328/plotly-chart-not-showing-in-jupyter-notebook
# > import plotly.offline as pyo
# > # Set notebook mode to work in offline
# > pyo.init_notebook_mode()    
# > ```
# >
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
#     
# </details>

# The "ordinary least squares" (OLS) method determines the line that minimizes the total of the squared residuals. Residuals (𝑒𝑖) are the differences between the actual observed values (𝑌𝑖) and the predicted values (𝑦̂𝑖) from the model. By squaring these residuals, OLS makes sure that all deviations are positive and emphasizes larger errors more strongly. This method helps identify the line that provides the best fit to the data by minimizing the overall prediction errors. The resulting line reflects the trend that most accurately represents the relationship between the independent and dependent variables, while reducing the sum of squared errors to a minimum.

# Summary:
#     The "ordinary least squares" (OLS) method selects the line that minimizes the sum of squared residuals (\(e_i\)), which are the differences between observed (\(Y_i\)) and predicted (\(\hat{y}_i\)) values. Squaring the residuals ensures all differences are positive and penalizes larger deviations more heavily, resulting in the best-fit line that minimizes prediction errors for the data.
#     
# Link: 
# https://chatgpt.com/share/672d46f5-7a00-8004-a4ae-13a84de9f8e4

# ### 6. Explain why the first expression below can be interpreted as "the proportion of variation in (outcome) Y explained by the model (i.e. _fitted_model.fittedvalues_)"; and therefore, why _fitted_model.rsquared_ can be interpreted as a measure of the accuracy of the model; and, therefore what the two _np.corrcoef(...)[0,1]\*\*2_ expressions capture in the context of _Simple Linear Regression models_.
# 
# 1. `1-((Y-fitted_model.fittedvalues)**2).sum()/((Y-Y.mean())**2).sum()`
# 2. `fitted_model.rsquared`
# 3. `np.corrcoef(Y,fitted_model.fittedvalues)[0,1]**2`
# 4. `np.corrcoef(Y,x)[0,1]**2`<br><br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _**R-squared** is the "the proportion of variation in (outcome) $Y$ explained by the model ($\hat y_i$)" and is defined as_
# >
# > _$R^2 = 1 - \frac{\sum_{i=1}^n(Y_i-\hat y)^2}{\sum_{i=1}^n(Y_i-\bar Y)^2}$_
# >
# > _The visuzation provided in the previous problem can be used to consider $(Y_i-\bar Y)^2$ as the squared distance of the $Y_i$ to their sample average $\bar Y$ as opposed to the squared **residuals** $(Y_i-\hat y)^2$ which is the squared distance of the $Y_i$ to their fitted (predicted) values $Y_i$._
# >    
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
# </details>

# ### 7. Indicate a couple of the assumptions of the *Simple Linear Regression* model specification that do not seem compatible with the example data below<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Hint: What even ARE the assumptions of the  **Simple Linear Regression** model, you ask? Have a look at the mathematical specification and see if what it seems to be assuming._
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
# </details>

# In[ ]:


import pandas as pd
from scipy import stats
import plotly.express as px
from plotly.subplots import make_subplots

# This data shows the relationship between the amount of fertilizer used and crop yield
data = {'Amount of Fertilizer (kg) (x)': [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 
                                          2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 
                                          4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 6, 6.2, 
                                          6.4, 6.6, 6.8, 7, 7.2, 7.4, 7.6, 7.8, 8, 
                                          8.2, 8.4, 8.6, 8.8,9, 9.2, 9.4, 9.6],
        'Crop Yield (tons) (Y)': [18.7, 16.9, 16.1, 13.4, 48.4, 51.9, 31.8, 51.3, 
                                  63.9, 50.6, 58.7, 82.4, 66.7, 81.2, 96.5, 112.2, 
                                  132.5, 119.8, 127.7, 136.3, 148.5, 169.4, 177.9, 
                                  186.7, 198.1, 215.7, 230.7, 250.4, 258. , 267.8, 
                                  320.4, 302. , 307.2, 331.5, 375.3, 403.4, 393.5,
                                  434.9, 431.9, 451.1, 491.2, 546.8, 546.4, 558.9]}
df = pd.DataFrame(data)
fig1 = px.scatter(df, x='Amount of Fertilizer (kg) (x)', y='Crop Yield (tons) (Y)',
                  trendline='ols', title='Crop Yield vs. Amount of Fertilizer')

# Perform linear regression using scipy.stats
slope, intercept, r_value, p_value, std_err = \
    stats.linregress(df['Amount of Fertilizer (kg) (x)'], df['Crop Yield (tons) (Y)'])
# Predict the values and calculate residuals
y_hat = intercept + slope * df['Amount of Fertilizer (kg) (x)']
residuals = df['Crop Yield (tons) (Y)'] - y_hat
df['Residuals'] = residuals
fig2 = px.histogram(df, x='Residuals', nbins=10, title='Histogram of Residuals',
                    labels={'Residuals': 'Residuals'})

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=('Crop Yield vs. Amount of Fertilizer', 
                                    'Histogram of Residuals'))
for trace in fig1.data:
    fig.add_trace(trace, row=1, col=1)
for trace in fig2.data:
    fig.add_trace(trace, row=1, col=2)
fig.update_layout(title='Scatter Plot and Histogram of Residuals',
    xaxis_title='Amount of Fertilizer (kg)', yaxis_title='Crop Yield (tons)',
    xaxis2_title='Residuals', yaxis2_title='Frequency', showlegend=False)

fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# ## "Week of Nov04" HW [due prior to the Nov08 TUT]
# 
# _**In place of the "Data Analysis Assignment" format we introduced for the previous weeks' HW, the remaining questions will be a collection of exercises based around the following data**_
# 
# > The details of the "LOWESS Trendline" shown below are not a part of the intended scope of the activities here, but it is included since it is suggestive of the questions we will consider and address here
# 

# In[ ]:


import plotly.express as px
import seaborn as sns
import statsmodels.api as sm

# The "Classic" Old Faithful Geyser dataset: ask a ChatBot for more details if desired
old_faithful = sns.load_dataset('geyser')

# Create a scatter plot with a Simple Linear Regression trendline
fig = px.scatter(old_faithful, x='waiting', y='duration', 
                 title="Old Faithful Geyser Eruptions", 
                 trendline='ols')#'lowess'

# Add a smoothed LOWESS Trendline to the scatter plot
lowess = sm.nonparametric.lowess  # Adjust 'frac' to change "smoothness bandwidth"
smoothed = lowess(old_faithful['duration'], old_faithful['waiting'], frac=0.25)  
smoothed_df = pd.DataFrame(smoothed, columns=['waiting', 'smoothed_duration'])
fig.add_scatter(x=smoothed_df['waiting'], y=smoothed_df['smoothed_duration'], 
                mode='lines', name='LOWESS Trendline')

fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# ### 8. Specify a *null hypothesis* of "no linear association (on average)" in terms of the relevant *parameter* of the *Simple Linear Regression* model, and use the code below to characterize the evidence in the data relative to the *null hypothesis* and interpret your subsequent beliefs regarding the Old Faithful Geyser dataset.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Remember that **Hypothesis Testing** is not a "mathematical proof"_
# >
# > - _We do not prove $H_0$ false, we instead give evidence against the $H_0$: "We reject the null hypothesis with a p-value of XYZ, meaning we have ABC evidence against the null hypothesis"_
# > - _We do not prove $H_0$ is true, we instead do not have evidence to reject $H_0$: "We fail to reject the null hypothesis with a p-value of XYZ"_
# 
# |p-value|Evidence|
# |-|-|
# |$$p > 0.1$$|No evidence against the null hypothesis|
# |$$0.1 \ge p > 0.05$$|Weak evidence against the null hypothesis|
# |$$0.05 \ge p > 0.01$$|Moderate evidence against the null hypothesis|
# |$$0.01 \ge p > 0.001$$|Strong evidence against the null hypothesis|
# |$$0.001 \ge p$$|Very strong evidence against the null hypothesis|
# 
# </details>    
# 
# > ```python
# > import seaborn as sns
# > import statsmodels.formula.api as smf
# >
# > # The "Classic" Old Faithful Geyser dataset
# > old_faithful = sns.load_dataset('geyser')
# > 
# > linear_for_specification = 'duration ~ waiting'
# > model = smf.ols(linear_for_specification, data=old_faithful)
# > fitted_model = model.fit()
# > fitted_model.summary()
# > ```
# 

# here is no linear association between the waiting time (waiting) and the duration of eruptions (duration), which means the true slope of the regression line is zero.

# ### 9. As seen in the introductory figure above, if the delay of the geyser eruption since the previous geyser eruption exceeds approximately 63 minutes, there is a notable increase in the duration of the geyser eruption itself. In the figure below we therefore restrict the dataset to only short wait times. Within the context of only short wait times, is there evidence in the data for a relationship between duration and wait time in the same manner as in the full data set? Using the following code, characterize the evidence against the *null hypothesis* in the context of short wait times which are less than  *short_wait_limit* values of *62*, *64*, *66*.<br>
# 

# In[ ]:


import plotly.express as px
import statsmodels.formula.api as smf


short_wait_limit = 62 # 64 # 66 #
short_wait = old_faithful.waiting < short_wait_limit

print(smf.ols('duration ~ waiting', data=old_faithful[short_wait]).fit().summary().tables[1])

# Create a scatter plot with a linear regression trendline
fig = px.scatter(old_faithful[short_wait], x='waiting', y='duration', 
                 title="Old Faithful Geyser Eruptions for short wait times (<"+str(short_wait_limit)+")", 
                 trendline='ols')

fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# For short wait times (<62, <64, <66 minutes), we fit a linear regression model for each subset to test if waiting time significantly affects eruption duration. The null hypothesis H_0 states no linear association between waiting time and duration beta_1 = 0. Based on the p-value from each model:
# 
# p > 0.1: No evidence against H_0, indicating no significant relationship.
# 0.05 \ p > 0.01: Moderate evidence against H_0, suggesting a potential linear relationship.
# 
# Thus, the evidence for a relationship varies with different wait limits, depending on p-values from the regression.

# ### 10. Let's now consider just the (*n=160*) long wait times (as specified in the code below), and write code to do the following:
# 
# 1. create fitted **Simple Linear Regression** models for **boostrap samples** and collect and visualize the **bootstrapped sampling distribution** of the **fitted slope coefficients** of the fitted models;  
# 
# 
# 2. **simulate** samples (of size `n=160`) from a **Simple Linear Regression** model that uses $\beta_0 = 1.65$, $\beta_1 = 0$, $\sigma = 0.37$ along with the values of `waiting` for $x$ to create **simuations** of $Y$ and use these collect and visualize the **sampling distribution** of the **fitted slope coefficient** under a **null hypothesis** assumption of "no linear association (on average)"; then,  
# 
# 
# 3. report if $0$ is contained within a 95\% **bootstrapped confidence interval**; and if the **simulated p-value** matches `smf.ols('duration ~ waiting', data=old_faithful[long_wait]).fit().summary().tables[1]`?<br><br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _You'll need to create `for` loops to repeatedly create fitted **Simple Linear Regression** models using different samples, collecting the **fitted slope coeffient** created in each `for` loop "step" in order to visualize the **simulated sampling distributions**_
# > 
# > - _A **bootstrapped sample** of the "long wait times" dataset can be created with `old_faithful[long_wait].sample(n=long_wait.sum(), replace=True)`_
# >
# >
# > - _A **simulated** version of the "long wait times under a null hypothesis assumption of **no linear association (on average)**" dataset can be created by first creating `old_faithful_simulation = old_faithful[long_wait].copy()` and then assigning the **simulated** it values with `old_faithful_simulation['duration'] = 1.65 + 0*old_faithful_simulation.waiting + stats.norm(loc=0, scale=0.37).rvs(size=long_wait.sum())`_ 
# >
# >  _The values $\beta_0 = 1.65$ and $\sigma = 0.37$ are chosen to match what is actually observed in the data, while $\beta_1 = 0$ is chosen to reflect a **null hypothesis** assumption of "no linear assocaition (on average)"; and, make sure that you understand why it is that_
# >
# >
# > - _if `bootstrapped_slope_coefficients` is the `np.array` of your **bootstrapped slope coefficients** then `np.quantile(bootstrapped_slope_coefficients, [0.025, 0.975])` is a 95\% **bootstrapped confidence interval**_
# > 
# >
# > - _if `simulated_slope_coefficients` is the `np.array` of your **fitted slope coefficients** **simulated** under a **null hypothesis** "no linear association (on average)" then `(np.abs(simulated_slope_coefficients) >= smf.ols('duration ~ waiting', data=old_faithful[long_wait]).fit().params[1]).mean()` is the **p-value** for the **simulated** **simulated sampling distribution of the slope coeficients** under a **null hypothesis** "no linear association (on average)"_
# 
# </details>
# <br>

# In[ ]:


import plotly.express as px

long_wait_limit = 71
long_wait = old_faithful.waiting > long_wait_limit

print(smf.ols('duration ~ waiting', data=old_faithful[long_wait]).fit().summary().tables[1])

# Create a scatter plot with a linear regression trendline
fig = px.scatter(old_faithful[long_wait], x='waiting', y='duration', 
                 title="Old Faithful Geyser Eruptions for short wait times (>"+str(long_wait_limit)+")", 
                 trendline='ols')
fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# In[ ]:


import numpy as np
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import scipy.stats as stats

# Load the Old Faithful Geyser dataset
old_faithful = sns.load_dataset('geyser')

# Step 1: Bootstrap Slope Coefficients for Long Wait Times
# Filter the dataset for long waits (n = 160)
long_wait_limit = 71
long_wait = old_faithful.waiting > long_wait_limit
long_wait_data = old_faithful[long_wait]

# Number of bootstrap samples
n_bootstrap = 1000
boot_slope_coefficients = []

# Create bootstrap samples and fit models
np.random.seed(42)  # For reproducibility
for _ in range(n_bootstrap):
    bootstrap_sample = old_faithful[long_wait].sample(n=long_wait.sum(), replace=True)
    model = smf.ols('duration ~ waiting', data=bootstrap_sample)
    fitted_model = model.fit()
    boot_slope_coefficients.append(fitted_model.params['waiting'])

# Plot the bootstrap sampling distribution of slope coefficients
plt.hist(boot_slope_coefficients, bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Slope Coefficient')
plt.ylabel('Frequency')
plt.title('Bootstrap Sampling Distribution of Slope Coefficients')
plt.show()

# Step 2: Simulate Data Under the Null Hypothesis (beta_1 = 0)
# Parameters for the null hypothesis model
beta_0 = 1.65
beta_1 = 0
sigma = 0.37
n_simulation = 1000
simulated_slope_coefficients = []

# Simulate data under null hypothesis and fit models
for _ in range(n_simulation):
    # Create simulated dataset under null hypothesis
    old_faithful_simulation = old_faithful[long_wait].copy()
    old_faithful_simulation['duration'] = 1.65 + 0 * old_faithful_simulation.waiting + stats.norm(loc=0, scale=sigma).rvs(size=long_wait.sum())

    # Fit model and collect slope coefficient
    model = smf.ols('duration ~ waiting', data=old_faithful_simulation)
    fitted_model = model.fit()
    simulated_slope_coefficients.append(fitted_model.params['waiting'])

# Plot the sampling distribution of slope coefficients under null hypothesis
plt.hist(simulated_slope_coefficients, bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Slope Coefficient')
plt.ylabel('Frequency')
plt.title('Sampling Distribution of Slope Coefficients Under Null Hypothesis')
plt.show()

# Step 3: 95% Bootstrapped Confidence Interval and p-value Comparison
# Calculate 95% confidence interval for bootstrapped slope coefficients
lower_bound, upper_bound = np.quantile(boot_slope_coefficients, [0.025, 0.975])
print(f"95% Bootstrapped Confidence Interval for Slope Coefficient: [{lower_bound:.4f}, {upper_bound:.4f}]")

# Check if 0 is within the confidence interval
contains_zero = lower_bound <= 0 <= upper_bound
if contains_zero:
    print("The value 0 is contained within the 95% bootstrapped confidence interval.")
else:
    print("The value 0 is NOT contained within the 95% bootstrapped confidence interval.")

# Compare p-value from the original fitted model
original_model = smf.ols('duration ~ waiting', data=long_wait_data).fit()
original_p_value = original_model.pvalues['waiting']
print(f"Original Model p-value for Slope Coefficient: {original_p_value:.4f}")

# Simulated p-value: Proportion of simulated slopes greater than or equal to observed slope
simulated_p_value = (np.abs(simulated_slope_coefficients) >= np.abs(original_model.params['waiting'])).mean()
print(f"Simulated p-value: {simulated_p_value:.4f}")

# Create a scatter plot with a linear regression trendline for long wait times
fig = px.scatter(long_wait_data, x='waiting', y='duration', 
                 title="Old Faithful Geyser Eruptions for Long Wait Times (>{} minutes)".format(long_wait_limit), 
                 trendline='ols')
fig.show()


# ### 11. Since we've considered wait times of around <64  "short" and wait times of >71 "long", let's instead just divide the data and insead call wait times of <68 "short" and otherwise just call them "long". Consider the *Simple Linear Regression* model specification using an *indicator variable* of the wait time length<br>
# 
# $$\large Y_i = \beta_{\text{intercept}} + 1_{[\text{"long"}]}(\text{k_i})\beta_{\text{contrast}} + \epsilon_i \quad \text{ where } \quad \epsilon_i \sim \mathcal N\left(0, \sigma\right)$$
# 
# ### where we use $k_i$ (rather than $x_i$) (to refer to the "kind" or "katagory" or "kontrast") column (that you may have noticed was already a part) of the original dataset; and, explain the "big picture" differences between this model specification and the previously considered model specifications<br>
# 
# 1. `smf.ols('duration ~ waiting', data=old_faithful)`
# 2. `smf.ols('duration ~ waiting', data=old_faithful[short_wait])`
# 3. `smf.ols('duration ~ waiting', data=old_faithful[long_wait])`
# 
# ### and report the evidence against a *null hypothesis* of "no difference between groups "on average") for the new *indicator variable* based model<br>
# 

# In[ ]:


from IPython.display import display

display(smf.ols('duration ~ C(kind, Treatment(reference="short"))', data=old_faithful).fit().summary().tables[1])

fig = px.box(old_faithful, x='kind', y='duration', 
             title='duration ~ kind',
             category_orders={'kind': ['short', 'long']})
fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_  
# </details>

# In this analysis, we modify our classification of waiting times for eruptions of Old Faithful to redefine "short" and "long" wait times. Instead of defining "short" as less than 64 minutes and "long" as greater than 71 minutes, we now define wait times as "short" if they are less than 68 minutes, and "long" otherwise. We then consider a Simple Linear Regression model using an indicator variable to capture these categories.
# 
# The new model can be represented as:
# Here,  refers to the "kind" or category column, which specifies whether the waiting time for observation  is "short" or "long". The model uses an indicator variable, assigning a value of 1 if  is "long" and 0 if it is "short".
# 
# Comparing to Previous Model Specifications
# Pooled Model: This model uses the entire dataset, treating "waiting" as a continuous variable to predict eruption duration. It estimates a single linear relationship across the full range of waiting times.
# Subset Models (Short and Long Waits): These models analyze the relationship between waiting time and eruption duration separately for the "short" and "long" groups. Each subset has its own linear regression, allowing potentially different slopes and intercepts for each group.
# 
# Indicator Variable-Based Model
# The new model using an indicator variable is represented as:
# This model uses the "kind" ("short" vs. "long") as a categorical predictor, with "short" as the reference category. The interpretation of coefficients is:
# 1. The mean duration for "short" wait times.
# 2. The difference in mean durations between "long" and "short" groups.
# 
# Big Picture Differences Between Models
# 
# 1. Continuous vs. Categorical Predictor: The pooled model uses "waiting" as a continuous variable, estimating the relationship over the entire data range. The indicator model, by contrast, uses a categorical approach to compare the mean durations between two distinct groups.
# 
# 2. Subset Analysis vs. Group Comparison: The subset models provide separate analyses of the relationship within each group, allowing for differences in trends between the two categories. The indicator model, on the other hand, provides a single unified framework to compare group averages.
# 
# 3. Interpretation and Simplicity: The indicator model offers a straightforward comparison of means between groups. It highlights whether there is a statistically significant difference between "short" and "long" categories without estimating two separate regression lines.
# 
# Evidence Against Null Hypothesis
# To test for evidence against the null hypothesis of "no difference between groups on average", we examine the p-value for the  coefficient in the indicator model. If the p-value is less than a specified significance level (e.g., 0.05), we reject the null hypothesis and conclude that there is a statistically significant difference in eruption duration between "short" and "long" wait times. A box plot comparing durations across the two categories is useful for visualizing the differences: This plot illustrates the distribution of durations for both "short" and "long" wait times, helping to visually assess the difference between the groups.

# Summary:
# Comparison to Previous Models:
# Pooled Model: Used "waiting" as a continuous predictor across the entire dataset.
# Subset Models: Separated the data into "short" and "long" wait times, estimating different regression lines for each group.
# Indicator Variable Model: Unlike the previous models, this approach uses a categorical variable for "kind" to directly compare the mean eruption duration between "short" and "long" wait times, making the analysis simpler and more interpretable.
# Key Differences:
# Continuous vs. Categorical: The pooled model uses "waiting" as a continuous variable, while the indicator model uses a categorical approach.
# Group Comparison: The indicator model unifies the comparison of "short" vs. "long" into a single regression, avoiding the need for separate analyses.
# Simpler Interpretation: The indicator model offers a straightforward way to test for a significant difference in mean durations without estimating separate regression lines for each group.
# 
# Link: 
# https://chatgpt.com/share/672d7a70-837c-8004-a563-3760e76aa108

# ### 12. Identify which of the histograms suggests the plausibility of the assumption that the distribution of *error* terms is normal for each of the models, and explain why the other three do not support this assumption.
# 
# > Hint: Question 5 of the *Communication Activity #2* of the Oct25 TUT (addressing an *omitted* section of the TUT) discusses how the assumption in *Simple Linear Regression* that the *error* terms $\epsilon_i \sim \mathcal N\left(0, \sigma\right)$ is diagnostically assessed by evaluating distributional shape of the *residuals* $\text{e}_i = \hat \epsilon_i = Y_i - \hat y_i$
# 

# In[ ]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go
from scipy import stats
import numpy as np

model_residuals = {
    '<br>Model 1:<br>All Data using slope': smf.ols('duration ~ waiting', data=old_faithful).fit().resid,
    '<br>Model 2:<br>Short Wait Data': smf.ols('duration ~ waiting', data=old_faithful[short_wait]).fit().resid,
    '<br>Model 3:<br>Long Wait Data': smf.ols('duration ~ waiting', data=old_faithful[long_wait]).fit().resid,
    '<br>Model 4:<br>All Data using indicator': smf.ols('duration ~ C(kind, Treatment(reference="short"))', data=old_faithful).fit().resid
}

fig = make_subplots(rows=2, cols=2, subplot_titles=list(model_residuals.keys()))
for i, (title, resid) in enumerate(model_residuals.items()):

    if i == 1:  # Apply different bins only to the second histogram (index 1)
        bin_size = dict(start=-1.9, end=1.9, size=0.2)
    else:
        bin_size = dict(start=-1.95, end=1.95, size=0.3)

    fig.add_trace(go.Histogram(x=resid, name=title, xbins=bin_size, histnorm='probability density'), 
                  row=int(i/2)+1, col=(i%2)+1)
    fig.update_xaxes(title_text="n="+str(len(resid)), row=int(i/2)+1, col=(i%2)+1)    
    
    normal_range = np.arange(-3*resid.std(),3*resid.std(),0.01)
    fig.add_trace(go.Scatter(x=normal_range, mode='lines', opacity=0.5,
                             y=stats.norm(loc=0, scale=resid.std()).pdf(normal_range),
                             line=dict(color='black', dash='dot', width=2),
                             name='Normal Distribution<br>(99.7% of its area)'), 
                  row=int(i/2)+1, col=(i%2)+1)
    
fig.update_layout(title_text='Histograms of Residuals from Different Models')
fig.update_xaxes(range=[-2,2])
fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# ### 13. The "short" and "long" wait times are not "before and after" measurements so there are not natural pairs on which to base differences on which to do a "one sample" (paired differences) *hypothesis test*; but, we can do "two sample" hypothesis testing using a *permuation test*, or create a 95% *bootstrap confidence interval* for the difference in means of the two populations. 
# 
# ### (A) Do a permuation test $\;H_0: \mu_{\text{short}}=\mu_{\text{long}} \; \text{ no difference in duration between short and long groups}$ by "shuffling" the labels
# ### (B) Create a 95% bootstrap confidence interval  by repeatedly bootstrapping within each group and applying *np.quantile(bootstrapped_mean_differences, [0.025, 0.975])* to the collection of differences between the sample means.    
# ### (a) Explain how the sampling approaches work for the two simulations.
# ### (b) Compare and contrast these two methods with the *indicator variable* based model approach used in Question 11, explaining how they're similar and different.<br>
#     
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _You'll need to create `for` loops for repeated (shuffling simulation) **permutation** and (subgroup) **bootstrapping**, where_
# >
# > - _"shuffling" for **permutation testing** is done like this `old_faithful.assign(kind_shuffled=old_faithful['kind'].sample(n=len(old_faithful), replace=False).values)#.groupby('kind').size()`; then, the **mean difference statistic** is then calculated using `.groupby('kind_shuffled')['duration'].mean().iloc[::-1].diff().values[1]` (so the **observed statistic** is `old_faithful.groupby('kind')['duration'].mean().iloc[::-1].diff().values[1]`_
# > 
# >
# > - _"two sample" **bootstrapping** is done like this `old_faithful.groupby('kind').apply(lambda x: x.sample(n=len(x), replace=True)).reset_index(drop=True)#.groupby('kind').size()`; then, the **bootstrapped mean difference statistic** is then calculated using `.groupby('kind')['duration'].mean().iloc[::-1].diff().values[1]` (like the **observed statistic** except this is applied to the **bootstrapped** resampling of `old_faithful`)_
# > ---
# > 
# > _Don't forget to ask for summaries of all your different ChatBot sessions and organize and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatBot) But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!_
# </details>

# (a) How the Sampling Approaches Work for the Two Simulations
# Permutation Test (Hypothesis Testing):
# The permutation test is used to test if there is a significant difference between the means of the two populations ("short" and "long" wait times).
# Steps:
# Shuffle the "kind" labels across the entire dataset (old_faithful) to create a "null distribution," where you assume there is no relationship between the kind and the duration.
# Reassign each observation to either the "short" or "long" group randomly, effectively breaking any connection between the groups and the outcome (duration).
# After shuffling, calculate the mean difference between the "short" and "long" groups.
# Repeat this procedure many times (e.g., 1000 or more) to generate a distribution of mean differences under the null hypothesis.
# Compare the observed difference to this null distribution to determine the significance (p-value).
# Bootstrap Confidence Interval for Difference in Means:
# Bootstrapping is used to generate a confidence interval for the difference in means between the "short" and "long" groups.
# Steps:
# Randomly resample with replacement within each group ("short" and "long") separately. This maintains the original structure of the data.
# Calculate the mean duration for both the "short" and "long" resamples and find the difference between these means.
# Repeat the above steps multiple times to get a distribution of bootstrapped differences.
# Apply np.quantile(bootstrapped_mean_differences, [0.025, 0.975]) to determine the 95% confidence interval for the difference between the means.
# (b) Comparison with the Indicator Variable Based Model
# Indicator Variable Based Model (e.g., Linear Regression):
# 
# In this approach, an indicator variable (dummy variable) is introduced to represent the categorical group ("short" or "long"). A linear model then includes this indicator variable to explain the effect of group membership on the outcome (duration).
# The key idea is that this model estimates the mean difference between groups by considering the effect of "kind" as a coefficient, which is tested for significance using regression.
# Similarities Between Permutation, Bootstrapping, and Indicator Model:
# 
# Focus on Difference: All three methods are used to understand if there is a significant difference between the two groups.
# Nonparametric vs. Parametric:
# Both the permutation test and bootstrapping are nonparametric methods, meaning they make fewer assumptions about the distribution of the data.
# The indicator variable model is more of a parametric approach that assumes a linear relationship and normality of residuals.
# Differences:
# 
# Permutation Test focuses on testing the null hypothesis by generating a distribution under the assumption of no effect. It provides a p-value for hypothesis testing.
# Bootstrapping focuses on estimating the uncertainty of the difference between the means by building a confidence interval, not directly testing a null hypothesis.
# Indicator Variable Model uses a linear regression framework and provides a hypothesis test for the group difference through the model’s coefficients. It requires assumptions about linearity and homoscedasticity, unlike the other two methods.

# Summary: 
# Permutation Test: Randomly shuffles labels to assess whether group membership significantly affects the outcome.
# Bootstrap Confidence Interval: Repeatedly resamples data within each group to estimate the variability of the difference in means.
# Indicator Variable Model: Fits a regression model with an indicator variable for group membership and tests the group effect based on model coefficients.
# 

# ### 14. Have you reviewed the course wiki-textbook and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# >  _Here is the link of [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) in case it gets lost among all the information you need to keep track of_  : )
# >
# > _Just answering "Yes" or "No" or "Somewhat" or "Mostly" or whatever here is fine as this question isn't a part of the rubric; but, the midterm and final exams may ask questions that are based on the tutorial and lecture materials; and, your own skills will be limited by your familiarity with these materials (which will determine your ability to actually do actual things effectively with these skills... like the course project...)_
# </details>    

# ## Recommended Additional Useful Activities [Optional]
# 
# The "Ethical Profesionalism Considerations" and "Current Course Project Capability Level" sections below **are not a part of the required homework assignment**; rather, they are regular weekly guides covering (a) relevant considerations regarding professional and ethical conduct, and (b) the analysis steps for the STA130 course project that are feasible at the current stage of the course 
# 
# <br>
# <details class="details-example"><summary style="color:blue"><u>Ethical Professionalism Considerations</u></summary>
# 
# ### Ethical Professionalism Considerations
#     
# The TUT and HW both addressed some of the assumptions used in **Simple Linear Regression**. The **p-values** provided by `statsmodels` via `smf.ols(...).fit()` depend on these assumptions, so if they are not (at least approximately) correct, the **p-values** (and any subsequent claims regarding the "evidience against" the **null hypothesis**) are not reliable. In light of this consideration, describe how you could diagnostically check the first three assumptions (given below) when using analyses based on **Simple Linear regression** model. From an Ethical and Professional perspective, do you think doing diagnostic checks on the assumptions of a **Simple Linear regression** model is something you can and should do whenever you're doing this kind of analysis? 
#             
# > The first three assumptions associated with the **Simple Linear regression** model are that
# > 
# > - the $\epsilon_i$ **errors** (sometimes referred to as the **noise**) are **normally distributed**
# > - the $\epsilon_i$ **errors** are **homoscedastic** (so their distributional variance $\sigma^2$ does not change as a function of $x_i$)
# > - the linear form is [at least reasonably approximately] "true" (in the sense that the above two remain [at least reasonably approximately] "true") so that then behavior of the $Y_i$ **outcomes** are represented/determined on average by the **linear equation**)<br>
# > 
# >    and there are additional assumptions; but, a deeper reflection on these is "beyond the scope" of STA130; nonetheless, they are that<br><br>
# > - the $x_i$ **predictor variable** is **measured without error**
# > - and the $\epsilon_i$ **errors** are **statistically independent** (so their values do not depend on each other)
# > - and the $\epsilon_i$ **errors** are **unbiased** relative to the **expected value** of **outcome** $E[Y_i|x_i]=\beta_0 + \beta_1x_i$ (which is equivalently stated by saying that the mean of the **error distribution** is $0$, or again equivalently, that the **expected value** of the **errors** $E[\epsilon_i] = 0$)
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
# > ### NEW DEVELOPMENT<br>New Abilities Achieved and New Levels Unlocked!!!    
# > **As noted, the Week 01 HW introduced the [STA130F24_CourseProject.ipynb](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F24_CourseProject.ipynb) notebook.** _And there it instructed students to explore the notebook through the first 16 cells of the notebook._ The following cell in that notebook (there marked as "run cell 17") is preceded by an introductory section titled, "**Now for some comparisons...**", _**and all material from that point on provides an example to allow you to start applying what you're learning about Hypothesis Testing to the CSCS data**_ **using a paired samples ("one sample") framework.**
# >
# > **NOW, HOWEVER, YOU CAN DO MORE.** 
# > - _**Now you can do "two sample" hypothesis testing without the need for paired samples.**_ All you need are two groups.
# > - _**And now you can do simple linear regression modeling.**_ All you need are two columns.
# 
# ### Current Course Project Capability Level
# 
# At this point in the course you should be able to do a **Simple Linear Regression** analysis for data from the Canadian Social Connection Survey data
#     
# 1. Create and test a **null hypothesis** of no linear association "on average" for a couple of columns of interest in the Canadian Social Connection Survey data using **Simple Linear Regression**
# 
# 2. Use the **residuals** of a fitted **Simple Linear Regression** model to diagnostically assess some of the assumptions of the analysis
# 
# 3. Use an **indicator variable** based **Simple Linear Regression** model to compare two groups from the Canadian Social Connection Survey data
# 
# 4. Compare and contrast the results of an **indicator variable** based **Simple Linear Regression** model to analyses based on a **permutation test** and a **bootstrapped confidence interval**   
#     
# </details>    

# In[ ]:




