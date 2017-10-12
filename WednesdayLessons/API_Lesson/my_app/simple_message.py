import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "Wanna-be Developer Andrea <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": ["andi.goldsworthy@gmail.com", "ayjaynaylor@gmail.com"],
              "subject": "Motivation Day - Thursday",
              "text": "Keep trying and keep studying.. it will pay off. Look at what you are doing now!"})

send_simple_message()
