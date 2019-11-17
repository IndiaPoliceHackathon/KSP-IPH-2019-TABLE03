import face_recognition
import os
import numpy as np
#%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import PIL
from generate_embeddings import gen_embs_from_folder
import time
import matplotlib.pyplot as plt
def match_faces(missing_path,testing_path,accurate_measure=1.0,printTime=False):
    '''
    accurate_measure == lower makes ur model precision higher/ makes hard matching
    '''
    print('Loading missing_embeddings : {}'.format(missing_path))
    #missing_path="cropped"
    missing_embs,missing_nm,e_me=gen_embs_from_folder(missing_path)

    
    print('Loading test_embeddings : {}'.format(testing_path))
    # Load a test image and get encondings for it
    #testing_path="cropped"
    testing_embs,testing_nm,e_te=gen_embs_from_folder(testing_path)
    print(len(missing_embs),len(testing_embs))
    #return missing_embs,testing_embs


    count_not_found=0
    not_found_id=[]
    matched_list=[]
    print('starting search')
    for i in range(len(missing_embs)):
        temp=[]
        found=False
        st=time.time()
        dic=dict()
        for j in range(len(testing_embs)):
            axx=face_recognition.compare_faces([missing_embs[i]],testing_embs[j],accurate_measure)[0]
            
            if axx:
                sim_val = face_recognition.face_distance([missing_embs[i]],testing_embs[j])[0]
                found=True
                img1=mpimg.imread(os.path.join(missing_path,missing_nm[i]))
                #imgplot = plt.imshow(img1)
                #plt.show()
                img2=mpimg.imread(os.path.join(testing_path,testing_nm[j]))
                #imgplot = plt.imshow(img2)
                #plt.show()
                #temp.append(sim_val)
                dic[j]=sim_val
                #matched_list.append((i,j))
                #print('founded {} at {} wid distance : {},{}'.format(i,j,axx, face_recognition.face_distance([missing_embs[i]],testing_embs[j],)[0] ))
                #break
        lis_=sorted(dic.items(), key = 
             lambda kv:(kv[1], kv[0]))        
        #lis_=sorted(dic.iteritems(), key = lambda x : x[1])
        lis_=lis_[:3]
        for k in range(len(lis_)):
            matched_list.append((i,lis_[k][0]))
        et=time.time()-st
        if printTime: print("finding time at {} :".format(i),et)
        if not found:
            count_not_found+=1
            not_found_id.append(i)

    print('The images that are found/not found is {}/{}'.format(len(missing_embs)-count_not_found ,count_not_found))

    '''
    for i, face_distance in enumerate(face_distances):
        print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
        print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
        print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
        print()
    '''
    return missing_nm,testing_nm,matched_list


        
def showMatched(missing_path,missing_nm,testing_path,testing_nm,matched_list,output_path):
    if not os.path.exists(output_path):
            os.makedirs(output_path)
    for ii,j in matched_list:
        images=[ os.path.join(missing_path,missing_nm[ii]),os.path.join(testing_path,testing_nm[j])]
        imgs    = [ PIL.Image.open(i) for i in images ]
        # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

        # save that beautiful picture
        imgs_comb = PIL.Image.fromarray( imgs_comb)
        imgs_comb.save( os.path.join(output_path,'{} +++ {}.jpg'.format(ii,j) ))    
        # for a vertical stacking it is simple: use vstack
        imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        imgs_comb = PIL.Image.fromarray( imgs_comb)
        imgs_comb.save(  os.path.join(output_path,'vertical_{} +++ {}.jpg'.format(ii,j) ) )    
        #imgs_comb.show()
#mn,tn,ml=match_faces('dataset/missing_images_out','dataset/ArrestPerson_images_out')   
#showMatched('dataset/missing_images_out',mn,'dataset/ArrestPerson_images_out',tn,ml,'matched')
