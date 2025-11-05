# CountDown Bot
<https://t.me/CountdownTimeKeeperBot>

## Libraries
 - [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
 - [python-dotenv](https://pypi.org/project/python-dotenv/)
 - [datetime](https://docs.python.org/3/library/datetime.html)

## Running
Clone this repo.
```bash
git clone https://github.com/parsivan/TelegramCountdownBot.git
```
You should use the .env example and paste your API key (from BotFather) in there 
```bash
mv .env.example .env
nvim .env
```
create a python venv and install required libraries.
```bash
python -m venv <name-directory>
pip install -r requirements.txt
```