# Import packages
from dotenv import load_dotenv
from random import choice
from flask import Flask, request

import os
import openai

# Load venv, openai key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = opneai.Completion()

start_sequence = "\nSharkbot"
restart_sequence = "\nPerson"
session_prompt = "You are talking to Sharkbot, a helpful virtual assistant that responds to questions about web development.\n\nHi there! I'm Sharkbot, a virtual assistant that responds to questions about web development. Feel free to ask me anything!\n\nperson: I am lookin to build a dapp. What do I need to know?\n\nYou'll need to know how to code in order to build a dapp. I'd recommend learning Solidity, which is the coding language used to create dapps on the Ethereum network.\n\nIs solidity similar to python?\n\nYes, Solidity is very similar to Python.\n\ngreat, can you provide a code example?\n\nSure! Here's a simple Solidity code example:\n\ncontract MyContract { uint myVariable; function MyContract() { myVariable = 5; } }\n\nThis code example will create a new contract called \"MyContract\" with a single variable called \"myVariable\". The variable will be set to the value \"5\" when the contract is created.\n\nthank you, i look forward to your advice\n\nYou're welcome!"

def ask(question, chat_log=None):
    response = openai.Completion.create(
    engine = "text-davinci-001",
    prompt = prompt_test,
    temperature = 0.7,
    max_tokens = 192,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
    stop = ["\n"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'