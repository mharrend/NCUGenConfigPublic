# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/Hadronizer_TuneEE5C_generic_LHE_herwigpp_cff.py --step GEN --conditions auto:mc --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.parseArguments()

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/Generator/python/Hadronizer_TuneEE5C_generic_LHE_herwigpp_cff.py nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string(options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("ThePEGHadronizerFilter",
    ue_2_3 = cms.vstring('cd /Herwig/UnderlyingEvent', 
        'set KtCut:MinKT 4.0', 
        'set UECuts:MHatMin 8.0', 
        'set MPIHandler:InvRadius 1.5', 
        'cd /'),
    powhegDefaults = cms.vstring('# Need to use an NLO PDF', 
        'set /Herwig/Particles/p+:PDF    /Herwig/Partons/MRST-NLO', 
        'set /Herwig/Particles/pbar-:PDF /Herwig/Partons/MRST-NLO', 
        '# and strong coupling', 
        'create Herwig::O2AlphaS O2AlphaS', 
        'set /Herwig/Generators/LHCGenerator:StandardModelParameters:QCD/RunningAlphaS O2AlphaS', 
        '# Setup the POWHEG shower', 
        'cd /Herwig/Shower', 
        '# use the general recon for now', 
        'set KinematicsReconstructor:ReconstructionOption General', 
        '# create the Powheg evolver and use it instead of the default one', 
        'create Herwig::PowhegEvolver PowhegEvolver HwPowhegShower.so', 
        'set ShowerHandler:Evolver PowhegEvolver', 
        'set PowhegEvolver:ShowerModel ShowerModel', 
        'set PowhegEvolver:SplittingGenerator SplittingGenerator', 
        'set PowhegEvolver:MECorrMode 0', 
        '# create and use the Drell-yan hard emission generator', 
        'create Herwig::DrellYanHardGenerator DrellYanHardGenerator', 
        'set DrellYanHardGenerator:ShowerAlpha AlphaQCD', 
        'insert PowhegEvolver:HardGenerator 0 DrellYanHardGenerator', 
        '# create and use the gg->H hard emission generator', 
        'create Herwig::GGtoHHardGenerator GGtoHHardGenerator', 
        'set GGtoHHardGenerator:ShowerAlpha AlphaQCD', 
        'insert PowhegEvolver:HardGenerator 0 GGtoHHardGenerator'),
    ue_2_4 = cms.vstring('cd /Herwig/UnderlyingEvent', 
        'set KtCut:MinKT 4.3', 
        'set UECuts:MHatMin 8.6', 
        'set MPIHandler:InvRadius 1.2', 
        'cd /'),
    cm7TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    pdfCTEQ6LL = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF /cmsPDFSet ThePEGLHAPDF.so', 
        'set /cmsPDFSet:PDFName cteq6ll.LHpdf', 
        'set /cmsPDFSet:RemnantHandler HadronRemnants', 
        'set /Herwig/Particles/p+:PDF /cmsPDFSet', 
        'set /Herwig/Particles/pbar-:PDF /cmsPDFSet', 
        'cd /'),
    pdfMRST2001 = cms.vstring('cd /Herwig/Partons', 
        'create Herwig::MRST MRST2001 HwMRST.so', 
        'setup MRST2001 ${HERWIGPATH}/PDF/mrst/2001/lo2002.dat', 
        'set MRST2001:RemnantHandler HadronRemnants', 
        'cd /', 
        'cp /Herwig/Partons/MRST2001 /cmsPDFSet', 
        'cd /Herwig/Particles', 
        'set p+:PDF /cmsPDFSet', 
        'set pbar-:PDF /cmsPDFSet', 
        '+ue_2_3'),
    cm13TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 13000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV'),
    reweightConstant = cms.vstring('mkdir /Herwig/Weights', 
        'cd /Herwig/Weights', 
        'create ThePEG::ReweightConstant reweightConstant ReweightConstant.so', 
        'cd /', 
        'set /Herwig/Weights/reweightConstant:C 1', 
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightConstant'),
    cm8TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 8000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    lheDefaults = cms.vstring('cd /Herwig/Cuts', 
        'create ThePEG::Cuts NoCuts', 
        'cd /Herwig/EventHandlers', 
        'create ThePEG::LesHouchesInterface LHEReader', 
        'set LHEReader:Cuts /Herwig/Cuts/NoCuts', 
        'create ThePEG::LesHouchesEventHandler LHEHandler', 
        'set LHEReader:MomentumTreatment RescaleEnergy', 
        'set LHEReader:WeightWarnings 0', 
        'set LHEHandler:WeightOption VarNegWeight', 
        'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor', 
        'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
        'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
        'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler', 
        'insert LHEHandler:LesHouchesReaders 0 LHEReader', 
        'cd /Herwig/Generators', 
        'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler', 
        'cd /Herwig/Shower', 
        'set Evolver:HardVetoScaleSource Read', 
        'set Evolver:MECorrMode No', 
        'cd /', 
        'set /Herwig/Shower/KinematicsReconstructor:ReconstructionOption General', 
        'set /Herwig/Shower/KinematicsReconstructor:InitialInitialBoostOption LongTransBoost', 
        'cd /Herwig/EventHandlers', 
        'set LHEReader:PDFA /cmsPDFSet', 
        'set LHEReader:PDFB /cmsPDFSet', 
        'cd /'),
    cmsDefaults = cms.vstring('+basicSetup', 
        '+setParticlesStableForDetector'),
    pdfMRST2008LOss = cms.vstring('cp /Herwig/Partons/MRST /cmsPDFSet', 
        'cd /Herwig/Particles', 
        'set p+:PDF /cmsPDFSet', 
        'set pbar-:PDF /cmsPDFSet', 
        '+ue_2_4'),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    basicSetup = cms.vstring('cd /Herwig/Generators', 
        'create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
        'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
        'set LHCGenerator:NumberOfEvents 10000000', 
        'set LHCGenerator:DebugLevel 1', 
        'set LHCGenerator:LogNonDefault 1', 
        'set LHCGenerator:UseStdout 0', 
        'set LHCGenerator:PrintEvent 0', 
        'set LHCGenerator:MaxErrors 10000'),
    run = cms.string('LHC'),
    repository = cms.string('HerwigDefaults.rpo'),
    cm14TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV'),
    dataLocation = cms.string('${HERWIGPATH}'),
    setParticlesStableForDetector = cms.vstring('cd /Herwig/Particles', 
        'set mu-:Stable Stable', 
        'set mu+:Stable Stable', 
        'set Sigma-:Stable Stable', 
        'set Sigmabar+:Stable Stable', 
        'set Lambda0:Stable Stable', 
        'set Lambdabar0:Stable Stable', 
        'set Sigma+:Stable Stable', 
        'set Sigmabar-:Stable Stable', 
        'set Xi-:Stable Stable', 
        'set Xibar+:Stable Stable', 
        'set Xi0:Stable Stable', 
        'set Xibar0:Stable Stable', 
        'set Omega-:Stable Stable', 
        'set Omegabar+:Stable Stable', 
        'set pi+:Stable Stable', 
        'set pi-:Stable Stable', 
        'set K+:Stable Stable', 
        'set K-:Stable Stable', 
        'set K_S0:Stable Stable', 
        'set K_L0:Stable Stable', 
        'cd /'),
    reweightPthat = cms.vstring('mkdir /Herwig/Weights', 
        'cd /Herwig/Weights', 
        'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so', 
        'cd /', 
        'set /Herwig/Weights/reweightMinPT:Power 4.5', 
        'set /Herwig/Weights/reweightMinPT:Scale 15*GeV', 
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightMinPT'),
    cm10TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV'),
    pdfCTEQ6L1 = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF /cmsPDFSet ThePEGLHAPDF.so', 
        'set /cmsPDFSet:PDFName cteq6ll.LHpdf', 
        'set /cmsPDFSet:RemnantHandler HadronRemnants', 
        'set /Herwig/Particles/p+:PDF /cmsPDFSet', 
        'set /Herwig/Particles/pbar-:PDF /cmsPDFSet', 
        'cd /'),
    pdfCT10 = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF /cmsPDFSet ThePEGLHAPDF.so', 
        'set /cmsPDFSet:PDFName CT10.LHgrid', 
        'set /cmsPDFSet:RemnantHandler HadronRemnants', 
        'set /Herwig/Particles/p+:PDF /cmsPDFSet', 
        'set /Herwig/Particles/pbar-:PDF /cmsPDFSet', 
        'cd /'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    EE5C = cms.vstring('+pdfCTEQ6L1', 
        '+EE5CEnergyExtrapol', 
        'set /Herwig/Hadronization/ColourReconnector:ColourReconnection Yes', 
        'set /Herwig/Hadronization/ColourReconnector:ReconnectionProbability 0.49', 
        'set /Herwig/Partons/RemnantDecayer:colourDisrupt 0.80', 
        'set /Herwig/UnderlyingEvent/MPIHandler:InvRadius 2.30', 
        'set /Herwig/UnderlyingEvent/MPIHandler:softInt Yes', 
        'set /Herwig/UnderlyingEvent/MPIHandler:twoComp Yes', 
        'set /Herwig/UnderlyingEvent/MPIHandler:DLmode 2'),
    EE5CEnergyExtrapol = cms.vstring('set /Herwig/UnderlyingEvent/MPIHandler:EnergyExtrapolation Power', 
        'set /Herwig/UnderlyingEvent/MPIHandler:ReferenceScale 7000.*GeV', 
        'set /Herwig/UnderlyingEvent/MPIHandler:Power 0.33', 
        'set /Herwig/UnderlyingEvent/MPIHandler:pTmin0 3.91*GeV'),
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(-1.0),
    parameterSets = cms.vstring('cmsDefaults', 
        'EE5C', 
        'lheDefaults'),
    filterEfficiency = cms.untracked.double(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

