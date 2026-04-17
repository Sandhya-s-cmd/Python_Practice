#Extracting certain portions or elements from the lists and strings.
#list [start:end:step]
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:-1:2])

sample_url="http://google.com"
# Reverse the Url
print(sample_url[::-1])

#Extract the top level domain 
print(sample_url[-4:])

#Print the url without the http://
print(sample_url[7:])

message = "Hello World"
print(message.lower())
print(message.upper())
print(message.count("Hello"))
print(message.count("l"))
print(message.find("World"))