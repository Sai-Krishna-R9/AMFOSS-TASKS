######## TASK-07

I Have focused only on core part of this task because of time constraints.

commands implemented:
- `!bounty` - check your current Berry balance
- `!setsail` - claim daily Berries (100), with a 24-hour cooldown
- `!trade @user <amount>` - transfer Berries to another user
- `!worstgeneration` - show the top 5 richest users


###APPROACH USED
Used discord.py for the bot framework and SQLite
Each useris user is stored with their discord id as the primary key.
everyone is given a starting balance of 100 berry.

#####concepts learned
discord.py bot setup,commands and intents
sqlite basics
