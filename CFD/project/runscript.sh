#! /bin/bash
comsol batch -inputfile "/home/henrik/Documents/umu/CFD/project/2021-12-25_normal_mesh_newBL_plate.mph" -outputfile "/home/henrik/Documents/umu/CFD/project/2021-12-25_normal_mesh_newBL_plate_RUN.mph"
python3 /home/henrik/.notify.py "sim with plate"
comsol batch -inputfile "/home/henrik/Documents/umu/CFD/project/2021-12-25_normal_mesh_newBL_injector.mph" -outputfile "/home/henrik/Documents/umu/CFD/project/2021-12-25_normal_mesh_newBL_injector_RUN.mph"
python3 /home/henrik/.notify.py "sim with injector"
python3 /home/henrik/.notify.py "The entire run is done"

