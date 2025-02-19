# This site is under development
This site will contain files for the Spring 2025 Python for Science class. 
$$Please Note: The first Lesson is a Jupyter Notebook on Installing Jupyter Lab. You can not run it without having Jupyter installed, so I create an HTML Version here: [https://rebelford.github.io/IOCT-TECH/01_aSetUpComputer%20.html](https://rebelford.github.io/IOCT-TECH/01_aSetUpComputer%20.html)

If you have any questions or concerns please contact [Bob Belford](mailto:rebelford@ualr.edu).

One can argue that in the 21st century coding is a critical skill that should be taught to science students, but is often missing in the undergraduate science curriculum, with students having to teach themselves when they enter grad schools or the workplace. The goal of this class is to expose science students to Python and coding with a focus on how to navigate scientific python packages.  

Students will first learn how to run Conda enviroments using miniconda hosted on Linux or Mac OS, and those with Windows machines will use Windows Subsystem Linux. Students will be generating Jupyter Notebooks in a Jupyter Lab in contrast to using a traditional IDE, as our objective is not to create a program but to understand coding and the use of scientific packagers in exploratory studies. Once they have mastered running notebooks in conda environments we will go over pythonic object oriented programming concepts with a goal of understanding classes, type and pythonic data structures.  Once this is done we will use this framework and AIs to explore the capabilities of various scientific data packages. 

Students will be expected to experiment with multiple AIs in this course, and are expected to buy a subscription for the duration of the course. I have subscriptions to [Perplexity.ai](https://www.perplexity.ai) and [ChatGPT](https://chatgpt.com/) and use them to help develop code and understand how different Python modules and packages work.
## GitHub Directory Descriptions
1. Assignments -  This is where student workbooks will be posted.  When you complete a workbook you should upload it to your UALR Google Drive for grading.
2. Module1-SetUp - This module includes 6 Jupyter Notebook based lesson plans to get you set up and understand how Python and Jupyter Lab runs. There is also an introduction to Git and GitHub. Note, I made an html version of [01-1_SetUpComputer.ipynb](https://rebelford.github.io/IOCT-TECH/01_aSetUpComputer%20.html) because you can not run the notebook and play the embedded video until you have installed Jupyter Lab.  That is, you can't run a lab on installing the lab until after you have installed the lab.
3. Module2-OOPDataStructures - This Module is an introduction to Python Object Oriented Programming and Data Structures. In addition to built-in volatile data structures we cover persistent data structures that reside outside of the python program.
4. Search_Utility - This directory contains a search utility program you can download to your computer and search all the jupyter notebooks in your home directory, or a specified subdirectory of your home directory.

## Directory Hierarchy on local PC
Organizing your files is very important and as you run the modules you should maintain an appropriate directory structure.  Many of the scripts in the modules will create embedded subdirectories within your home directory  and it is important you understand how to navigate this. I am going to share part of the directory hierarchy I have created, both manually and automagically, and how I use the search utility and AI programs like Perplexity and ChatGPT. 


```/home/user/
    └── minconda3/
        └── envs/
    └── projects/
    │   └── py4sci(.git repo)/
    │   └── other_project(.git repo)/
    ├──sandbox/
    ├── data/
    │   ├── project_a/
    │   └── project_b/
    ├──search_results/
    ├──ai_books/


```
### Local Directory Descriptions
- **minconda3/** - Created when installed miniconda, the envs folders are generated every time a virtual environment created
- **projects/** - Manually Created - each conda environment needs a project folder to organize the python files and jupyter notebooks that need the packages of that environment. The files in this folder can be git repositories, and this is where your class folder should be cloned.
- **sandbox/** - Automagically created by scripts, this is where we will keep files we use as we play around and experiment.  This should not be a git repo as you do not want to sync this with github, this is your "sandbox"
- **data/** - Automagically created by scripts (with subdirectories) and this is where we will keep data files associated with assignments, that is, real data, and so it needs to be structured so you can find it when you need it. This should not be in a git repo that you push from, unless you want to upload all that data to github, which is probably not wise.
- **search_results/** Auotmagically created the first time you run the search-utility program.  You should move that program to this folder after it is created. Everytime you run a search an html file will be generated with a name like search_search-term.html, so if I searched for csv it would be called serch_csv.html.  When you open this in the Jupyter Lab an html page will open with links to different notebooks, followed by a list of all headers that contain that link.  You can not open the notebook in the current notebook, but have to open in new tab or new window.  What I do is open a bunch in different tabs, and then browse through them to find what I need, allowing me to quickly look through all my notebooks that have a topic I am working on. This should not be a git repo as you are searching your own work space.
- **ai_books/** - When I engaged an AI on a search topic I copy the results into a markdown cell.  These are already formatted to generate headers that can be found by the search utility.  I will often design new headers to allow me to find topics by search terms, and I will also create small code cells that demonstrate coding concepts. I would not make this a git repo, as this is more like a collection of my private note resulting from my interactions with AIs.
## Interacting with AIs
Before delving into best practices for the use of AIs we should take a quick look into what AIs are and how they learn.  The AIs we are dealing with are Large Language Models (LLMs) and they do not learn the way a human does, but generate results based on probability. That is, they generate a "pattern-based" answer based on training data. For example, if you were to ask the AI what was the capital of England, based on the data the AI was trained with, the most probable answer would be London, that is, it gives the most probable answer based on its training data. A useful analogy would be the difference between a chef, a human who understands ingredients, techniques and flavors and a giant cookbook with millions of recipes (the AI). If a recipe was missing a step the human could experiment with logic and common sense, while all the AI can do is combine elements of recipes it contains.

So you need to look at the AI as your partner that has access to huge amounts of information, but not as a wise entity that knows the answers.  The AI does not learn like a human does, and it lacks reasoning and original thought. So why treat the AI as a partner and what is the value of AIs mimicking understanding through Linguistic patterns? I believe the answer to this lies in conversational learning, that is human to human conversation is an archetypal schema for information transference and processing, and our ability to learn is enhanced when we communicate with an AI as if it was a human, even though it is not. 

### AI vs. Traditional Searches
When you do a traditional search you are limited to reviewing the pages you can manually view, and even if Google returns several thousand hits, you seldom look past the first page. An AI refines your search and many AIs like Perplexity show you how they generate new searches from your original search. They AI can then process far more documents in a fraction of the time that a human can and so you have a greater depth and breadth of the search. Finally, the AI can assist in interpreting the results of the search.

### AI Learning Library
In this class I am asking you to create AI Learning Journals that are compiled in your AI_books directory. That is, you start your human to AI interaction with a search and refine it with a discussion. If you transfer this conversations to the markdown cells of Jupyter notebook dedicated to this topic you have created a learning journal on that topic. With the `search_utility` inside of the `search_results` directory you are quickly able to access all the notebooks that have headers with a search term. The result is an easily navigatable learning library of the conversations you have generated with your AI discourse, all within the Jupyter Lab.

OK, let's try and develop some "do's" and "don'ts" with regards to AIs and learning, and realize this dichotomy will evolve as we gain more experience.

### Best Practies In Education
**Do's**
- Use AI as **thinking partner**.
- Use AI for Exploration, not just answers.
- Use AIs for Feedback, Share your thoughts.
- Leverage AI for Brainstorming and Ideation.
- Let the AI know when you think it made a mistake and feel free to argue with it (have a dialogue as if it was human)

**Don'ts**
- Don't passively accept AI answers as truth.
- Don't use AI as a shortcut to avoid learning.
- Don't rely on AI for original thought and creativity
- Don't rely on the AI for everything
- Don't ask AIs to write full projects for you.
- 


### Best Practices in AI assisted Queries 

**Do's**
- Ask specific well-defined questions
   - Don't ask "How do I use Pandas?"
   - Ask "How do I read a csv file into a Pandas dataframe". 
- Verify AI-Generated Code (I have examples where AIs have gone in circles)
- Break Large tasks into little steps (and have a conversation along the way)
- Use the AI to Debug!
- Ask the AI to explain code line-by-line, or element-by-element

**Don'ts**
- Don't just copy-paste without understanding
- Don't assume the AI is always correct
- Don't skip writing the code
- Don't get frustrated when AI gives perplexing answers

Finally, you should always acknowledge the use of AI assistance in your work. OK, go out and experiment.  But AIs are of great value in navigating Python packages and data science resources in general. 

# Acknowledgements 
 This content was developed with assistance from [Perplexity AI](https://www.perplexity.ai/) and [Chat GPT](https://chatgpt.com/). Multiple queries were made during the Fall 2024 and the Spring 2025.