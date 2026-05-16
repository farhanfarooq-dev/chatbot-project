print("Hello! I am your Movie Chatbot.")

while True:
    print("\nWhat type of movie do you want? (funny / action / love / scary)")
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    if "funny" in user_input or "comedy" in user_input:
        print("Bot: You may like 'The Mask' or 'Superbad'")
    elif "action" in user_input or "fight" in user_input:
        print("Bot: You may like 'John Wick' or 'Mad Max'")
    elif "love" in user_input or "romantic" in user_input:
        print("Bot: You may like 'The Notebook' or 'La La Land'")
    elif "scary" in user_input or "horror" in user_input:
        print("Bot: You may like 'The Conjuring' or 'Insidious'")
    else:
        print("Bot: I don't understand. Please choose funny, action, love, or scary.")