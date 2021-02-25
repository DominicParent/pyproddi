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

from pyproddi.io.protobuf import ddicdi_pb2
from pyproddi.ddicdi import (Concept, PhysicalStructureGroup, Universe)

class PhysicalStructureGroupTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.concept = Concept(conceptName=["name"], description="desc",
                               isCharacteristic="True", label=["label"])
        self.uni = Universe("Name")
        self.psg = PhysicalStructureGroup(self.concept, "desc", False,
                                          ["keyw"], ["label"], ["psgn"],
                                          PhysicalStructureGroup(),
                                          ["subject"], "topsg", [self.uni])

    def test_PhysicalStructureGroup(self):
        my_psg = PhysicalStructureGroup(self.concept, "desc", False, ["keyw"],
                                        ["label"], ["psgn"], self.psg,
                                        ["subject"], "topsg", [self.uni])
        
        print("Python object")
        print(my_psg)

        my_psg_pb = my_psg.to_pb()

        print("Protocol buffer message")
        print(my_psg_pb)

if __name__ == "__main__":
    unittest.main()
