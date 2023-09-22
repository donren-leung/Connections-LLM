import lmql
from dataclasses import dataclass
from typing import TypeVar, List
import sys, json


class OpenAiConfig():
    model_path='openai/text-ada-001'
    temperature=0.75
    top_p=0.85
    frequency_penalty=0.03
    "Connections-LLM/Scrape/prompts/filtered_prompt_sys_nowhile.txt"

    def __init__(self):
        pass

@lmql.query
def process_json(system_prompt: str, user_query: str):
    '''lmql
        sample(temperature=0.75, max_len=6000, chunksize=256, chatty_openai=True)
            "{:system} {system_prompt}"
            "{:user} Here is the input puzzles I want you to analyse in detail. Remember each wall has 4 categories and 4 words within them.\n"
            "```json\n{user_query}\n```"
            "{:assistant} [ANSWER]"
        from
            'openai/gpt-3.5-turbo-16k'
        # where
        #     len(ANSWER) < 700
    '''

def main():
    sys_prompt = open(sys.argv[1], 'r').read()
    # print(sys_prompt)

    episodes = json.load(open(sys.argv[2], 'r'))
    for i, (episode, walls) in enumerate(episodes.items()):
        print(x:=json.dumps({episode: walls}, separators=(',', ':')))
        print(process_json(sys_prompt, x)[0].variables.get('ANSWER', None))
        if i > 0:
            break

if __name__ == "__main__":
    main()
    from lmql.runtime.bopenai import get_stats
    print(get_stats())
