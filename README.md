<p align="center">
    <h2 align="center">Countdown Bot</h2> <br>
    <img src="https://img.shields.io/badge/BOT-%2357abe8?style=for-the-badge&logo=Telegram&logoSize=auto&label=Telegram&labelColor=%23007090&link=https%3A%2F%2Ft.me%2FCountdownTimeKeeperBot
">
</p>


### Gettings Started
Clone this repo.
```bash
git clone https://github.com/parsivan/CountdownBot.git
```
You should use the .env example and paste your API key (from BotFather) in there 
```bash
mv .env.example .env  # rename to .env
nvim .env  # edit and add API key
```
Install [UV](https://docs.astral.sh/uv/getting-started/installation/) and run the command bellow to run.
```bash
uv sync  # only to setup environment
uv run main.py  # will setup up environment and run program
```

### Testing
```bash
uv run pytest  # how to use pytest
uv run ruff check .  # How to use ruff to check for formatting errors
```

### Libraries
 - [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
 - [python-dotenv](https://pypi.org/project/python-dotenv/)
 - [datetime](https://docs.python.org/3/library/datetime.html)

