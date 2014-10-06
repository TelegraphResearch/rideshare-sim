# Global Clock (seconds)
clock = 0
logStart = 1*60*60
logEnd = logStart + 6*60*60
simLength= logEnd

# Arrival Rate
needGroupFrequency = 0.06

# Group and Vehicle Variables (seconds)
travelTimeAverage = 15 * 60      # 15 minutes
travelTimeStdDev = 3 * 60        # 3 minutes
vehicleHoldTimeAverage = 3 * 60  # 3 minutes
vehicleHoldTimeStdDev = 30       # 30 seconds
vehiclePickUpTimeAverage = 5 * 60 # 5 minutes
vehiclePickUpTimeStdDev = 2 * 60 # 2 minutes

# Vehicle Quantity
vehicleQuantity = {'dedicated': 100, 'pooled': 100}

# Ultimate Output
logs = {'dedicated': [], 'pooled': []} # group logs
vehicleLogs = {'dedicated': [], 'pooled': []}

def collectStats():
    return (clock >= logStart) and (clock < logEnd)

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
