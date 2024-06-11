# This Python script is demonstrating the usage of a library or API for interacting with a service
# related to prompts and questions. Here's a breakdown of what the script is doing:
import sys

sys.path.append("../")

from mtai.mt import MT

secret_key = "your_secret_key_here"

mt = MT(secret_key=secret_key)
print(mt.prompts.list())
print(mt.prompts.ask_question(prompt="What is the capital of India?"))
print(mt.prompts.get_prompt_by_id("66530b1fb28d0dec9cfdc2bd"))
print(mt.prompts.delete_prompt_by_id("66530b1fb28d0dec9cfdc2bd"))

# Static Use
from mtai.prompts import Prompt

print(Prompt.list())
print(Prompt.ask_question(prompt="What is the capital of India?"))
print(Prompt.get_prompt_by_id("66530b1fb28d0dec9cfdc2bd"))
print(Prompt.delete_prompt_by_id("66530b1fb28d0dec9cfdc2bd"))
