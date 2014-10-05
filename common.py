clock = 0
logStart = 1*60*60
logEnd = logStart + 6*60*60
simLength= logEnd

def collectStats():
    return (clock >= logStart) and (clock < logEnd)

# Arrival Rate
needGroupFrequency = 0.06

# Timing in seconds
travelTimeAverage = 15 * 60      # 15 minutes
travelTimeStdDev = 3 * 60        # 3 minutes
vehicleHoldTimeAverage = 3 * 60  # 3 minutes
vehicleHoldTimeStdDev = 30       # 30 seconds
vehiclePickUpTimeAverage = 5 * 60 # 6 minutes
vehiclePickUpTimeStdDev = 2 * 60 # 2 minutes

# Vehicle Quantity
vehicleQuantity = {'uber': 100, 'hitch': 100}

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

def resetLogs():
    clock = 0
    logs = {'uber': [], 'hitch': []}
    vehicleLogs = {'uber': [], 'hitch': []}
