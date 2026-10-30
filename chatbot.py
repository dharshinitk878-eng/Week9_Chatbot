
import ollama
import csv
from datetime import datetime

messages = [
    {
        "role": "system",
        "content": "You are an educational chatbot. Explain computer science, Python, AI and technology in simple words."
    }
]

print("Welcome to the Educational AI Chatbot!")
print("Type 'exit' to stop the chatbot.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": question
    })

    try:
        response = ollama.chat(
            model="gemma3:1b",
            messages=messages
        )

        answer = response["message"]["content"]

        messages.append({
            "role": "assistant",
            "content": answer
        })

        print("Chatbot:", answer)

        with open("dataset/chat_history.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now(),
                question,
                answer
            ])

        with open("dataset/chatbot_logs.txt", "a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} - Chat completed\n")

    except Exception as error:
        print("Error:", error)
