# Python 3.9
# Made by: Fortbonnitar
# This works as a bridge between Unreal Engine and Python by allowing the exchanging of data through a local TCP socket connection.

import socket
import numpy











# THESE BASE FUNCTIONS CAN BE ADDED TO FOR WHATEVER YOU WOULD LIKE TO DO WITH YOUR DATA #
##########################################################################################
# BASIC FUNCTIONS
###########################################################################################


def change_type(current_data, new_type: str):
    '''
    Currently can convert a variable to types, [float, int, str, bool]
    
    '''
    try:

        if new_type == 'float':
            result = float(current_data)
        if new_type == 'int':
            result = int(current_data)
        if new_type == 'string' or new_type == 'str':
            result = str(current_data)
        if new_type == 'boolean' or new_type == 'bool':
            result = bool(current_data)
        return result
    except Exception as conv_error:
        print(conv_error)
        return current_data










# NO MODIFICATION TO THIS SECTION IS REQUIRED BY DEFAULT #
##########################################################################################
# Set this script as a TCP-Server and create the socket and listen for Unreal connection 
###########################################################################################


# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the server socket to a specific IP address and port
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)


# Listen for incoming connections
server_socket.listen(1)
print("Server started. Waiting for connections...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Client connected: {client_address}")












# THIS SECTION HANDLES THE RECEIVING OF THE INCOMING DATA FROM UNREAL #
##############################################################################
# After Connection established successfully, if data recieved set as variable
###############################################################################



# Main Loop
while True:
    data = client_socket.recv(4096)
    # print(f'data_oring = {data}')
    

    # Data is firstly decoded from bytes to a string
    data_string = data.decode()
    print(f'data as string = {data_string}')




#############################################################################################################
# Unformating incoming data and convert each to float
##############################################################################################################


    # Splitting the data into 3 floats 
    # 1 is throttle distance
    # 2 is left sensor distance
    # 3 is right sensor distance

    data_split1 = data_string.split(':')
    data_split2 = data_split1[1].split(';')
    throttle_in = float(data_split1[0])
    left_in = float(data_split2[0])
    right_in = float(data_split2[1])
    print(f'throttle= {throttle_in}, left= {left_in}, right= {right_in}')






#############################################################################################################
# Altering the data for testing, This is where you implement your code that handles what to do with your data
##############################################################################################################
 
    # Handling Throttle Calculations
    if throttle_in < 1.0:
        throttle_out = throttle_in / 0.25
    else:
        throttle_out = .5


    # Handling Steering Calculations
    if left_in >= 1.0 and right_in >= 1.0:
        steering_out = 0
    else:
        steering_out = left_in + -right_in




# NO MODIFICATION TO THIS SECTION IS REQUIRED BY DEFAULT #
###################################################################################################
# Formatting and converting data to string
###################################################################################################

    # converting processed data from float to string

    result_data_string = f'{throttle_out}:{steering_out}'
    print(f'throttle= {throttle_out}, steering= {steering_out}')






# NO MODIFICATION TO THIS SECTION IS REQUIRED BY DEFAULT #
###################################################################################################
# Send the data back to Unreal Engine
###################################################################################################

    # Converting the sending data from string to bytes 
    reply_data = bytes(result_data_string, 'utf-8')
    # print(f'reply_data = {reply_data}')

    # Sending back to Unreal Engine
    send = client_socket.send(reply_data)
    # print(f'send = {send}')









