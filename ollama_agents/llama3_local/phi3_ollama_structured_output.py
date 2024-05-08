from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.llms.ollama_functions import OllamaFunctions

# Schema for structured response
class Person(BaseModel):
    name: str = Field(description="The person's name", required=True)
    height: float = Field(description="The person's height", required=True)
    hair_color: str = Field(description="The person's hair color")

context = """Alex is 5 feet tall. 
Claudia is 1 feet taller than Alex and jumps higher than him. 
Claudia is a brunette and Alex is blonde."""

# Prompt template phi 3
prompt = PromptTemplate.from_template(
    """<|user|>{context}

QUESTION: {question}<|end|>
<|assistant|>AI: """
)

# Chain
llm = OllamaFunctions(model="phi3", 
                      format="json", 
                      temperature=0)

structured_llm = llm.with_structured_output(Person)
chain = prompt | structured_llm

response = chain.invoke({
    "question": "Who is taller?",
    "context": context
    })

print(response)