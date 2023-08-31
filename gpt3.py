import openai

def generate_text_with_gpt(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4097,
    )

    return response.choices[0].text.strip()


