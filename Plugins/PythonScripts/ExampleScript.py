# Python 3.9
# Made by: Fortbonnitar
# This works as a bridge between Unreal Engine and Python by allowing the exchanging of data through a local TCP socket connection.


# # # # # # # # # # # # # # # # # ## # # # # # # # # # # # # # # # # ################                                 ##############        ########################
# XXX XXX XXX XXX XXX XXX XXX XXX ## XXX XXX XXX XXX XXX XXX XXX XXX ################         ############            ################      ########################
# XXX XXX# # # # # # # # #XXX XXX ## XXX XXX# # # # # # # # #XXX XXX ###                    ####        ####          ###           ###                ### 
# XXX #         ###         # XXX ## XXX #         ###         # XXX ###                  ###              ###        ###            ###               ### 
# XXX #       ### ###       # XXX ## XXX #       ### ###       # XXX ###                ###                  ###      ###            ###               ### 
# XXX #      ###   ###      # XXX ## XXX #      ###   ###      # XXX ############      ###                    ###     ###           ###                ### 
# XXX #     ###  X  ###     # XXX ## XXX #     ###  X  ###     # XXX ############      ###                    ###     ###         ###                  ### 
# XXX #      ###   ###      # XXX ## XXX #      ###   ###      # XXX ###               ###                    ###     #############                    ### 
# XXX #       ### ###       # XXX ## XXX #       ### ###       # XXX ###                ###                  ###      ###         ###                  ### 
# XXX #         ###         # XXX ## XXX #         ###         # XXX ###                 ###                ###       ###           ###                ### 
# XXX XXX# # # # # # # # #XXX XXX ## XXX XXX# # # # # # # # #XXX XXX ###                  ###              ###        ###             ###              ### 
# XXX XXX XXX XXX XXX XXX XXX XXX ## XXX XXX XXX XXX XXX XXX XXX XXX ###                   ###            ###         ###              ###             ### 
# # # # # # # # # # # # # # # # # ## # # # # # # # # # # # # # # # # ###                     ##############           ###               ###            ###                                
                  #################################
                  #  |_|_|_|_|_|_|_|_|_|_|_|_|_|  #                  #####################################################################################################
                  #  | | | | | | | | | | | | | |  #
                  #################################



print("""

Developed by Fortbonnitar

####   #    # #   # # # # # 
#     # #   #  #      #
##   #   #  ###       #
#     # #   #  #      #
#      #    #   #     #
# # # # # # # # # # # # # # 
""")





import socket
import random





##########################################################################################
# Set this script as a TCP-Server and create the socket and listen for Unreal connection 
###########################################################################################

class TCP:
    def __init__(self, ip_adress: str='127.0.0.1', port: int=8000):
        self.running = True
        self.ip_adress = ip_adress
        self.port = port
        self.debug = True
        self.directions = ['up', 'right', 'down', 'left']
        self.out_data = ''

        # Create a TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # Bind the server socket to a specific IP address and port
        self.server_address = (self.ip_adress, self.port)
        self.server_socket.bind(self.server_address)

    def listen(self):
        # Listen for incoming connections
        self.server_socket.listen(1)
        print("Server started. Waiting for connections...")

        # Accept a client connection
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Client connected: {self.client_address}")




        ##############################################################################
        # After Connection established successfully, if data recieved set as variable
        ###############################################################################


        
    def get_incoming(self):
        # Main Loop
        while self.running:
            try:
                data = self.client_socket.recv(4096)
                
                # Data is firstly decoded from bytes to a string
                self.in_data = data.decode()

                if self.debug == True:
                    print(f'data as string = {self.in_data}')

                
                if self.in_data.startswith('001:'):

                    

                    self.out_data = random.choice(self.directions)






                self.send_data(f'001:{self.out_data}')
            
            except Exception as e:
                print(e)




            
            
    def send_data(self, data_string, encoding='utf-8'):
            # Converting the sending data from string to bytes 
            reply_data = bytes(data_string, encoding)


            # Sending back to Unreal Engine
            send = self.client_socket.send(reply_data)
            
server = TCP()
server.listen()
server.get_incoming()