import nltk
nltk.data.path.append("C:/Users/Mahima/AppData/Roaming/nltk_data")
from nltk.tokenize import word_tokenize


# Knowledge base dictionary
chat_dict = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Need any assistance?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is your name": "I'm your friendly chatbot, created using Python!",
    "bye": "Goodbye! Have a great day!"
}

# Response logic
def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in chat_dict:
        return chat_dict[user_input]
    else:
        return "I'm not sure how to respond to that!"



# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Bye! Take care.")
        break
    response = get_response(user_input)
    print("Chatbot:", response)

