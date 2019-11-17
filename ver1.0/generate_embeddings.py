import face_recognition
import os
def gen_embs_from_folder(img_path,img_type="jpg"):
    embeds=[]
    embed_name=[]
    err=[]
    for file in os.listdir(img_path):
        if file.endswith("."+img_type):
            curr_img_path=os.path.join(img_path, file)
            image = face_recognition.load_image_file(curr_img_path)
            # Find all the faces in the image using the default HOG-based model.
            # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
            # See also: find_faces_in_picture_cnn.py
            try:
                enc = face_recognition.face_encodings(image)[0]#.reshape(1,-1)
            except IndexError:
                err.append(file)
                continue
            embeds.append(enc)
            embed_name.append(file)
    return embeds,embed_name,err
        
