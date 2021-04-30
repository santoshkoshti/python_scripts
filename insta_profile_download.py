#pip install instaloader

import instaloader
ob = instaloader.Instaloader()
user = input("enter username:")
print("taken input")
ob.download_profile(user,profile_pic_only=True)
print("downloaded")