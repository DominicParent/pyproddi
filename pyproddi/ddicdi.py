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

    def add_to_pb(self, pbm):
        if(self is None):
            return None

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

# Filler class.
class CategoryScheme:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.CategoryScheme()

        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class UnitType:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.UnitType()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

class ConceptualVariable:
    def __init__(self, categorySchemeReference=None, conceptReference=None,
                 conceptualVariableName=[], description="", label=[],
                 unitTypeReference=[]):
        self.categorySchemeReference = categorySchemeReference # CategoryScheme
        self.conceptReference = conceptReference # Concept
        self.conceptualVariableName = conceptualVariableName # List of String
        self.description = description # String
        self.label = label # List of String
        self.unitTypeReference = unitTypeReference # List of UnitType

    def to_pb(self):
        pbm = ddicdi_pb2.ConceptualVariable()

        if(self.categorySchemeReference is not None):
            self.categorySchemeReference.add_to_pb(pbm.CategorySchemeReference)
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        
        for convarname in self.conceptualVariableName:
            pbconvarname = pbm.ConceptualVariableName.append(convarname)

        pbm.Description = self.description

        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        if(self.unitTypeReference is not None):
            self.unitTypeReference.add_to_pb(pbm.UnitTypeReference)

        return pbm

    def add_to_pb(self, pbm):
        if(self.categorySchemeReference is not None):
            self.categorySchemeReference.add_to_pb(pbm.CategorySchemeReference)
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        
        for convarname in self.conceptualVariableName:
            pbconvarname = pbm.ConceptualVariableName.append(convarname)

        pbm.Description = self.description

        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        if(self.unitTypeReference is not None):
            self.unitTypeReference.add_to_pb(pbm.UnitTypeReference)

# Filler class.
class ManagedRepresentation:
    def __init__(self, name = ""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.ManagedRepresentation()

        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

class RepresentedVariable:
    def __init__(self, categorySchemeReference=None, conceptReference=None,
                 conceptualVariableReference=None, description="", label=[],
                 representedVariableName=[], unitTypeReference=None,
                 valueRepresentation="", valueRepresentationReference=None):
        self.categorySchemeReference = categorySchemeReference # CategoryScheme
        self.conceptReference = conceptReference # Concept
        self.conceptualVariableReference = conceptualVariableReference # ConceptualVariable
        self.description = description # String
        self.label = label # List of String
        self.representedVariableName = representedVariableName # List of String
        self.unitTypeReference = unitTypeReference # UnitType
        self.valueRepresentation = valueRepresentation # String
        self.valueRepresentationReference = valueRepresentationReference # ManagedRepresentation

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariable()
        if(self.categorySchemeReference is not None):
            self.categorySchemeReference.add_to_pb(pbm.CategorySchemeReference)
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        if(self.conceptualVariableReference is not None):
            self.conceptualVariableReference.add_to_pb(pbm.ConceptualVariableReference)
        pbm.Description = self.description
        
        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        for repvarname in self.representedVariableName:
            pbrepvarname = pbm.RepresentedVariableName.append(repvarname)
        if(self.unitTypeReference is not None):
            self.unitTypeReference.add_to_pb(pbm.UnitTypeReference)
        pbm.ValueRepresentation = self.valueRepresentation
        if(self.valueRepresentationReference is not None):
            self.valueRepresentationReference.add_to_pb(pbm.ValueRepresentationReference)

        return pbm

    def add_to_pb(self, pbm):
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

# Filler class.
class MeasurementItem:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.MeasurementItem()

        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class Question:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.Question()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class Universe:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.Universe()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class Weighting:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.Weighting()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

class Variable:
    def __init__(self, analysisUnit="", conceptReference=None,
                 conceptualVariableReference=None, description="", embargoReference="",
                 isGeographic=False, isTemporal=False, isWeight=False, label=[],
                 measurementReference=[],outParameter="", questionReference=[],
                 representedVariableReference=None, sourceParameterReference="",
                 sourceUnit="", sourceVariableReference=[], unitTypeReference=None,
                 universeReference=[], variableRepresentation="",
                 weightingProcessReference=None):
        self.analysisUnit = analysisUnit # String
        self.conceptReference = conceptReference # Concept
        self.conceptualVariableReference = conceptualVariableReference # ConceptualVariable
        self.description = description # String
        self.embargoReference = embargoReference # String
        self.isGeographic = isGeographic # Boolean
        self.isTemporal = isTemporal # Boolean
        self.isWeight = isWeight # Boolean
        self.label = label # List of String
        self.measurementReference = measurementReference # List of String
        self.outParameter = outParameter # String
        self.questionReference = questionReference # List of Question
        self.representedVariableReference = representedVariableReference # RepresentedVariable
        self.sourceParameterReference = sourceParameterReference # String
        self.sourceUnit = sourceUnit # String
        self.sourceVariableReference = sourceVariableReference # List of Variable
        self.unitTypeReference = unitTypeReference # UnitType
        self.universeReference = universeReference # List of Universe
        self.variableRepresentation = variableRepresentation # String
        self.weightingProcessReference = weightingProcessReference # Weighting

    def to_pb(self):
        pbm = ddicdi_pb2.Variable()
        pbm.AnalysisUnit = self.analysisUnit
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        if(self.conceptualVariableReference is not None):
            self.conceptualVariableReference.add_to_pb(pbm.ConceptualVariableReference)
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.IsGeographic = self.isGeographic
        pbm.IsTemporal = self.isTemporal
        pbm.IsWeight = self.isWeight
        
        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        for mref in self.measurementReference:
            if(mref is not None):
                pbmref = pbm.MeasurementReference.append(mref.to_pb())

        pbm.OutParameter = self.outParameter

        for q in self.questionReference:
            if(q is not None):
                pbq = pbm.QuestionReference.append(q.to_pb())

        if(self.representedVariableReference is not None):
            self.representedVariableReference.add_to_pb(pbm.RepresentedVariableReference)
        pbm.SourceParameterReference = self.sourceParameterReference
        pbm.SourceUnit = self.sourceUnit

        for svr in self.sourceVariableReference:
            if(svr is not None):
                psvr = pbm.SourceVariableReference.append(svr.to_pb())

        if(self.unitTypeReference is not None):
            self.unitTypeReference.add_to_pb(pbm.UnitTypeReference)

        for uni in self.universeReference:
            if(uni is not None):
                puni = pbm.UniverseReference.append(uni.to_pb())

        pbm.VariableRepresentation = self.variableRepresentation
        if(self.weightingProcessReference is not None):
            self.weightingProcessReference.add_to_pb(pbm.WeightingProcessReference)

        return pbm

    def add_to_pb(self, pbm):
        pbm.AnalysisUnit = self.analysisUnit
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        if(self.conceptualVariableReference is not None):
            self.conceptualVariableReference.add_to_pb(pbm.ConceptualVariableReference)
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.Description = self.description
        pbm.EmbargoReference = self.embargoReference
        pbm.IsGeographic = self.isGeographic
        pbm.IsTemporal = self.isTemporal
        pbm.IsWeight = self.isWeight
        
        for lab in self.label:
            pblabel = pbm.Label.append(lab)

        for mref in self.measurementReference:
            if(mref is not None):
                pbmref = pbm.MeasurementReference.append(mref.to_pb())

        pbm.OutParameter = self.outParameter

        for q in self.questionReference:
            if(q is not None):
                pbq = pbm.QuestionReference.append(q.to_pb())

        if(self.representedVariableReference is not None):
            self.representedVariableReference.add_to_pb(pbm.RepresentedVariableReference)
        pbm.SourceParameterReference = self.sourceParameterReference
        pbm.SourceUnit = self.sourceUnit

        for svr in self.sourceVariableReference:
            if(svr is not None):
                psvr = pbm.SourceVariableReference.append(svr.to_pb())

        if(self.unitTypeReference is not None):
            self.unitTypeReference.add_to_pb(pbm.UnitTypeReference)

        for uni in self.universeReference:
            if(uni is not None):
                puni = pbm.UniverseReference.append(uni.to_pb())

        pbm.VariableRepresentation = self.variableRepresentation
        if(self.weightingProcessReference is not None):
            self.weightingProcessReference.add_to_pb(pbm.WeightingProcessReference)

# Filler class.
class MissingValuesReference:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.MissingValuesReference()
        pbm.Name = self.name
        
        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

class VariableStatistics:
    def __init__(self, filteredCategoryStatistics=[], 
                 managedMissingValuesRepresentation=None, standardWeightReference="",
                 summaryStatistic=[], totalResponses="", 
                 unfilteredCategoryStatistics=[], variableReference=None,
                 weightVariableReference=None):
        self.filteredCategoryStatistics = filteredCategoryStatistics # List of String
        self.managedMissingValuesRepresentation = managedMissingValuesRepresentation # MissingValuesReference
        self.standardWeightReference = standardWeightReference # String
        self.summaryStatistic = summaryStatistic # List of String
        self.totalResponses = totalResponses # String
        self.unfilteredCategoryStatistics = unfilteredCategoryStatistics # List of String
        self.variableReference = variableReference # Variable
        self.weightVariableReference = weightVariableReference # Variable

    def to_pb(self):
        pbm = ddicdi_pb2.VariableStatistics()

        for fcs in self.filteredCategoryStatistics:
            if(fcs is not None):
                pbfcs = pbm.FilteredCategoryStatistics.append(fcs)

        if(self.managedMissingValuesRepresentation is not None):
            self.managedMissingValuesRepresentation.add_to_pb(pbm.ManagedMissingValuesRepresentation)
        pbm.StandardWeightReference = self.standardWeightReference
        
        for sumstat in self.summaryStatistic:
            pbsumstat = pbm.SummaryStatistic.append(sumstat)

        pbm.TotalResponses = self.totalResponses

        for ucs in self.unfilteredCategoryStatistics:
            pbucs = pbm.UnfilteredCategoryStatistics.append(ucs)

        if(self.variableReference is not None):
            self.variableReference.add_to_pb(pbm.VariableReference)
        if(self.weightVariableReference is not None):
            self.weightVariableReference.add_to_pb(pbm.WeightVariableReference)

        return pbm

    def add_to_pb(self, pbm):
        for fcs in self.filteredCategoryStatistics:
            if(fcs is not None):
                pbfcs = pbm.FilteredCategoryStatistics.append(fcs)

        if(self.managedMissingValuesRepresentation is not None):
            self.managedMissingValuesRepresentation.add_to_pb(pbm.ManagedMissingValuesRepresentation)
        pbm.StandardWeightReference = self.standardWeightReference
        
        for sumstat in self.summaryStatistic:
            pbsumstat = pbm.SummaryStatistic.append(sumstat)

        pbm.TotalResponses = self.totalResponses

        for ucs in self.unfilteredCategoryStatistics:
            pbucs = pbm.UnfilteredCategoryStatistics.append(ucs)

        if(self.variableReference is not None):
            self.variableReference.add_to_pb(pbm.VariableReference)
        if(self.weightVariableReference is not None):
            self.weightVariableReference.add_to_pb(pbm.WeightVariableReference)

class VariableGroup:
    def __init__(self, conceptReference=None, description="", isOrdered=False, keyword=[],
                 label=[], subject=[], typeOfVariableGroup="", universeReference=None,
                 variableGroupName=[], variableGroupReference=None, variableReference=None):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = keyword # List of String
        self.label = label # List of String
        self.subject = subject # List of String
        self.typeOfVariableGroup = typeOfVariableGroup # String
        self.universeReference = universeReference # Universe
        self.variableGroupName = variableGroupName # List of String
        self.variableGroupReference = variableGroupReference # VariableGroup
        self.variableReference = variableReference # Variable

    def to_pb(self):
        pbm = ddicdi_pb2.VariableGroup()

        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        pbm.TypeOfVariableGroup = self.typeOfVariableGroup
        if(self.universeReference is not None):
            self.universeReference.add_to_pb(pbm.UniverseReference)

        for vgn in self.variableGroupName:
            pbvgn = pbm.VariableGroupName.append(vgn)

        if(self.variableGroupReference is not None):
            self.variableGroupReference.add_to_pb(pbm.VariableGroupReference)
        if(self.variableReference is not None):
            self.variableReference.add_to_pb(pbm.VariableReference)

        return pbm

    def add_to_pb(self, pbm):
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        pbm.TypeOfVariableGroup = self.typeOfVariableGroup
        if(self.universeReference is not None):
            self.universeReference.add_to_pb(pbm.UniverseReference)

        for vgn in self.variableGroupName:
            pbvgn = pbm.VariableGroupName.append(vgn)

        if(self.variableGroupReference is not None):
            self.variableGroupReference.add_to_pb(pbm.VariableGroupReference)
        if(self.variableReference is not None):
            pbm.VariableReference = self.variableReference.to_pb()

class VariableScheme:
    def __init__(self, description="", label=[], variableGroupReference=[],
                 variableReference=[], variableSchemeName=[], 
                 variableSchemeReference=[]):
        self.description = description # String
        self.label = label # List of String
        self.variableGroupReference = variableGroupReference # List of VariableGroup
        self.variableReference = variableReference # List of Variable
        self.variableSchemeName = variableSchemeName # List of String
        self.variableSchemeReference = variableSchemeReference # List of VariableScheme

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
                pbvr = pbm.VariableReference.append(vr.to_pb())

        for vsn in self.variableSchemeName:
            pbvsn = pbm.VariableSchemeName.append(vsn)

        for vsr in self.variableSchemeReference:
            if(vsr is not None):
                pbvsr = pbm.VariableSchemeReference.append(vsr.to_pb())

        return pbm

    def add_to_pb(self, pbm):

        pbm.Description = self.description

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for vgr in self.variableGroupReference:
            if(vgr is not None):
                pbvgr = pbm.VariableGroupReference.append(vgr.to_pb())

        for vr in self.variableReference:
            if(vr is not None):
                pbvr = pbm.VariableReference.append(vr.to_pb())

        for vsn in self.variableSchemeName:
            pbvsn = pbm.VariableSchemeName.append(vsn)

        for vsr in self.variableSchemeReference:
            if(vsr is not None):
                pbvsr = pbm.VariableSchemeReference.append(vsr.to_pb())

class Dataset:
    def __init__(self, arrayBase = "", dataSetName=[], defaultVariableSchemeReference=None,
                 identifyingVariableReference=None, itemSet="", recordSet="", 
                 variableSet=""):
        self.arrayBase = arrayBase # String
        self.dataSetName = dataSetName # List of String
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.identifyingVariableReference = identifyingVariableReference # Variable
        self.itemSet = itemSet # String
        self.recordSet = recordSet # String
        self.variableSet = variableSet # String

    def to_pb(self):
        pbm = ddicdi_pb2.Dataset()

        pbm.ArrayBase = self.arrayBase

        for dn in self.dataSetName:
            pbdn = pbm.DataSetName.append(dn)

        if(self.defaultVariableSchemeReference is not None):
            pbm.DefaultVariableSchemeReference = self.defaultVariableSchemeReference.to_pb()
        if(self.identifyingVariableReference is not None):
            pbm.IdentifyingVariableReference = self.identifyingVariableReference.to_pb()
        pbm.ItemSet = self.itemSet
        pbm.RecordSet = self.recordSet
        pbm.VariableSet = self.variableSet

        return pbm

class RecordLayout:
    def __init__(self, arrayBase="", characterSet="", dataItem=[],
                 defaultVariableSchemeReference=None, namesOnFirstRow=False):
        self.arrayBase = arrayBase # String
        self.characterSet = characterSet # String
        self.dataItem = dataItem # List of String
        self.defaultVariableSchemeReference = defaultVariableSchemeReference # VariableScheme
        self.namesOnFirstRow = namesOnFirstRow # Boolean

    def to_pb(self):
        pbm = ddicdi_pb2.RecordLayout()

        pbm.ArrayBase = self.arrayBase
        pbm.CharacterSet = self.characterSet

        for di in self.dataItem:
            pbdi = pbm.DataItem.append(di)

        if(self.defaultVariableSchemeReference is not None):
            self.defaultVariableSchemeReference.add_to_pb(pbm.DefaultVariableSchemeReference)
        pbm.NamesOnFirstRow = self.namesOnFirstRow

        return pbm

    def add_to_pb(self, pbm):
        pbm = ddicdi_pb2.RecordLayout()

        pbm.ArrayBase = self.arrayBase
        pbm.CharacterSet = self.characterSet

        for di in self.dataItem:
            pbdi = pbm.DataItem.append(di)

        if(self.defaultVariableSchemeReference is not None):
            self.defaultVariableSchemeReference.add_to_pb(pbm.DefaultVariableSchemeReference)
        pbm.NamesOnFirstRow = self.namesOnFirstRow

# Filler class.
class DataRelationship:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.DataRelationship()

        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class ManagedMissingValuesRepresentation:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.ManagedMissingValuesRepresentation()

        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):

        pbm.Name = self.name

# Filler class.
class InformationClassification:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.InformationClassification()

        pbm.Name = self.name

        return pbm

# Filler class.
class QualityStatement:
    def __init__(self, name=""):
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
        self.dataFileIdentification = dataFileIdentification # List of String
        self.dataFileVersion = dataFileVersion # String
        self.dataFingerprint = dataFingerprint # List of String
        self.dataRelationshipReference = dataRelationshipReference # List of DataRelationship
        self.defaultMissingValuesReference = defaultMissingValuesReference # ManagedMissingValuesRepresentation
        self.grossFileStructure = grossFileStructure # String
        self.informationClassificationReference = informationClassificationReference # List of InformationClassification
        self.proprietaryInfo = proprietaryInfo # Boolean
        self.qualityStatementReference = qualityStatementReference # List of QualityStatement
        self.recordLayoutReference = recordLayoutReference # List of RecordLayout
        self.statisticalSummary = statisticalSummary # String
        self.variableGroupReference = variableGroupReference # List of VariableGroup

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
                pbdrf = pbm.DataRelationshipReference.append(drf.to_pb())

        if(self.defaultMissingValuesReference is not None):
            self.defaultMissingValuesReference.add_to_pb(pbm.DefaultMissingValuesReference)
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
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.RepresentedVariableGroup()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

class RepresentedVariableScheme:
    def __init__(self, description="", label=[], representedVariableGroupReference=[],
                 representedVariableReference=[], representedVariableSchemeName=[],
                 representedVariableSchemeReference=[]):
        self.description = description # String
        self.label = label # List of String
        self.representedVariableGroupReference = representedVariableGroupReference # List of RepresentedVariableGroup
        self.representedVariableReference = representedVariableReference # List of RepresentedVariable
        self.representedVariableSchemeName = representedVariableSchemeName # List of String
        self.representedVariableSchemeReference = representedVariableSchemeReference # List of RepresentedVariableScheme

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
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.CodeListScheme()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class ManagedRepresentationScheme:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.ManagedRepresentationScheme()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

# Filler class.
class CubeScheme:
    def __init__(self, name=""):
        self.name = name # String

    def to_pb(self):
        pbm = ddicdi_pb2.CubeScheme()
        pbm.Name = self.name

        return pbm

    def add_to_pb(self, pbm):
        pbm.Name = self.name

class LogicalProduct:
    def __init__(self, categorySchemeReference=[], codeListSchemeReference=[],
                 managedRepresentationSchemeReference=[], nCubeSchemeReference=[],
                 representedVariableSchemeReference=[], variableSchemeReference=[]):
        self.categorySchemeReference = categorySchemeReference # List of CategoryScheme
        self.codeListSchemeReference = codeListSchemeReference # List of CodeListScheme
        self.managedRepresentationSchemeReference = managedRepresentationSchemeReference # List of ManagedRepresentationScheme
        self.nCubeSchemeReference = nCubeSchemeReference # List of CubeScheme
        self.representedVariableSchemeReference = representedVariableSchemeReference # List of RepresentedVariableScheme
        self.variableSchemeReference = variableSchemeReference # List of VariableScheme

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
                pbmrsr = pbm.ManagedRepresentationSchemeReference.append(mrsr.to_pb())

        for ncsr in self.nCubeSchemeReference:
            if(ncsr is not None):
                pbncsr = pbm.NCubeSchemeReference.append(ncsr.to_pb())

        for rvsr in self.representedVariableSchemeReference:
            if(rvsr is not None):
                pbrvsr = pbm.RepresentedVariableSchemeReference.append(rvsr.to_pb())

        for vsr in self.variableSchemeReference:
            if(vsr is not None):
                pbvsr = pbm.VariableSchemeReference.append(vsr.to_pb())

        return pbm

class RecordLayoutGroup:
    def __init__(self, conceptReference=None, description="", isOrdered=False, keyword=[],
                 label=[], recordLayoutGroupName=[], recordLayoutGroupReference=None,
                 recordLayoutReference=None, subject=[], typeOfRecordLayoutGroup="",
                 universeReference=[]):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = keyword # List of String
        self.label = label # List of String
        self.recordLayoutGroupName = recordLayoutGroupName # List of String
        self.recordLayoutGroupReference = recordLayoutGroupReference # RecordLayoutGroup
        self.recordLayoutReference = recordLayoutReference # RecordLayout
        self.subject = subject # List of String
        self.typeOfRecordLayoutGroup = typeOfRecordLayoutGroup # String
        self.universeReference = universeReference # List of Universe

    def to_pb(self):
        pbm = ddicdi_pb2.RecordLayoutGroup()

        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for rlgn in self.recordLayoutGroupName:
            pbrlgn = pbm.RecordLayoutGroupName.append(rlgn)

        if(self.recordLayoutGroupReference is not None):
            self.recordLayoutGroupReference.add_to_pb(pbm.RecordLayoutGroupReference)
        if(self.recordLayoutReference is not None):
            self.recordLayoutReference.add_to_pb(pbm.RecordLayoutReference)

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        pbm.TypeOfRecordLayoutGroup = self.typeOfRecordLayoutGroup

        for uni in self.universeReference:
            if(uni is not None):
                pbuni = pbm.UniverseReference.append(uni.to_pb())

        return pbm

    def add_to_pb(self, pbm):
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for rlgn in self.recordLayoutGroupName:
            pbrlgn = pbm.RecordLayoutGroupName.append(rlgn)

        if(self.recordLayoutGroupReference is not None):
            self.recordLayoutGroupReference.add_to_pb(pbm.RecordLayoutGroupReference)
        if(self.recordLayoutReference is not None):
            pbm.RecordLayoutReference = self.recordLayoutReference.to_pb()

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        pbm.TypeOfRecordLayoutGroup = self.typeOfRecordLayoutGroup

        for uni in self.universeReference:
            if(uni is not None):
                pbuni = pbm.UniverseReference.append(uni.to_pb())

class PhysicalStructure:
    def __init__(self, defaultDataType="", defaultDecimalPositions="",
                 defaultDecimalSeparator="", defaultDelimiter="", 
                 defaultDigitGroupSeparator="", description="", fileFormat="",
                 grossRecordStructure=[], label=[], physicalStructureName=[]):
        self.defaultDataType = defaultDataType # String
        self.defaultDecimalPositions = defaultDecimalPositions # String
        self.defaultDecimalSeparator = defaultDecimalSeparator # String
        self.defaultDelimiter = defaultDelimiter # String
        self.defaultDigitGroupSeparator = defaultDigitGroupSeparator # String
        self.description = description # String
        self.fileFormat = fileFormat # String
        self.grossRecordStructure = grossRecordStructure # List of String
        self.label = label # List of String
        self.physicalStructureName = physicalStructureName # List of String

    def to_pb(self):
        pbm = ddicdi_pb2.PhysicalStructure()

        pbm.DefaultDataType = self.defaultDataType
        pbm.DefaultDecimalPositions = self.defaultDecimalPositions
        pbm.DefaultDecimalSeparator = self.defaultDecimalSeparator
        pbm.DefaultDelimiter = self.defaultDelimiter
        pbm.DefaultDigitGroupSeparator = self.defaultDigitGroupSeparator
        pbm.Description = self.description
        pbm.FileFormat = self.fileFormat
        
        for grs in self.grossRecordStructure:
            pbgrs = pbm.GrossRecordStructure.append(grs)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for psn in self.physicalStructureName:
            pbpsn = pbm.PhysicalStructureName.append(psn)

        return pbm

    def add_to_pb(self, pbm):
        pbm.DefaultDataType = self.defaultDataType
        pbm.DefaultDecimalPositions = self.defaultDecimalPositions
        pbm.DefaultDecimalSeparator = self.defaultDecimalSeparator
        pbm.DefaultDelimiter = self.defaultDelimiter
        pbm.DefaultDigitGroupSeparator = self.defaultDigitGroupSeparator
        pbm.Description = self.description
        pbm.FileFormat = self.fileFormat
        
        for grs in self.grossRecordStructure:
            pbgrs = pbm.GrossRecordStructure.append(grs)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for psn in self.physicalStructureName:
            pbpsn = pbm.PhysicalStructureName.append(psn)

class BaseRecordLayout:
    def __init__(self, endOfLineMarker="", physicalStructureLinkReference=None,
                 textQualifier=""):
        self.endOfLineMarker = endOfLineMarker # String
        self.physicalStructureLinkReference = physicalStructureLinkReference # PhysicalStructure
        self.textQualifier = textQualifier # String

    def to_pb(self):
        pbm = ddicdi_pb2.BaseRecordLayout()

        pbm.EndOfLineMarker = self.endOfLineMarker
        if(self.physicalStructureLinkReference is not None):
            self.physicalStructureLinkReference.add_to_pb(pbm.PhysicalStructureLinkReference)
        pbm.TextQualifier = self.textQualifier

        return pbm

class PhysicalStructureGroup:
    def __init__(self, conceptReference=None, description="", isOrdered=False, keyword=[],
                 label=[], physicalStructureGroupName=[], physicalStructureReference=None,
                 subject=[], typeOfPhysicalStructureGroup="", universeReference=[]):
        self.conceptReference = conceptReference # Concept
        self.description = description # String
        self.isOrdered = isOrdered # Boolean
        self.keyword = keyword # List of String
        self.label = label # List of String
        self.physicalStructureGroupName = physicalStructureGroupName # List of String
        self.physicalStructureReference = physicalStructureReference # PhysicalSTructureGroup
        self.subject = subject # List of String
        self.typeOfPhysicalStructureGroup = typeOfPhysicalStructureGroup # String
        self.universeReference = universeReference # List of Universe

    def to_pb(self):
        pbm = ddicdi_pb2.PhysicalStructureGroup()

        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for psgn in self.physicalStructureGroupName:
            pbpsgn = pbm.PhysicalStructureGroupName.append(psgn)

        if(self.physicalStructureReference is not None):
            self.physicalStructureReference.add_to_pb(pbm.PhysicalStructureReference)

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        if(self.typeOfPhysicalStructureGroup is not None):
            pbm.TypeOfPhysicalStructureGroup = self.typeOfPhysicalStructureGroup

        for uni in self.universeReference:
            if(uni is not None):
                pbuni = pbm.UniverseReference.append(uni.to_pb())

        return pbm
    
    def add_to_pb(self, pbm):
        if(self.conceptReference is not None):
            self.conceptReference.add_to_pb(pbm.ConceptReference)
        pbm.Description = self.description
        pbm.IsOrdered = self.isOrdered

        for kw in self.keyword:
            pbkw = pbm.Keyword.append(kw)

        for lab in self.label:
            pblab = pbm.Label.append(lab)

        for psgn in self.physicalStructureGroupName:
            pbpsgn = pbm.PhysicalStructureGroupName.append(psgn)

        if(self.physicalStructureReference is not None):
            self.physicalStructureReference.add_to_pb(pbm.PhysicalStructureReference)

        for sub in self.subject:
            pbsub = pbm.Subject.append(sub)

        if(self.typeOfPhysicalStructureGroup is not None):
            pbm.TypeOfPhysicalStructureGroup = self.typeOfPhysicalStructureGroup

        for uni in self.universeReference:
            if(uni is not None):
                pbuni = pbm.UniverseReference.append(uni.to_pb())
