import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet

# Download NLTK data (WordNet and stopwords)
nltk.download("wordnet", quiet=True)
nltk.download("stopwords", quiet=True)

# Predefined task categories
categories = {
    "work": ["meeting", "presentation", "report"],
    "personal": ["groceries", "exercise", "call"],
    "shopping": ["buy", "purchase", "shopping"]
}

# Function to get word similarity using Wu-Palmer Similarity
def get_word_similarity(word1, word2):
    synset1 = wordnet.synsets(word1)
    synset2 = wordnet.synsets(word2)

    if synset1 and synset2:
        similarity = synset1[0].wup_similarity(synset2[0])
        return similarity if similarity is not None else 0.0
    else:
        return 0.0

# Main to-do list
to_do_list = []

while True:
    print("To-Do List:")
    for idx, task in enumerate(to_do_list, start=1):
        print(f"{idx}. {task['description']} (Category: {task['category']})")

    action = input("Enter 'add' to add a task or 'exit' to quit: ")

    if action == "exit":
        break
    elif action == "add":
        task_description = input("Enter your task: ")

        # Tokenize the input task description
        task_tokens = task_description.lower().split()

        # Initialize category similarity
        max_similarity = 0.0
        similar_category = "uncategorized"

        # Iterate through each token and calculate similarity
        for token in task_tokens:
            for cat, keywords in categories.items():
                for keyword in keywords:
                    similarity = get_word_similarity(token, keyword)
                    if similarity > max_similarity:
                        max_similarity = similarity
                        similar_category = cat

        # Assign the category with the highest similarity
        category = similar_category

        to_do_list.append({"description": task_description, "category": category})
        print(f"Task added! (Category: {category})")

print("Goodbye!")


