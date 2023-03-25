import os
import openai
from datetime import datetime
import github
from github import Github
import sys

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%A %d %B %Y %H:%M")


openai.api_key = "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"
g = Github("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")


file_name = "chatgpt_log.txt"
# # Set the model and prompt
model_engine = "text-davinci-003"
prompt = input("Enter your question: ")

# # Set the maximum number of tokens to generate in the response
max_tokens = 1024

# # Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# # Print the response
response = completion.choices[0].text

print("Response: ", response)
print("GitHub Gist: https://gist.github.com/da2c2f354931c9cc303871e8771549a8")
desc = "New Entry: " + dt_string

with open(file_name, 'a') as f:
    f.write(dt_string)
    f.write('\nQ: {}\n'.format(prompt))
    f.write('A: {}\n\n'.format(response))

# Upload the file to the Gist
with open(file_name, 'r') as r:
    content = r.read()
    gist = g.get_gist("da2c2f354931c9cc303871e8771549a8")

    gist.edit(
        description=desc,
        files={file_name: github.InputFileContent(content)},
    )
