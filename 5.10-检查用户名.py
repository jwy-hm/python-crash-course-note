current_users = ["admin","Ybz",'yz','lsz',"hjw"]
new_users = ["Ybz","yz","lsw","hjm","nbld"]
current_users_lower = [usr.lower() for usr in current_users]
new_users_lower = [usr.lower() for usr in new_users]
for new_usr_lower in new_users_lower:
    if new_usr_lower in current_users_lower:
        print("需要输入别的用户名")
    else:
        print("这个用户名未被使用")