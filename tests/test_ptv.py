from unittest import TestCase, main

import responses

from impactdata import ptv


class TestGetDisruptions(TestCase):
    def setUp(self):
        self.response = {
            'disruptions': {
                'metro_train': [
                    {
                        'description': 'foo',
                        'routes': [
                            {'route_id': 1},
                            {'route_id': 2},
                        ]
                    }
                ]
            }
        }

    @responses.activate
    def test(self):
        responses.add(
            responses.GET, 'https://timetableapi.ptv.vic.gov.au/v3/disruptions',
            json=self.response)
        disruptions = ptv.get_disruptions()
        self.assertGreater(len(disruptions), 0)
        self.assertEqual(disruptions[0]['description'], 'foo')


class TestFilterDisruptions(TestCase):
    def setUp(self):
        self.disruptions = [
            {
                'description': 'foo',
                'routes': [
                    {'route_id': 1},
                ]
            },
            {
                'description': 'bar',
                'routes': [
                    {'route_id': 1},
                    {'route_id': 2},
                ]
            }
        ]

    def test_route_1(self):
        result = ptv.filter_disruptions(self.disruptions, 1)
        self.assertEqual(len(result), 2)

    def test_route_2(self):
        result = ptv.filter_disruptions(self.disruptions, 2)
        self.assertEqual(len(result), 1)

    def test_no_results(self):
        result = ptv.filter_disruptions(self.disruptions, 3)
        self.assertEqual(len(result), 0)


class TestGetDescriptions(TestCase):
    def setUp(self):
        self.disruptions = [
            {
                'description': 'foo',
                'routes': [
                    {'route_id': 1},
                ]
            },
            {
                'description': 'bar',
                'routes': [
                    {'route_id': 1},
                    {'route_id': 2},
                ]
            }
        ]

    def test(self):
        result = ptv.get_descriptions(self.disruptions)
        self.assertEqual(result, 'foo, bar')


if __name__ == '__main__':
    main()
