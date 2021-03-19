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
from pyproddi.ddicdi import (Concept, RecordLayout, RecordLayoutGroup,
                             Universe, VariableScheme)

class RecordLayoutGroupTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.concept = Concept(conceptName=["name"], description="desc",
                               isCharacteristic="True", label=["test_label"])
        self.rlg = RecordLayoutGroup()
        self.rl = RecordLayout("arraybase", "char set", ["data item list"],
                               VariableScheme(), False)
        self.uni = Universe("Name")

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_RecordLayoutGroup(self):
        my_rlg = RecordLayoutGroup(self.concept, 'desc', False, ['keyw'],
                                   ['label'], ['rlgname'], self.rlg, self.rl,
                                   ['subject'], 'typerlg', [self.uni])
        
        print("Python object")
        print(my_rlg)

        my_rlg_pb = my_rlg.to_pb()

        print("Protocol buffer message")
        print(my_rlg_pb)

    def test_RecordLayoutGroup_json(self):
        my_rlg_json = {
        "RecordLayoutGroup" : {
            "ConceptReference" : {},
            "Description" : "Some desc.",
            "IsOrdered" : True,
            "Keyword" : ["kw1", "kw2"],
            "Label" : ["label1"],
            "RecordLayoutGroupName" : ["name1", "name2", "name3"],
            "RecordLayoutGroupReference" : {},
            "RecordLayoutReference" : {}
          }
        }

        print("JSON RecordLayoutGroup message")
        print(validate(instance=my_rlg_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
