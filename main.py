import os
from groq import Groq

class SentimentAnalyzer:
    def __init__(self) -> None:
        self.client = Groq(api_key='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')

    def analyze_sentiment(self, text):
        # Mocking the sentiment analysis functionality
        print("Analyzing sentiment for:", text)
        sentiment = "Positive" if "good" in text else "Neutral"
        return sentiment


class Brain:
    def __init__(self) -> None:
        self.client = Groq(api_key='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')
        self.sentiment_analyzer = SentimentAnalyzer()
        self.chat_history = [
            {"role": "system", "content": "you are a doctor. ask simple question seperately about each symptoms. for eg:( user: i have fever , doctor:  A fever is a common symptom! Can you tell me more about your fever? How high is it? Is it accompanied by any other symptoms, such as chills, headaches, or body aches? ),predict the disease."}
        ]  # Initializes the conversation with system instructions

    def generate(self, message):
        # Add user message to chat history
        self.chat_history.append({"role": "user", "content": message})

        # Send chat history to model for context-aware completion
        chat_completion = self.client.chat.completions.create(
            messages=self.chat_history,
            model="llama3-8b-8192",
        )

        # Retrieve and print the response
        response = chat_completion.choices[0].message.content
        return response

        # Add assistant's response to chat history
        self.chat_history.append({"role": "assistant", "content": response})
        
        # Perform sentiment analysis (optional)
        #sentiment = self.sentiment_analyzer.analyze_sentiment(response)
       # print("Sentiment Analysis:", sentiment)


# Continuous Chat Loop with Memory
if __name__ == "__main__":
    brain = Brain()
    print("Start chatting with the AI (type 'bye' to end):")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Ending chat. Goodbye!")
            break
        brain.generate(user_input)