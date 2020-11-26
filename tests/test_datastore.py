#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Copyright © Her Majesty the Queen in Right of Canada, as represented
# by the Minister of Statistics Canada, 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from pyproddi.model import InstanceValue
from pyproddi.model import DataPoint
from pyproddi.model import KeyMember
from pyproddi.model import Key
from pyproddi.model import DataSet

class DatasetTest(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++")
        print("New test %s" % self._testMethodName)
        print("+++++++++++++++")

    def tearDown(self):
        pass

    def test_create_InstanceValue(self):
        my_ival = InstanceValue("42")
        self.assertTrue("42" == my_ival.value)

    def test_create_DataPoint(self):
        my_datapoint = DataPoint("42")
        self.assertTrue("42" == my_datapoint.ival)

    def test_create_KeyMember(self):
        my_keymember = KeyMember("42")
        self.assertTrue("42" == my_keymember.ival)

    def test_create_Key(self):
        pass

    def test_add_KeyMember(self):
        pass

    def test_create_DataSet(self):
        pass

    def test_add_Key(self):
        pass

    def test_add_Datapoint(self):
        pass
