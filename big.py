import openai

openai.api_key = "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"
model_engine = "text-davinci-002"
prompt = "Hello, whats up?"
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.5,
)

# Access the raw content of the response as a file-like object
response_data = response.raw

# Read the content of the file-like object
response_string = response_data.read()

print(response_string)

