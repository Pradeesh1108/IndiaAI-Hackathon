import ollama

model = "llama3.2:latest"

print("Welcome to Llama Translator!")
while True:
    hinglish_text = input("Enter Hinglish text to translate to English: ")

    # Send the translation prompt to Llama 3.2
    response = ollama.chat(model=model, messages=[
        {
            'role': 'user',
            'content': f"Translate the following Hinglish text to English without giving any additional informations: '{hinglish_text}'"
        }
    ])

    # Extract and print the translation
    ol_response = response['message']['content']
    print("Translation:", ol_response)
