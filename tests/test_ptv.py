from unittest import TestCase, main

from impactdata import ptv


class TestGetDisruptions(TestCase):
    def test(self):
        disruptions = ptv.get_disruptions()
        self.assertGreater(disruptions, 0)


if __name__ == '__main__':
    main()
