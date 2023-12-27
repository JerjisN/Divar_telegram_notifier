import requests
import json
import os
from telegram import Bot
import time
import asyncio

# Telegram bot token and chat ID
TOKEN = 'your_telegram_bot_token'
CHAT_ID = 'your_telegram_chat_id'
bot = Bot(token=TOKEN)

# API endpoint for Divar to fetch car advertisements 
url = "https://api.divar.ir/v8/web-search/[Your City]/Link after city..."

def get_new_ads(url):
    # Make a GET request to the Divar API to fetch car advertisements
    response = requests.get(url)
    data = response.json()
    
    # Extract the list of advertisements from the response data
    ads = data['web_widgets']['post_list']
    return ads

# Define old_ads as a global variable to keep track of previous advertisements
global old_ads
old_ads = get_new_ads(url)

# Define a set to store the IDs of ads that have been sent to avoid duplicates
sent_ads = set()

async def check_new_ads():
    # Declare old_ads and sent_ads as global inside the function
    global old_ads, sent_ads
    
    while True:
        # Fetch the latest advertisements from Divar
        new_ads = get_new_ads(url)
        
        # Iterate through the new advertisements
        for ad in new_ads:
            ad_id = ad['data'].get('token', '')
            
            # Check if the ad is new and hasn't been sent before
            if ad not in old_ads and ad_id not in sent_ads:
                title = ad['data'].get('title', '')
                ad_link = 'https://divar.ir/v/' + ad_id
                
                # Compose the message to be sent to Telegram
                message = f"Ad Title: {title}\n" \
                          f"Ad Link: {ad_link}"
                
                # Save the message to a file for backup or reference
                with open('new_ads.txt', 'w', encoding='utf-8') as f:
                    f.write(message)
                
                # Send the contents of the file to Telegram
                with open('new_ads.txt', 'r', encoding='utf-8') as f:
                    await bot.send_message(chat_id=CHAT_ID, text=f.read())
                    
                # Add the ID of the ad to the set of sent ads
                sent_ads.add(ad_id)
                
                # Delete the contents of the file after sending the message
                open('new_ads.txt', 'w').close()
                
        # Update old_ads to the latest advertisements for the next iteration
        old_ads = new_ads
        
        # Wait for 5 seconds before checking for new ads again
        await asyncio.sleep(5)

# Run the asynchronous function to check for new ads
asyncio.run(check_new_ads())
