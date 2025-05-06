import Pyro5.api

@Pyro5.api.expose
class StringService:
    def concatenate(self, s1, s2):
        return s1 + s2

# Start the Pyro daemon and register the object
def main():
    daemon = Pyro5.server.Daemon()
    uri = daemon.register(StringService)
    print("Server is running. Object URI =", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
