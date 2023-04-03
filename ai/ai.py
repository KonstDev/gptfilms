import openai
from keys import OPENAI_API_KEY


def getFilm(prompt):
    openai.api_key = OPENAI_API_KEY
    #prompt = 'Soviet film about contrabandists that tries to bring diamonds'
    context = 'You cant say nothing but the name of the following film'


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content
    print (result)
    return result