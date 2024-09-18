#!/usr/bin/env python
# coding: utf-8

# Pre-lecture 2. For better readability, the chatbot will simplify complex code, transforming it into a more understandable format with clear hints and detailed explanations. The chatbot will also break down each part of the code, providing step-by-step clarifications to ensure users can easily grasp the key elements and logic behind the code. 

# In[6]:


#Pre-Lecture 3
import numpy as np

# Initial setup
all_door_options = (1, 2, 3)  # Possible doors
my_door_choice = 1  # Starting door choice
i_won = 0  # Counter for wins when using the switch strategy
reps = 100000  # Number of repetitions

# Simulation loop
for _ in range(reps):
    # Randomly select the winning door
    secret_winning_door = np.random.choice(all_door_options)
    
    # Remove the secret winning door from the list of doors Monty can reveal
    all_door_options_list = [door for door in all_door_options if door != secret_winning_door]
    
    # Remove player's initial choice if it is still in the list (not the winning door)
    if my_door_choice in all_door_options_list:
        all_door_options_list.remove(my_door_choice)
    
    # Monty reveals one of the remaining doors (which always has a goat)
    goat_door_reveal = np.random.choice(all_door_options_list)
    
    # Player is forced to switch to the remaining door
    if my_door_choice != secret_winning_door:
        my_door_choice = secret_winning_door  # Player wins by switching

    # Check if the player's new choice is the winning door
    if my_door_choice == secret_winning_door:
        i_won += 1

# Calculate the win rate when always switching
win_rate = i_won / reps
print(win_rate)


# Pre-lecture
# Chatgpt: 
# https://chatgpt.com/share/66e8a54b-9fac-8004-924b-21f5268c7664
# Summary: 
# 
# In this conversation, we explored the concept of a Markovian ChatBot, which is a chatbot that generates responses based on a Markov chain. The Markov chain predicts the next word in a sequence by analyzing patterns from a text corpus and identifying which words frequently follow others.
# 
# We discussed how an early version of such a chatbot works, focusing on:
# 
# Text Data Collection – the chatbot learns from a corpus of text.
# Building a Markov Chain – a dictionary that maps words to possible next words based on the text.
# Response Generation – the chatbot generates responses by selecting the next word probabilistically from the Markov chain.
# We also reviewed a simple implementation of this chatbot in Python, demonstrating how it processes text, builds the Markov chain, and generates responses based on user input. Overall, the Markovian chatbot provides simple responses with limited context understanding, making it a foundational but unsophisticated conversational model compared to modern AI-driven chatbots.

# Post-lecture question 5: 
# 
# chatgpt link 
# 1) https://chatgpt.com/share/66eb4068-c780-8004-a73e-734c345fe227
# 2) https://chatgpt.com/share/66eb408f-0b64-8004-bc67-3c5ee5b5c588
# 
# summary: 
# Here’s a summary of our conversation:
# 1) 
# Markov Chain Code Review and Suggestions:
# 
# You initially shared some code for generating a Markov chain model, specifically tracking word transitions in bigrams and their occurrences.
# I suggested refactoring the code using defaultdict to make it more concise and Pythonic.
# Bigram Extension:
# 
# You extended the code to use bigrams (two consecutive words as the "state") for the Markov model, and I explained how this adds more context to predictions.
# I provided suggestions for further extensions, such as moving to higher-order n-grams and implementing smoothing techniques.
# Character-Specific Bigram Model:
# 
# You then introduced a more complex model where word sequences are specific to different characters from a dataset (avatar.character).
# I provided an optimized version of your code, leveraging defaultdict to simplify the logic and avoid redundant checks.
# Let me know if you'd like more details or clarifications!
# 
# 2) 
# In this conversation, you shared two segments of code related to building a Markov model for text generation. The first segment built a basic Markov chain model using word transitions, tracking how frequently a word follows another word. The second segment expanded on this by using bigrams (pairs of words) and associating them with specific characters from the avatar dataset. This more advanced model tracked how bigrams transitioned to subsequent words based on individual characters in the dataset. You requested a breakdown and summary of both code sections.

# Post-lecture question 6: 
# 1) 
# ChatGPT significantly enhances the speed at which code can be understood. It does this by breaking down the code into clear, manageable sections, allowing users to focus on key elements and core functions.ChatGPT can explain complex coding concepts in simpler terms and provide practical examples to reinforce understanding. 
# 
# 2) 
# Sometimes, ChatGPT may not solve questions correctly. Instead, it might provide incorrect explanations without diving deeply into the problem or thinking through the details. This can happen because ChatGPT doesn't "think" in the same way a human does. It relies on patterns from its dataset, and in many cases, those patterns work for solving typical problems. However, when faced with more nuanced or complex issues, the responses may miss key details or fail to apply the appropriate context needed for an accurate solution.
# 
# 3) 
# chatgpt is a very useful code for analyzing code. I think Chatgpt is our second professor in the university. 

# Post-lecture question 7
# My opinion remains the same. ChatGPT is a powerful tool for helping us understand complicated concepts more easily. It breaks down complex knowledge into more digestible parts, making learning more efficient. Additionally, ChatGPT can save us a significant amount of time when it comes to writing and analyzing code, offering quick solutions and examples that streamline the process.

# Post-lecture question 8
# 1~3
# Chatgpt link: https://chatgpt.com/share/66eb4b8f-cf64-8004-a1a8-05b4d36c9458
# summary: In this conversation, we discussed multiple topics, starting with the importance of learning and adaptability, communication, coding, and statistics and data analysis in the modern world. These skills are crucial for personal and professional success across industries, particularly in fields like data science, which is heavily reliant on data analysis, coding, and communication to interpret data-driven insights. I explained that pursuing a career as a statistician or data scientist would be difficult without coding or data analysis, as both roles fundamentally require these skills. However, I suggested alternative career paths such as data visualization specialist, data strategy consultant, and project management in the field of data science that may involve less hands-on coding.
# 
# Next, we shifted to your interest in becoming a game designer or game coder. I outlined the different skill sets required for each path. A game designer focuses on the creative aspects, such as gameplay mechanics, storytelling, and user experience design, with a need for game design theory, creativity, and basic prototyping skills. A game coder, on the other hand, requires strong technical skills in programming languages (C++, C#, Python), game engines (Unity, Unreal), and core computer science concepts like algorithms and data structures. Both roles require teamwork, problem-solving, and communication to collaborate effectively with other members of a game development team.
# 
# In conclusion, both game design and game coding require a mix of creativity and technical ability, with the former focusing on conceptualizing and building engaging experiences and the latter focused on programming and bringing those experiences to life through code.
# 
# 5. 
# I prefer to ask ChatGPT for specific knowledge rather than inquiring about the future of certain areas or majors. I find that ChatGPT is more effective when providing detailed information or explanations on particular topics rather than speculating about long-term trends or predictions.

# In[ ]:


Post-lecture question 9
Yes

