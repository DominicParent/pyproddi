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

import uuid
from pyproddi.io.protobuf import dataset_pb2

class InstanceValue:
    def __init__(self, value):
        self.value = value

class DataPoint:
    def __init__(self, ival):
        self.ival = ival

class KeyMember:
    def __init__(self, ival):
        self.ival = ival

class Key:
    def __init__(self, keym):
        self.keym = []
        self.keym.append(keym)

    def addkeymember(self, keym):
        self.keym.append(keym)

class DataSet:
    def __init__(self, datap, key):
        self.datap = []
        self.key = []
        self.datap.append(datap)
        self.key.append(key)

    def addkey(self, key):
        self.key.append(key)

    def adddatapoint(self, datap):
        self.datap.append(datap)

    def converttopb(self):
        """
        Serialize a dataset python object into a protocol buffer.

        Returns
        -------
            An object containing a protocol buffer.
        """
        dspb = dataset_pb2.DataSet()
        
        for k in self.key:
            kpb = dspb.key.add()
            for km in k.keym:
                kmpb = kpb.keym.add()
                ivalpb = kmpb.ival
                ivalpb.value = km.ival.value

        for d in self.datap:
            dpb = dspb.datap.add()
            ivalpb = dpb.ival
            ivalpb.value = d.ival.value
            
        return dspb


    def serializetopb(self):
        """
        Serialize a dataset python object into a protocol buffer.

        Returns
        -------
            An object containing a protocol buffer in string serialized form.
        """

        return self.converttopb().SerializeToString()
