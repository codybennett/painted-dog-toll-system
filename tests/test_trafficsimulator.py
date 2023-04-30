import logging
from unittest import TestCase
from unittest.mock import patch

logging.getLogger().setLevel(logging.DEBUG)

import trafficsimulator


class TestTrafficSimulator(TestCase):

    def setUp(self):
        pass

    @patch("trafficsimulator.mysql.connector")
    def test_mysql(self, mock_mysql):
        result = trafficsimulator.incoming("ABC")
        mock_mysql.connect.assert_called()

