#start=`date +%s`

python3 /home/amtf/notify.py "Started run. Note time."
#comsol batch -inputfile 2022-01-03_finer_mesh_newBL_new_contraction_meshconv_sesam2.mph -outputfile 2022-01-03_finer_mesh_newBL_new_contraction_meshconv_sesam2_RUN.mph; 
#end=`date +%s`
#runtime=$((end-start))
#python3 /home/amtf/notify.py "First run, not smooth transition, is done."

comsol batch -inputfile 2022-01-03_finer_mesh_newBL_new_contraction_meshconv_sesam2_smoothtrans.mph -outputfile 2022-01-03_finer_mesh_newBL_new_contraction_meshconv_sesam2_smoothtrans_RUN.mph 
python3 /home/amtf/notify.py "Second run, smooth transition, is done."



python3 /home/amtf/notify.py "All runs done. Note time. "
