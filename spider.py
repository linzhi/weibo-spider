#! /usr/bin/env python
# -*- coding = utf-8 -*-

from time import sleep

class WeiboSpider:
    '''
        crawl sina weibo comments
    '''
    def __init__(self, user_id):
        self.user_id = user_id

    def delay_time(self, seconds):
        self.seconds = seconds

        sleep(seconds)

    def get_friendships(self, user_id):
        self.user_id = user_id

        tmp_count = 0
        while tmp_count < 10:
            friendship = client.get.friendships__friends__ids(uid=user_id)
            if friendship.ids:
                break
            else:
                tmp_count += 1

        uid_set = []

        if friendship.ids:
            for each_uid in friendship.ids:
                uid_set.append(each_uid)

            return uid_set

        else:
            return uid_set

    def get_user_info(self, user_id):
        self.user_id = user_id

        tmp_count = 0
        while tmp_count < 10:
            user_info = client.get.users__show(uid=user_id)
            if user_info:
                break 
            else:
                tmp_count += 1

        user = []

        if user_info:
            user.append(user_info.id)
            user.append(user_info.screen_name)
            user.append(user_info.gender)

        return user

    def get_statuses(self, user_id):
        self.user_id = user_id

        tmp_count = 0
        while tmp_count < 10:
            status = client.get.statuses__user_timeline(uid=user_id, count=100)
            if status.statuses:
                break
            else:
                tmp_count += 1

        status_id       = []
        status_writer   = []
        status_time     = []
        status_text     = []
        status_comments = []

        if status.statuses:
            for each_status in status.statuses:
                if len(each_status) != 6:
                    status_id.append(each_status.id)
                    status_writer.append(each_status.user.screen_name)
                    status_time.append(each_status.created_at)
                    status_text.append(each_status.text)
                    status_comments.append(each_status.comments_count)

            return (status_id, status_writer, status_time, status_text, status_comments)

        else:
            return (status_id, status_writer, status_time, status_text, status_comments)

    def get_comments(self, status_id):
        self.status_id = status_id

        tmp_count =  0
        while tmp_count < 10:
            comment = client.get.comments__show(id=status_id, count=50)
            if comment.comments:
                break
            else:
                tmp_count += 1

        comment_writer_id = []
        comment_writer    = []
        comment_time      = []
        comment_text      = []

        if comment.comments:
            for each_comment in comment.comments:
                comment_writer_id.append(each_comment.user.id)
                comment_writer.append(each_comment.user.screen_name)
                comment_time.append(each_comment.created_at)
                comment_text.append(each_comment.text)

            return (comment_writer_id, comment_writer, comment_time, comment_text)

        else:
            return (comment_writer_id, comment_writer, comment_time, comment_text)

            
if __name__ == "__main__":
    from client import Client

    client = Client()
    client = client.set_client()

    user_id = raw_input("Please input user's id: ")
    spider = WeiboSpider(user_id)

    uid_set = spider.get_friendships(user_id)

    try:
        out_file = open('comments.dat', 'w')
    except IOError:
        print "Error: open file failed"

    for m in range(len(uid_set)):
        (tmp_id, tmp_writer, tmp_time, tmp_text, tmp_comments) = spider.get_statuses(uid_set[m])

        print "> statuses before filter: %d" % len(tmp_id)

        status_id       = []
        status_writer   = []
        status_time     = []
        status_text     = []
        status_comments = []

        for n in range(len(tmp_id)):
            if tmp_comments[n] != 0:
                status_id.append(tmp_id[n])
                status_writer.append(tmp_writer[n])
                status_time.append(tmp_time[n])
                status_text.append(tmp_text[n])
                status_comments.append(tmp_comments[n])

        print "> statuses after filter: %d" % len(status_id)
        
        for i in range(len(status_id)):
            print "> Grabbing comments of %s | statuses +%d" % (status_writer[i], i+1)
            print status_text[i] 
            writer = status_writer[i].encode('utf-8')

            spider.delay_time(30)

            (comment_writer_id, comment_writer, 
             comment_time, comment_text) = spider.get_comments(status_id[i])

            for j in range(len(comment_writer_id)):
                if comment_writer_id[j] == int(user_id):
                    name = comment_writer[j].encode('utf-8')
                    time = comment_time[j].encode('utf-8')
                    text = comment_text[j].encode('utf-8')
    
                    out_file.write(name + ' ' + writer + ' ' + 
                                   time + ' ' + text + '\n')

    out_file.close()
    





