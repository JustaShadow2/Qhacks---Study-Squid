
id = "Q6XVVP-E4R2JPV6TH"
import requests
def getSteps(math):
    #api = "http://api.wolframalpha.com/v1/conversation.jsp?appid=" + id + "&i=" + math + "&background=" + str(background) + "&foreground=" + str(foreground) + "&format=image"
    api = "http://api.wolframalpha.com/v2/query?appid=" + id +"&input=" + math + "&podstate=Step-by-step%20solution&format=image&output=json"
    image = requests.get(api)
    return image.text #uses .text to acsess response content stored in image. assigns this to value.

def getAnswer(math):
    api = "http://api.wolframalpha.com/v1/result?appid=" + id + "&i=" + math
    answer = requests.get(api)
    return answer.text

# def getAnswer(math):
#     api = "http://api.wolframalpha.com/v1/result?appid=" + id + "&i=" + math
#     answer = requests.get(api)
#     value = answer.text
#     return value
#returns new string with proper formatting
#old testing code
#math = "3z+1%3D909888"
#math = editMath(math)
#print(getImage(0x36454F,0x000000,math))
#print("blank\n")
#print(getAnswer(math))
#note: math expression may be different from what u give wolfram. wolfram expecgts more 'english', and to be told "solve" whatever, rather than just a straight math equation. check wolframs site to see how it suggests you fill things like "linearly approximate [] and mimic that grammar per question"

