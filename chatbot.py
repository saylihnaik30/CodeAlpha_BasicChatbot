
# CodeAlpha - Basic Chatbot

def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I'm CodeAlpha Chatbot!"

    elif message == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that message."


print("Welcome to CodeAlpha Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower().strip() == "bye":
        break
