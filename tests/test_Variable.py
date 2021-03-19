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

import unittest, json
from jsonschema import Draft7Validator, validate

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

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

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

    def test_Variable_json(self):
        my_var_json = {
        "Variable" : {
            "AnalysisUnit" : "Some value.",
            "ConceptReference" : {},
            "ConceptualVariableReference" : {},
            "Description" : "Some description.",
            "EmbargoReference" : "Some embargo.",
            "IsGeographic" : True,
            "IsTemporal" : False,
            "IsWeight" : True,
            "Label" : ["label1", "Label2", "label3"],
            "MeasurementReference" : [],
            "OutParameter" : "Some output.",
            "QuestionReference" : [],
            "RepresentedVariableReference" : {},
            "SourceParameterReference" : "Some param ref.",
            "SourceUnit" : "Some source unit.",
            "SourceVariableReference" : [],
            "UnitTypeReference" : {},
            "UniverseReference" : [],
            "VariableRepresentation" : "Some var rep.",
            "WeightingProcessReference" : {}
          }
        }

        print("JSON Variable message")
        print(validate(instance=my_var_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
