import instaloader
import csv
import time
# list of profile data we want to fetch
def get_profile_data():
    temp_li=[profile.biography,profile.mediacount,profile.is_private,
    profile.profile_pic_url, profile.business_category_name,profile.followers,profile.followees]
    return temp_li
# header name of csv file
def get_csv_header():
    temp_li=['Bio','postnumber','is_private','profile_picture','business_category',
    'number_of_followers','number_of_followees','best_post_url']
    return temp_li
# list of profile name
def get_list_of_profilename():
    list1=['mezon_moda']
    return list1
    
loader = instaloader.Instaloader()
loader.login('xxxx', 'xxxxx')


with open(r'instagram.csv', 'w', newline ='',encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(get_csv_header())
    for i in range(len(get_list_of_profilename())):
        time.sleep(5)
        profile = instaloader.Profile.from_username(loader.context,get_list_of_profilename()[i])
        temp2=[]
        for i in range(len(get_profile_data())):
            temp2.append(get_profile_data()[i])
        posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments+int(0 if p.video_view_count is None else p.video_view_count),
                               reverse=True)
        temp2.append(posts_sorted_by_likes[0].url)
        writer.writerow(temp2)
