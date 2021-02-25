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
from pyproddi.ddicdi import (CategoryScheme, Concept, ConceptualVariable,
                             ManagedRepresentation, RepresentedVariable, 
                             RepresentedVariableGroup,
                             RepresentedVariableScheme, UnitType)

class RepresentedVariableSchemeTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.csr = CategoryScheme("CSName")
        self.cr = Concept(conceptName=["Concept Name"], description="Desc",
                          isCharacteristic="True", label=["label"])
        self.ut = UnitType("UT Name")
        self.mr = ManagedRepresentation("MR Name")
        self.cvr = ConceptualVariable(self.csr, self.cr, ["con_var_name"],
                                      'desc', ['label'], self.ut)
        self.rv = RepresentedVariable(self.csr, self.cr, self.cvr, "desc",
                                      ["label"], ['rvn'], self.ut, 'vr', self.mr)
        self.rvg = RepresentedVariableGroup("name")
        self.rvs = RepresentedVariableScheme()

    def test_RepresentedVariableScheme(self):
        my_rvs = RepresentedVariableScheme("desc", ["label"], [self.rvg], 
                                           [self.rv], ["vsn"], [self.rvs])
        
        print("Python object")
        print(my_rvs)

        my_rvs_pb = my_rvs.to_pb()

        print("Protocol buffer message")
        print(my_rvs_pb)

if __name__ == "__main__":
    unittest.main()
