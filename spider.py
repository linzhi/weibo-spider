#! /usr/bin/env python
# -*- coding = utf-8 -*-

from time import sleep

class WeiboSpider:
    '''
        crawl sina weibo comments
    '''
    def __init__(self, user_id):
        self.user_id = user_id

    def delay_time(self):
        '''
            limit to access sina server delay time
        '''
        sleep(60)

    def get_friendships(self, user_id):
        '''
            get user's(uid=user_id) following list
            default setting is 500
        '''
        self.user_id = user_id

        friendship = client.get.friendships__friends__ids(uid=user_id)

        uid_set = []

        for each_uid in friendship.ids:
            uid_set.append(each_uid)

        return uid_set

    def get_user_info(self, user_id):
        '''
            get user id=user_id basic information
        '''
        self.user_id = user_id

        user_info = client.get.user__show(uid=user_id)

        user = []

        user.append(user_info.id)
        user.append(user_info.screen_name)
        user.append(user_info.gender)

        return user

    def get_statuses(self, user_id):
        '''
            get 50 statuses from user id=user_id
        '''
        self.user_id = user_id

        status = client.get.statuses__user_timeline(uid=user_id, count=50)

        status_id       = []
        status_writer   = []
        status_time     = []
        status_text     = []
        status_comments = []
        
        for each_status in status.statuses:
            status_id.append(each_status.id)
            status_writer.append(each_status.user.screen_name)
            status_time.append(each_status.created_at)
            status_text.append(each_status.text)
            status_comments.append(each_status.comments_count)

        return (status_id, status_writer, status_time, status_text, status_comments)

    def get_comments(self, status_id):
        '''
            get 50 comments on statuses id=status_id
        '''
        self.status_id = status_id

        comment = client.get.comments__show(id=status_id, count=50)

        comment_writer_id = []
        comment_writer    = []
        comment_time      = []
        comment_text      = []

        for each_comment in comment.comments:
            comment_writer_id.append(each_comment.user.id)
            comment_writer.append(each_comment.user.screen_name)
            comment_time.append(each_comment.created_at)
            comment_text.append(each_comment.text)

        return (comment_writer_id, comment_writer, comment_time, comment_text)

            
if __name__ == "__main__":
    from client import Client

    client = Client()
    client = client.set_client()

    user_id = raw_input("Please input user's id: ")
    spider = WeiboSpider(user_id)

    uid_set = spider.get_friendships(user_id)

    out_file = open('comments.dat', 'w')

    for each_uid in uid_set:
        (temp_status_id, temp_status_writer, temp_status_time,
         temp_status_text, temp_status_comments) = spider.get_statuses(each_uid)

        print "number of statuses before filter: %d" % len(temp_status_id)

        status_id       = []
        status_writer   = []
        status_time     = []
        status_text     = []
        status_comments = []

        for k in range(len(temp_status_id)):
            if temp_status_comments[k] != 0:
                status_id.append(temp_status_id[k])
                status_writer.append(temp_status_writer[k])
                status_time.append(temp_status_time[k])
                status_text.append(temp_status_text[k])
                status_comments.append(temp_status_comments[k])

        print "number of statuses after filter: %d" % len(status_id)
        
        for i in range(len(status_id)):
            print ">Grabbing data of: %s" % status_writer[i]
            writer = status_writer[i].encode('utf-8')

            spider.delay_time()

            (comment_writer_id, comment_writer, comment_time,
             comment_text) = spider.get_comments(status_id[i])

            for j in range(len(comment_text)):
                if comment_writer_id[j] == int(user_id):
                    name = comment_writer[j].encode('utf-8')
                    time = comment_time[j].encode('utf-8')
                    text = comment_text[j].encode('utf-8')
    
                    out_file.write(name + ' ' + writer + ' ' + 
                                   time + ' ' + text + '\n')

    out_file.close()
    





