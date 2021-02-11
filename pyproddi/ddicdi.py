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
from pyproddi.io.protobuf import ddicdi_pb2 # New protobuf model.

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

    def to_pb(self):
        pbm = ddicdi_pb2.Concept()
        
        for name in self.conceptName:
            pbname = pbm.Name.add()
            pbname = name

        pbm.Description = self.description
        
        for excon in self.excludesConceptReference:
            pbexcon = pbm.ExcludesConceptReference.add()
            pbexcon = excon.to_pb()

        for incon in self.includesConceptReference:
            pbincon = pbm.IncludeConceptReference.add()
            pbincon = incon.to_pb()

        pbm.IsCharacteristic = self.isCharacteristic

        for lab in self.label:
            pblabel = pbm.Label.add()
            pblabel = lab

        for simcon in self.similarConcept:
            pbsimcon = pbm.SimilarConcept.add()
            pbsimcon = simcon.to_pb()

        for subref in self.subclassOfReference:
            pbsubref = pbm.SubclassOfReference
            pbsubref = subref.to_pb()

        return pbm

# Filler class.
class CategoryScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.CategoryScheme()

        pbm.Name = self.name

        return pbm

# Filler class.
class UnitType:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.UnitType()
        pbm.Name = self.name

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.ConceptualVariable()

        pbm.CategorySchemeReference = self.categorySchemeReference.to_pb()
        pbm.ConceptReference = self.conceptReference.to_pb()
        
        for convarname in self.conceptualVariableName:
            pbconvarname = pbm.ConceptualVariableName.add()
            pbconvarname = convarname

        pbm.Description = self.description

        for lab in label:
            pblabel = pbm.Label.add()
            pblabel = lab

        pbm.UnitTypeReference = self.unitTypeReference.to_pb

        return pbm

# Filler class.
class ManagedRepresentation:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.ManagedRepresentation()

        pbm.Name = self.name

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariable()
        pbm.CategorySchemeReference = self.categorySchemeReference.to_pb()
        pbm.ConceptReference = self.conceptReference.to_pb()
        pbm.ConceptualVariableReference = self.conceptualVariableReference.to_pb()
        pbm.Description = self.description
        
        for lab in self.label:
            pblabel = pbm.Label.add()
            pblabel = lab

        for repvarname in self.representedVariableName:
            pbrepvarname = pbm.RepresentedVariableName.add()

        pbm.UnitTypeReference = self.unitTypereference.to_pb()
        pbm.ValueRepresentation = self.valueRepresentation
        pbm.ValueRepresentationReference = self.valueRepresentationReference.to_pb()

        return pbm

# Filler class.
class MeasurementItem:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.MeasurementItem()

        pbm.Name = self.name

        return pbm

# Filler class.
class Question:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.Question()
        pbm.Name = self.name

        return pbm

# Filler class.
class Universe:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.Universe()
        pbm.Name = self.name

        return pbm

# Filler class.
class Weighting:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.Weighting()
        pbm.Name = self.name

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.Variable()
        pbm.AnalysisUnit = self.analysisUnit
        pbm.ConceptReference = self.conceptReference.to_pb()
        pbm.ConceptualVariableReference = self.conceptualVariableReference.to_pb()
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.IsGeographic = self.isGeographic
        pbm.IsTemporal = self.isTemporal
        pbm.IsWeigh = self.isWeight
        
        for lab in self.label:
            pblabel = pbm.Label.add()
            pblabel = lab

        for mref in self.measurementReference:
            pbmref = pbm.MeasurementReference.add()
            pbmref = mref.to_pb()

        pbm.OutParameter = self.outParameter

        for q in self.question:
            pbq = pbm.Question.add()
            pbq = q.to_pb()

        pbm.RepresentedVariableReference = self.representedVariableReference.to_pb()
        pbm.SourceParameterReference = self.sourceParemeterReference
        pbm.SourceUnit = self.sourceUnit

        for svr in self.sourceVariableReference:
            psvr = pbm.SourceVariableReference.add()
            psvr = svr.to_pb()

        pbm.UnitTypeReference = self.unitTypeReference.to_pb()

        for uni in self.universe:
            puni = pbm.Universe.add()
            puni = uni.to_pb()

        pbm.VariableRepresentation = self.variableRepresentation
        pbm.WeightingProcessReference = self.weightingProcessReference.to_pb()

        return pbm

# Filler class.
class MissingValuesReference:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.MissingValuesReference()
        pbm.Name = self.name
        
        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.VariableStatistics()

        for fcs in self.filteredCategoryStatistics:
            pbfcs = pbm.FilteredCategoryStatistics.add()
            pbfcs = fcs

        pbm.ManagedMissingValuesRepresentation = self.managedMissingValuesRepresentation.to_pb()
        pbm.StandardWeightReference = self.standardWeightReference
        
        for sumstat in self.summaryStatistics:
            pbsumstat = pbm.SummaryStatistics.add()
            pbsumstat = sumstat

        pbm.TotalResponse = self.totalResponse

        for ucs in self.unfilteredCategoryStatistics:
            pbucs = pbm.UnfilteredCategoryStatistics.add()
            pbucs = ucs

        pbm.VariableReference = self.variableReference.to_pb()
        pbm.WeightVariableReference = self.weightVariableReference.to_pb()

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.VariableGroup()

        pbm.ConceptReference = self.conceptReference.to_pb()
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.add()
            pbkw = kw

        for lab in label:
            pblab = pbm.Label.add()
            pblab = lab

        for sub in subject:
            pbsub = pbm.Subject.add()
            pbsub = sub

        pbm.TypeOfVariableGroup = self.typeOfVariableGroup
        pbm.UniverseReference = self.universeReference.to_pb()

        for vgn in self.variableGroupName:
            pbvgn = pbm.VariableGroupName.add()
            pbvgn = vgn

        pbm.VariableGroupReference = self.variableGroupReference.to_pb()
        pbm.VariableReference = self.variableReference.to_pb()

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.VariableScheme()

        pbm.Description = self.description

        for lab in self.label:
            pblab = pbm.Label.add()
            pblab = lab

        for vgr in self.variableGroupReference:
            pbvgr = pbm.VariableGroupReference.add()
            pbvgr = vgr.to_pb()

        for vr in self.variableReference:
            pbvr = pbm.variableReference.add()
            pbvr = vr.to_pb()

        for vsn in self.variableSchemeName:
            pbvsn = pbm.VariableSchemeName.add()
            pbvsn = vsn

        for vsr in self.variableSchemeReference:
            pbvsr = pbm.VariableSchemeReference.add()
            pbvsr = vsr.to_pb()

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.Dataset()

        pbm.ArrayBase = self.arrayBase

        for dn in self.dataSetName:
            pbdn = pbm.DataSetName.add()
            pbdn = dn

        pbm.DefaultVariableSchemeReference = self.defaultVariableSchemeReference.to_pb()
        pbm.IdentifyingVariableReference = self.IdentifyingVariableReference.to_pb()
        pbm.ItemSet = self.itemSet
        pbm.RecordSet = self.recordSet
        pbm.VariableSet = self.variableSet

        return pbm

class RecordLayout:
    def __init__(self, arrayBase, characterSet, dataItem,
                 defaultVariableSchemeReference, namesOnFirstRow):
        self.arrayBase = arrayBase # String
        self.characterSet = characterSet # String
        self.dataItem = [] # List of String
        self.dataItem.add(dataItem)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.namesOnFirstRow = namesOnFirstRow # Boolean

    def to_pb(self):
        pbm = ddicdi_pb2.RecordLayout()

        pbm.ArrayBase = self.arrayBase
        pbm.CharacterSet = self.characterSet

        for di in self.dataItem:
            pbdi = pbm.DataItem.add()
            pbdi = di

        pbm.DefaultVariableSchemeReference = self.defaultVariableSchemeReference.to_pb()
        pbm.NamesOnFirstRow = self.namesOnFirstRow

        return pbm

# Filler class.
class DataRelationship:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.DataRelationship()

        pbm.Name = self.name

        return pbm

# Filler class.
class ManagedMissingValuesRepresentation:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.ManagedMissingValuesRepresentation()

        pbm.Name = self.name

        return pbm

# Filler class.
class InformationClassification:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.InformationClassification()

        pbm.Name = self.name

        return pbm

# Filler class.
class QualityStatement:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.QualityStatement()

        pbm.Name = self.name

        return pbm

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

    def to_pb(self):
        pbm = ddicdi_pb2.PhysicalInstance()

        pbm.ByteOrder = self.byteOrder
        pbm.Citation = self.citation
        pbm.Coverage = self.coverage
        
        for dfi in self.dataFileIdentification:
            pbdfi = pbm.DataFileIdentification.add()
            pbdfi = dfi

        pbm.DataFileVersion = self.dataFileVersion

        for df in self.dataFingerprint:
            pbdf = pbm.DataFingerprint.add()
            pbdf = df

        for drf in self.dataRelationshipReference:
            pbdrf = pbm.DataFingerprint.add()
            pbdrf = drf.to_pb()

        pbm.DefaultMissingValuesReference = self.defaultMissingValuesReference.to_pb()
        pbm.GrossFileStructure = self.grossFileStructure

        for icr in self.informationClassificationReference:
            pbicr = pbm.InformationClassificationReference.add()
            pbicr = icr.to_pb()

        pbm.ProprietaryInfo = self.proprietaryInfo

        for qsr in self.qualityStatementReference:
            pbqsr = pbm.QualityStatementReference.add()
            pbqsr = qsr.to_pb()

        for rlf in self.recordLayoutReference:
            pbrlf = pbm.RecordLayoutReference.add()
            pbrlf = rlf.to_pb()

        pbm.StatisticalSummary = self.statisticalSummary

        for vgr in self.variableGroupReference:
            pbvgr = pbm.VariableGroupReference.add()
            pbvgr = vgr.to_pb()

        return pbm

# Filler class.
class RepresentedVariableGroup:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pass

# Filler class.
class RepresentedVariable:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pass

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

    def to_pb(self):
        pass

# Filler class.
class CategoryScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pass

# Filler class.
class CodeListScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pass

# Filler class.
class ManagedRepresentationScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pass

# Filler class.
class CubeScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pass

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

    def to_pb(self):
        pass

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

    def to_pb(self):
        pass

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

    def to_pb(self):
        pass

class BaseRecordLayout:
    def __init__(self, endOfLineMarker, physicalStructureLinkReference,
                 textQualifier):
        self.endOfLineMarker = endOfLineMarker # String
        self.physicalStructureLinkReference = physicalStructureLinkReference # PhysicalStructure
        self.textQualifier = textQualifier # String

    def to_pb(self):
        pass

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

    def to_pb(self):
        pass
