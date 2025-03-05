from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional

load_dotenv()

model = ChatOpenAI(model="gpt-4")

# schema
class Review(BaseModel):
    Key_Topics: list[str] = Field(description="List of key topics discussed in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["Pos", "Neg", "Neutral"] = Field(description="The sentiment of the review (positive, negative, neutral)")
    pros: Optional[list[str]] = Field(default=None,description="List of pros mentioned in the review")
    cons: Optional[list[str]] = Field(default=None, description="List of cons mentioned in the review")
    reviewer_name: Optional[EmailStr] = Field(default=None,description="Email of the reviewer")

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
print(result.sentiment) # sentiment: Negative
print(result.summary) # summary: The phone is not durable, and it will not last long.
print(result.Key_Topics) # Key_Topics: ['battery life', 'sound quality', 'user-friendly', 'app']
print(result.pros) # pros: ['The phone is good', 'It is durable']
print(result.cons) # cons: ['The battery life is not as long as expected', 'The sound quality is not good']
print(result.reviewer_name) # reviewer_name: None
