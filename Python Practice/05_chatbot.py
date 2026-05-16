while True:
    user_input = input("you: ").lower ()

    if user_input == "bye" :
        print("Bot: Goodbye!")
        break

    elif "hello" in user_input:
        print("Bot: Hi there!")

    elif "name" in user_input:
        print("Bot: I am your simple chatbot")

    elif "age" in user_input:
        print("Bot: I dont have age 😊 ")

    else:
        print("Bot: I dont understand 😒")
