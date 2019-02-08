# -*- coding: utf-8 -*-

import car
import drive
import unittest
from unittest.mock import patch, MagicMock
import pytest

class DriveTestCase(unittest.TestCase):

    """
    @patch.object(drive.car.Ignition, 'start_engine', autospec=True)
    @patch.object(drive.car.Car, 'find_ignition', autospec=True)
    def test_ignition(self, mock_ignition, mock_engine):
        d = drive.Drive()
        d.go_driving()

        # verify

        mock_ignition.assert_called_once()
        mock_engine.assert_called_once()
    """

    @patch.object(drive.car.Car, 'find_ignition', autospec=True)
    def test_ignition2(self, mock_ignition):
        engine = MagicMock()

        mock_ignition.return_value.start_engine.return_value = engine

        d = drive.Drive()
        d.go_driving()

        # verify
        mock_ignition.return_value.start_engine.assert_called_once()
