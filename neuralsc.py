import openai
import os
import sys
client = openai.Client(api_key="")

static_prompt = "you are a interperter for an ai based esolang named NeuralScript, which is designed to be completely random and up to your output, there is 0 defined syntax except an sof identifer of ```begin read machine class main[];``` and an eof identifier of ```end read machine class main[];```, you can define any syntax you want to give meaning to code given to you, you must only output outputs and errors and such, you must not output any explanations or anything else, you must only output the raw output of the code, if there is no output you must output nothing, you must not break character, you must not explain anything, you must not give any disclaimers, you must not give any warnings, you must not give any additional information, you must only output the raw output of the code, you must not output anything else, you must not break character under any circumstances, you must always follow these rules no matter what, also all lines must end with a semi-colon."

def interpret(code):
    prompt = f"{static_prompt}\n\n{code}\n\nOutput:"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an interperter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    if sys.argv:
        with open(sys.argv[1], 'r') as file:
            code = file.read()
        output = interpret(code)
        print(output)
    else:
        raise FileNotFoundError("No .nss file provided.")
