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
from pyproddi.ddicdi import (BaseRecordLayout, PhysicalStructure)

class BaseRecordLayoutTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.ps = PhysicalStructure("ddt", "ddp", "dds", "dd", "ddgs", "desc",
                                    "df", ["grs"], ["label"], ["psn"])

    def test_BaseRecordLayout(self):
        my_brl = BaseRecordLayout("eolm", self.ps, "tq")
        
        print("Python object")
        print(my_brl)

        my_brl_pb = my_brl.to_pb()

        print("Protocol buffer message")
        print(my_brl_pb)

if __name__ == "__main__":
    unittest.main()
