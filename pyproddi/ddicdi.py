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
    def __init__(self, conceptName=[], description="", excludesConceptReference=[],
                 includesConceptReference=[], isCharacteristic=None, label=[],
                 similarConcept=[], subclassOfReference=[]):
        self.conceptName = conceptName # List of Concept
        self.description = description # String
        self.excludesConceptReference = excludesConceptReference # List of Concept
        self.includesConceptReference = includesConceptReference # List of Concept
        self.isCharacteristic = isCharacteristic # Boolean
        self.label = label # List of String
        self.similarConcept = similarConcept # List of Concept
        self.subclassOfReference = subclassOfReference # List of Concept

    def to_pb(self):
        if(self is None):
            return None

        pbm = ddicdi_pb2.Concept()
        
        for name in self.conceptName:
            pbname = pbm.ConceptName.append(name)

        pbm.Description = self.description
        
        for excon in self.excludesConceptReference:
            if(excon is not None):
                pbexcon = pbm.ExcludesConceptReference.append(excon.to_pb())

        for incon in self.includesConceptReference:
            if(incon is not None):
                pbincon = pbm.IncludeConceptReference.append(incon.to_pb())

        pbm.IsCharacteristic = self.isCharacteristic

        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        for simcon in self.similarConcept:
            if(simcon is not None):
                pbsimcon = pbm.SimilarConcept.append(simcon.to_pb())

        for subref in self.subclassOfReference:
            if(subref is not None):
                pbsubref = pbm.SubclassOfReference.append(subref.to_pb())

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
        self.conceptualVariableName.append(conceptualVariableName)
        self.description = description # String
        self.label = [] # List of String
        self.label.append(label)
        self.unitTypeReference = [] # List of UnitType
        self.unitTypeReference.append(unityTypeReference)

    def to_pb(self):
        pbm = ddicdi_pb2.ConceptualVariable()

        if(self.categorySchemeReference is not None):
            pbm.CategorySchemeReference = self.categorySchemeReference.to_pb()
        if(self.conceptReference is not None):
            pbm.ConceptReference = self.conceptReference.to_pb()
        
        for convarname in self.conceptualVariableName:
            pbconvarname = pbm.ConceptualVariableName.append(convarname)

        pbm.Description = self.description

        for lab in label:
            pblabel = pbm.Label.append(lab)

        if(self.unitTypeReference is not None):
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
        self.label.append(label)
        self.representedVariableName = [] # List of String
        self.representedVariableName.append(representedVariableName)
        self.unitTypeReference = unitTypeReference # UnitType
        self.valueRepresentation = valueRepresentation # String
        self.valueRepresentationReference = valueRepresentationReference # ManagedRepresentation

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariable()
        if(self.categorySchemeReference is not None):
            pbm.CategorySchemeReference = self.categorySchemeReference.to_pb()
        if(self.conceptReference is not None):
            pbm.ConceptReference = self.conceptReference.to_pb()
        if(self.conceptualVariableReference is not None):
            pbm.ConceptualVariableReference = self.conceptualVariableReference.to_pb()
        pbm.Description = self.description
        
        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        for repvarname in self.representedVariableName:
            pbrepvarname = pbm.RepresentedVariableName.append(repvarname)
        if(self.unitTypeReference is not None):
            pbm.UnitTypeReference = self.unitTypeReference.to_pb()
        pbm.ValueRepresentation = self.valueRepresentation
        if(self.valueRepresentationReference is not None):
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
        self.label.append(label)
        self.measurementReference = [] # List of String
        self.measurementReference.append(measurementReference)
        self.outParameter = outParameter # String
        self.questionReference = [] # List of Question
        self.questionReference.append(questionReference)
        self.representedVariableReference = representedVariableReference # RepresentedVariable
        self.sourceParameterReference = sourceParameterReference # String
        self.sourceUnit = sourceUnit # String
        self.sourceVariableReference = [] # List of Variable
        self.sourceVariableReference.append(sourceVariableReference)
        self.unitTypeReference = unitTypeReference # UnitType
        self.universeReference = [] # List of Universe
        self.universeReference.append(universeReference)
        self.variableRepresentation = variableRepresentation # String
        self.weightingProcessReference = weightingProcessReference # Weighting

    def to_pb(self):
        pbm = ddicdi_pb2.Variable()
        pbm.AnalysisUnit = self.analysisUnit
        if(self.conceptReference is not None):
            pbm.ConceptReference = self.conceptReference.to_pb()
        if(self.conceptualVariableReference is not None):
            pbm.ConceptualVariableReference = self.conceptualVariableReference.to_pb()
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.IsGeographic = self.isGeographic
        pbm.IsTemporal = self.isTemporal
        pbm.IsWeigh = self.isWeight
        
        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        for mref in self.measurementReference:
            if(mref is not None):
                pbmref = pbm.MeasurementReference.append(mref.to_pb())

        pbm.OutParameter = self.outParameter

        for q in self.question:
            if(q is not None):
                pbq = pbm.Question.append(q.to_pb())

        if(self.representedVariableReference is not None):
            pbm.RepresentedVariableReference = self.representedVariableReference.to_pb()
        pbm.SourceParameterReference = self.sourceParemeterReference
        pbm.SourceUnit = self.sourceUnit

        for svr in self.sourceVariableReference:
            if(svr is not None):
                psvr = pbm.SourceVariableReference.append(svr.to_pb())

        if(self.unitTypeReference is not None):
            pbm.UnitTypeReference = self.unitTypeReference.to_pb()

        for uni in self.universe:
            if(uni is not None):
                puni = pbm.Universe.append(uni.to_pb())

        pbm.VariableRepresentation = self.variableRepresentation
        if(self.weightingProcessReference is not None):
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
        self.filteredCategoryStatistics.append(filteredCategoryStatistics)
        self.managedMissingValuesRepresentation = managedMissingValuesRepresentation # MissingValuesReference
        self.standardWeightReference = standardWeightReference # String
        self.summaryStatistic = [] # List of String
        self.summaryStatistic.append(summaryStatistic)
        self.totalResponses = totalResponses # String
        self.unfilteredCategoryStatistics = [] # List of String
        self.unfilteredCategoryStatistics.append(unfilteredCategoryStatistics)
        self.variableReference = variableReference # Variable
        self.weightVariableReference = weightVariableReference # Variable

    def to_pb(self):
        pbm = ddicdi_pb2.VariableStatistics()

        for fcs in self.filteredCategoryStatistics:
            if(fcs is not None):
                pbfcs = pbm.FilteredCategoryStatistics.append(fcs)

        if(self.managedMIssingValuesRepresentation is not None):
            pbm.ManagedMissingValuesRepresentation = self.managedMissingValuesRepresentation.to_pb()
        pbm.StandardWeightReference = self.standardWeightReference
        
        for sumstat in self.summaryStatistics:
            pbsumstat = pbm.SummaryStatistics.append(sumstat)

        pbm.TotalResponse = self.totalResponse

        for ucs in self.unfilteredCategoryStatistics:
            pbucs = pbm.UnfilteredCategoryStatistics.append(ucs)

        if(self.variableReference is not None):
            pbm.VariableReference = self.variableReference.to_pb()
        if(self.weightVariableReference is not None):
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
        self.keyword.append(keyword)
        self.label = [] # List of String
        self.label.append(label)
        self.subject = [] # List of String
        self.subject.append(subject)
        self.typeOfVariableGroup = typeOfVariableGroup # String
        self.universeReference = universeReference # Universe
        self.variableGroupName = [] # List of String
        self.variableGroupName.append(variableGroupName)
        self.variableGroupReference = variableGroupReference # VariableGroup
        self.variableReference = variableReference # Variable

    def to_pb(self):
        pbm = ddicdi_pb2.VariableGroup()

        if(self.conceptReference is not None):
            pbm.ConceptReference = self.conceptReference.to_pb()
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in label:
            pblab = pbm.Label.append(lab)

        for sub in subject:
            pbsub = pbm.Subject.append(sub)

        pbm.TypeOfVariableGroup = self.typeOfVariableGroup
        if(self.universeReference is not None):
            pbm.UniverseReference = self.universeReference.to_pb()

        for vgn in self.variableGroupName:
            pbvgn = pbm.VariableGroupName.append(vgn)

        if(self.variableGroupReference is not None):
            pbm.VariableGroupReference = self.variableGroupReference.to_pb()
        if(self.variableReference is not None):
            pbm.VariableReference = self.variableReference.to_pb()

        return pbm

class VariableScheme:
    def __init__(self, description, label, variableGroupReference,
                 variableReference, variableSchemeName, 
                 variableSchemeReference):
        self.description = description # String
        self.label = [] # List of String
        self.label.append(label)
        self.variableGroupReference = [] # List of VariableGroup
        self.variableGroupReference.append(variableGroupReference)
        self.variableReference = [] # List of Variable
        self.variableReference.append(variableReference)
        self.variableSchemeName = [] # List of String
        self.variableSchemeName.append(variableSchemeName)
        self.variableSchemeReference = [] # List of VariableScheme
        self.variableSchemeReference.append(variableSchemeReference)

    def to_pb(self):
        pbm = ddicdi_pb2.VariableScheme()

        pbm.Description = self.description

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for vgr in self.variableGroupReference:
            if(vgr is not None):
                pbvgr = pbm.VariableGroupReference.append(vgr.to_pb())

        for vr in self.variableReference:
            if(vr is not None):
                pbvr = pbm.variableReference.append(vr.to_pb())

        for vsn in self.variableSchemeName:
            pbvsn = pbm.VariableSchemeName.append(vsn)

        for vsr in self.variableSchemeReference:
            if(vsr is not None):
                pbvsr = pbm.VariableSchemeReference.append(vsr.to_pb())

        return pbm

class Dataset:
    def __init__(self, arrayBase, dataSetName, defaultVariableSchemeReference,
                 identifyingVariableReference, itemSet, recordSet, 
                 variableSet):
        self.arrayBase = arrayBase # String
        self.dataSetName = [] # List of String
        self.dataSetName.append(dataSetName)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.identifyingVariableReference = identifyingVariableReference # Variable
        self.itemSet = itemSet # String
        seelf.recordSet = recordSet # String
        self.variableSet = variableSet # String

    def to_pb(self):
        pbm = ddicdi_pb2.Dataset()

        pbm.ArrayBase = self.arrayBase

        for dn in self.dataSetName:
            pbdn = pbm.DataSetName.append(dn)

        if(self.defaultVariableSChemeReference is not None):
            pbm.DefaultVariableSchemeReference = self.defaultVariableSchemeReference.to_pb()
        if(self.identifyingVariableReference is not None):
            pbm.IdentifyingVariableReference = self.identifyingVariableReference.to_pb()
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
        self.dataItem.append(dataItem)
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.namesOnFirstRow = namesOnFirstRow # Boolean

    def to_pb(self):
        pbm = ddicdi_pb2.RecordLayout()

        pbm.ArrayBase = self.arrayBase
        pbm.CharacterSet = self.characterSet

        for di in self.dataItem:
            pbdi = pbm.DataItem.append(di)

        if(self.defaultVariableSChemeReference is not None):
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
        self.dataFileIdentification.append(dataFileIdentification)
        self.dataFileVersion = dataFileVersion # String
        self.dataFingerprint = [] # List of String
        self.dataFingerprint.append(dataFingerprint)
        self.dataRelationshipReference = [] # List of DataRelationship
        self.dataRelationshipReference.append(dataRelationshipReference)
        self.defaultMissingValuesReference = defaultMissingValuesReference # ManagedMissingValuesRepresentation
        self.grossFileStructure = grossFileStructure # String
        self.informationClassificationReference = [] # List of InformationClassification
        self.informationClassificationReference.append(informationClassificationReference)
        self.proprietaryInfo = proprietaryInfo # Boolean
        self.qualityStatementReference = [] # List of QualityStatement
        self.qualityStatementReference.append(qualityStatementReference)
        self.recordLayoutReference = [] # List of RecordLayout
        self.recordLayoutReference.append(recordLayoutReference)
        self.statisticalSummary = statisticalSummary # String
        self.variableGroupReference = [] # List of VariableGroup
        self.variableGroupReference.append(variableGroupReference)

    def to_pb(self):
        pbm = ddicdi_pb2.PhysicalInstance()

        pbm.ByteOrder = self.byteOrder
        pbm.Citation = self.citation
        pbm.Coverage = self.coverage
        
        for dfi in self.dataFileIdentification:
            pbdfi = pbm.DataFileIdentification.append(dfi)

        pbm.DataFileVersion = self.dataFileVersion

        for df in self.dataFingerprint:
            pbdf = pbm.DataFingerprint.append(df)

        for drf in self.dataRelationshipReference:
            if(drf is not None):
                pbdrf = pbm.DataFingerprint.append(drf.to_pb())

        if(self.defaultMissingValuesReference is not None):
            pbm.DefaultMissingValuesReference = self.defaultMissingValuesReference.to_pb()
        pbm.GrossFileStructure = self.grossFileStructure

        for icr in self.informationClassificationReference:
            if(icr is not None):
                pbicr = pbm.InformationClassificationReference.append(icr.to_pb())

        pbm.ProprietaryInfo = self.proprietaryInfo

        for qsr in self.qualityStatementReference:
            if(qsr is not None):
                pbqsr = pbm.QualityStatementReference.append(qsr.to_pb())

        for rlf in self.recordLayoutReference:
            if(rlf is not None):
                pbrlf = pbm.RecordLayoutReference.append(rlf.to_pb())

        pbm.StatisticalSummary = self.statisticalSummary

        for vgr in self.variableGroupReference:
            if(vgr is not None):
                pbvgr = pbm.VariableGroupReference.append(vgr.to_pb())

        return pbm

# Filler class.
class RepresentedVariableGroup:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariableGroup()
        pbm.Name = self.name

        return pbm

# Filler class.
class RepresentedVariable:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariable()
        pbm.Name = self.name

        return pbm

class RepresentedVariableScheme:
    def __init__(self, description, label, representedVariableGroupReference,
                 representedVariableReference, representedVariableSchemeName,
                 representedVariableSchemeReference):
        self.description = description # String
        self.label = [] # List of String
        self.label.append(label)
        self.representedVariableGroupReference = [] # List of RepresentedVariableGroup
        self.representedVariableGroupReference.append(representedVariableGroupReference)
        self.representedVariableReference = [] # List of RepresentedVariable
        self.representedVariableReference.append(representedVariableReference)
        self.representedVariableSchemeName = [] # List of String
        self.representedVariableSchemeName.append(representedVariableSchemeName)
        self.representedVariableSchemeReference = [] # List of RepresentedVariableScheme
        self.representedVariableSchemeReference.append(representedVariableSchemeReference)

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariableScheme()

        pbm.Description = self.description

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for rvgr in self.representedVariableGroupReference:
            if(rvgr is not None):
                pbrvgr = pbm.RepresentedVariableGroupReference.append(rvgr.to_pb())

        for rvr in self.representedVariableReference:
            if(rvr is not None):
                pbrvr = pbm.RepresentedVariableReference.append(rvr.to_pb())

        for rvsn in self.representedVariableSchemeName:
            pbrvsn = pbm.RepresentedVariableSchemeName.append(rvsn)

        for rvsr in self.representedVariableSchemeReference:
            if(rvsr is not None):
                pbrvsr = pbm.RepresentedVariableSchemeReference.append(rvsr.to_pb())

        return pbm

# Filler class.
class CodeListScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.CodeListScheme()
        pbm.Name = self.name

        return pbm

# Filler class.
class ManagedRepresentationScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.ManagedRepresentationScheme()
        pbm.Name = self.name

        return pbm

# Filler class.
class CubeScheme:
    def __init__(self, name):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.CubeScheme()
        pbm.Name = self.name

        return pbm

class LogicalProduct:
    def __init__(self, categorySchemeReference, codeListSchemeReference,
                 managedRepresentationSchemeReference, NCubeSchemeReference,
                 representedVariableSchemeReference, variableSchemeReference):
        self.categorySchemeReference = [] # List of CategoryScheme
        self.categorySchemeReference.append(categorySchemeReference)
        self.codeListSchemeReference = [] # List of CodeListScheme
        self.codeListSchemeReference.append(codeListSChemeReference)
        self.managedRepresentationSchemeReference = [] # List of ManagedRepresetnationScheme
        self.managedRepresentationSchemeReference.append(managedRepresentationSchemeReference)
        self.nCubeSchemeReference = [] # List of CubeScheme
        self.nCubeSchemeReference.append(nCubeSchemeReference)
        self.representatedVariableSchemeReference = [] # List of RepresentedVariableScheme
        self.representatedVariableSchemeReference.append(representedVariableSchemeReference)
        self.variableSchemeReference = [] # List of VariableScheme
        self.variableSchemeReference.append(variableSchemeReference)

    def to_pb(self):
        pbm = ddicdi_pb2.LogicalProduct()

        for csr in self.categorySchemeReference:
            if(csr is not None):
                pbcsr = pbm.CategorySchemeReference.append(csr.to_pb())

        for clsr in self.codeListSchemeReference:
            if(clsr is not None):
                pbclsr = pbm.CodeListSchemeReference.append(clsr.to_pb())

        for mrsr in self.managedRepresentationSchemeReference:
            if(mrsr is not None):
                pbmrsr = pbm.ManagedRepresentationSchemeReference.append(clsr.to_pb())

        for ncsr in self.nCubeSchemeReference:
            if(ncsr is not None):
                pbncsr = pbm.NCubeSChemeReference.append(ncsr.to_pb())

        for rvsr in self.representedVariableSchemeReference:
            if(rvsr is not None):
                pbrvsr = pbm.RepresentedVariableSchemeReference.append(rvsr.to_pb())

        for vsr in self.variableSchemeReference:
            if(vsr is not None):
                pbvsr = pbm.VariableSchemeReference.append(vsr.to_pb())

        return pbm

class RecordLayoutGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, recordLayoutGroupName, recordLayoutGroupReference,
                 recordLayoutReference, subject, typeOfRecordLayoutGroup,
                 universeReference):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = [] # List of String
        self.keyword.append(keyword)
        self.label = [] # List of String
        self.label.append(label)
        self.recordLayoutGroupName = [] # List of String
        self.recordLayoutGroupName.append(recordLayoutGroupName)
        self.recordLayoutGroupReference = recordLayoutGroupReference # RecordLayoutGroup
        self.recordLayoutReference = recordLayoutReference # RecordLayout
        self.subject = [] # List of String
        self.subject.append(subject)
        self.typeOfRecordLayoutGroup = typeOfRecordLayoutGroup # String
        self.universeReference = universeReference # List of Universe

    def to_pb(self):
        pbm = ddicdi_pb2.RecordLayoutGroup()

        pbm.ConceptReference = self.conceptReference.to_pb()
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for rlgn in self.recordLayoutGroupName:
            pbrlgn = pbm.RecordLayoutGroupName.append(rlgn)

        if(self.recordLayoutGroupReference is not None):
            pbm.RecordLayoutGroupReference = self.recordLayoutGroupReference.to_pb()
        if(self.recordLayoutReference is not None):
            pbm.RecordLayoutReference = self.recordLayoutReference.to_pb()

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        pbm.TypeOfRecordLayoutGroup = self.typeOfRecordLayoutGroup

        for uni in self.universe:
            if(uni is not None):
                pbuni = pbm.Universe.append(uni.to_pb())

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
        self.grossRecordStructure.append(grossRecordStructure)
        self.label = [] # List of String
        self.label.append(label)
        self.physicalStructureName = [] # List of String
        self.physicalStructureName.append(physicalStructureName)

    def to_pb(self):
        pbm = ddicdi_pb2.PhysicalStructure()

        pbm.DefaultDataType = self.defaultDataType
        pbm.DefaultDecimalPositions = self.defaultDecimalPositions
        pbm.DefaultDecimalSeparator = self.defaultDecimalSeparator
        pbm.DefaultDelimiter = self.defaultDelimiter
        pbm.DefaultDigitGroupSeparator = self.defaultDigitGroupSeparator
        pbm.Description = self.description
        pbm.DefaultFileFormat = self.fileFormat
        
        for grs in self.grossRecordStructure:
            pbgrs = pbm.GrossRecordStructure.append(grs)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for psn in self.physicalStructureName:
            pbpsn = pbm.PhysicalStructureName.append(psn)

        return pbm

class BaseRecordLayout:
    def __init__(self, endOfLineMarker, physicalStructureLinkReference,
                 textQualifier):
        self.endOfLineMarker = endOfLineMarker # String
        self.physicalStructureLinkReference = physicalStructureLinkReference # PhysicalStructure
        self.textQualifier = textQualifier # String

    def to_pb(self):
        pbm = ddicdi_pb2.BaseRecordLayout()

        pbm.EndOfLineMarker = self.endOfLineMarker
        if(self.physicalStructureLinkReference is not None):
            pbm.PhysicalStructureLinkReference = self.physicalStructureLinkReference.to_pb()
        pbm.TextQualifier = self.textQualifier

        return pbm

class PhysicalStructureGroup:
    def __init__(self, conceptReference, description, isOrdered, keyword,
                 label, physicalStructureGroupName, physicalStructureReference,
                 ssubject, typeOfPhysicalStructureGroup, universeReference):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = [] # List of String
        self.keyword.append(keyword)
        self.label = [] # List of String
        self.label.append(label)
        self.physicalStructureGroupName = [] # List of String
        self.physicalStructureGroupName.append(physicalStructureGroupName)
        self.physicalStructureReference = physicalStructureReference # PhysicalSTructureGroup
        self.subject = [] # List of String
        self.subject.append(subject)
        self.typeOfPHysicalStructureGroup = typeOfPHysicalStructureGroup # String
        self.universeReference = [] # List of Universe
        self.universeReference.append(universeReference)

    def to_pb(self):
        pbm = ddicdi_pb2.PhysicalStructureGroup()

        if(self.conceptReference is not None):
            pbm.ConceptReference = self.conceptReference.to_pb()
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for psgn in self.physicalStructureGroupName:
            pbpsgn = pbm.PhysicalStructureGroupName.append(psgn)

        if(self.physicalStructureReference is not None):
            pbm.PhysicalStructureReference = self.physicalStructureReference.to_pb()

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        if(self.typeOfPhysicalStructureGroup is not None):
            pbm.TypeOfPhysicalStructureGroup = self.typeOfPhysicalStructureGroup.to_pb()

        for uni in self.universe:
            if(uni is not None):
                pbuni = pbm.Unviverse.append(uni.to_pb())
