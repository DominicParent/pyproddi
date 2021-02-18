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
from pyproddi.ddicdi import (CategoryScheme, UnitType, ManagedRepresentation,
                             MeasurementItem, Question, Universe, Weighting,
                             MissingValuesReference, DataRelationship,
                             ManagedMissingValuesRepresentation,
                             InformationClassification, QualityStatement,
                             RepresentedVariableGroup, CodeListScheme, 
                             ManagedRepresentationScheme, CubeScheme)

class TestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Begining new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

    def test_CategoryScheme(self):
        my_catscheme = CategoryScheme('test_name')
        
        print("Python object")
        print(my_catscheme)

        my_catscheme_pb = my_catscheme.to_pb()

        print("Protocol buffer message")
        print(my_catscheme_pb)

    def test_UnitType(self):
        my_utype = UnitType('test_name')
        
        print("Python object")
        print(my_utype)

        my_utype_pb = my_utype.to_pb()

        print("Protocol buffer message")
        print(my_utype_pb)

    def test_ManagedRepresentation(self):
        my_manrep = ManagedRepresentation('test_name')
        
        print("Python object")
        print(my_manrep)

        my_manrep_pb = my_manrep.to_pb()

        print("Protocol buffer message")
        print(my_manrep_pb)

    def test_MeasurementItem(self):
        my_mitem = MeasurementItem('test_name')
        
        print("Python object")
        print(my_mitem)

        my_mitem_pb = my_mitem.to_pb()

        print("Protocol buffer message")
        print(my_mitem_pb)

    def test_Question(self):
        my_q = Question('test_name')
        
        print("Python object")
        print(my_q)

        my_q_pb = my_q.to_pb()

        print("Protocol buffer message")
        print(my_q_pb)

    def test_Universe(self):
        my_u = Universe('test_name')
        
        print("Python object")
        print(my_u)

        my_u_pb = my_u.to_pb()

        print("Protocol buffer message")
        print(my_u_pb)

    def test_Weighting(self):
        my_w = Weighting('test_name')
        
        print("Python object")
        print(my_w)

        my_w_pb = my_w.to_pb()

        print("Protocol buffer message")
        print(my_w_pb)

    def test_MissingValuesReference(self):
        my_mvr = MissingValuesReference('test_name')
        
        print("Python object")
        print(my_mvr)

        my_mvr_pb = my_mvr.to_pb()

        print("Protocol buffer message")
        print(my_mvr_pb)

    def test_DataRelationship(self):
        my_dr = DataRelationship('test_name')
        
        print("Python object")
        print(my_dr)

        my_dr_pb = my_dr.to_pb()

        print("Protocol buffer message")
        print(my_dr_pb)

    def test_ManagedMissingValuesRepresentation(self):
        my_mmvr = ManagedMissingValuesRepresentation('test_name')
        
        print("Python object")
        print(my_mmvr)

        my_mmvr_pb = my_mmvr.to_pb()

        print("Protocol buffer message")
        print(my_mmvr_pb)

    def test_InformationClassification(self):
        my_ic = InformationClassification('test_name')
        
        print("Python object")
        print(my_ic)

        my_ic_pb = my_ic.to_pb()

        print("Protocol buffer message")
        print(my_ic_pb)

    def test_QualityStatement(self):
        my_qs = QualityStatement('test_name')
        
        print("Python object")
        print(my_qs)

        my_qs_pb = my_qs.to_pb()

        print("Protocol buffer message")
        print(my_qs_pb)

    def test_RepresentedVariableGroup(self):
        my_rvg = RepresentedVariableGroup('test_name')
        
        print("Python object")
        print(my_rvg)

        my_rvg_pb = my_rvg.to_pb()

        print("Protocol buffer message")
        print(my_rvg_pb)

    def test_CodeListScheme(self):
        my_cls = CodeListScheme('test_name')
        
        print("Python object")
        print(my_cls)

        my_cls_pb = my_cls.to_pb()

        print("Protocol buffer message")
        print(my_cls_pb)

    def test_ManagedRepresentationScheme(self):
        my_mrs = ManagedRepresentationScheme('test_name')
        
        print("Python object")
        print(my_mrs)

        my_mrs_pb = my_mrs.to_pb()

        print("Protocol buffer message")
        print(my_mrs_pb)

    def test_CubeScheme(self):
        my_cs = CubeScheme('test_name')
        
        print("Python object")
        print(my_cs)

        my_cs_pb = my_cs.to_pb()

        print("Protocol buffer message")
        print(my_cs_pb)

if __name__ == "__main__":
    unittest.main()
