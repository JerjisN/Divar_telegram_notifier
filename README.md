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

The script will check for new ads every 5 seconds and send notifications to your Telegram chat for any new ads found.
