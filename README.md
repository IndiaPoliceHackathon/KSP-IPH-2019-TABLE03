***Synopsis***

This system endeavours towards comprehensive solution for facial-features
based Identication and Tracking. It can search subjects across the web and will
be able to locate them within several live video streams. It expedites the
investigation by quickly tagging the subject in any specic video footage. We
also intend to generate all possible photos of a specic person (at various
possible ages) to create a database of long missing persons. This can later be
extended to build publicly accessible/queried image database of habitual JohnDoe fraudsters. The same can be used by vigilant citizen for identifying criminal
before next fraud is committed
******


This project is an end-to-end face recognition application which can do live streaming of CCTV camera, find faces in a stored Image/Video.
We use Image Enhancement techniques like Super Resolution Improvement using state-of-the-art SRGAN, FaceAPP like face style generation using CYCLEGANs, and used TPGAN for face_rotation.
Code for the same is provided in the repo with the weights as well.

***please look at the high_level_architecture.png for better understanding***
*******
*******

Primary Objective:
Finding missing person from the database ... DONE

Secondary Objective:
Image Enhancement... Partially DONE < more styles can be used>
GUI linkage with all functions... Partially DONE <need to call the corresponding function based on the corresponding gui action>
Using state-of-the-art Face_recognition/Face_detection models... DONE <We can further use different models based on the latest research work>
Light-weight mode... Partially Done. In this hackathon, we emphasized more precision and thus went with more heavier config model like DLIB for face recognition, although we use mobilenet for face_detection so the work done is partial.
*******
*******


Terminology :
    We store all the missing/criminal/unnatural death/XYZ images folder in "dataset" folder.
    We save all the outputs of matched faces in "matched" folder.
*******
*******

RESULTS: 
- You may find the video search results in 'media' folder as final_output.mp4
- You may find matched_faces results in 'matched' folder.
*******
*******
 
HOW TO RUN ::: 
**Requirement file** 
Please run 'pip install -r requirment.txt'

**Face_Detection**
-from the "face_detection.py" file import face_detector.
- Use "face_detector(input_image_path,out_path=None,type='jpg')" function.
    - pass input_image_path  :: folder path
    - pass output_image_path :: folder path :: stores the detected faces from the images.


**Face_Matching**
-from the "face_recognition.py" file import match_faces function.
- Use "match_faces(missing_path,testing_path,
output_path,accurate_measure=1.0,printTime=False,total_time=True)"
 function.
    - pass missing_path  :: folder path ::  the person we are looking for.
    - pass testing_path :: folder path ::  database of person under any of the case like arrested, unnatural death and wanted .

**Live_Streaming**
- Use liveStream(database,resizer_X=0.5,resizer_Y=0.5,accurate_measure=0.5) from "fr_live_stream.py"
    - database :: this is the missing person/wanted people database.
    
    






