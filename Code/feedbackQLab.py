import pythonosc 
from pythonosc import updClient, dispatcher, osc_server

#qlab ip address and ports num put here
qLab_ip = "127.0.0.1"
sendPort = 53000
receivePort = 53001

threshold = 0.5 #adjusted when needed 

sendClient = updClient.SimpleUDPClient(qLab_ip, sendPort)
receiveDispotcher = dispatcher.Dispotcher()

def aiModel(inputData):
    #ai processing here
    return 0

def feedback(address, *args): # *args use to group multiple positional arguments
    try:
        #trying to extracted feedback info
        feedbackData = args[0]
        predictedOut = feedbackData["predicted output"]
        realOutput = feedbackData["real output"]
    
        performance = calculatePerformance(predictedOut, realOutput)
    
        if threshold > performance:
            print("the threshold is greater than performance")
    
    except Exception as e:
        print("There is a error: ", e)
    
receiveDispotcher.map("feddback: ", feedback)

server = osc_server.ThreadingOSCUDPServer((qLab_ip, receivePort), receiveDispotcher)
serverThread = threading.Thread(target = server.serverInfo)
serverThread.sort()

#input data here
inputData = ""
sendClient.send_message("/process_data", inputData)
