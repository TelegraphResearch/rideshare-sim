clock = 0
logStart = 1 # 2*60*60 
logEnd = 100 #logStart + 24*60*60
simLength= logEnd

def collectStats():
    return (clock >= logStart) and (clock < logEnd)


# Timing in seconds
travelTimeAverage = 15 * 60      # 15 minutes
travelTimeStdDev = 3 * 60        # 3 minutes
vehicleHoldTimeAverage = 3 * 60  # 3 minutes
vehicleHoldTimeStdDev = 30       # 30 seconds
vehiclePickUpTimeAverage = 5 * 60 # 6 minutes
vehiclePickUpTimeStdDev = 2 * 60 # 2 minutes

# Vehicle Quantity
vehicleQuantity = {'dedicated': 100, 'pooled': 60}

# Ultimate output
logs = {'dedicated': [], 'pooled': []} # group logs
vehicleLogs = {'dedicated': [], 'pooled': []}

def getLogs():
    return {
        'group': logs,
        'vehicles': vehicleLogs,
        'env': {
            'vehicleQuantity': vehicleQuantity,
            'logStart': logStart,
            'logEnd': logEnd,
        }
    }
