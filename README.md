# divar_telegram_notifier
This Python script checks for new car advertisements on Divar using its API and sends notifications to a Telegram bot. It is designed to run periodically, keeping you updated on the latest ads.

## Configuration

1. Get your Telegram bot token by talking to [@BotFather](https://t.me/BotFather).
2. Replace `'your_telegram_bot_token'` with your actual bot token in the script.
3. Determine the chat ID where you want to receive notifications and replace `'your_telegram_chat_id'` with the actual chat ID in the script.


## Usage

1. Make sure you have Python installed on your system.
2. Install the required libraries using the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script using the following command:

    ```bash
    python divar_telegram_notifier.py
    ```
4. Before running the script, open your web browser and do the following:
   - Go to (https://divar.ir/).
   - Perform a search for Intended advertisements in your city.
   - Copy the URL from the browser's address bar.

5. Replace the `[Your City]` part of the URL in the script with the actual name of your city.

6. After completing the above steps, you can run the script, and it will notify you of new car advertisements in your city.
   
The script will check for new ads every 5 seconds and send notifications to your Telegram chat for any new ads found.


