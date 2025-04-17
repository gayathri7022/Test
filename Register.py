import time
def register(email,mob):
    
    
    char = '@'
    if char in email and email.endswith((".com",".in",".org")):
        if len(mob) == 10:
            print("Verification code has sent to your mobile number.")
        else:
            print("Mobile number is incorrect")
    else:
        print("Invalid email.")


register("gayathri@gmail.com","1234569054")
register("gayathri@gmail.com","12345694")
register("gayathrigmail.com","1234569054")