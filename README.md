Sina Weibo Comments Spider
===========
Spider.py is a script that can extract weibo user's _comments_ on his or her following list people through official API documents[1].

There are some sina weibo python SDK examples[2]


Explanation
------------
Collect user's following person's top 100 _statuses_ and then get top 50 _comments_, extract the comments of input uid.

Usage:

    python spider.py
    
Then input the _uid_ of any weibo account of which one you choose


Issues
-----------
+ APIerror[3] 10023 User requests out of rate limit
+ Takes long time to dig data
+ APP_KEY will out of date about 7 days 


Contributors
------------
+ @[linzhi] To implement


Todo List
------------
+ Set the appropriate delay time




[1]: http://open.weibo.com/wiki/API%E6%96%87%E6%A1%A3_V2
[2]: http://code.google.com/p/sinaweibopy/wiki/OAuth2
[3]: http://open.weibo.com/wiki/Error_code
[linzhi]: https://github.com/linzhi
