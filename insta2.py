import instaloader
import cv2
import glob
from datetime import datetime


#CODE for showing insta posts that are downloaded
def show(username):
    files = glob.glob('C:\\Users\\Admin\\'+username+'\\*.jpg')+glob.glob('C:\\Users\\Admin\\'+username+'\\*.mp4')
    for file in files:

        if file.endswith(".mp4"):
            vid = cv2.VideoCapture(file)
            if vid.isOpened()== False:
                print("Error playing video")
                break

            while vid.isOpened():
                ret, frame = vid.read()
            
                if ret == True:
                    cv2.imshow(username, frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else: 
                    break
            vid.release()
            cv2.destroyAllWindows()
    
        else:
            image = cv2.imread(file)
            image = cv2.resize(image,(700,700))
            cv2.imshow(username,image)
            cv2.waitKey(7000)
            cv2.destroyAllWindows()
        
    
    cv2.destroyAllWindows()
    
ig = instaloader.Instaloader()

i, k = 0, 0
#To login with your credentials uncomment the below line.
#ig.login('YOUR USERNAME','PASSWORD')

username=str(input("Enter the Username:"))
profile= instaloader.Profile.from_username(ig.context,username)

print("Total Media Count: ",profile.mediacount)
posts = profile.get_posts()

lim_choice = str(input("Do you want to set Post Limit(Yes/No) : " ))
Yes = str('Yes')

if lim_choice == Yes:
    max = int(input("Enter the Number of post to show:"))

    date_choice = str(input("Do you want to set Date limit(Yes/No) : "))

    if date_choice == Yes:
        y1, m1, d1 = [int(x) for x in input("Enter From Date(yyyy/mm/dd) : ").split('/')]
        y2, m2, d2 = [int(x) for x in input("Enter To Date(yyyy/mm/dd) : ").split("/")]

        SINCE = datetime(y1, m1, d1)  
        UNTIL = datetime(y2, m2, d2)
    
        for post in posts:
            postdate = post.date

            if postdate > UNTIL:
                continue
            elif postdate <= SINCE:
                i += 1
                if i == 25:
                    break
                else:
                    continue
            else:
                if k<max:
                    ig.download_post(post, username)
                    k = k+1
                else:
                    print("Limit Reached!\n")
                    break
    
        show(username)
        
    else:
        ig.posts_download_loop(posts, target=username, max_count=max)
        show(username)

else:


    date_choice = str(input("Do you want to set Date limit(Yes/No) : "))

    if date_choice == Yes:
        y1, m1, d1 = [int(x) for x in input("Enter From Date(yyyy/mm/dd) : ").split('/')]
        y2, m2, d2 = [int(x) for x in input("Enter To Date(yyyy/mm/dd) : ").split("/")]

        SINCE = datetime(y1, m1, d1)  
        UNTIL = datetime(y2, m2, d2)
    
        for post in posts:
            postdate = post.date

            if postdate > UNTIL:
                continue
            elif postdate <= SINCE:
                i += 1
                if i == 25:
                    break
                else:
                    continue
            else:
                ig.download_post(post, username)
    
        show(username)
    
    else:
        for post in posts:
            ig.download_post(post, username)
            show(username)





    

    
        

    












