from asynctest import TestCase

from myproj import sum


class TestExample(TestCase):
    async def test_true(self):
        self.assertEqual(2, sum(1, 1))
