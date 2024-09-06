import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM
from dotenv import load_dotenv
from graph import create_workflow

# Load environment variables from .env file
load_dotenv()


# Create the workflow
app = create_workflow(LLM)

# test instruction
# test_instruction = "Write a 5000 words, current and up to date 100% unique guide for my intermittent fasting for women over 50 cookbook on \u201cSnacks\u201d with humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively."
test_instruction = "Write a 5000 word piece on the HBO TV show WestWorld and its plot, characters, and themes. \
    Make sure to cover the tropes that relate to AI, robots, and consciousness. \
    Finally tackle where you think the show was going in future seasons had it not been cancelled."


# Run the workflow
inputs = {"initial_prompt": test_instruction,  
          "num_steps": 0,
          "llm_name": "llama3.1-70b-groq"}
output = app.invoke(inputs)

# print(output['final_doc'])