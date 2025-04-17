from Register import register

def Test_cases():
    assert register("gayathri@gmail.com","1234569054") == "Verification code has sent to your mobile number."
    assert register("gayathri@gmail.com","12345694") == "Mobile number is incorrect"
    assert register("gayathrigmail.com","1234569054") == "Invalid email."