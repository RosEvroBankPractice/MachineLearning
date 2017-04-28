import json
from models import FacebookUser, Group, JoinFriends, JoinGroups

text = open('data_2.json', 'r')

result = json.load(text)

date = result['date']
items = result['items']

users = []
groups = []

for item in items:
    subscription = item['subscription']
    friends = item['fiends']

    id = item['id']
    url = item['url']
    name = item['name']
    birthday = item['birthday']
    job = item['job']
    raw_groups = item['groups']

    try:
        if birthday != 'null':
            birthday = birthday.split()[2]
        else:
            birthday = 0
    except Exception as e:
        print(birthday)
        birthday = 0
    try:
        user_tuple = FacebookUser.get_or_create(id=id, url=url, name=name, job=job, birthday=birthday)
        user = user_tuple[0]
        users.append(user)
    except Exception as ex:
        print(ex)

    if isinstance(raw_groups, str):
        print(raw_groups)
    else:

        for raw_group in raw_groups:
            raw_group_name = raw_group['name']
            raw_group_id = raw_group['id']
            try:
                group_tuple = Group.get_or_create(id=raw_group_id, name=raw_group_name)
                group = group_tuple[0]
                groups.append(groups)
            except Exception as ex:
                print(ex)

print('creating joins')

for item in items:
    try:
        cur_user_id = item['id']
        cur_user = FacebookUser.get(id=cur_user_id)
        friends = item['fiends']
        if isinstance(friends, str):
            print(friends)
        else:
            for raw_friend in friends:
                friend_id = raw_friend['id']
                friend_name = raw_friend['name']
                friend = FacebookUser.get_or_create(id=friend_id, name=friend_name)
                friend = friend[0]
                try:
                    JoinFriends.get_or_create(user=cur_user, user2=friend)
                except Exception as ex:
                    print(ex)

        raw_groups = item['groups']

        if isinstance(raw_groups, str):
            print(raw_groups)
        else:

            for raw_group in raw_groups:
                raw_group_name = raw_group['name']
                raw_group_id = raw_group['id']
                try:
                    group = Group.get(id=raw_group_id)
                    JoinGroups.get_or_create(user=cur_user, group=group)
                except Exception as ex:
                    print(ex)
    except Exception as ex:
        print(ex)
print('quit')
