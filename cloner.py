import os
from ROOT import *

samples=["*Wenu*","*Wmunu*","*Wtaunu*","*Zee*","*Zmumu*","*Ztautau*"]
channels = ["ejets/","mujets/","ee/","emu/","mumu/"]

input_root_file="/eos/atlas/atlascerngroupdisk/phys-top/toproperties/ttgamma/v010_production/SR1/"
output_root_file="./SR1S/"

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

  newFile=TFile(output_root_file+channel+"3641XX.Vjets.p2952.v010.root","recreate")

  # Loop over the systematics.
  # Create a clone of the nominal and rename it the systematic
  for syst in systematic_tree:
    print "Cloning ", syst[0]
    
    # Open a new file and clone the chains tree into it
    newTree = chain.CloneTree()
    newTree.SetName(syst[0])
    newFile.Write()
  
  newFile.Close()
