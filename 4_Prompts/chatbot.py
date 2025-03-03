##OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.5, max_completion_tokens=10)

chat_history = [
     SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)


print(chat_history)




























##HuggingFace API
# from langchain_huggingface import  ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv('HF_TOKEN')

# llm = HuggingFaceEndpoint(
#     repo_id = "microsoft/Phi-4-mini-instruct",
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm = llm)

# chat_history = []


# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("AI: ", result.content)


# print(chat_history)
