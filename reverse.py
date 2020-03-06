message = 'hello world!'

reversed_message = ''

i = len(message) - 1

while i >= 0:
    reversed_message += message[i]
    i -= 1
print(reversed_message)
