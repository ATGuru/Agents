import os
from meta_agent.main import MetaAgent

def ask_clarification(prompt):
    # Simple heuristic for demonstration; in production, use NLP or LLM
    if len(prompt.strip()) < 15:
        return "Your prompt is quite short. Can you provide more details?"
    if 'agent' not in prompt.lower():
        return "Should this prompt create a new agent, or perform another action?"
    return None

def fix_prompt(prompt, clarification_response):
    # For demonstration, just append clarification
    return prompt + "\n# Clarification: " + clarification_response

def main():
    print("Prompt Reviewer Agent started.")
    meta_agent = MetaAgent()
    while True:
        user_prompt = input("Enter your prompt (or 'exit'): ")
        if user_prompt.lower() == 'exit':
            break
        clarification = ask_clarification(user_prompt)
        if clarification:
            print("Clarification needed:", clarification)
            user_response = input("Your answer: ")
            final_prompt = fix_prompt(user_prompt, user_response)
            print("Final prompt:", final_prompt)
        else:
            final_prompt = user_prompt
        print("Sending to generator...")
        meta_agent.handle_prompt(final_prompt)

if __name__ == '__main__':
    main()
