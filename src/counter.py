from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}


# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """ Create a counter """
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


#    1. Create a route for method PUT on endpoint /counters/<name>.
#    2. Create a function to implement that route.
#    3. Increment the counter by 1.
#    4. Return the new counter and a 200_OK return code.
@app.route('/counters/<name>', methods=['PUT'])  # create route for PUT
def update_counter(name):
    """ Update a counter """
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        COUNTERS[name] += 1  # Increment counter by 1
        return {name: COUNTERS[name]}, status.HTTP_200_OK  # return the new counter and a 200_OK return code
    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND  # If no counter, return error msg


@app.route('/counters/<name>', methods=['GET'])  # create route for GET
def read_counter(name):
    """ Read a counter """
    app.logger.info(f"Request to read counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {name: COUNTERS[name]}, status.HTTP_200_OK  # return the counter and a 200_OK return code
    return {"Message": f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND  # If no counter, return error msg


@app.route('/counters/<name>', methods=['DELETE'])  # create route for DELETE
def delete_counter(name):
    """ Delete a counter """
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        del COUNTERS[name]
        # return a message stating which counter has been deleted and a 204_NO_CONTENT return code
        return {"Message": f"Counter {name} has been deleted"}, status.HTTP_204_NO_CONTENT  #
    # If the counter we wanted to delete doesn't exist, return an error message and a 404_NOT_FOUND return code
    return {"Message": f"Cannot delete counter {name}, it does not exist"}, status.HTTP_404_NOT_FOUND

