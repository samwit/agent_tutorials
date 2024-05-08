import json
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

json_schema = {
    "title": "Person",
    "description": "Identifying information about a person.",
    "type": "object",
    "properties": {
        "name": {"title": "Name", "description": "The person's name", "type": "string"},
        "age": {"title": "Age", "description": "The person's age", "type": "integer"},
        "favorite_food": {
            "title": "Fav Food",
            "description": "The person's favorite food",
            "type": "string",
        },
    },
    "required": ["name", "age","fav_food"],
}

llm = ChatOllama(
    model="llama3",
    format="json",
    keep_alive=-1, # keep the model loaded indefinitely
    temperature=0.1,
    max_new_tokens=512
    )

messages = [
    HumanMessage(
        content="Please tell me about a person using the following JSON schema:"
    ),
    HumanMessage(content="{schema}"),
    HumanMessage(
        content="Now, considering the schema, tell me about a person named John who is 35 years old and loves pizza."
    ),
]

prompt = ChatPromptTemplate.from_messages(messages)

#converting the json schema to a string
dumps = json.dumps(json_schema, indent=2)

# chain = prompt | llm | StrOutputParser()
chain = prompt | llm | JsonOutputParser()

response = chain.invoke({"schema": dumps})
print(response)
print(type(response))