
def parrot(sound = 'Squawk!'):
    print(sound)
    return sound

# Calling the function with the default argument
result = parrot()  
print(result)       

# Calling the function with a custom argument
custom_result = parrot("Hello, world!")  
print(custom_result)                     
