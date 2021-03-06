COM_ENERGY = 13000.
MGLU = 1000  # GeV
MCHI = 800  # GeV
CTAU = 1000  # mm
CROSS_SECTION = 0.385 # pb
SLHA_TABLE="""
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27836266E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     2.82870000E+05   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     1.00218262E+16   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.17473404E+02   #  h^0
        35     4.63466455E+03   #  H^0
        36     4.60420850E+03   #  A^0
        37     4.62050830E+03   #  H^+
   1000001     5.26110645E+03   #  dnl
   1000002     5.26050488E+03   #  upl
   1000003     5.26110645E+03   #  stl
   1000004     5.26050488E+03   #  chl
   1000005     4.59925488E+03   #  b1
   1000006     3.83768652E+03   #  t1
   1000011     1.01695599E+03   #  el-
   1000012     9.82228577E+02   #  nuel
   1000013     1.01695599E+03   #  mul-
   1000014     9.82228577E+02   #  numl
   1000015     8.14143616E+02   #  tau1
   1000016     9.60563965E+02   #  nutl
   1000021     %.9g   #  glss
   1000022     7.99861450E+02   #  z1ss
   1000023     2.61068994E+03   #  z2ss
   1000024     8.00035156E+02   #  w1ss
   1000025    -4.40436084E+03   #  z3ss
   1000035     4.40551318E+03   #  z4ss
   1000037     4.41120557E+03   #  w2ss
   2000001     5.34743115E+03   #  dnr
   2000002     5.29265430E+03   #  upr
   2000003     5.34743115E+03   #  str
   2000004     5.29265430E+03   #  chr
   2000005     5.30680615E+03   #  b2
   2000006     4.64177100E+03   #  t2
   2000011     8.16208069E+02   #  er-
   2000013     8.16208069E+02   #  mur-
   2000015     9.79908020E+02   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.97611898E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     7.59116933E-02   # O_{11}
  1  2    -9.97114539E-01   # O_{12}
  2  1     9.97114539E-01   # O_{21}
  2  2     7.59116933E-02   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99985218E-01   # O_{11}
  1  2     5.43311611E-03   # O_{12}
  2  1    -5.43311611E-03   # O_{21}
  2  2     9.99985218E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     1.09243631E-01   # O_{11}
  1  2     9.94014978E-01   # O_{12}
  2  1    -9.94014978E-01   # O_{21}
  2  2     1.09243631E-01   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1    -7.94264197E-04   #
  1  2     9.99831140E-01   #
  1  3    -1.76664572E-02   #
  1  4     5.00912219E-03   #
  2  1     9.99844968E-01   #
  2  2     1.10197510E-03   #
  2  3     1.46711469E-02   #
  2  4    -9.67472792E-03   #
  3  1    -3.54152918E-03   #
  3  2     8.94684903E-03   #
  3  3     7.07005918E-01   #
  3  4     7.07142174E-01   #
  4  1     1.72303095E-02   #
  4  2    -1.60176214E-02   #
  4  3    -7.06834614E-01   #
  4  4     7.06987619E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.99664187E-01   # U_{11}
  1  2     2.59140767E-02   # U_{12}
  2  1    -2.59140767E-02   # U_{21}
  2  2    -9.99664187E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.99951184E-01   # V_{11}
  1  2     9.88030620E-03   # V_{12}
  2  1    -9.88030620E-03   # V_{21}
  2  2    -9.99951184E-01   # V_{22}
Block GAUGE Q=  4.02882178E+03   #
     1     3.57524961E-01   # g`
     2     6.52378559E-01   # g_2
     3     1.21928000E+00   # g_3
Block YU Q=  4.02882178E+03   #
  3  3     8.36005747E-01   # y_t
Block YD Q=  4.02882178E+03   #
  3  3     6.48209378E-02   # y_b
Block YE Q=  4.02882178E+03   #
  3  3     5.15556112E-02   # y_tau
Block HMIX Q=  4.02882178E+03   # Higgs mixing parameters
     1     4.40950830E+03   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51802856E+02   # Higgs vev at Q
     4     2.11987360E+07   # m_A^2(Q)
Block MSOFT Q=  4.02882178E+03   # DRbar SUSY breaking parameters
     1     2.64877222E+03   # M_1(Q)
     2     7.60767517E+02   # M_2(Q)
     3    -5.11175781E+03   # M_3(Q)
    31     9.90100281E+02   # MeL(Q)
    32     9.90100281E+02   # MmuL(Q)
    33     9.69131042E+02   # MtauL(Q)
    34     8.43792542E+02   # MeR(Q)
    35     8.43792542E+02   # MmuR(Q)
    36     7.78837646E+02   # MtauR(Q)
    41     5.00258447E+03   # MqL1(Q)
    42     5.00258447E+03   # MqL2(Q)
    43     4.39563135E+03   # MqL3(Q)
    44     5.03392529E+03   # MuR(Q)
    45     5.03392529E+03   # McR(Q)
    46     3.69262158E+03   # MtR(Q)
    47     5.08750146E+03   # MdR(Q)
    48     5.08750146E+03   # MsR(Q)
    49     5.11095166E+03   # MbR(Q)
Block AU Q=  4.02882178E+03   #
  1  1     4.39446729E+03   # A_u
  2  2     4.39446729E+03   # A_c
  3  3     4.39446729E+03   # A_t
Block AD Q=  4.02882178E+03   #
  1  1     1.04963750E+04   # A_d
  2  2     1.04963750E+04   # A_s
  3  3     1.04963750E+04   # A_b
Block AE Q=  4.02882178E+03   #
  1  1     2.95507666E+03   # A_e
  2  2     2.95507666E+03   # A_mu
  3  3     2.95507666E+03   # A_tau
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000021     5.50675438E+00 # gluino decay
#  BR              NDA  ID1  ID2  ID3
   2.50000000E-01  3    1    -1   1000022
   2.50000000E-01  3    2    -2   1000022
   2.50000000E-01  3    1    -2   1000024
   2.50000000E-01  3    -1   2    -1000024
#
#         PDG            Width
DECAY   1000024     %.9g # chargino decay
#
""" % (MGLU, (1.97326979e-13 / CTAU))

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(-1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:gg2gluinogluino = on',
            'SUSY:qqbar2gluinogluino = on',
            '1000024:isResonance = false',
            '1000024:oneChannel = 1 1.0 100 1000022 211',
            '1000024:tau0 = %.1f' % CTAU,
            'ParticleDecays:tau0Max = %.1f' % (CTAU * 10),
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi:
    slhaFile = cms.untracked.string(''),   # value not used
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
    particleFile = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/DisappTrksAMSBCascade/test/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU/10))
)

ProductionFilterSequence = cms.Sequence(generator)
