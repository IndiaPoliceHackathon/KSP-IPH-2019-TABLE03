from PIL import Image
import face_recognition
import os
def face_detector(img_path,out_path=None,type='jpg'):
    # Load the jpg file into a numpy array
    cant_find=0
    cant=[]
    err_=0
    err_l=[]
    if out_path is None:
        out_path= img_path+"_out"
        if not os.path.exists(out_path):
            os.makedirs(out_path)
    for file in os.listdir(img_path):
        if file.endswith("."+type):
            curr_img_path=os.path.join(img_path, file)
            try:
                image = face_recognition.load_image_file(curr_img_path)
            except OSError:
                err_+=1
                err_l.append(file)
                continue
            # Find all the faces in the image using the default HOG-based model.
            # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
            # See also: find_faces_in_picture_cnn.py
            face_locations = face_recognition.face_locations(image)
            #print("I found {} face(s) in this photograph.".format(len(face_locations)))
            if len(face_locations)==0:
                cant_find+=1
                cant.append(curr_img_path)
            count=0
            for face_location in face_locations:

                # Print the location of each face in this image
                top, right, bottom, left = face_location
                print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

                # You can access the actual face itself like this:
                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                pil_image.save(os.path.join(out_path, file+str(count)+"."+type))
                count+=1
    print('Images that could not be loaded because of some error(if thr exists one):',"\n".join(cant),'Done')
