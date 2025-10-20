from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

review_example = """The hardware is great, but the software is a little clunky. There are too many apps thate were pre-installed that I cannot remove. Also, UI looks outdated when compared with other brands. Hoping for software updates to fix these issues."""

result = structured_model.invoke(review_example)

print(result)

# type of result is dict here - so systematically we can access the data through keys

# print(result["summary"])
# print(result["sentiment"])