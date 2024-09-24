import openai
import osc

#in the string put the openai key id
openai.apiKey = "API KEY ID"

client = osc.client("127.0.0.1", 53000) #readjust IP address and port num in Qlab

#this will process and generate text for QLab
def holdTextGenerator(address, args):
    textGenerator = args[0] #zero to avoid randomness in openai api 
    print("Here's your text message: ", textGenerator)
    
    if "start cue" in textGenerator:
        handleCue = textGenerator.add{"starting cue"}[0].split()
    
def textGenerator(prompt):
    response = openai.Completion.create (
        engine = "gpt-3.5-turbo-instruct", #this has a pricing of InputL $1.50 / 1M tokens Output: $2.00 / 1M tokens. Cna be changed
        prompt = prompt,
        token = 1000,
        count = 1,
        stop = None,
        temperature = 0, #zero to avoid randomness for 
    )
    textGenerator = response.choices[0].text
    client.sendMessage("/text_generated", textGenerator)

# OSC handler
client.addMessage("/generate_text", textGenerator)
client.addMessage("/text_generated", holdTextGenerator)

# Start OSC client
client.serve_forever()