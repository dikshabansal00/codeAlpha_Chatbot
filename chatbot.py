def chatbot():
    print("chatbot: hello! type 'bye' to end")
while True:
    user_input=input("you:").lower()
    if "hello" in user_input:
        print("chatbot: hi!")
    elif "how are you" in user_input:
        print("chatbot: i'm fine, thanks!")
    elif "bye" in user_input:
        print("chatbot: goodbye!")
        break
    else:
        print("chatbot: i didn't understand that.")
chatbot()  
