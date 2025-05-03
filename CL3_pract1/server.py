from xmlrpc.server import SimpleXMLRPCServer

# Define the factorial function
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Create the RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the function
server.register_function(factorial, "factorial")

# Run the server
server.serve_forever()
