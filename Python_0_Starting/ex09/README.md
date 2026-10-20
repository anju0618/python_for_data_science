# ft_package

A sample test package.

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

Build (creates `dist/ft_package-0.0.1.tar.gz` and
`dist/ft_package-0.0.1-py3-none-any.whl`):

```sh
uv build
```

or, without uv:

```sh
pip install build
python -m build
```

Install:

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Check:

```sh
pip show -v ft_package
```
