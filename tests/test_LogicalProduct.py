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
from pyproddi.ddicdi import (CategoryScheme, CodeListScheme, CubeScheme,
                             ManagedRepresentationScheme, LogicalProduct, 
                             RepresentedVariableScheme, VariableScheme,
                             RepresentedVariableGroup, RepresentedVariable)

class LogicalProductTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.cs = CategoryScheme("Name")
        self.cls = CodeListScheme("Name")
        self.cubes = CubeScheme("Name")
        self.mrs = ManagedRepresentationScheme("Name")
        self.rvg = RepresentedVariableGroup("Name")
        self.rv = RepresentedVariable()
        self.rvs = RepresentedVariableScheme()
        self.rvs2 = RepresentedVariableScheme("desc", ["label"], [self.rvg],
                                             [self.rv], ["vsn"], [self.rvs])
        self.vs = VariableScheme()

    def test_LogicalProduct(self):
        my_lp = LogicalProduct([self.cs], [self.cls], [self.mrs], [self.cubes],
                               [self.rvs2], [self.vs])
        
        print("Python object")
        print(my_lp)

        my_lp_pb = my_lp.to_pb()

        print("Protocol buffer message")
        print(my_lp_pb)

if __name__ == "__main__":
    unittest.main()
