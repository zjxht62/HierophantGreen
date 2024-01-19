## Pytest用例管理框架如何执行

1. 命令行
2. 主函数

```python
import pytest

if __name__ == '__main__':
    pytest.main()
```

3. 通过配置文件`pytest.ini`来改变以及执行测试用例  
   **不管是命令行还是主函数，都会读取pytest.ini配置文件来执行。**

## Pytest用例管理框架的前后置操作（固件、夹具）

```python

def setup_method(self):
    print('每个用例前执行')


def teardown_method(self):
    print('每个用例后执行')


def setup_class(self):
    print('每个类前执行')


def teardown_class(self):
    print('每个类后执行')
```

更强大的前后置：fixture 固件

装饰器：  
`@pytest.fixture(scope='作用域',params='参数',autouse='自动执行', ids='参数别名', name=’固件别名‘)`

+ scope：function（默认）、class、module、session（整个测试会话，从pytest启动到退出）
+ params：参数化['mysql','redis']
  + 需要使用request参数和yield request.param
+ autouse：自动执行Ture/False
+ ids：参数别名
+ name：fixture别名，用了之后原名称失效 

## 接口关联封装（基于一个独立的yaml文件）
```yaml
-
  feature: 模块
  story: 接口
  title: 用例标题
  request:
    method: post
    url: https://api.weixin.qq.com/cgi-bin/tags/update
    headers: null
    params: {'access_token': access_token}
    json: {"tag": {"id": 5075, 'name': '广东人'}}
  validate: 断言
```
实现方式
```python
    # 使用pytest的参数化注解读取yaml，其中yaml最外层是一个列表，正好每个列表元素作为caseinfo传到测试函数中
    @pytest.mark.parametrize('caseinfo', read_yaml_testcase('testcases/test_select_flag.yaml'))
    def test_select_flag(self, caseinfo):
        # 从读入的yaml中，取对应的值
        method = caseinfo['request']['method']
        urls = caseinfo['request']['url']
        datas = caseinfo['request']['params']
        # 某些值暂时无法动态从yaml获取，还得手动从存储中间变量的yaml中取
        datas['access_token'] = read_yaml('access_token')
        RequestsUtil().send_all_request(method=method, url=urls, params=datas)
```
## 数据驱动1
@pytest.mark.parametrize('caseinfo', read_yaml_testcase('testcases/test_select_flag.yaml'))

存在的问题：
+ 如果有接口关联，那么在下一个接口里无法直接调用Python中的方法，而是需要在代码里读取并覆盖值
+ 如何在yaml中调用随机数方法
+ 如果一个用例有跟多的反例，那么yaml文件会很冗余 
+ 断言


