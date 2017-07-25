from unittest import TestCase, main

from impactdata.utils import get_disruptions


class TestGetDisruptions(TestCase):
    def test(self):
        disruptions = get_disruptions()
        self.assertGreater(disruptions, 0)


if __name__ == '__main__':
    main()
