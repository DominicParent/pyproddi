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
from pyproddi.ddicdi import (Concept, DataRelationship,
                             ManagedMissingValuesRepresentation,
                             InformationClassification, QualityStatement,
                             VariableScheme, VariableGroup, Variable,
                             RecordLayout, Universe, PhysicalInstance)

class PhysicalInstanceTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

        self.concept = Concept(conceptName=["test name"], description="desc",
                               isCharacteristic="False", label=["label"])
        self.dr = DataRelationship("Data Relationship")
        self.mmvr = ManagedMissingValuesRepresentation("MMVR")
        self.ic = InformationClassification("Information Classification")
        self.qs = QualityStatement("Quality Statement")
        self.vs = VariableScheme("desc", ["label"], [VariableGroup()],
                                 [Variable()], ["var scheme name"], [])
        self.rl = RecordLayout("arraybase", "char set", ["data item list"],
                               self.vs, False)
        self.vg = VariableGroup(self.concept, "desc", True, ["keyword"],
                                ["label"], ["subject"], "var type",
                                Universe("uni name"), ["var group name"],
                                VariableGroup(), Variable())

        with open("pyproddi/io/json/ddicdi.json") as f:
            self.schema = json.load(f)

        print("Schema validator result:")
        print(Draft7Validator.check_schema(self.schema))

    def test_PhysicalInstance(self):
        my_pi = PhysicalInstance("byteorder", "citation", "coverage", ["dfi"],
                                 "dfv", ["df"], [self.dr], self.mmvr, "gfs",
                                 [self.ic], False, [self.qs], [self.rl],
                                 "stat sum", [self.vg])
        
        print("Python object")
        print(my_pi)

        my_pi_pb = my_pi.to_pb()

        print("Protocol buffer message")
        print(my_pi_pb)

    def test_PhysicalInstance_json(self):
        my_pi_json = {
        "PhysicalInstance" : {
            "ByteOrder" : "little endian",
            "Citation" : "Some citation",
            "Coverage" : "90%",
            "DataFileIdentification" : ["dfi1", "dfi2"],
            "DataFileVersion" : "v9.0.0",
            "DataFingerprint" : ["df1", "df2"],
            "DataRelationshipReference" : [],
            "DefaultMissingValuesReference" : {},
            "GrossFileStructure" : "posix compliant",
            "InformationClassificationReference" : [],
            "ProprietaryInfo" : False,
            "QualityStatementReference": [],
            "RecordLayoutReference" : [],
            "StatisticalSummary" : "A stats summary.",
            "VariableGroupReference" : []
          }
        }

        print("JSON PhysicalInstance message")
        print(validate(instance=my_pi_json, schema=self.schema))

if __name__ == "__main__":
    unittest.main()
