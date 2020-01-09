# Thermal Simulation

## Introduction
This program simulates water flowing through pipe being warmed by solar radiation, pressurized by a pump, and cooled,  
in a tank,back to its initial temperature.in a tank. There are many dangerous assumptions made in the simulation, but it
will give you an idea of my coding skills in this 'simple simulation'.

To run simulation open the main file and select run
Required libraries are:
- numpy
- pandas
- Tkinter

## Assumptions
- This simulation is a **steady state system**.  It does not simulate any transient periods. 
- All pipe sections are evaluated as fully developed 
- Minor Losses are ignored
- Simulation only works on laminar flow
- Only Considers saturated water and doesn't go into superheated water 
- all temperatures are reported in degrees Celsius 
- Potential energy gain/losses are neglected

### Solar Heating
- Heat flux is constant around the surface area of the pipe pipe, and 100% of the solar radiation is absorbed. 
### Pump
- The pump is adiabatic
- The pump as an output pressure of 150Kpa
- Head Loss is reported in (mm)

### Tank
 -The tank allows enough heat transfer for the water to cool to its original temperature

 


