from xmlrpc.server import SimpleXMLRPCServer

# Define the function to expose
def concatenate_strings(s1, s2):
    return s1 + s2

# Set up server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on http://localhost:8000")

# Register the function
server.register_function(concatenate_strings, "concatenate")

# Run the server loop
server.serve_forever()
