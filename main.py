def linkedin_post(topic):
    prompt = f"Write a professional Business-Proposal-Writer for:\n{topic}"
    return run_llama(prompt)

if __name__ == "__main__":
    topic = input("Business topic: ")
