sina weibo comments spider
===========

+ extract weibo user's basic information, such as _statuses_ _comments_.
this is official documentation[1].

weibo.py
------------------

+ sina weibo python SDK and some examples[2]


spider.py
--------------------

+ Collect any user's followeing list persons' top 100 _statuses_ and then get top 50 _comments_, at last I grab the comments that I need

Usage:

    python spider.py
    

difficult points
---------------

+ the total number of _requests_ is only 1000 times/hour for a test user, so I can't get more information
+ error 10023  user requests out of rate limit

BTW
---------------

+ sina weibo Python SDK has lots of bug

[1]: http://open.weibo.com/wiki/API%E6%96%87%E6%A1%A3_V2
[2]: http://code.google.com/p/sinaweibopy/wiki/OAuth2

