"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app

# we need to import the file that contains the status codes
from src import status

class CounterTest(TestCase):
    """Counter tests"""

    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def setUp(self):
        self.client = app.test_client()

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    # Make a call to Create a counter.
    # Ensure that it returned a successful return code.
    # Check the counter value as a baseline.
    # Make a call to Update the counter that you just created.
    # Ensure that it returned a successful return code.
    # Check that the counter value is one more than the baseline you measured in step 3.
    def test_update_a_counter(self):
        client = app.test_client()
        result = self.client.post('/counters/newCounter')                    # Create a counter
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)   # Check for successful return code
        baseValue = result.json["newCounter"]               # Grab the counter value for baseline comparison
        result = client.put('/counters/newCounter')         # Update/replace the counter with PUT
        self.assertEqual(result.status_code, status.HTTP_200_OK)    # Check for successful return code (again)
        self.assertGreater(result.json["newCounter"], baseValue)    # Check that the counter is greater than baseline
        result = client.put('/counters/fakeCounter')
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

    def test_read_a_counter(self):
        client = app.test_client()
        result = self.client.post('/counters/readCounter')      # Create a counter to read
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)  # Check for successful return code
        result = client.get('/counters/readCounter')             # Read the counter
        self.assertEqual(result.status_code, status.HTTP_200_OK)  # Check that the counter was read successfully
        result = client.get('/counters/fakeCounter')             # Read a counter that doesn't exist
