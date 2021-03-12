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
import json
from jsonschema import Draft7Validator, validate

from pyproddi.io.protobuf import ddicdi_pb2
from pyproddi.ddicdi import Concept

class ConceptTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema:")
        print(self.schema)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_Concept(self):
        my_concept = Concept(conceptName=["test_name","test_name2","test_name3"], 
                             description="test_desc", isCharacteristic="True",
                             label=["test_label"])
        
        my_concept2 = Concept(conceptName=["test_name2","test_name2","test_name3"], 
                             description="test_desc", isCharacteristic="True",
                             label=["test_label"])
        
        my_concept3 = Concept(conceptName=["test_name3","test_name2","test_name3"], 
                             description="test_desc",excludesConceptReference=[my_concept, my_concept2], isCharacteristic="True",
                             label=["test_label"])
        
        print("Python object")
        print(my_concept)

        my_concept_pb = my_concept.to_pb()

        print("Protocol buffer message")
        print(my_concept_pb)

        my_concept3_pb = my_concept3.to_pb()

        print("Protocol buffer message with")
        print(my_concept3_pb)

    def test_Concept_json(self):
        
        jsonmessage = {
        "Concept" : {
            "ConceptName" : ["testname"],
            "Description" : "This is a description",
            "ExcludesConceptReference" : [],
            "IncludesConceptReference" : [],
            "IsCharacteristic" : "A characteristic",
            "Label" : [],
            "SimilarConcept" : [],
            "SubclassOfReference" : []
          }
        }

        jsonmessage2 = {
        "Concept" : {
            "ConceptName" : ["testname"],
            "Description" : "This is a description",
            "ExcludesConceptReference" : [jsonmessage],
            "IncludesConceptReference" : [jsonmessage],
            "IsCharacteristic" : "A characteristic",
            "Label" : [],
            "SimilarConcept" : [jsonmessage],
            "SubclassOfReference" : [jsonmessage]
          }
        }

        print("JSON Concept message")
        print(validate(instance=jsonmessage2, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
