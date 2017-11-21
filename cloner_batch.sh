executable            = /afs/cern.ch/work/j/jwsmith/github/ttgammaCloner/run_cloner.sh
getenv                = True
transfer_input_files  = cloner.py,systTrees.txt
JobBatchName	      = cloner_vjets
+JobFlavour           = "testmatch"

output = output/$(ClusterId).$(ProcId)
error = error/$(ClusterId).$(ProcId)
log = log/$(ClusterId).$(ProcId)
queue
