import os
import openai
 ##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
# Set your OpenAI API key here
import openai

def generate_text_with_gpt(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
    )

    return response.choices[0].text.strip()


