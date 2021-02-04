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
        self.conceptName = [] # List of String
        self.conceptName.append(conceptName)
        self.description = description # String
        self.excludesConceptReference = [] # List of Concept
        self.excludesConceptReference.add(excludesConceptReference)
        self.includesConceptReference = [] # List of Concept
        self.includesConceptReference.add(includesConceptReference)
        self.isCharacteristic = isCharacteristic # Boolean
        self.label = [] # List of String
        self.label.add(label)
        self.similarConcept = [] # List of Concept
        self.similarConcept.add(similarConcept)
        self.subclassOfReference = [] # List of Concept
        self.subclassOfReference.add(subclassOfReference)

# Filler class.
class CategoryScheme:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class UnitType:
    def __init__(self, name):
        self.name = name # String

class ConceptualVariable:
    def __init__(self, categorySchemeReference, conceptReference,
                 conceptualVariableName, description, label,
                 unitTypeReference):
        self.categorySchemeReference = categorySchemeReference # CategoryScheme
        self.conceptReference = conceptReference # Concept
        self.conceptualVariableName = [] # List of String
        self.conceptualVariableName.add(conceptualVariableName)
        self.description = description # String
        self.label = [] # List of String
        self.label.add(label)
        self.unitTypeReference = [] # List of UnitType
        self.unitTypeReference.add(unityTypeReference)

# Filler class.
class ManagedRepresentation:
    def __init__(self, name):
        self.name = name # String

class RepresentedVariable:
    def __init__(self, categorySchemeReference, conceptReference,
                 conceptualVariableReference, description, label,
                 representedVariableName, unitTypeReference,
                 valueRepresentation, valueRepresentationReference):
        self.categorySchemeReference = categorySchemeReference # CategoryScheme
        self.conceptReference = conceptReference # Concept
        self.conceptualVariableReference = conceptualVariableReference # ConceptualVariable
        self.description = description # String
        self.label = [] # List of String
        self.label.add(label)
        self.representedVariableName = [] # List of String
        self.representedVariableName.add(representedVariableName)
        self.unitTypeReference = unitTypeReference # UnitType
        self.valueRepresentation = valueRepresentation # String
        self.valueRepresentationReference = valueRepresentationReference # ManagedRepresentation

# Filler class.
class MeasurementItem:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class Question:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class Universe:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class Weighting:
    def __init__(self, name):
        self.name = name # String

class Variable:
    def __init__(self, analysisUnit, conceptReference,
                 conceptualVariableReference, description, embargoReference,
                 isGeographic, isTemporal, isWeight, label,
                 measurementReference,outParameter, questionReference,
                 representedVariableReference, sourceParameterReference,
                 sourceUnit, sourceVariableReference, unitTypeReference,
                 universeReference, variableRepresentation,
                 weightingProcessReference):
        self.analysisUnit = analysisUnit # String
        self.conceptReference = conceptReference # Concept
        self.conceptualVariableReference = conceptualVariableReference # ConceptualVariable
        self.description = description # String
        self.embargoReference = embargoReference # String
        self.isGeographic = isGeographic # Boolean
        self.isTemporal = isTemporal # Boolean
        self.isWeight = isWeight # Boolean
        self.label = [] # List of String
        self.label.add(label)
        self.measurementReference = [] # List of String
        self.measurementReference.add(measurementReference)
        self.outParameter = outParameter # String
        self.questionReference = [] # List of Question
        self.questionReference.add(questionReference)
        self.representedVariableReference = representedVariableReference # RepresentedVariable
        self.sourceParameterReference = sourceParameterReference # String
        self.sourceUnit = sourceUnit # String
        self.sourceVariableReference = [] # List of Variable
        self.sourceVariableReference.add(sourceVariableReference)
        self.unitTypeReference = unitTypeReference # UnitType
        self.universeReference = [] # List of Universe
        self.universeReference.add(universeReference)
        self.variableRepresentation = variableRepresentation # String
        self.weightingProcessReference = weightingProcessReference # Weighting

# Filler class.
class MissingValuesReference:
    def __init__(self, name):
        self.name = name # String

class VariableStatistics:
    def __init__(self, filteredCategoryStatistics, 
                 managedMissingValuesRepresentation, standardWeightReference,
                 summaryStatistic, totalResponses, 
                 unfilteredCategoryStatistics, variableReference,
                 weightVariableReference):
        self.filteredCategoryStatistics = [] # List of String
        self.filteredCategoryStatistics.add(filteredCategoryStatistics)
        self.managedMissingValuesRepresentation = managedMissingValuesRepresentation # MissingValuesReference
        self.standardWeightReference = standardWeightReference # String
        self.summaryStatistic = [] # List of String
        self.summaryStatistic.add(summaryStatistic)
        self.totalResponses = totalResponses # String
        self.unfilteredCategoryStatistics = [] # List of String
        self.unfilteredCategoryStatistics.add(unfilteredCategoryStatistics)
        self.variableReference = variableReference # Variable
        self.weightVariableReference = weightVariableReference # Variable

class VariableGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, subject, typeOfVariableGroup, universeReference,
                 variableGroupName, variableGroupReference, variableReference):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = [] # List of String
        self.keyword.add(keyword)
        self.label = [] # List of String
        self.label.add(label)
        self.subject = [] # List of String
        self.subject.add(subject)
        self.typeOfVariableGroup = typeOfVariableGroup # String
        self.universeReference = universeReference # Universe
        self.variableGroupName = [] # List of String
        self.variableGroupName.add(variableGroupName)
        self.variableGroupReference = variableGroupReference # VariableGroup
        self.variableReference = variableReference # Variable

class VariableScheme:
    def __init__(self, description, label, variableGroupReference,
                 variableReference, variableSchemeName, 
                 variableSchemeReference):
        self.description = description # String
        self.label = [] # List of String
        self.label.add(label)
        self.variableGroupReference = [] # List of VariableGroup
        self.variableGroupReference.add(variableGroupReference)
        self.variableReference = [] # List of Variable
        self.variableReference.add(variableReference)
        self.variableSchemeName = [] # List of String
        self.variableSchemeName.add(variableSchemeName)
        self.variableSchemeReference = [] # List of VariableScheme
        self.variableSchemeReference.add(variableSchemeReference)

class Dataset:
    def __init__(self, arrayBase, dataSetName, defaultVariableSchemeReference,
                 identifyingVariableReference, itemSet, recordSet, 
                 variableSet):
        self.arrayBase = arrayBase # String
        self.dataSetName = [] # List of String
        self.dataSetName.add(dataSetName)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.identifyingVariableReference = identifyingVariableReference # Variable
        self.itemSet = itemSet # String
        seelf.recordSet = recordSet # String
        self.variableSet = variableSet # String

class RecordLayout:
    def __init__(self, arrayBase, characterSet, dataItem,
                 defaultVariableSchemeReference, namesOnFirstRow):
        self.arrayBase = arrayBase # String
        self.characterSet = characterSet # String
        self.dataItem = [] # List of String
        self.dataItem.add(dataItem)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.namesOnFirstRow = namesOnFirstRow # Boolean

# Filler class.
class DataRelationship:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class ManagedMissingValuesRepresentation:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class InformationClassification:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class QualityStatement:
    def __init__(self, name):
        self.name = name # String

class PhysicalInstance:
    def __init__(self, byteOrder, citation, coverage, dataFileIdentification,
                 dataFileVersion, dataFingerprint, dataRelationshipReference,
                 defaultMissingValuesReference, grossFileStructure,
                 informationClassificationReference, proprietaryInfo,
                 qualityStatementReference, recordLayoutReference,
                 statisticalSummary, variableGroupReference):
        self.byteOrder = byteOrder # String
        self.citation = citation # String
        self.coverage = coverage # String
        self.dataFileIdentification = [] # List of String
        self.dataFileIdentification.add(dataFileIdentification)
        self.dataFileVersion = dataFileVersion # String
        self.dataFingerprint = [] # List of String
        self.dataFingerprint.add(dataFingerprint)
        self.dataRelationshipReference = [] # List of DataRelationship
        self.dataRelationshipReference.add(dataRelationshipReference)
        self.defaultMissingValuesReference = defaultMissingValuesReference # ManagedMissingValuesRepresentation
        self.grossFileStructure = grossFileStructure # String
        self.informationClassificationReference = [] # List of InformationClassification
        self.informationClassificationReference.add(informationClassificationReference)
        self.proprietaryInfo = proprietaryInfo # Boolean
        self.qualityStatementReference = [] # List of QualityStatement
        self.qualityStatementReference.add(qualityStatementReference)
        self.recordLayoutReference = [] # List of RecordLayout
        self.recordLayoutReference.add(recordLayoutReference)
        self.statisticalSummary = statisticalSummary # String
        self.variableGroupReference = [] # List of VariableGroup
        self.variableGroupReference.add(variableGroupReference)

# Filler class.
class RepresentedVariableGroup:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class RepresentedVariable:
    def __init__(self, name):
        self.name = name # String

class RepresentedVariableScheme:
    def __init__(self, description, label, representedVariableGroupReference,
                 representedVariableReference, representedVariableSchemeName,
                 representedVariableSchemeReference):
        self.description = description # String
        self.label = [] # List of String
        self.label.add(label)
        self.representedVariableGroupReference = [] # List of RepresentedVariableGroup
        self.representedVariableGroupReference.add(representedVariableGroupReference)
        self.representedVariableReference = [] # List of RepresentedVariable
        self.representedVariableReference.add(representedVariableReference)
        self.representedVariableSchemeName = [] # List of String
        self.representedVariableSchemeName.add(representedVariableSchemeName)
        self.representedVariableSchemeReference = [] # List of RepresentedVariableScheme
        self.representedVariableSchemeReference.add(representedVariableSchemeReference)

# Filler class.
class CategoryScheme:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class CodeListScheme:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class ManagedRepresentationScheme:
    def __init__(self, name):
        self.name = name # String

# Filler class.
class CubeScheme:
    def __init__(self, name):
        self.name = name # String

class LogicalProduct:
    def __init__(self, categorySchemeReference, codeListSchemeReference,
                 managedRepresentationSchemeReference, NCubeSchemeReference,
                 representedVariableSchemeReference, variableSchemeReference):
        self.categorySchemeReference = [] # List of CategoryScheme
        self.categorySchemeReference.add(categorySchemeReference)
        self.codeListSchemeReference = [] # List of CodeListScheme
        self.codeListSchemeReference.add(codeListSChemeReference)
        self.managedRepresentationSchemeReference = [] # List of ManagedRepresetnationScheme
        self.managedRepresentationSchemeReference.add(managedRepresentationSchemeReference)
        self.nCubeSchemeReference = [] # List of CubeScheme
        self.nCubeSchemeReference.add(nCubeSchemeReference)
        self.representatedVariableSchemeReference = [] # List of RepresentedVariableScheme
        self.representatedVariableSchemeReference.add(representedVariableSchemeReference)
        self.variableSchemeReference = [] # List of VariableScheme
        self.variableSchemeReference.add(variableSchemeReference)

class RecordLayoutGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, recordLayoutGroupName, recordLayoutGroupReference,
                 recordLayoutReference, subject, typeOfRecordLayoutGroup,
                 universeReference):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = [] # List of String
        self.keyword.add(keyword)
        self.label = [] # List of String
        self.label.add(label)
        self.recordLayoutGroupName = [] # List of String
        self.recordLayoutGroupName.add(recordLayoutGroupName)
        self.recordLayoutGroupReference = recordLayoutGroupReference # RecordLayoutGroup
        self.recordLayoutReference = recordLayoutReference # RecordLayout
        self.subject = [] # List of String
        self.subject.add(subject)
        self.typeOfRecordLayoutGroup = typeOfRecordLayoutGroup # String
        self.universeReference = universeReference # List of Universe

class PhysicalStructure:
    def __init__(self, defaultDataType, defaultDecimalPositions,
                 defaultDecimalSeparator, defaultDelimiter, 
                 defaultDigitalGroupSeparator, description, fileFormat,
                 grossRecordStructure, label, physicalStructureName):
        self.defaultDataType = defaultDataType # String
        self.defaultDecimalPositions = defaultDecimalPositions # String
        self.defaultDecimalSeparator = defaultDecimalSeparator # String
        self.defaultDelimiter = defaultDelimiter # String
        self.defaultDigitGroupSeparator = defaultDigitGroupSeparator # String
        self.description = description # String
        self.fileFormat = fileFormat # String
        self.grossRecordStructure = [] # List of String
        self.grossRecordStructure.add(grossRecordStructure)
        self.label = [] # List of String
        self.label.add(label)
        self.physicalStructureName = [] # List of String
        self.physicalStructureName.add(physicalStructureName)

class BaseRecordLayout:
    def __init__(self, endOfLineMarker, physicalStructureLinkReference,
                 textQualifier):
        self.endOfLineMarker = endOfLineMarker # String
        self.physicalStructureLinkReference = physicalStructureLinkReference # PhysicalStructure
        self.textQualifier = textQualifier # String

class PhysicalStructureGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, physicalStructureGroupName, physicalStructureReference,
                 ssubject, typeOfPhysicalStructureGroup, universeReference):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = [] # List of String
        self.keyword.add(keyword)
        self.label = [] # List of String
        self.label.add(label)
        self.physicalStructureGroupName = [] # List of String
        self.physicalStructureGroupName.add(physicalStructureGroupName)
        self.physicalStructureReference = physicalStructureReference # PhysicalSTructureGroup
        self.subject = [] # List of String
        self.subject.add(subject)
        self.typeOfPHysicalStructureGroup = typeOfPHysicalStructureGroup # String
        self.universeReference = [] # List of Universe
        self.universeReference.add(universeReference)

