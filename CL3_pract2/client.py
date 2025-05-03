import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Remote procedure call
result = proxy.concatenate(s1, s2)

# Output result
print("Concatenated String:", result)
