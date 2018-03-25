#! cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/python/2.7.13-x86_64-slc6-gcc62/2.7.13-597a5/x86_64-slc6-gcc62-opt/bin/python
# Remember to lsetup root
import os
from ROOT import *

samples=["*Wenu*p3317*","*Wmunu*p3317*","*Wtaunu*p3317*","*Zee*p3317*","*Zmumu*p3317*","*Ztautau*p3317*"]
#samples=["*ttV*p3317*"]
#channels = ["ee/","emu/","mumu/","ejets/","mujets/"]
channels = ["ee/","emu/","mumu/"]

input_root_file="/eos/atlas/atlascerngroupdisk/phys-top/toproperties/ttgamma/v010_march18/SR1/"
output_root_file="/eos/atlas/atlascerngroupdisk/phys-top/toproperties/ttgamma/v010_march18/SR1S/"

systematic_tree = []
syst_file = open("systTrees.txt", "r") 
for l in syst_file:
  systematic_tree.append(l.split())


# Get the nominal tree in the samples and chain them together 
# while looping over channels
for channel in channels:
  chain = TChain("nominal")
  for sample in samples:
    chain.Add(input_root_file+channel+sample)

  newFile=TFile(output_root_file+channel+"3641XX.Vjets.p3317.v010.root","recreate")
  #newFile=TFile(output_root_file+channel+"3641XX.TTV_DummySysts.p3317.v010.root","recreate")

  # Loop over the systematics.
  # Create a clone of the nominal and rename it the systematic
  for syst in systematic_tree:
    print channel,": Cloning ", syst[0]
    
    # Open a new file and clone the chains tree into it
    newTree = chain.CloneTree()
    newTree.SetName(syst[0])
    newFile.Write()
  
  newFile.Close()
