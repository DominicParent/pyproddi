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
from pyproddi.ddicdi import (Concept, Universe, Variable, VariableGroup,
                             VariableScheme, RecordLayout)

class RecordLayoutTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.vs = VariableScheme("desc", ["label"], [VariableGroup()],
                                 [Variable()], ["var scheme name"], [])

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_RecordLayout(self):
        my_rl = RecordLayout("arraybase", "char set", ["data item list"],
                             self.vs, False)
        
        print("Python object")
        print(my_rl)

        my_rl_pb = my_rl.to_pb()

        print("Protocol buffer message")
        print(my_rl_pb)

    def test_RecordLayout_json(self):
        my_rl_json = {
        "RecordLayout" : {
            "ArrayBase" : "An arraybase.",
            "CharacterSet" : "A character set.",
            "DataItem" : ["di1", "di2"],
            "DefaultVariableSchemeReference" : {},
            "NamesOnFirstRow" : False
          }
        }

        print("JSON RecordLayout message")
        print(validate(instance=my_rl_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
