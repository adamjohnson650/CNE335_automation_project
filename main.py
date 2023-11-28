# This is the template code for the CNE335 Final Project
# Adam Johnson
# CNE 335 Fall

from server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Adam Johnson")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_ip = "54.187.174.1"
    server = Server(server_ip)
    # TODO - Call Ping method and print the results

    ping_result = server.ping()
    print(ping_result)