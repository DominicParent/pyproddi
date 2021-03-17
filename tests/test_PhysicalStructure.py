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
from pyproddi.ddicdi import PhysicalStructure

class PhysicalStructureTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_PhysicalStructure(self):
        my_ps = PhysicalStructure("ddt", "ddp", "dds", "dd", "ddgs", "desc",
                                  "df", ["grs"], ["label"], ["psn"])
        
        print("Python object")
        print(my_ps)

        my_ps_pb = my_ps.to_pb()

        print("Protocol buffer message")
        print(my_ps_pb)

    def test_PhysicalStructure_json(self):
        my_ps_json = {
          "PhysicalStructure" : {
              "DefaultDataType" : "ddt",
              "DefaultDecimalPositions" : "ddp",
              "DefaultDecimalSeparator" : "dds",
              "DefaultDelimiter" : "dd",
              "DefaultDigitGroupSeparator" : "ddgs",
              "Description" : "Some desc.",
              "FileFormat" : "ff",
              "GrossRecordStructure" : ["grs1", "grs2", "grs3", "grs4"],
              "Label" : ["lab1"],
              "PhysicalStructureName" : ["psn1", "psn2", "psn3", "psn4"]
          }
        }

        print("JSON PhysicalStructure message")
        print(validate(instance=my_ps_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
