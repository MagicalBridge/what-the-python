"""
在 Python 中，标识符是用于命名变量、函数、类、模块和其他对象的名称。标识符的命名规则如下：

### 标识符命名规则：
1. **字母和下划线开头**：标识符必须以字母（大写或小写）或下划线（`_`）开头。
2. **后续字符**：标识符可以包含字母、数字（0-9）和下划线（`_`）。
3. **区分大小写**：Python 是区分大小写的，因此 `myVar` 和 `myvar` 是两个不同的标识符。
4. **不能使用关键字**：标识符不能是 Python 的关键字（保留字），例如 `if`、`else`、`while`、`for` 等。
5. **不能使用内置函数名**：标识符不能是 Python 的内置函数名或模块名，例如 `print`、`len`、`str` 等。

### 示例：
以下是一些合法的标识符示例：
- `myVar`
- `_var`
- `var123`
- `MyClass`
- `__private_var`

以下是一些非法的标识符示例：
- `123var` （以数字开头）
- `my-var` （包含非法字符 `-`）
- `if` （Python 关键字）
- `print` （内置函数名）

### Python 关键字：
Python 关键字是保留字，不能用作标识符。以下是 Python 3.x 中的关键字列表：

```python
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```
### 总结：
标识符在 Python 中用于命名各种对象，如变量、函数、类等。标识符必须遵循特定的命名规则，并且不能使用 Python 的关键字或内置函数名。

"""