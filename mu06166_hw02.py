import cv2
import math
import time

boolGrayscale = False
image = cv2.imread("tulip.jpg")  #reading image
# image = cv2.imread("Jellyfish.jpg")
image = cv2.resize(image, dsize=(350,180)) #rescaling image

H, W = image.shape[0], image.shape[1]  #extracting dimensions of an image
ascii = ["&","#", "@", "!", "*", "+", "-", "^", "."]  #curating a list of ascii characters
range_= int(math.floor(255/len(ascii)))  #our ascii list has 9 chracters dividing by 255 (max inetnsity) to find range 

final_arr = ''   #curating a final array
final_arr2 = ''

#looping over all the pixels
for y in range(H):
    line = ''  #a temporary variable
    line2=''
    for x in range(W):
        intensity = image[y,x]  #extracting intensities of a given pixel
        #Since we have three channels we'll find the mean of the intensity
        index = int((math.floor(intensity[0]/range_) + math.floor(intensity[1]/range_) + math.floor(intensity[2]/range_))/3)-1 
        # print(index)
        # if index == 0:
            # exit()
        ch = ascii[index]  #extracting the given charcater
        #providing html tags using samp tag
        if boolGrayscale:
            line += f'<samp style="color: rgb({index},{index},{index})">{ch}</samp>'
        else:
            line += f'<samp style="color: rgb({intensity[2]},{intensity[1]},{intensity[0]})">{ch}</samp>'
        line2 += ch
    line2 += '\n'
    final_arr += line + '</br>'  #adding to our final array with a line break
    final_arr2 += line2

#creating and writing a file
f = open('a.txt','w')
f.write(final_arr2)
f.close()

#creating and writing on a html file
h = open('b.html', 'w')
h.write(final_arr)
h.close()

start_time = time.time()

print("%s milliseconds" % ((time.time() - start_time)*1000))


