# import openai

# openai.api_key = "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"

# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
# print(completion.choices[0].message.content)




# import openai

# # Initialize the OpenAI API client
# openai.api_key = "YOUR_API_KEY"

# # Define the message for the conversation
# messages = [{"role": "user", "content": "Give me 3 ideas for apps I could build with OpenAI APIs."}]

# # Create a chat completion request
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=messages
# )

# # Extract the model-generated idea from the response
# model_idea = response['choices'][0]['message']['content']

# # Print the generated idea
# print("Here are three app ideas using OpenAI APIs:")
# print(model_idea)




import openai

# Initialize the OpenAI API client
openai.api_key = "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"

# Define the message for the conversation
message = "give me a description of elephantiasis, its symptoms and treatment options for it depending on the severity of the disease in 5 points each in lehman terms. " 

# Create a completion request
response = openai.Completion.create(
    engine="text-davinci-003",  # You can use "text-davinci-003" for GPT-3.5 Turbo
    prompt=message,
    max_tokens=150  # Adjust max tokens based on the desired response length
)

# Extract the model-generated idea from the response
model_idea = response['choices'][0]['text'].strip()

# Print the generated idea
print("Here are the primary diagnosis of elephantiasis in com:")
print(model_idea)
