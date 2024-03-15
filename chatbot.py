def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'hello':
            print("Chatbot: Hi there!")
        elif user_input == 'how are you?':
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking!")
        elif user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you please repeat or ask something else?")

if __name__ == "__main__":
    chatbot()
