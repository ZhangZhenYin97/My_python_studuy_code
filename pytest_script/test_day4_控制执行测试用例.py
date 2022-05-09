'''
1.在第N个用例失败后，结束测试执行
pytest -x                    # 第01次失败，就停止测试
pytest --maxfail=2     # 出现2个失败就终止测试

2.指定测试模块
pytest test_mod.py

3.指定测试目录
pytest testing/

4.通过关键字表达式过滤执行
pytest -k "MyClass and not method"

5.通过 node id 指定测试用例
nodeid由模块文件名、分隔符、类名、方法名、参数构成，举例如下：
运行模块中的指定用例
pytest test_mod.py::test_func
ytest test_mod.py::TestClass::test_method

6.通过标记表达式执行
pytest -m slow
这条命令会执行被装饰器 @pytest.mark.slow 装饰的所有测试用例

7.通过包执行测试
pytest --pyargs pkg.testing
这条命令会自动导入包 pkg.testing，并使用该包所在的目录，执行下面的用例。
'''