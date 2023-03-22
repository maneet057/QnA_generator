import os
import openai

openai.api_key = "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"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text

def generateQnA(text):
    qna_prompt = 'Refer to this text: '+text+'\n Now generate atleast 3 long answers questions from this text in the form of a python dictionary where the question is the key and the answer is the value. Do not store it in a variable. Use double quotes for the keys and values. The Answers should be detailed and long.'
    qna = openai_create(qna_prompt)
    # print(qna)
    return qna