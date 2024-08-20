#!/usr/bin/env python
import sys
import os
from dotenv import load_dotenv
from blog_post_creator.crew import BlogPostCreatorCrew

# Load environment variables from .env file
load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    print("Running crew")
    """
    Run the crew.
    """
    inputs = {
        'url': 'https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/'
    }
    BlogPostCreatorCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'url': 'https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/'
    }
    try:
        BlogPostCreatorCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BlogPostCreatorCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'url': 'https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/'
    }
    try:
        BlogPostCreatorCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

