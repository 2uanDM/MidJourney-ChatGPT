import openai
import os

openai.organization = "org-ZtzXEzkbNhCREYG7OZ3cwF3V"
openai.api_key = "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"

model = "text-davinci-003"
temperature = 0.5
max_tokens = 70

prompts = []
with open('sample.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        prompt = line.rstrip()
        prompts.append(prompt)

with open('output.txt', 'w', encoding="UTF-8") as f:
    for i, prompt in enumerate(prompts):
        print(f'Running query {i+1}th...')
        respose = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        # Call the answer
        answer = respose.choices[0].text.strip()
        f.write(answer + '\n')
