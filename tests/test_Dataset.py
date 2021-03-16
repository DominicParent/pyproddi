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
from pyproddi.ddicdi import (Concept, Dataset, Universe, Variable,
                             VariableGroup, VariableScheme)

class DatasetTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.concept = Concept(conceptName=["test name"], description="desc",
                               isCharacteristic="False", label=["label"])
        self.uni = Universe("Universe name")
        self.v = Variable()
        self.vg = VariableGroup(self.concept, "desc", True, ["keyword"],
                                ["label"], ["subject"], "var type", self.uni,
                                ["var group name"], VariableGroup(), self.v)
        self.vs = VariableScheme("desc", ["label"], [self.vg], [self.v],
                                 ["var scheme name"], [])

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_Dataset(self):
        my_dataset = Dataset("arraybase", ["dataset name"], )
        
        print("Python object")
        print(my_dataset)

        my_dataset_pb = my_dataset.to_pb()

        print("Protocol buffer message")
        print(my_dataset_pb)

    def test_Dataset_json(self):
        my_dataset_json = {
          "Dataset" : {
            "ArrayBase" : "Some arraybase.",
            "DataSetName" : ["dsn1", "dsn2"],
            "DefaultVariableSchemeReference" : {},
            "IdentifyingVariableReference" : {},
            "ItemSet" : "An item set.",
            "RecordSet" : "A record set.",
            "VariableSet" : "A variable set."
          }
        }

        print("JSON Dataset message")
        print(validate(instance=my_dataset_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
