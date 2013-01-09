sina weibo comments spider
===========

+ extract weibo user's basic information, such as _statuses_ _comments_.
this is official documentation[1].


weibo
------------------

+ sina weibo python SDK and some examples[2]


spider
--------------------

+ collect any user's followeing list persons' top 100 _statuses_ and then get top 50 _comments_, at last I grab the comments that I need.

Usage:

    python spider.py


question
---------------

+ KeyError: 'user' in `status_writer.append(each_status.user.screen_name)` after run a few hours.








[1]: http://open.weibo.com/wiki/API%E6%96%87%E6%A1%A3_V2
[2]: http://code.google.com/p/sinaweibopy/wiki/OAuth2
