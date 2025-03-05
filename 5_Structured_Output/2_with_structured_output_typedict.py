from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4")

# schema
class Review(TypedDict):
    Key_Topics: Annotated[str, "List of key topics discussed in the review"]
    summary: Annotated[Literal["Positive", "Negative", "Neutral"], "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review (positive, negative, neutral)"]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review"]

structured_model = model.with_structured_output(Review)    

# write the review of phone in this format
result = structured_model.invoke("""The phone is good, but the battery 
life is not as long as expected. The screen is too bright, 
and the sound quality is not good. The phone is not user-friendly, 
and the app is not easy to use. The phone is not durable, 
and it will not last long.
Pros: The phone is good, and it is durable. 
Cons: The battery life is not as long as expected, 
and the sound quality is not good. 
The phone is not user-friendly, 
and the app is not easy to use. 
The phone is not durable, 
and it will not last long.""")

print(result)
print(result['sentiment']) 
print(result['summary']) 
print(result['Key_Topics'])
print(result['pros'])
print(result['cons'])