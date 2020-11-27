#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
from pyproddi.io.protobuf import dataset_pb2

class ProtoTest(unittest.TestCase):
    def setUp(self):
        print("++++++++++++++")
        print("New test %s" % self._testMethodName)
        print("++++++++++++++")

        self.my_ival1=InstanceValue("42")
        self.my_ival2=InstanceValue("43")
        self.my_datap1=DataPoint(InstanceValue("44"))
        self.my_datap2=DataPoint(InstanceValue("45"))
        self.my_keym1=KeyMember(InstanceValue("46"))
        self.my_keym2=KeyMember(InstanceValue("47"))
        self.my_key1=Key(KeyMember(InstanceValue("48")))
        self.my_key2=Key(KeyMember(InstanceValue("49")))
        self.my_dataset=DataSet(DataPoint(InstanceValue("50")),Key(KeyMember(InstanceValue("51"))))

    def tearDown(self):
        self.my_ival1=None
        self.my_ival2=None
        self.my_datap1=None
        self.my_datap2=None
        self.my_keym1=None
        self.my_keym2=None
        self.my_key1=None
        self.my_key2=None
        self.my_dataset=None

    def test_create_buff(self):
        my_ds = dataset_pb2.DataSet()
        my_key = my_ds.key.add()
        my_keym = my_key.keym.add()
        my_ival = my_keym.ival
        my_ival.value = self.my_ival1.value

        print(my_ds)

    def test_write_buff(self):
        pass

    def test_read_buff(self):
        pass
