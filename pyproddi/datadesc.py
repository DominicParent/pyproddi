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

class VariableStatistics:
    def __init__(self, filteredCategoryStatistics, 
                 managedMissingValuesRepresentation, standardWeightReference,
                 summaryStatistic, totalResponses, 
                 unfilteredCategoryStatistics, variableReference,
                 weightVariableReference):
        self.filteredCategoryStatistics = []
        self.filteredCategoryStatistics.add(filteredCategoryStatistics)
        self.managedMissingValuesRepresentation = managedMissingValuesRepresentation
        self.standardWeightReference = standardWeightReference
        self.summaryStatistic = []
        self.summaryStatistic.add(summaryStatistic)
        self.totalResponses = totalResponses
        self.unfilteredCategoryStatistics = []
        self.unfilteredCategoryStatistics.add(unfilteredCategoryStatistics)
        self.variableReference = variableReference
        self.weightVariableReference = weightVariableReference

class VariableGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, subject, typeOfVariableGroup, universeReference,
                 variableGroupName, variableGroupReference, variableReference):
        self.conceptReference = conceptReference
        self.description = description
        self.isOrdered = isOrdered
        self.keyword = []
        self.keyword.add(keyword)
        self.label = []
        self.label.add(label)
        self.subject = []
        self.subject.add(subject)
        self.typeOfVariableGroup = typeOfVariableGroup
        self.universeReference = universeReference
        self.variableGroupName = []
        self.variableGroupName.add(variableGroupName)
        self.variableGroupReference = variableGroupReference
        self.variableReference = variableReference

class VariableScheme:
    def __init__(self, description, label, variableGroupReference,
                 variableReference, variableSchemeName, 
                 variableSchemeReference):
        self.description = description)
        self.label = []
        self.label.add(label)
        self.variableGroupReference = []
        self.variableGroupReference.add(variableGroupReference)
        self.variableReference = []
        self.variableReference.add(variableReference)
        self.variableSchemeName = []
        self.variableSchemeName.add(variableSchemeName)
        self.variableSchemeReference = []
        self.variableSchemeReference.add(variableSchemeReference)

class Dataset:
    def __init__(self, arrayBase, dataSetName, defaultVariableSchemeReference,
                 identifyingVariableReference, itemSet, recordSet, 
                 variableSet):
        self.arrayBase = arrayBase
        self.dataSetName = []
        self.dataSetName.add(dataSetName)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference
        self.identifyingVariableReference = identifyingVariableReference
        self.itemSet = itemSet
        seelf.recordSet = recordSet
        self.variableSet = variableSet

class RecordLayout:
    def __init__(self, arrayBase, characterSet, dataItem,
                 defaultVariableSchemeReference, namesOnFirstRow):
        self.arrayBase = arrayBase
        self.characterSet = characterSet
        self.dataItem = []
        self.dataItem.add(dataItem)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference
        self.namesOnFirstRow = namesOnFirstRow

class DataRelationship:
    def __init__(self, name):
        self.name = name

class ManagedMissingValuesRepresentation:
    def __init__(self, name):
        self.name = name

class InformationClassification:
    def __init__(self, name):
        self.name = name

class QualityStatement:
    def __init__(self, name):
        self.name = name

class PhysicalInstance:
    def __init__(self, byteOrder, citation, coverage, dataFileIdentification,
                 dataFileVersion, dataFingerprint, dataRelationshipReference,
                 defaultMissingValuesReference, grossFileStructure,
                 informationClassificationReference, proprietaryInfo,
                 qualityStatementReference, recordLayoutReference,
                 statisticalSummary, variableGroupReference):
        self.byteOrder = byteOrder
        self.citation = citation
        self.coverage = coverage
        self.dataFileIdentification = []
        self.dataFileIdentification.add(dataFileIdentification)
        self.dataFileVersion = dataFileVersion
        self.dataFingerprint = []
        self.dataFingerprint.add(dataFingerprint)
        self.dataRelationshipReference = []
        self.dataRelationshipReference.add(dataRelationshipReference)
        self.defaultMissingValuesReference = dfeaultMissingValuesReference
        self.grossFileStructure = grossFileStructure
        self.informationClassificationReference = []
        self.informationClassificationReference.add(informationClassificationReference)
        self.proprietaryInfo = proprietaryInfo
        self.qualityStatementReference = []
        self.qualityStatementReference.add(qualityStatementReference)
        self.recordLayoutReference = []
        self.recordLayoutReference.add(recordLayoutReference)
        self.statisticalSummary = statisticalSummary
        self.variableGroupReference = []
        self.variableGroupReference.add(variableGroupReference)

class RepresentedVariableGroup:
    def __init__(self, name):
        self.name = name

class RepresentedVariable:
    def __init__(self, name):
        self.name = name

class RepresentedVariableScheme:
    def __init__(self, description, label, representedVariableGroupReference,
                 representedVariableReference, representedVariableSchemeName,
                 representedVariableSchemeReference):
        self.description = description
        self.label = []
        self.label.add(label)
        self.representedVariableGroupReference = []
        self.representedVariableGroupReference.add(representedVariableGroupReference)
        self.representedVariableReference = []
        self.representedVariableReference.add(representedVariableReference)
        self.representedVariableSchemeName = []
        self.representedVariableSchemeName.add(representedVariableSchemeName)
        self.representedVariableSchemeReference = []
        self.representedVariableSchemeReference.add(representedVariableSchemeReference)

class CategoryScheme:
    def __init__(self, name):
        self.name = name

class CodeListScheme:
    def __init__(self, name):
        self.name = name

class ManagedRepresentationScheme:
    def __init__(self, name):
        self.name = name

class CubeScheme:
    def __init__(self, name):
        self.name = name

class LogicalProduct:
    def __init__(self, categorySchemeReference, codeListSchemeReference,
                 managedRepresentationSchemeReference, NCubeSchemeReference,
                 representedVariableSchemeReference, variableSchemeReference):
        self.categorySchemeReference = []
        self.categorySchemeReference.add(categorySchemeReference)
        self.codeListSchemeReference = []
        self.codeListSchemeReference.add(codeListSChemeReference)
        self.managedRepresentationSchemeReference = []
        self.managedRepresentationSchemeReference.add(managedRepresentationSchemeReference)
        self.nCubeSchemeReference = []
        self.nCubeSchemeReference.add(nCubeSchemeReference)
        self.representatedVariableSchemeReference = []
        self.representatedVariableSchemeReference.add(representedVariableSchemeReference)
        self.variableSchemeReference = []
        self.variableSchemeReference.add(variableSchemeReference)

class RecordLayoutGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, recordLayoutGroupName, recordLayoutGroupReference,
                 recordLayoutReference, subject, typeOfRecordLayoutGroup,
                 universeReference):
        self.conceptReference = conceptReference
        self.description = description
        self.isOrdered = isOrdered
        self.keyword = []
        self.keyword.add(keyword)
        self.label = []
        self.label.add(label)
        self.recordLayoutGroupName = []
        self.recordLayoutGroupName.add(recordLayoutGroupName)
        self.recordLayoutGroupReference = recordLayoutGroupReference
        self.recordLayoutReference = recordLayoutReference
        self.subject = []
        self.subject.add(subject)
        self.typeOfRecordLayoutGroup = typeOfRecordLayoutGroup
        self.universeReference = universeReference

class PhysicalStructure:
    def __init__(self, defaultDataType, defaultDecimalPositions,
                 defaultDecimalSeparator, defaultDelimiter, 
                 defaultDigitalGroupSeparator, description, fileFormat,
                 grossRecordStructure, label, physicalStructureName):
        self.defaultDataType = defaultDataType
        self.defaultDecimalPositions = defaultDecimalPositions
        self.defaultDecimalSeparator = defaultDecimalSeparator
        self.defaultDelimiter = defaultDelimiter
        self.defaultDigitGroupSeparator = defaultDigitGroupSeparator
        self.description = description
        self.fileFormat = fileFormat
        self.grossRecordStructure = []
        self.grossRecordStructure.add(grossRecordStructure)
        self.label = []
        self.label.add(label)
        self.physicalStructureName = []
        self.physicalStructureName.add(physicalStructureName)

class BaseRecordLayout:
    def __init__(self, endOfLineMarker, physicalStructureLinkReference,
                 textQualifier):
        self.endOfLineMarker = endOfLineMarker
        self.physicalStructureLinkReference = physicalStructureLinkReference
        self.textQualifier = textQualifier

class PhysicalStructureGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, physicalStructureGroupName, physicalStructureReference,
                 ssubject, typeOfPhysicalStructureGroup, universeReference):
        self.conceptReference = conceptReference
        self.description = description
        self.isOrdered = isOrdered
        self.keyword = []
        self.keyword.add(keyword)
        self.label = []
        self.label.add(label)
        self.physicalStructureGroupName = []
        self.physicalStructureGroupName.add(physicalStructureGroupName)
        self.physicalStructureReference = physicalStructureReference
        self.subject = []
        self.subject.add(subject)
        self.typeOfPHysicalStructureGroup = typeOfPHysicalStructureGroup
        self.universeReference = []
        self.universeReference.add(universeReference)

