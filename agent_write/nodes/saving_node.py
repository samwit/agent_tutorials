import os
from typing import Any, Dict

from langchain.schema import Document
from tools import write_markdown_file


def saving_node(state):
    """take the finished long doc and save it to local disk as a .md file   """
    print("---SAVING THE DOC---")
    initial_prompt = state['initial_prompt']
    plan = state['plan']
    final_doc = state['final_doc']
    word_count = state['word_count']
    llm_name = state['llm_name']
    num_steps = int(state['num_steps'])
    num_steps += 1

    final_doc = final_doc + f"\n\nTotal word count: {word_count}"

    # save to local disk
    write_markdown_file(final_doc, f"final_doc_{llm_name}")
    write_markdown_file(plan, f"plan_{llm_name}")

    return { "num_steps":num_steps}