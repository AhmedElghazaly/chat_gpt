import openai

openai.api_key = "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"

user_name = "Ahmed: "
bot_name = "Chatbot: "
prev_conversation = ""

while True:
    ask = input(user_name)
    context = prev_conversation + user_name + ask +"\n" + bot_name
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= context,
        temperature=0.9,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text = response['choices'][0]['text']
    print(bot_name + text)
    prev_conversation = context + text + "\n"
