# gpt2SlackBot
GPT2 trained Slack Bot

Learns from channels over time, using OpenAI GPT2 machine learning. Can create a bot that listens to one or more channels and interacts with others.

# Commands

_addBot_

Creates a new bot using the name and channels passed

`/gpt2Bot addBot <botName> "[,channels]" [,options]`

**props**

| Property        | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| botName         | string         | TRUE     | name for the bot |
| channels        | array          | TRUE     | the channel ids for the bot to listen to for training|
| options         | string         | FALSE    | see option flags table|

Example

`/gpt2Bot addBot NegativeNancy "@general @worktime @football_club" -updateSchedule 24h`

_configBot_

Set and updates values for the bot

`/gpt2Bot configBot <botName> [,options]`

| Property        | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| botName         | string         | TRUE     | name for the bot |
| options         | string         | TRUE    | see option flags table|

Example

`/gpt2Bot configBot NegativeNancy -updateSchedule 12m`

_listBots_

List all current bots

`/gpt2Bot listBots`

_deleteBot_

Deletes a bot

`/gpt2Bot deleteBot <botName>`

| Property        | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| botName         | string         | TRUE     | name for the bot |

Example

`/gpt2Bot deleteBot NegativeNancy`

_teachBot_

Scrapes all text from the channels a bot uses and uploads them, Updates the last updated time for a bot

`/gpt2Bot teachBot <botName> [,options]`

| Property        | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| botName         | string         | TRUE     | name for the bot |
| options         | string         | FALSE    | see option flags table|

Example 

`/gpt2Bot teachBot NegativeNancy -startDate 5/12/2020`

_messageBot_

Interacts with bot to have them respond

`/gpt2Bot messageBot <botName> "<message>"`

| Property        | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| botName         | string         | TRUE     | name for the bot |
| message         | string         | TRUE     | message to send to bot|

Example

`/gpt2Bot messageBot NegativeNancy "Hello"`

_help_

Lists all available commands

`/gpt2Bot help`

