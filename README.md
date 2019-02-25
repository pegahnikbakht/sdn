# SDN-based simulation of smart city

## About the project

This is a project for simulating a smart city based on SDN network. This project would be consists of three different use cases: 

- Traffic management in case of emergency
- Smart mobility
- Smart industry

In the simulations we have decided to choose mininet-wifi as the network simulator and Ryu as the SDN-based controller. For managing vehicular network we have decided to use Sumo simulator. 

SDN controller is set up on a remote controller in a docker container and mininet wifi will connect to it remotely. 

## Base Functions

There are a number of base functions availbale for the smart city such as:
- Creating a sample topology
- Creating a simple vanet network
- Creatig a Vanet and conect it to sumo

## Execution 

You need to install latest version of mininet and sumo in order to run existing files. Existing map and config files need to be replaced with default sumo config files. 
All files need to be run under root permission. 

