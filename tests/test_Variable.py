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
from pyproddi.ddicdi import (Concept, ConceptualVariable, Question,
                             RepresentedVariable, MeasurementItem, Variable,
                             UnitType, Universe, Weighting, CategoryScheme)

class VariableTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.concept = Concept(conceptName=["test_name"], description="desc",
                               isCharacteristic="False", label=["label"])
        self.cs = CategoryScheme("cs_name")
        self.q = Question("Question Name")
        self.mi = MeasurementItem("Measurement item")
        self.rv = RepresentedVariable()
        self.var = Variable()
        self.ut = UnitType("Unit Type Name")
        self.uni = Universe("Universe Name")
        self.w = Weighting("Weighting Name")
        self.cv = ConceptualVariable(self.cs, self.concept, ['con_var_name'],
                                     'desc', ['label'], self.ut)

    def test_Variable(self):
        my_var = Variable("analysisunit", self.concept, self.cv, "desc",
                          "embargo ref", False, False, False, ["label"],
                          [self.mi], "out parameter", [self.q],
                          self.rv, "sourceparref", "source unit", [self.var],
                          self.ut, [self.uni], "var rep", self.w)
        
        print("Python object")
        print(my_var)

        my_var_pb = my_var.to_pb()

        print("Protocol buffer message")
        print(my_var_pb)

if __name__ == "__main__":
    unittest.main()
