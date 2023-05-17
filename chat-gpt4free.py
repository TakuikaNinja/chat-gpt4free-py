#!/usr/bin/env python3
import signal
import sys
from gpt4free import you

def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)

chat = []
signal.signal(signal.SIGINT, signal_handler) # setup signal handler to detect ^C
while True:
    prompt = input("You: ")
    response = you.Completion.create(
        prompt=prompt,
        chat=chat)
    # display output, making sure to decode the unicode escape sequences
    print("\nBot: {}\n".format(response.text.encode().decode('unicode-escape')))
    chat.append({"question": prompt, "answer": response.text})
