from unittest import TestCase, main

import responses

from ptvalerts import ptv, slack


class TestGetDisruptions(TestCase):
    def setUp(self):
        self.users = [ptv.User('@beau', 'Belgrave', 1)]
        self.disruptions = (
            {
                'description': 'foo',
                'routes': [
                    {'route_id': 1},
                    {'route_id': 2},
                ]
            },
        )

    def test(self):
        slack.send(self.users, self.disruptions)
