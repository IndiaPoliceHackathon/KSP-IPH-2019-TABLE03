We start with face

dataset\missing_images_out
dataset\ArrestPerson_images_out

dataset\Test_data_full

missing_nm,testing_nm,matched_list=match_faces("dataset\missing_images_out","dataset\Test_data_full",accurate_measure=1.0,printTime=False)

showMatched('dataset\missing_images_out',missing_nm,'dataset\Test_data_full',testing_nm,matched_list,"dataset\matched_full_topk")