import math
from statistics import *
import sys, json

'''
This script is run from the command line and opens a specified data run in JSON
then runs calculations and exports a summary script
'''

# set global constants
services = ['dedicated', 'pooled']
output = {}
for service in services:
    output[service] = {}

VEHICLE_QUANT = [
    'sum',
    'sumSquared',
]
VEHICLE_QUANT_CATEGORIES = [
    'groups',
    'passengers',
    'groupsAssigned', # to be picked up
    'passengersAssigned',
]

VEHICLE_STATES = [
    'idle',
    'drivingOccupied',
    'drivingUnoccupied',
    'holdingOccupied',
    'holdingUnoccupied',
]

VEHICLE_ACTIVE_STATES = [
    'drivingOccupied',
    'holdingOccupied',
]

VEHICLE_DRIVING_STATES = [
    'drivingOccupied',
    'drivingUnoccupied',
]

GROUP_ATTRIBUTES = [
    'spawn',
    'driverAssigned',
    'start',
    'end',
    'size',
]

GROUP_TIMES = [
    'driverAssigned',
    'start',
    'end',
]


# open file
sys.argv[1]

# import data
f = open(sys.argv[1], 'r')
data = json.loads(f.read())
f.close()



# run calculations

simLength = data['env']['logEnd'] - data['env']['logStart']
for service in services:
    vehicles = data['env']['vehicleQuantity'][service]

    vehicleStateSums = {}
    vehicleStateCount = {}
    for state in VEHICLE_STATES:
        vehicleStateSums[state] = 0
        vehicleStateCount[state] = 0

    vehicleMetrics = {
        'idle': [],
        'driving': [],
        'utilization': []
    }

    vehicleQuantSum = {}
    for item in VEHICLE_QUANT:
        vehicleQuantSum[item] = {}
        for category in VEHICLE_QUANT_CATEGORIES:
            vehicleQuantSum[item][category] = 0

    vehicleQuantMetrics = {
        'avg': {},
        'variance': {},
    }
    for category in VEHICLE_QUANT_CATEGORIES:
        vehicleQuantMetrics['avg'][category] =  []
        vehicleQuantMetrics['variance'][category] =[]


    for vehicle in data['vehicles'][service]:
        # distribution of states
        for state in VEHICLE_STATES:
            vehicleStateCount[state] += vehicle['stateCount'][state]

        # helper
        stateCount = vehicle['stateCount']

        vehicleMetrics['idle'].append(stateCount['idle'] / simLength)

        drivingSum = 0
        for state in VEHICLE_DRIVING_STATES:
            drivingSum += stateCount[state]

        activeSum = 0
        for state in VEHICLE_ACTIVE_STATES:
            activeSum += stateCount[state]

        vehicleMetrics['idle'].append(stateCount['idle'] / simLength)
        vehicleMetrics['driving'].append(drivingSum / simLength)
        vehicleMetrics['utilization'].append(activeSum / simLength)

        # quant 
        for category in VEHICLE_QUANT_CATEGORIES: 
            # average over time for the vehicle
            vehicleQuantMetrics['avg'][category].append(vehicle['sum'][category]/simLength)
            vehicleQuantMetrics['variance'][category].append(
                    (simLength * vehicle['sumSquared'][category] - vehicle['sum'][category]^2) / (simLength * (simLength-1))
            )
            for item in VEHICLE_QUANT: # sum and sumSquared
                vehicleQuantSum[item][category] += vehicle[item][category]

    # post vehicle loop
    systemDrivingSum = 0
    for state in VEHICLE_DRIVING_STATES:
        systemDrivingSum += vehicleStateCount[state]

    systemActiveSum = 0
    for state in VEHICLE_ACTIVE_STATES:
        systemActiveSum += vehicleStateCount[state]

    output[service]['system idle'] = vehicleStateCount['idle'] / (simLength * vehicles)
    output[service]['system driving'] = systemDrivingSum / (simLength * vehicles)
    output[service]['system utilization'] = systemActiveSum / (simLength * vehicles)
    output[service]['average idle'] = mean(vehicleMetrics['idle'])
    output[service]['average driving'] = mean(vehicleMetrics['driving'])
    output[service]['average utilization'] = mean(vehicleMetrics['utilization'])
    output[service]['stdev idle'] = stdev(vehicleMetrics['idle'])
    output[service]['stdev driving'] = stdev(vehicleMetrics['driving'])
    output[service]['stdev utilization'] = stdev(vehicleMetrics['utilization'])

    # quant

    for category in VEHICLE_QUANT_CATEGORIES:
        output[service]['vehicle average ' + category] = mean(vehicleQuantMetrics['avg'][category])
        output[service]['system average ' + category] = vehicleQuantSum['sum'][category] / (simLength * vehicles)
        output[service]['vehicle stdev ' + category] = math.sqrt(mean(vehicleQuantMetrics['variance'][category]))

        output[service]['stdev of vehicle average ' + category] = stdev(vehicleQuantMetrics['avg'][category])
        output[service]['system stdev of ' + category] = math.sqrt(
                    (simLength*vehicles * vehicleQuantSum['sumSquared'][category] - vehicleQuantSum['sum'][category]^2) / (simLength*vehicles * (simLength*vehicles-1))
        )
        #phew


        #
        # GROUPS
        #

        groupMetrics = {}
        groupMetrics['all'] = {}
        for attribute in GROUP_TIMES:
            groupMetrics['all'][attribute] = []

        for size in range(1,4):
            groupMetrics[str(size)] = {}
            for attribute in GROUP_TIMES:
                groupMetrics[str(size)][attribute] = []

        for group in data['group'][service]:
            size = group['size']
            spawn = group['spawn']
            for attribute in GROUP_TIMES:
                normalizedTime = group[attribute] - spawn
                groupMetrics[str(size)][attribute].append(normalizedTime)
                groupMetrics['all'][attribute].append(normalizedTime)

        for size in ['1', '2', '3', 'all']:
            for attribute in GROUP_TIMES:
                output[service][
                     'Average time to %s for group size %s' % (attribute, size)
                 ] = mean(groupMetrics[size][attribute])

                output[service][
                    'stdev time to %s for group size %s' % (attribute, size)
                 ] = stdev(groupMetrics[size][attribute])



# Save the results of the file to json 
f = open(sys.argv[2], 'w')
f.write(json.dumps(output))
f.close()
