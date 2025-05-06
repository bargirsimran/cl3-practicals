import Pyro5.api

# Use the URI printed by the server, or resolve it via name server
uri = input("Enter the URI from server (e.g. PYRO:obj_abc@localhost:port): ")
proxy = Pyro5.api.Proxy(uri)

# Get user input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Call remote method
result = proxy.concatenate(s1, s2)
print("Concatenated String:", result)
