import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from LLMs.llm import LLM

# Load the write prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'write.txt'), 'r') as file:
    write_template = file.read()

# Create a ChatPromptTemplate
write_prompt = ChatPromptTemplate([
    ('user', write_template)
    ])

# Create the write chain
write_chain = write_prompt | LLM | StrOutputParser()

if __name__ == "__main__":
    # Test the write_chain
    test_instruction = "Write a 1500-word essay about the impact of artificial intelligence on modern society, covering its benefits, potential risks, and ethical considerations."
    test_plan = "Paragraph 1 - Main Point: Introduction to AI and its growing influence - Word Count: 200 words"
    test_text = "Artificial Intelligence (AI) has become an integral part of our modern society, revolutionizing various aspects of our daily lives and industries."
    
    # Invoke the write_chain
    result = write_chain.invoke({
        "intructions": test_instruction,
        "plan": test_plan,
        "text": test_text,
        "STEP": "Paragraph 1"
    })
    
    # Print the result
    print("Generated Paragraph:")
    print(result)
