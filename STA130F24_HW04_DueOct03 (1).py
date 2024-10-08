#!/usr/bin/env python
# coding: utf-8

# ## STA130 Homework 04 
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
# 1. Code and write all your answers (for both the "Prelecture" and "Postlecture" HW) in a python notebook (in code and markdown cells) 
#     
#     > It is *suggested but not mandatory* that you complete the "Prelecture" HW prior to the Monday LEC since (a) all HW is due at the same time; but, (b) completing some of the HW early will mean better readiness for LEC and less of a "procrastentation cruch" towards the end of the week...
#     
# 2. Paste summaries of your ChatBot sessions (including link(s) to chat log histories if you're using ChatGPT) within your notebook
#     
#     > Create summaries of your ChatBot sessions by using concluding prompts such as "Please provide a summary of our exchanges here so I can submit them as a record of our interactions as part of a homework assignment" or, "Please provide me with the final working verson of the code that we created together"
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
# 
# 
# 

# ### Marking Rubric (which may award partial credit) 
# 
# - [0.1 points]: All relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] are reported within the notebook
# - [0.3 points]: Evaluation of correctness and effectiveness of written communication for Question "1"
# - [0.3 points]: Correctness of understanding confirmed by code comments and relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] for Question "4"
# - [0.3 points]: Evaluation of correctness and effectiveness of written communication for Question "6"
# <!-- - [0.3 points]: Evaluation of submission for Question "9" -->

# ### "Pre-lecture" HW [*completion prior to next LEC is suggested but not mandatory*]
# 
# #### To prepare for this weeks lecture, first watch this video [introduction to bootstrapping](https://www.youtube.com/watch?v=Xz0x-8-cgaQ)
# 

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('Xz0x-8-cgaQ', width=800, height=500)


# #### 1. The "Pre-lecture" video (above) mentioned the "standard error of the mean" as being the "standard deviation" of the distribution bootstrapped means.  What is the difference between the "standard error of the mean" and the "standard deviation" of the original data? What distinct ideas do each of these capture? Explain this concisely in your own words.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _To answer this question, you could start a ChatBot session and try giving a ChatBot a shot at trying to explain this distinction to you. If you're not sure if you've been able to figure it out out this way, review [this ChatGPT session](https://github.com/pointOfive/stat130chat130/blob/main/CHATLOG/wk4/GPT/SLS/00002_gpt3p5_SEM_vs_SD_Difference.md)._
# > - _If you discuss this question with a ChatBot, don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)._
# > 
# > _Note that the "Pre-lecture" video (above) and the last *Question 5* of The **Week 04 TUT Communication Actvity #2** address the question of "What is bootstrapping?", but the question of "What is the difference between the "standard error of the mean" and the "standard deviation" of the original data?" does not really depend on what bootstrapping is._
# > 
# > _If you were to be interested in answering the question of "What is bootstrapping?", probably just asking a ChatBot directly would work. Or even something like "Explain variability of means, function of sample size, bootstrapping" or "How does the variability of means of simulated samples change as a function of sample size? Explain this to me in a simple way using bootstrapping!" would likely be pretty effective as prompts. ChatBots are not particularly picky about prompts when it comes to addressing very well understood topics (like bootstrapping). That said, the more concise context you provide in your prompt, the more you can guide the relevance and relatability of the responses of a ChatBot in a manner you desire. The "Further Guidance" under *Question 5* of **Communication Actvity #2** in TUT is a good example of this._
#     
# </details>

# The standard deviation is used to calculate the variability of the centralized data (spread around the mean). It remains unchanged as the sample size increases. A smaller standard deviation indicates that the data is more tightly clustered around the average value.
# 
# On the other hand, the standard error of the mean measures how much the sample mean is expected to vary from the true population mean, indicating the precision of the sample mean as an estimate of the population mean. The standard error decreases as the sample size increases, as larger samples tend to provide more accurate estimates of the population mean.

# Chatgpt link: https://chatgpt.com/share/66fca649-e160-8004-8bc8-9136e289ea12
# Summary: 
# In this conversation, we discussed the difference between Standard Deviation (SD) and Standard Error of the Mean (SEM) in detail:
# 
# Standard Deviation (SD) measures the variability or spread of individual data points within a dataset, reflecting how much the values differ from the mean.
# 
# Standard Error of the Mean (SEM) measures the accuracy of the sample mean as an estimate of the population mean, indicating the precision of the sample mean.
# 
# Key differences:
# 
# SD is independent of sample size, while SEM decreases as the sample size increases.
# SD captures the variability of the data points, while SEM captures the variability of the sample mean in relation to the population mean.
# SEM is always smaller than SD and is used when estimating the precision of the sample mean, while SD is used to describe the data's spread.
# 
# 
# 
# 
# 
# 

# #### 2. The "Pre-lecture" video (above) suggested that the "standard error of the mean" could be used to create a confidence interval, but didn't describe exactly how to do this.  How can we use the "standard error of the mean" to create a 95% confidence interval which "covers 95% of the bootstrapped sample means"? Explain this concisely in your own words.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Just describe the proceedure itself (probably as reported by a ChatBot), but explain the procedure in your own words in a way that makes the most sense to you. The point is not to understand or explain the theoretical justification as to why this procedure exists, it's just to recognize that it does indeed exist and to briefly describe it. This is because in this class we're going to instead focus on understanding and using 95% bootstrapped confidence intervals. So this "sample mean plus and minus about 2 times the standard error" really only provides some context against which to contrast and clarify bootstrapped confidence intervals_
# >
# > - _If you continue get help from a ChatBot for this question (as is intended and expected for this problem), don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)._
# </details>

# First we need to get the mean of the sample. Secondly, compute the standard error of the mean (SEM) by dividing the standard deviation by the square root of the sample size. Then, multiply the SEM by 1.96, which corresponds to a 95% confidence level for a normal distribution. Finally, add and subtract this result from the sample mean to determine the confidence interval. 

# Summary:
# In this conversation, we discussed how to use the standard error of the mean (SEM) to create a 95% confidence interval. Here's the summary:
# 
# Procedure for Confidence Interval with SEM:
# 
# Calculate the sample mean.
# Compute the SEM by dividing the standard deviation by the square root of the sample size.
# Multiply the SEM by 1.96 to cover 95% of the distribution.
# Add and subtract this value from the sample mean to form the 95% confidence interval.
# Why 1.96?: We use 1.96 because it corresponds to the 95% confidence level in a normal distribution, meaning 95% of the data points fall within 1.96 standard deviations from the mean. Using a smaller number like 1.00 would only give a confidence level of 68%.
# 
# The focus of the conversation was on understanding this traditional approach, which contrasts with the bootstrapped confidence intervals that will be the focus in your class. 

# Chatgpt link: https://chatgpt.com/share/66fca649-e160-8004-8bc8-9136e289ea12

# #### 3. Creating the "sample mean plus and minus about 2 times the standard error" confidence interval addressed in the previous problem should indeed cover approximately 95% of the bootstrapped sample means. Alternatively, how do we create a 95% bootstrapped confidence interval using the bootstrapped means (without using their standard deviation to estimate the standard error of the mean)? Explain this concisely in your own words.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _A good explaination here would likely be based on explaining how (and why) to use the `np.quantile(...)` function on a collection of bootstrapped sample means. The "pre-lecture video" describes what this should be, just not in terms of`np.quantile(...)`, right before the "double bam"._
# >
# > _That said, there are many other questions about bootstrapping that you should be working on familiarizing yourself with as as you're thinking through th proceedure that answers this question._
# > 
# > - _If you had a_ ~theoretical distribution~ _histogram of bootstrapped sample means representing the variability/uncertianty of means (of "averages") that an observed sample of size n produces, how would you give a range estimating what the sample mean of a future sample of size n might be?_
# >
# > - _Unlike the "sample mean plus and minus about 2 times the standard error" approach which would only cover **approximately** 95% of the bootstrapped sample means, a 95% bootstrapped confidence interval would cover exactly 95% of the bootstrapped means._
# >
# > - _While the variability/uncertainty of sample mean statistics when sampling from a population is a function of the sample size (n) [how?], we would NEVER consider using a bootstrapped sample size that was different than the size of the original sample [why?]._
# >
# > - _Are bootstrapped samples different if they are the same size as the original sample and created by sampling **without replacement**?_
# 
# </details>

# first, we need to resample our original data multiple times to generate bootstrap samples. Then, calculate the mean of each bootstrap sample. Next, we sort the resulting bootstrapped means and use np.quantile(...) to find the 2.5th percentile and the 97.5th percentile of the sorted means. The range between these two percentiles forms the 95% bootstrapped confidence interval, covering exactly 95% of the bootstrapped means.

# Chatgpt summary: 
# In this conversation, we discussed how to use the np.quantile(...) function to create a 95% bootstrapped confidence interval:
# 
# Generate multiple bootstrapped samples, calculate their means, and use np.quantile(...) to find the 2.5th and 97.5th percentiles of the bootstrapped means.
# These percentiles form the 95% confidence interval, covering exactly 95% of the bootstrapped means.
# We also clarified that bootstrapped samples must be the same size as the original sample and created with replacement to accurately estimate variability and uncertainty of sample means. Sampling without replacement would distort the variability needed for proper estimation.

# Chatgpt link: https://chatgpt.com/share/66fca649-e160-8004-8bc8-9136e289ea12

# #### 4. The "Pre-lecture" video (above) mentioned that bootstrap confidence intervals could apply to other statistics of the sample, such as the "median". Work with a ChatBot to create code to produce a 95% bootstrap confidence interval for a population mean based on a sample that you have and comment the code to demonstrate how the code can be changed to produce a 95% bootstrap confidence interval for different population parameter (other than the population mean, such as the population median).<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Hint: you can ask your ChatBot to create the code you need, and even make up a sample to use; but, you should work with your ChatBot to make sure you understand how the code works and what it's doing. Just having a ChatBot comment what the code does is not what this problem is asking you to do. This problem wants YOU to understand what the code does. To make sure you're indeed doing this, consider deleting the inline explanatory comments your ChatBot provides to you and write them again in your own words from scratch._
# >
# > - _Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)!_
# 
# </details>

# In[ ]:


# Create an empty list to store the bootstrap medians
boot_medians = []

# Generate bootstrap samples and calculate the median for each
for i in range(n_iterations):
    boot_sample = np.random.choice(data, size=n_size, replace=True)
    # Calculate the median of the bootstrap sample and store it
    boot_medians.append(np.median(boot_sample))

# Calculate the 95% confidence interval for the median
lower_bound = np.quantile(boot_medians, 0.025)
upper_bound = np.quantile(boot_medians, 0.975)

# Print the 95% bootstrap confidence interval for the median
print(f"95% Bootstrap Confidence Interval for the Median: ({lower_bound}, {upper_bound})")


# Summary 
# In this conversation, we explored how to create a 95% bootstrap confidence interval for the population mean using Python code. The process involves generating many bootstrap samples from the original dataset, calculating the mean for each sample, and using np.quantile() to find the 2.5th and 97.5th percentiles of the bootstrapped means, which form the confidence interval.
# 
# We also discussed how to adapt this procedure to calculate a confidence interval for other statistics, such as the median, by simply replacing np.mean() with np.median() in the code. Each part of the code was explained step by step for full understanding.

# Code summary:
# Here’s a summary of the code for generating a 95% bootstrap confidence interval for the population mean (or other statistics like the median):
# 
# Generate a dataset: A sample dataset is defined as an array (data).
# 
# Set bootstrap parameters: Define the number of bootstrap iterations (n_iterations) and the sample size (n_size).
# 
# Create bootstrap samples: Use a loop to randomly resample (with replacement) from the original dataset 10,000 times. For each resample, calculate the mean (or other statistics, like the median) and store it in a list.
# 
# Compute percentiles: Use np.quantile() to find the 2.5th and 97.5th percentiles of the stored bootstrapped means, which form the 95% confidence interval.
# 
# Display the result: Print the calculated confidence interval for the statistic (mean or median).
# 
# This code can easily be modified to calculate the confidence interval for other statistics by changing the function used in the loop (e.g., np.mean() to np.median()).

# Chatgpt link: https://chatgpt.com/share/66fca649-e160-8004-8bc8-9136e289ea12

# <details class="details-example"><summary style="color:blue"><u>Continue now...?</u></summary>
# 
# ### Pre-lecture VS Post-lecture HW
# 
# Feel free to work on the "Post-lecture" HW below if you're making good progress and want to continue: some of the "Post-lecture" HW questions continue to address the "Pre-lecture" video, so it's not particularly unreasonable to attempt to work ahead a little bit... 
# 
# - The very first question of the the "Post-lecture" HW addresses the previously emphasized topic of *parameters* versus *statistics*, and would again be a very good thing to be clear about in preparation for the upcoming lecture...
#     
# *The benefits of continue would are that (a) it might be fun to try to tackle the challenge of working through some problems without additional preparation or guidance; and (b) this is a very valable skill to be comfortable with; and (c) it will let you build experience interacting with ChatBots (and beginning to understand their strengths and limitations in this regard)... it's good to have sense of when using a ChatBot is the best way to figure something out, or if another approach (such as course provided resources or a plain old websearch for the right resourse) would be more effective*
#     
# </details>    

# ### "Post-lecture" HW [*submission along with "Pre-lecture" HW is due prior to next TUT*]

# #### 5. The previous question addresses making a confidence interval for a population parameter based on a sample statistic. Why do we need to distinguish between the role of the popualation parameter and the sample sample statistic when it comes to confidence intervals? Explain this concisely in your own words.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _This question helps clarify the nature and relative roles of (population) parameters and (sample) statistics, which forms the fundamental conceptual relationship in statistics and data science; so, make sure you interact with a ChatBot (or search online or in the course [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki)) carefully and thoroughly to ensure that you understand the distinctions here in the context of confidence intervals._
# >
# > - _As always, don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)._
# 
# </details>

# The population parameter is the true but unknown value we're trying to estimate. The sample statistic is the value we calculate from our sample data 

# Summary: 
# The population parameter is the true, unknown value we want to estimate, while the sample statistic is a value calculated from a sample. Confidence intervals use the sample statistic to estimate a range that likely contains the population parameter. Distinguishing between the two helps us interpret confidence intervals correctly as estimates about the population, rather than just descriptions of the sample.

# Link: https://chatgpt.com/share/66fdf56c-a8fc-8004-9bb8-d988284a1850

# #### 6. Provide written answers explaining the answers to the following questions in an informal manner of a conversation with a friend with little experience with statistics. <br>
# 
# 1. What is the process of bootstrapping? 
# 2. What is the main purpose of bootstrapping? 
# 3. If you had a (hypothesized) guess about what the average of a population was, and you had a sample of size n from that population, how could you use bootstrapping to assess whether or not your (hypothesized) guess might be plausible?
#    
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Your answers to the previous questions 3-5 above (and the "Further Guidance" comments in question 3) should be very helpful for answering this question; but, they are very likely be more technical than would be useful for explaining these ideas to your friends. Work to use descriptive and intuitive language in your explaination._
# 
# </details>

# 1. Randomly select a number from the dataset and repeat this process until you have the same number of selections as the total number of values in the dataset. Then, calculate the average value of this sample. Repeat this process thousands of times, and you will obtain a more accurate representation (distribution) of the possible means, giving insight into the variability and uncertainty of the dataset. 
# 2. To measure the uncertainty of the dataset, we use bootstrapping. This ensures that the values in the dataset are reliable by assessing how much variation there is in the possible means.
# 3. After bootstrapping and obtaining a distribution, you can check the estimated mean against this distribution. For example, if you predict the mean to be 170, you can see if 170 falls within the 95% confidence interval of the bootstrapped distribution. If it does, then 170 is likely to be a reasonable estimate for the true average of the dataset.

# 
# #### 7. The "Pre-lecture" video (above) introduced hypothesis testing by saying that "the confidence interval covers zero, so we cannot reject the hypothesis that the drug is **[on average]** not doing anything".  This conclusion could be referred to as "failing to reject the null hypothesis", where the term "null" refers to the concept of "no effect **[on average]**".  Why does a confidence interval overlapping zero "fail to reject the null hypothesis" when the observed sample mean statistic itself is not zero? Alternatively, what would lead to the opposite conclusion in this context; namely, instead choosing "to reject the null hypothesis"? Explain the answers to these questions concisely in your own words.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _This question (which addresses a very similar content to the third question of the previous probelm) is really about characterizing and leveraging the behavior of the variability/uncertainty of sample means that we expect at a given sample size. Understanding why this characterization would explain the answer to this question is the key idea underlying statistics. In fact, this concept is the primary consideration in statistics and the essense of how statistical analysis works._
# > 
# > - In answering this question it is surely helpful to note the difference between the observed sample values in the sample $x_i$ (for $i = 1, \cdots, n$), the observed sample average $\bar x$, and the actual value of the parameter $\mu$ clearly. Hopefully the meanings and distinctions here are increasingly obvious, as they should be if you have a clear understanding of the answer to question "5" above. Related to this, the quotes above have been edited to include "**[on average]**" which more accurately clarifies the intended meaning of the statements from the video. It's very relevent (again related to Question "5" above) to understand why are we bothering with making an explicit distinction with this, and why is it slightly different to say that "the drug is on average not doing anything" as opposed to saying "the drug is not doing anything"._
# > 
# > Using a **null hypotheses** (and corresponding **alternative hypothesis**) will be addressed next week; but, to give a sneak peak preview of the **hypothesis testing** topic, the "null" and "alternative" are formally specified as 
# >    
# > $H_0: \mu=0 \quad \text{ and } \quad H_A: H_0 \text{ is false}$
# >
# > which means that our **null hypotheses** is that the average value $\mu$ of the population is $0$, while our **alternative hypothesis** is that the average value $\mu$ of the population is not $0$. 
# > 
# > **Statistical hypothesis testing** proceeds on the basis of the **scientific method** by defining the **null hypothesis** to be what we beleive until we have sufficient evidence to no longer believe it. As such, the **null hypotheses** is typically something that we *may not actually believe*; and, actually, the **null hypotheses** simply serves as a sort of "straw man" which we in fact really intend to give evidence against so as to no longer believe it (and hence move forward following the procedure of the **scientific method**).
# </details>

# Bootstrapping is a method that uses resampling with replacement to estimate the variability of a statistic. In hypothesis testing, the null hypothesis assumes the drug's average effect is zero. When the confidence interval includes zero, it means that zero is a plausible value for the population mean, so there isn’t enough evidence to show the drug has a significant effect, and we "fail to reject the null hypothesis." If the confidence interval does not include zero, we have evidence that the drug has a statistically significant effect, and we reject the null hypothesis.

# #### 8. Complete the following assignment. 
# 

# ### Vaccine Data Analysis Assignment
# 
# #### Overview
# 
# The company AliTech has created a new vaccine that aims to improve the health of the people who take it. Your job is to use what you have learned in the course to give evidence for whether or not the vaccine is effective. 
# 
# #### Data 
# AliTech has released the following data.
# 
# ```csv
# PatientID,Age,Gender,InitialHealthScore,FinalHealthScore
# 1,45,M,84,86
# 2,34,F,78,86
# 3,29,M,83,80
# 4,52,F,81,86
# 5,37,M,81,84
# 6,41,F,80,86
# 7,33,M,79,86
# 8,48,F,85,82
# 9,26,M,76,83
# 10,39,F,83,84
# ```
# 
# #### Deliverables
# While you can choose how to approach this project, the most obvious path would be to use bootstrapping, follow the analysis presented in the "Pre-lecture" HW video (above). Nonetheless, we are  primarily interested in evaluating your report relative to the following deliverables.
# 
# - A visual presentation giving some initial insight into the comparison of interest.
# - A quantitative analysis of the data and an explanation of the method and purpose of this method.
# - A conclusion regarding a null hypothesis of "no effect" after analyzing the data with your methodology.
# - The clarity of your documentation, code, and written report. 
# 
# > Consider organizing your report within the following outline template.
# > - Problem Introduction 
# >     - An explaination of the meaning of a Null Hypothesis of "no effect" in this context
# >     - Data Visualization (motivating and illustrating the comparison of interest)
# > - Quantitative Analysis
# >     - Methodology Code and Explanations
# >     - Supporting Visualizations
# > - Findings and Discussion
# >     - Conclusion regarding a Null Hypothesis of "no effect"
# >     - Further Considerations
# 
# #### Further Instructions:
# - When using random functions, you should make your analysis reproducible by using the `np.random.seed()` function
# - Create a CSV file and read that file in with your code, but **do not** include the CSV file along with your submission
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Calculate the difference between final and initial health scores
data['HealthDiff'] = data['FinalHealthScore'] - data['InitialHealthScore']

# Function to perform bootstrapping
def bootstrap_mean_diff(data, num_samples=10000):
    boot_means = []
    for _ in range(num_samples):
        sample = np.random.choice(data['HealthDiff'], size=len(data), replace=True)
        boot_means.append(np.mean(sample))
    return boot_means

# Perform bootstrapping
bootstrap_means = bootstrap_mean_diff(data)

# Calculate the 95% confidence interval
ci_lower = np.percentile(bootstrap_means, 2.5)
ci_upper = np.percentile(bootstrap_means, 97.5)

# Plot the bootstrap distribution
plt.hist(bootstrap_means, bins=30, alpha=0.7, color='blue')
plt.axvline(ci_lower, color='red', linestyle='--', label='95% CI Lower')
plt.axvline(ci_upper, color='green', linestyle='--', label='95% CI Upper')
plt.axvline(0, color='black', linestyle='-', label='Zero (Null Hypothesis)')
plt.legend()
plt.title('Bootstrap Distribution of Mean Health Score Differences')
plt.xlabel('Mean Difference (Final - Initial)')
plt.ylabel('Frequency')
plt.show()

print(f"95% Confidence Interval: ({ci_lower}, {ci_upper})")


# #### 9. Have you reviewed the course wiki-textbook and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?<br>
#     
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# >  Here is the link of [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) in case it gets lost among all the information you need to keep track of  : )
# > 
# > Just answering "Yes" or "No" or "Somewhat" or "Mostly" or whatever here is fine as this question isn't a part of the rubric; but, the midterm and final exams may ask questions that are based on the tutorial and lecture materials; and, your own skills will be limited by your familiarity with these materials (which will determine your ability to actually do actual things effectively with these skills... like the course project...)
# 
# </details>
# 
# _**Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)!**_

# # Recommended Additional Useful Activities [Optional]
# 
# The "Ethical Profesionalism Considerations" and "Current Course Project Capability Level" sections below **are not a part of the required homework assignment**; rather, they are regular weekly guides covering (a) relevant considerations regarding professional and ethical conduct, and (b) the analysis steps for the STA130 course project that are feasible at the current stage of the course 
# 
# <br>
# <details class="details-example"><summary style="color:blue"><u>Ethical Professionalism Considerations</u></summary>
# 
# 1. What is the difference between reporting a sample statistic (say, from the Canadian Social Connection Survey) as opposed to the a population parameter (chacterizing the population of the Canadians the Canadian Social Connection Survey samples)?
# 2. Why should bootsrapping (and confidence intervals in particular) be utilized when reporting sample statistics (say, from the Canadian Social Connection Survey)?
# 3. How does bootsrapping (and confidence intervals in particular) help us relate the data we have to all Canadians? 
# 4. Is the population that the Canadian Social Connection Survey samples really actually all Canadians? Or is it biased in some way? 
# 5. Why are the previous questions "Ethical" and "Professional" in nature?
# 6. If the Canadian Social Connection Survey samples Canadians in some sort of biased way, how could we begin considering if the results can generalize to all Canadians; or, perhaps, the degree to which the results could generalize to all Canadians?
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
# At this point in the course you should be able to compute a bootstrap confidence interval for the (candian) population mean of a numeric variable of the sample of the Canadian Social Connection Survey. On the basis of only using the techniques we've encountered in the course so far, it would only be possible to assess a null hypothesis of "no effect" if we had "paired" (e.g., "before and after") measurements in our data; but, we could of course assess a hypothesized parameter value estimated by the bootstrapped confidence interval of a relevant sample statistic...
#     
# 1. What are the different samples and populations that are part of the data related to the Canadian Social Connection Survey?
#     
# 2. Consider whether or not we have "paired" (e.g., "before and after") measurements in our data which could be used to assess a null hypothesis of "no effect" (in the manner of the "Pre-lecture" HW video above); and, if such data is available, create a confidence interval for the average sample difference and use it to assess a null hypothesis of "no effect".
#     
# 3. Pick a couple numeric variables from the Canadian Social Connection Survey with different amounts of non-missing data and create a 95% bootstrapped confidence intervals estimating population parameters for the variables.  
#     1. You would not want to do this by hand [why?]; but, could you nonetheless describe how this process would be done if you were to do it by hand? 
# 
#     2. [For Advanced Students Only] There are two factors that go into the uncertainty of sample means: the standard deviation of the original sample and the size of the sample (and they create a standard error of the mean that is theoretically "the standard deviation of the original sample divided by the square root of n").  Compute the theoretical standard errors of the sample mean for the different variables you've considered; and, if they're different, confirm that they influence the (variance/uncertainty) bootstrapped sampling distribution of the mean as expected
# 
# </details>            
