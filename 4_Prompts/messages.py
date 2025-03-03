from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.5, max_completion_tokens=5)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LLM')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)