# Midjourney_auto introduction

We know that **Mid Journey**, an AI application in form of **Discord** chatbot, allows us to generate pictures through prompts.

Click here to know more about Mid Journey: https://www.midjourney.com/home/

We know that **Mid Journey**, an AI application in form of Discord chatbot, allows us to generate pictures through prompts.

For example, you want to generate a picture with this idea: "A funny cow is flying in the sky with a broom"

This idea is generally simple, but you want to generate magic, sparkling pictures. This work can be done with the help of ChatGPT.

The main idea of this application is using ChatGPT API to generate thorough prompts from your simple ideas, and then automatically send these prompts to MidJourney chatbot using `pyautogui`

Here is the instruction for using this application:

## Component I: ChatGPT prompts generator

The main source code for this component is `keywords_gen.py`. In this script, I use `openai` packages to call API from ChatGPT. With the help of ChatGPT, my idea will be converted to diverse prompts

Instead of asking directly like this
![](https://github.com/2uanDM/API-chatgpt/blob/main/raw/demo/ask.png)

I will use API to export prompts directly from script
![](https://github.com/2uanDM/API-chatgpt/blob/main/raw/demo/prompts.png)

A lot of nouns, adjectives, configurations is placed in folder `word_components`. You can use `combine.py` to generate a lot of ideas or you can text your own ideas.

After you have ideas in `ideas.txt`, run the script `keywords_gen.py` and the output prompts will be placed in `output_prompts.txt`

_Remeber that you need to declare you organization id and your API key to run this script. For the security problem, I save all the authentication key in `.env` file._

## Component II: Auto sending prompts and download images generated from MidJourney using Discord Bot and `pyautogui`

You need to open two file `BotDownload.bat` and `BotSending.bat` first until your Bots alive in your Discord server, which containing the MidJourney Bot,

Type _automation_ in the box chat and script `sending_bot.py` will simulate our step to generate a picture: `/`, `imagine`, `prompts...`, `enter`

# Requirements

## pip

```
> pip install openai pyautogui discord python-dotenv
```
