from math import log10, pi
import matplotlib.pyplot as plt
from os import remove

def calculatePr(pT: float, gT: float, gR: float, lCable: float, lConnector: float, totalDistance: float, frequency: float) -> float:  # noqa: E501
    """
    This function calculates the free space path loss and received power for a wireless
    communication system and plots them against distance on every 10 meters.
    
    :param pT: transmitted power in dBm
    :type pT: float
    :param gT: The gain of the transmitting antenna in dB
    :type gT: float
    :param gR: gR stands for the gain of the receiving antenna. It is a measure of how
    well the antenna can receive signals from a particular direction
    :type gR: float
    :param lCable: lCable refers to the loss caused by the cable (in dB)
    :type lCable: float
    :param lConnector: lConnector refers to the loss caused by the connector used to
    connect the transmitter and receiver. It is usually measured in decibels (dB)
    :type lConnector: float
    :param totalDistance: The total distance between the transmitter and receiver in meters
    :type totalDistance: float
    :param frequency: The frequency of the signal being transmitted, in Hz. You can find
    on the datasheet of the transmitter.
    :type frequency: float
    """  # noqa: E501
    try:
        remove("results.txt")
    except FileNotFoundError:
        pass
    
    received_power_list = []
    fspl_list = []
    
    lambdaa = 3*(10**8) / frequency #Wavelength
    with open('results.txt', 'w', encoding='utf-8') as file:
        file.write(f"Wavelength: {lambdaa}\n\n\n")
    
    for distance in range(10, totalDistance + 10, 10):
        fspl = 20 * log10(4*pi*distance / lambdaa) #Free Space Path Loss
        receivedPower = pT- + gT + gR - fspl - lCable - lConnector #Received Power
        fspl_list.append(fspl)
        received_power_list.append(receivedPower)
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(f"Free Space Path Loss for {distance}m: {fspl} dB\n")
            file.write(f"Received Power for {distance}m: {receivedPower} dB\n")
            file.write(f"Received Power Equation for {distance}m : {pT} + {gT} + {gR} - {fspl} - {lCable} - {lConnector}\n\n")  # noqa: E501
        
    plt.plot(range(10, totalDistance + 10, 10), fspl_list, marker="o")
    plt.plot(range(10, totalDistance + 10, 10), received_power_list, marker="o")
    plt.xlabel("Distance (m)")
    plt.ylabel("dB")
    plt.legend(["Free Space Path Loss", "Received Power"])
    plt.show()
    
calculatePr(13, 2.1, 2.1, 0, 0, 1500, 863*(10**6))
