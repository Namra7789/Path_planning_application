import socket
import json
import math

BUFFER_SIZE = 1024

def calculate_heading_angle(current_location, destination):
    delta_x = destination[0] - current_location[0]
    delta_y = destination[1] - current_location[1]
    angle_rad = math.atan2(delta_y, delta_x)
    angle_deg = math.degrees(angle_rad)
    return (angle_deg + 360) % 360  # Ensure the result is in the range [0, 360)

def calculate_distance(current_location, destination):
    delta_x = destination[0] - current_location[0]
    delta_y = destination[1] - current_location[1]
    distance = math.sqrt(delta_x*2 + delta_y*2)
    return distance

def get_destination_coordinates():
    destination_lat = float(input("Enter the destination latitude: "))
    destination_lon = float(input("Enter the destination longitude: "))
    destination = (destination_lat, destination_lon)
    return destination

def start_client():
    server_address = input("Enter the server IP address: ")
    server_port = int(input("Enter the server port: "))

    destination = get_destination_coordinates()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address_port = (server_address, server_port)

    try:
