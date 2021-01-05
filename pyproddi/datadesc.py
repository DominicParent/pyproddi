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
# from pyproddi.io.protobuf import datadesc_pb2 # New protobuf model.

class Concept:
    def __init__(self, conceptName, description, excludesConceptReference,
                 includesConceptReference, isCharacteristic, label,
                 similarConcept, subClassOfReference):
        self.conceptName = []
        self.conceptName.append(conceptName)
        self.description = description
        self.excludesConceptReference = []
        self.excludesConceptReference.add(excludesConceptReference)
        self.includesConceptReference = []
        self.includesConceptReference.add(includesConceptReference)
        self.isCharacteristic = isCharacteristic
        self.label = []
        self.label.add(label)
        self.similarConcept = []
        self.similarConcept.add(similarConcept)
        self.subclassOfReference = []
        self.subclassOfReference.add(subclassOfReference)

class CategoryScheme:
    def __init__(self, name):
        self.name = name

class UnitType:
    def __init__(self, name):
        self.name = name

class ConceptualVariable:
    def __init__(self, categorySchemeReference, conceptReference,
                 conceptualVariableName, description, label,
                 unitTypeReference):
        self.categorySchemeReference = categorySchemeReference
        self.conceptReference = conceptReference
        self.conceptualVariableName = []
        self.conceptualVariableName.add(conceptualVariableName)
        self.description = description
        self.label = []
        self.label.add(label)
        self.unitTypeReference = []
        self.unitTypeReference.add(unityTypeReference)

class ManagedRepresentation:
    def __init__(self, name):
        self.name = name

class RepresentedVariable:
    def __init__(self, categorySchemeReference, conceptReference,
                 conceptualVariableReference, description, label,
                 representedVariableName, unitTypeReference,
                 valueRepresentation, valueRepresentationReference):
        self.categorySchemeReference = categorySchemeReference
        self.conceptReference = conceptReference
        self.conceptualVariableReference = conceptualVariableReference
        self.description = description
        self.label = []
        self.label.add(label)
        self.representedVariableName = []
        self.representedVariableName.add(representedVariableName)
        se
        self.conceptReference = conceptReference
        self.conceptualVariableName = []
        self.conceptualVariableName.add(conceptualVariableName)
        self.description = description
        self.label = []
        self.label.add(label)
        self.unitTypeReference = []
        self.unitTypeReference.add(unityTypeReference)

class ManagedRepresentation:
    def __init__(self, name):
        self.name = name

class RepresentedVariable:
    def __init__(self, categorySchemeReference, conceptReference,
                 conceptualVariableReference, description, label,
                 representedVariableName, unitTypeReference,
                 valueRepresentation, valueRepresentationReference):
        self.categorySchemeReference = categorySchemeReference
        self.conceptReference = conceptReference
        self.conceptualVariableReference = conceptualVariableReference
        self.description = description
        self.label = []
        self.label.add(label)
        self.representedVariableName = []
        self.representedVariableName.add(representedVariableName)
        self.unitTypeReference = unitTypeReference
        self.valueRepresentation = valueRepresentation
        self.valueRepresentationReference = valueRepresentationReference

class MeasurementItem:
    def __init__(self, name):
        self.name = name

class Question:
    def __init__(self, name):
        self.name = name

class Universe:
    def __init__(self, name):
        self.name = name

class Weighting:
    def __init__(self, name):
        self.name = name

class Variable:
    def __init__(self, analysisUnit, conceptReference,
                 conceptualVariableReference, description, embargoReference,
                 isGeographic, isTemporal, isWeight, label,
                 measurementReference,outParameter, questionReference,
                 representedVariableReference, sourceParameterReference,
                 sourceUnit, sourceVariableReference, unitTypeReference,
                 universeReference, variableRepresentation,
                 weightingProcessReference):
        self.analysisUnit = analysisUnit
        self.conceptReference = conceptReference
        self.conceptualVariableReference = conceptualVariableReference
        self.description = description
        self.embargoReference = embargoReference
        self.isGeographic = isGeographic
        self.isTemporal = isTemporal
        self.isWeight = isWeight
        self.label = []
        self.label.add(label)
        self.measurementReference = []
        self.measurementReference.add(measurementReference)
        self.outParameter = outParameter
        self.questionReference = []
        self.questionReference.add(questionReference)
        self.representedVariableReference = representedVariableReference
        self.sourceParameterReference = sourceParameterReference
        self.sourceUnit = sourceUnit
        self.sourceVariableReference = []
        self.sourceVariableReference.add(sourceVariableReference)
        self.unitTypeReference = unitTypeReference
        self.universeReference = []
        self.universeReference.add(universeReference)
        self.variableRepresentation = variableRepresentation
        self.weightingProcessReference = weightingProcessReference

class MissingValuesReference:
    def __init__(self, name):
        self.name = name
