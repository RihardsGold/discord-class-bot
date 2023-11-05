import openai
import re

# Global variable to store the conversation context by user
conversation_context = {}

def generate_gpt_response(user_id, user_name, prompt):
    global conversation_context  # Access the global variable

    try:
        if user_id not in conversation_context:
            conversation_context[user_id] = {"name": user_name, "text": ""}

        conversation_context[user_id]["text"] += f"{conversation_context[user_id]['name']}: {prompt}\n"  # Store user and conversation
        full_prompt = conversation_context[user_id]["text"]
        sanitized_prompt = sanitize_input(full_prompt)
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{sanitized_prompt} "}]
        )

        reply = ""

        if 'choices' in response and len(response['choices']) > 0:
            reply = response['choices'][0]['message']['content']
            conversation_context[user_id]["text"] += f"ChatGPT: {reply}\n"  # Store AI response
            return reply

    except Exception as e:
        print("Error:", e)

    return "Something went wrong."

def set_openai_api_key(api_key):
    openai.api_key = api_key

def sanitize_input(prompt):
    sanitized_prompt = re.sub(r"<@!\d+>", "", prompt)
    sanitized_prompt = re.sub(r"```.*\n", "", sanitized_prompt)
    sanitized_prompt = re.sub(r"```", "", sanitized_prompt)
    
    return sanitized_prompt