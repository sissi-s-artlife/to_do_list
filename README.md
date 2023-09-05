###Simple To-Do List Application
##Overview
This is a simple command-line to-do list application built in Python. The application allows users to manage their tasks, categorize them, and view their to-do list.

##Features
Add Tasks: Users can add tasks to their to-do list with a description.

##Category Assignment: The application automatically assigns a category to each task based on keywords found in the task description.

##View To-Do List: Users can view their to-do list with tasks and their corresponding categories.

##Exit the Application: Users can exit the application when they are done managing their tasks.

##How It Works
When a user adds a task, the application tokenizes the task description into words and compares each word with predefined categories and their associated keywords.

The category with the highest similarity to the task description is assigned to the task.

Users can continue to add tasks and view their to-do list until they choose to exit the application.

##Getting Started
Clone this repository to your local machine.

#Make sure you have Python installed.

#Install the required dependencies using pip:

pip install nltk
pip install wordnet
Run the application:

python main.py
Follow the prompts to add tasks and manage your to-do list.

###Why Use This Application?
Simplified Task Management: This application provides a simple and efficient way to manage your tasks without the need for complex user interfaces.

#Automatic Categorization: It automatically assigns categories to tasks, helping you organize your tasks without manual effort.

#Customizable Keywords: You can customize the predefined categories and keywords to match your specific needs.

#Quick Setup: With just a few steps, you can start using this to-do list application to stay organized.
