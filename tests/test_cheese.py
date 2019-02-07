# -*- coding: utf-8 -*-

import car
import drive
import unittest
from unittest.mock import patch
import pytest

class DriveTestCase(unittest.TestCase):

    @patch.object(drive.car.Ignition, 'start_engine', autospec=True)
    @patch.object(drive.car.Car, 'find_ignition', autospec=True)
    def test_ignition(self, mock_ignition, mock_engine):
        d = drive.Drive()
        d.go_driving()

        # verify
        
        mock_ignition.assert_called_once()
        mock_engine.assert_called_once()
