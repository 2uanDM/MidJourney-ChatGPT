import openai
import os

openai.organization = "org-ZtzXEzkbNhCREYG7OZ3cwF3V"
openai.api_key = "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"

prompt = "Generate for me fifty random questions"
model = "text-davinci-002"
temperature = 1.0
max_tokens = 1000

response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
)

answer = response.choices[0].text.strip()

print(answer)
