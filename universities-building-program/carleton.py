import requests

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif "quote" in message:
        response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["quote"]
            author = data[0]["author"]
            return f'"{quote}" - {author}'
        else:
            return "Sorry, I couldn’t fetch a quote right now."
    else:
        return "I'm sorry, I didn’t understand your message."

if __name__ == "__main__":
    user_input = input("Enter a message for the agent: ")
    print(handle_message(user_input))


