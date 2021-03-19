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
from pyproddi.ddicdi import (CategoryScheme, Concept, ConceptualVariable,
                             UnitType, ManagedRepresentation,
                             RepresentedVariable)

class RepresentedVariableTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.csr = CategoryScheme("CSName")
        self.cr = Concept(conceptName=["Concept Name"], description="Description",
                          isCharacteristic="True", label=["concept label"])
        self.ut = UnitType("UT Name")
        self.mr = ManagedRepresentation("MR Name")
        self.cvr = ConceptualVariable(self.csr, self.cr, ["con_var_name"],
                                     'desc', ['label'], self.ut)

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_RepresentedVariable(self):
        my_rv = RepresentedVariable(self.csr, self.cr, self.cvr, "desc",
                                    ['label'],['rvn'], self.ut, 'vr', self.mr)
        
        print("Python object")
        print(my_rv)

        my_rv_pb = my_rv.to_pb()

        print("Protocol buffer message")
        print(my_rv_pb)

    def test_RepresentedVariable_json(self):
        my_rv_json = {
        "RepresentedVariable" : {
            "CategorySchemeReference" : {},
            "ConceptReference" : {},
            "ConceptualVariableReference" : {},
            "Description" : "Test description.",
            "Label" : ["test1", "test2", "test3"],
            "RepresentedVariableName" : ["name1", "name2", "name3"],
            "UnitTypeReference" : {},
            "ValueRepresentation" : "representation",
            "ValueRepresentationReference" : {}
          }
        }

        print("JSON RepresentedVariable Message")
        print(validate(instance=my_rv_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
