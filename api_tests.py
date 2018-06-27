import unittest
import json
from api import app


class TestCases(unittest.TestCase):

    @staticmethod
    def try_(ride_id, available_seats, date_and_time, from_, to):

        ride = {
            "Id": ride_id,
            "available_seats": available_seats,
            "date_and_time": date_and_time,
            "from_": from_,
            "to":to
        }

        return ride

    def setUp(self):

        self.test_client = app.test_client()
#test for adding a single ride offer
    def test_addRide(self):

        data = json.dumps(self.try_(1, "available_seats", "10/02/2009 10pm", "Mukono","Arua"))

        response = self.test_client.post('/api/v1/rides/create', data=data, headers=self.json_headers)
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.try_(1, "available_seats", "10/02/2009 10pm", "Mukono","Arua")})
        self.assertEqual(response.status_code, 200)

    def test_returnRide(self):
#test for returning a single ride offer
        response = self.test_client.get('/api/v1/rides/1')
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.find_sample_ride(1)})
        self.assertEqual(response.status_code, 200)

    def test_returnRides(self):
#test for returning all ride offers
        response = self.test_client.get('/api/v1/rides')

        if type(response.data) == str:

            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            print(response.data.decode())
            self.assertEqual(results, {"rides": [self.try_(1, "available_seats", "10/02/2009 10pm", "Mukono","Arua")]})
            self.assertEqual(response.status_code, 200)

    def test_removeRide(self):
#test for deleting a ride offer
        response = self.test_client.delete('/api/v1/rides/delete/1')
        results = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(results, {"remaining_rides": []})

    def find_sample_ride(self, ride_id):

        return self.try_(ride_id, "4", "10/02/2009 10pm", "Mukono", "Arua")

    json_headers = {'Content-Type': 'application/json'}
if __name__ == '__main__':
    unittest.main()
