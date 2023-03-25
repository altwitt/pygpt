import os
import openai
from datetime import datetime
from github import Github
import sys

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%A %d %B %Y %H:%M")


openai.api_key = "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"
g = Github("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")\

# Create a new Gist
gist = g.get_user().create_gist(public=True, files={})

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

print("Gibberts Response is being saved to the my_chats.txt file, and it's right here---> ", response)


with open(file_name, 'a') as f:
    f.write(dt_string)
    f.write('\n\nMY QUESTION: {}\n\n'.format(prompt))
    f.write('GIBBERTS RESPONSE: {}\n\n\n'.format(response))

# Upload the file to the Gist
with open(file_name, 'r') as r:
    content = f.read()
    gist.edit(files={file_name: github.InputFileContent(content)})
