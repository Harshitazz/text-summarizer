from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  
)

def summarize_text(text):
    prompt = (f"Please summarize the following text into clear and concise bullet points:\n\n"
              f"{text}\n\n"
              f"Summary (in bullet points):")    
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ],
        model='qwen2:0.5b',
    )
    
    choices = response.choices
    c = choices[0].message
    summary = c.content.strip()
    
    return summary
