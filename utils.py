#utils.py

def store_channel(channel_id):
    with open("channels.txt", "a") as file:
        file.write(channel_id + "\n")

def retrieve_channels():
    try:
        with open("channels.txt", "r") as file:
            channels = file.readlines()
            return [channel.strip() for channel in channels]
    except FileNotFoundError:
        return []

def fetch_channel_details(channel_id):
    # yahan aap Telegram API ka use karke channel ki details fetch kar sakte hain
    pass

def handle_error(error):
    # yahan aap error handling ka logic define kar sakte hain
    pass
