## 蚂蚁学社

西安电子科技大学学习互助社团

[![Build Status](https://travis-ci.com/windard/AntClub.svg?token=spobLW7cfpqx95SyUxyc&branch=master)](https://travis-ci.org/windard/AntClub)


### 总结

flask-login 中可以自定义 ValidationError 作为验证信息，但是这个验证信息使用 flask-wtf 自定义的表单样式就可以显示出来，如果自行定义就无法显示，不能做很好的自定义表单和 ajax。一直以为是在 flask-wtf 和 wtforms 这两个库中找寻，结果只看到定义 ValidationError ，而没有看到捕获异常的地方。终于在 flask-bootstrap 中看到 filed.error 属性，查看 flask 的 form 表单的 _fields 中每一个 filed 的属性，才终于明白，在定义了 ValidationError 之后，flask 会将验证消息放在 每一个 filed 的 error 属性中，flask-bootstrap 如果在看到 error 信息时就会对其进行处理。

这样的话，如果想要进行处理的话，如果想要使用 ajax 还是比较困难，因为错误信息无法直接得到，只能得到一个包含 错误信息的 form 表单，除非直接将 form 表单发送过去，或者是将 form 表单在后台进行处理，找到错误信息进行组合之后使用 json 发送过去。无法直接发送 form 表单，那如果还要使用 ajax 的话就只能在后台先将表单进行处理，找到错误信息，然后将错误信息发送过去了。。。

但是觉得这样也有不好的地方，比如说，这样使用 ajax 的话，如果没有验证码，那么每一次使用 ajax 都是可以的，因为 CSRF 没有进行修改，使用一次的 CSRF 进行多次发送。。。这样当时是不应该可以的吖，应该每一次都是使用新的 CSRF token ，使用 ajax 的话，不好更改 token。

2017-3-24

csrf 不是这样用的，可以使用 ajax，因为没有验证码，所以使用登陆次数限制，在十分钟之内登陆错误次数不能超过五次。

使用 redis 做登陆次数限制
使用 Celery 做任务队列发送邮件
使用 pytest 做测试
使用 Travis CI 做集成开发

2017-3-25

1. 使用 mysql+pymysql 而不再使用 仅单独使用 MySQLdb，装不上。
2. 没有验证码，pillow 不好装
3. 不是不好装，而是需要先装一些，还好这些库是可以装上的
