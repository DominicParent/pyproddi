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
from jsonschema import validate

from pyproddi.io.protobuf import ddicdi_pb2
from pyproddi.ddicdi import (CategoryScheme, Concept, UnitType,
                             ConceptualVariable)

class ConceptualVariableTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.cs = CategoryScheme('cs_name')
        self.concept = Concept(['concept_name'], "desc",[],[],'False',
                               ['test_label'],[],[])
        self.ut = UnitType('ut_name')

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

    def test_ConceptualVariable(self):
        my_cv = ConceptualVariable(self.cs, self.concept, ['con_var_name'],
                                   'desc', ['label'], self.ut)
        
        print("Python object")
        print(my_cv)

        my_cv_pb = my_cv.to_pb()

        print("Protocol buffer message")
        print(my_cv_pb)

    def test_ConceptualVariable_json(self):
        cv_json = {
            "ConceptualVarialbe" : {
                "CategorySchemeReference" : {},
                "ConceptReference" : {},
                "ConceptVariableName" : {"Test", "Test"},
                "Description" : {"This is a description"},
                "Label" : {"Label1", "Label2"},
                "UnitTypeReference" : {}
            }
        }

        print("JSON ConceptualVariable message")
        print(validate(instance=cv_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
