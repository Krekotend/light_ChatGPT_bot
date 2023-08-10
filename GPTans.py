import openai

openai.api_key = " " # your key for openAi


def shows_answer(qst: str, character: str = None, addition: str = None):
    resps = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": character},
                                                                          {"role": "assistant", "content": addition},
                                                                          {"role": "user", "content": qst}])

    return resps['choices'][0]['message']['content']


def easy_shows_answer(qst: str):
    resps = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": qst}])

    return resps['choices'][0]['message']['content']

