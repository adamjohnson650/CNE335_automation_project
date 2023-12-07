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
    server_ip = Server("52.32.42.247")

    # TODO - Call Ping method and print the results

    ping_result = server_ip.ping()
    print("Ping Results:", ping_result)
    result = server_ip.update()