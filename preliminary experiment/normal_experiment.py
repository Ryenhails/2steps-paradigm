from gpt3 import generate_text_with_gpt

# Set your OpenAI API key here
api_key = "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"

# Prompt for the model to generate text
prompt = "Can you give me a example of how to cook Delicious Chinese Dinner？ "

# Call the function to generate text
generated_output= generate_text_with_gpt(prompt, api_key)


print(generated_output)

