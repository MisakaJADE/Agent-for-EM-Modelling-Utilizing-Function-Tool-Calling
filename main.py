import openai
from openai import OpenAI
import os
import json
import Modelfunc
from datetime import datetime
import gpt_tool
import gpt_tool_array

openai_api_key = os.getenv("OPENAI_API_KEYS")

client = OpenAI(api_key=openai_api_key)
tools = gpt_tool.tools
array_tools = gpt_tool_array.tools

# initialize the vba
vba_code_heading = 'Option Explicit \n Sub Main () \n'
vba_code_ending = '\nEnd Sub'
vba_code_1 = ''

# initial log file
log_file = 'chatgpt_api_log_RISarray.json' # change the file name according to the model
with open(log_file,"w",encoding="utf-8"):
    pass
# write in the log file
def log_interaction(request, response):
    with open(log_file,"a",encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "request": request,
            "response": response.to_dict()
        }, ensure_ascii=False) + "\n")

continue_input = True
array_mode = False  # flag of the array modelling mode

while continue_input:
    # Entering the requests
    text_request2gpt = input("Enter your request here:\n")
    input_messages = [{"role": "user", "content": text_request2gpt}]
    response = client.responses.create(
        model="gpt-4o-mini-2024-07-18",
        input=input_messages,
        tools=tools,
        parallel_tool_calls=False,
    )

    # save log file
    log_interaction(input_messages, response)

    # Output and conduct the functions
    for tool_call in response.output:
        if tool_call.type != "function_call":
            continue

        name = tool_call.name
        # full_name = 'Modelfunc.' + name
        args = json.loads(tool_call.arguments)

        func_called = getattr(Modelfunc,name)
        vba_code_1 = func_called(vba_code_1, **args)
        print(vba_code_1)

    while True:
        continue_input = input("Continue modelling? [y/n] ")
        if continue_input == 'y':
            continue_input = True
            break
        if continue_input == 'n':
            continue_input = False
            break
        else:
            print('Invalid input, please input y or n ')
            continue_input = True



vba_code_final = vba_code_heading + vba_code_1 + vba_code_ending
print(vba_code_final)
