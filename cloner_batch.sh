executable            = /afs/cern.ch/work/j/jwsmith/github/ttgammaCloner/run_cloner.sh
getenv                = True
JobBatchName	      = cloner_vjets
+JobFlavour           = "testmatch"

output = output/$(ClusterId).$(ProcId)
error = error/$(ClusterId).$(ProcId)
log = log/$(ClusterId).$(ProcId)
queue
