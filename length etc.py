text = "Hello, #Python"
print(len(text)) 

text = "hello"
print(text.upper())

text = "#Python Program"
print(text.lower())

text = "hello #Python Program"
print(text.title())

text ="hello #Python Program"
print(text.capitalize())

text = " "
print(text.strip())

text = "Hello"
print(text.lstrip())

text = " "
print(text.rstrip())

text = "Hello, world!"
print(text.replace("world", "#Python Program"))
                   
text = "apple,banana,orange"
print(text.split(","))

words = ["Hello", " #Python Program"]
print("".join(words))

text = "programming"
print(text.find("program"))

text = "banana banana"
print(text.count("banana"))

text ="Hello, #Python Program!"
print(text.startswith("Hello"))

text ="is fun!"
print(text.endswith("fun!"))
                    
text ="Hello"
print(text.isalpha())

num = "12345"
print(num.isdigit())

text = "Hello123"
print(text.isalnum())

text = "Hello #Python Program"
print(text.swapcase())

text = "42"
print(text.zfill(5))