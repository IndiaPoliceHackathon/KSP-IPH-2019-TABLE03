#USE GUI for running the specific case of searching from database.
#or Use each command line.

#for face detection stuff
from face_detection import face_detector
face_detector('dataset/Test_data_full')




#for example for matching faces
from face_match_v3 import match_faces
mn,tn,ml,aa=match_faces('dataset/missing_images_out','dataset/Test_data_full','matched/final_output_top3')

