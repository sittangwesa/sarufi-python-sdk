import json
from sarufi import Sarufi

sarufi = Sarufi("testing@gmail.com", "xxx")


def create_insuarance_bot():
    response = sarufi.create_bot(
        name="My Insurace Bot",
        description="My bot can do a lot",
        intents=json.load(open("intents.json")),
        flow=json.load(open("flow.json")),
    )

    print(response)


def chat():
    while True:
        message = input("Me : ")
        response = sarufi.chat(project_id=3, chat_id="furaha", message=message)
        print(f"Bot: {response}")


def respond(message, chat_id):
    response = sarufi.chat(bot_id=3, chat_id=chat_id, message=message)
    return response.get("message")


if __name__ == "__main__":
    # create_insuarance_bot()
    chat()
