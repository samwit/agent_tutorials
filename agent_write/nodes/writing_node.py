from langchain.schema import Document
from chains.write_chain import write_chain

def count_words(text):
        """
        Count the number of words in the given text.
        
        Args:
            text (str): The input text to count words from.
        
        Returns:
            int: The number of words in the text.
        """
        # Split the text into words and count them
        words = text.split()
        return len(words)

def writing_node(state):
    """take the initial prompt and write a plan to make a long doc"""
    print("---WRITING THE DOC---")
    initial_instruction = state['initial_prompt']
    plan = state['plan']
    num_steps = int(state['num_steps'])
    num_steps += 1

    plan = plan.strip().replace('\n\n', '\n')
    planning_steps = plan.split('\n')
    text = ""
    responses = []
    if len(planning_steps) > 50:
        print("plan is too long")
        # print(plan)
        return
    for idx,step in enumerate(planning_steps):
        # Invoke the write_chain
        result = write_chain.invoke({
            "intructions": initial_instruction,
            "plan": plan,
            "text": text,
            "STEP": step
        })
        # result = step
        # print(f"----------------------------{idx}----------------------------")
        # print(step)
        # print("----------------------------\n\n")
        responses.append(result)
        text += result + '\n\n'

    final_doc = '\n\n'.join(responses)

    # Count words in the final document
    word_count = count_words(final_doc)
    print(f"Total word count: {word_count}")

    return {"final_doc": final_doc, "word_count": word_count, "num_steps":num_steps}



