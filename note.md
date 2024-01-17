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


