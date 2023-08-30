from gpt3 import generate_text_with_gpt

# Set your OpenAI API key here
api_key = "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"

# Prompt for the model to generate text
prompt = "I want you to act as a ChatGPT prompt generator, I will send a topic, " \
         "you have to generate a ChatGPT prompt based on the content of the topic, " \
         "the prompt should start with \"I want you to act as \", and guess what I might do, " \
         "and expand the prompt accordingly Describe the content to make it useful. " \
         "The following is my topic: Can you give me a example of how to cook Delicious Chinese Dinner？ "

# Call the function to generate text
generated_prompt = generate_text_with_gpt(prompt, api_key)

# Print the generated text
print(generated_prompt)

generated_output = generate_text_with_gpt(generated_prompt, api_key)

print(generated_output)

