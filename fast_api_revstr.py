#----------------------------------------------------------------------------------------------------------------------
#                                          REVERSING THE STRING - fastapi implementation
#______________________________________________________________________________________________________________________

# Reversing the string does not modify the server state, Because the server does not explicitly stores or updates the string or its reversal in some database or file.
# Reversing the string is a pute function --> It does not have any sude effects on  server or the environment
# It only takes an input and returns the outputs, not changing anything else

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Define app routes

# Home page
# Route that listens for GET requests at the root (“/”) of your application. When a request is received, it returns an HTML response.
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#  route that listens for GET requests at the “/get” endpoint of your application.
@app.get("/get")
# Function for the "bot response" --> reverses the string
async def get_bot_response(msg: str): # It takes a string parameter "msg" from the request
    return {"response": str(reverse_str(msg))} # returns the reversed string in a JSON response.

# Function iteratively reverse string
def reverse_str(string):
    str_len = len(string)
    rev = ""
    i = str_len - 1
    while i >= 0:
        rev += string[i]
        i -= 1
    return rev

# Function recursively reverse string
def recursive_reverse(string, itered = 0):
    str_len = len(string)   # Length of string
    if str_len == 0 | str_len == 1: 
        return string
    if itered == str_len//2:
        return string
    # In Python strings are immutable, you cannot change their individual characters directly using indexing and assignment.
    # Convert the string to a list
    str_list = list(string)
    temp = string[itered]
    str_list[itered] = str_list[str_len-itered-1]
    
    str_list[str_len-itered-1] = temp

    # Convert the list back to a string
    reversed_string = ''.join(str_list)

    return recursive_reverse(reversed_string, itered+1)

#------------------------------------------
#              Async Function             |
#------------------------------------------
# In the context of FastAPI, 
#               - async allows your API to handle multiple requests at the same time without waiting for other requests to complete. 
#               - This can greatly improve the performance of your application.
# async keyword in Python is used to define a function as a "coroutine". 
#               - Coroutines are a special type of function that can be paused and resumed, allowing them to be non-blocking. 
#               - This is particularly useful in I/O operations, which spend a lot of time waiting for data to be sent or received.
