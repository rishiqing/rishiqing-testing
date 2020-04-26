# rishiqing-testing
日事清接口测试python框架v0.1


框架说明
-----
1.framework
框架基本支持，抽象层，包括网络连接、基础用例父类、工具类等。

2.rishiqing
业务逻辑类

入口
-----
<pre>
entry.py
</pre>
entry.py是唯一运行入口

开发环境配置
-----
1.安装pipenv
<pre>
pip install pipenv
</pre>

2.使用pipenv安装依赖
<pre>
pipenv install
</pre>

3.根据使用的IDE自行设置pipenv虚拟环境解释器

ui测试方法
-----
1.使用测试模板case/example.xlsx

2.在模板中编写测试用例

3.在程序中运行测试用例查看结果

ui测试用例说明
-----
遵循json语法，使用css选择器进行选择，一个测试用例的简单示例：
<pre>
[{"action":[{"homePage":""}]},
{"element":"link_text=登录","action":[{"click":""}]},
{"element":"name=username","action":[{"click":""},{"clear":""},{"sendKey":"qy02@qq.com"}]},
{"element":"name=password","action":[{"click":""},{"clear":""},{"sendKey":"rsq123456"}]},
{"element":"css_selector=button:nth-child(5)","action":[{"click":""}]},
{"element":"css=.error-msg > span","action":[{"sleep": 10},{"check":"用户名或密码错误"}]}]
</pre>

ui测试语法详解
-----


