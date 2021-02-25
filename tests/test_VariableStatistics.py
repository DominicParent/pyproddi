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
from pyproddi.ddicdi import (Concept, CategoryScheme, ConceptualVariable, MeasurementItem,
                             MissingValuesReference, Question, RepresentedVariable, UnitType, Universe,
                             Variable, VariableStatistics, Weighting)

class VariableStatisticsTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.concept = Concept(conceptName=["test_name"], description="desc",
                               isCharacteristic="False", label=["label"])
        self.cs = CategoryScheme("cs_name")
        self.ut = UnitType("Unit Type Name")
        self.cv = ConceptualVariable(self.cs, self.concept, ['con_var_name'],
                                     'desc', ['label'], self.ut)
        self.mvr = MissingValuesReference("mvr name")
        self.q = Question("Question name")
        self.mi = MeasurementItem("Measurement item")
        self.uni = Universe("Universe Name")
        self.ut = UnitType("Unit Type Name")
        self.w = Weighting("Weighting Name")
        self.rv = RepresentedVariable()
        self.v = Variable("analysisunit", self.concept, self.cv, "desc",
                            "embargo ref", False, False, False, ["label"],
                            [self.mi], "out parameter", [self.q], self.rv,
                            "sourceparref", "source unit", [],
                            self.ut, [self.uni], "var rep", self.w)

    def test_VariableStatistics(self):
        my_vs = VariableStatistics(["fcs"], self.mvr, "std weight ref", 
                                   ["sum stat"], "total response", ["ucs"],
                                   self.v, self.v)
        
        print("Python object")
        print(my_vs)

        my_vs_pb = my_vs.to_pb()

        print("Protocol buffer message")
        print(my_vs_pb)

if __name__ == "__main__":
    unittest.main()
