from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)


# Giving Comand as last tetx
command = '''
[12/8/2024 3:30 PM] +91 79924 68300: Hi
[12/8/2024 3:30 PM] +91 79924 68300: Where are you
[12/8/2024 3:32 PM] +91 79924 68300: Ok
[12/8/2024 3:32 PM] +91 79924 68300: Miss you too
[12/8/2024 3:33 PM] : hey
[12/8/2024 3:33 PM] : jese ho anar
[12/8/2024 3:33 PM] +91 79924 68300: Theek hai
[12/8/2024 3:33 PM] : ghar pe sab lese hai
[12/8/2024 3:33 PM] +91 79924 68300: Sab badhiya
[12/8/2024 3:33 PM] : aur sab bhta
[12/8/2024 3:33 PM] +91 79924 68300: Aur sab theek hai
[12/8/2024 3:33 PM] : mze me na zindagi
[12/8/2024 3:34 PM] : thoda idhar bhi dhyan de de
[12/8/2024 3:34 PM] +91 79924 68300: Ha ha q nhi
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person Ptã Ñhí Kon Hãi Yé who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Ptã Ñhí Kon Hãi Yé"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)