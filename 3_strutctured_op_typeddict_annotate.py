from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

#schema
class Review(TypedDict):
    summary: Annotated[str, "A summary of the review."]
    sentiment: Annotated[str, "The sentiment of the review (positive, negative, neutral)."]

structured_model =model.with_structured_output(Review)

review_example = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Srinivas"""
result = structured_model.invoke(review_example)

print(result)

# type of result is dict here - so systematically we can access the data through keys

# print(result["summary"])
# print(result["sentiment"])