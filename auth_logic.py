import time

# 1. Using your exact credentials
corrected_username = "dhara"
corrected_pswrd = "25"

# 2. Getting User Input
provided_username = input("Enter username: ")
provided_pswrd = input("Enter password: ")

# 3. Running your exact logic
if corrected_username == provided_username and corrected_pswrd == provided_pswrd:
    print("Login Successfully!")
    
    # This is the 'time' feature you wrote
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    str_time = "Current Time: " + time.asctime(t)
    print(str_time)
else:
    print("Incorrect Username or Password!")
  
