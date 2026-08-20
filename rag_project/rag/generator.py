import os
from openai import OpenAI
client=OpenAI(api_key = os.getenv("OPENAI_API_KEY")) #setup of real open ai api key
def generate_answer(question,context): #with thes aregumes we goona pass the hole chunks and our quesiton 
    prompt= f""" ANSWER THe giveing provinded answer to the question with only porvided context of chunks
    context:{context} 
    question:{question}"""
    response=client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
        
    )
    
    return response.output_text

