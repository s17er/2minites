import sys
import gkeepapi

def getnotes(email, password):
    keep = gkeepapi.Keep()
    success = keep.login(email, password) 
    if not success:
        print("Login error.")
        return
    print("OK")


if __name__ == '__main__':
    args = sys.argv
    email = args[1]
    password = args[2]
    print("Mail:" + email)
    
    getnotes(email, password)