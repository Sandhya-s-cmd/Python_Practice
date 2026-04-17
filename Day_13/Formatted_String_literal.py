greeting="Hello"
name="Sandhya"

message=f'{greeting}, {name.upper} Welcome!'
print(message)

#Using the format method
message2='{}, {} Welcome!'.format(greeting, name.upper())       
print(message2)

#Cancatenating the string
greeting="Hello"
name="Sandhya"  
message3=greeting+','+name + "Welcome!"
print(message3)
