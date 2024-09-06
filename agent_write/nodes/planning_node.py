from langchain.schema import Document
# from search_tools import web_search_tool, write_markdown_file
from chains.plan_chain import plan_chain


def planning_node(state):
    """take the initial prompt and write a plan to make a long doc"""
    print("---PLANNING THE WRITING---")
    initial_prompt = state['initial_prompt']
    num_steps = int(state['num_steps'])
    num_steps += 1

    plan = plan_chain.invoke({"intructions": initial_prompt})
    # print(plan)

    return {"plan": plan, "num_steps":num_steps}
