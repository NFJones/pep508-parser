# pep508-parser

A parser for the [PEP508](https://www.python.org/dev/peps/pep-0508/) dependency specification.

# Example
```python
#!/usr/bin/env python3

from pep508_parser import parser

tests = [
    "A",
    "A.B-C_D",
    "aa",
    "name",
    "name<=1",
    "name>=3",
    "name>=3,<2",
    "name@http://foo.com",
    "name [fred,bar] @ http://foo.com ; python_version=='2.7'",
    "name[quux, strange];python_version<'2.7' and platform_version=='2'",
    "name; os_name=='a' or os_name=='b'",
    # Should parse as (a and b) or c
    "name; os_name=='a' and os_name=='b' or os_name=='c'",
    # Overriding precedence -> a and (b or c)
    "name; os_name=='a' and (os_name=='b' or os_name=='c')",
    # should parse as a or (b and c)
    "name; os_name=='a' or os_name=='b' and os_name=='c'",
    # Overriding precedence -> (a or b) and c
    "name; (os_name=='a' or os_name=='b') and os_name=='c'",
]


def main():
    for test in tests:
        parsed = parser.parse(test)
        print("{} -> {}".format(test, parsed))


if __name__ == '__main__':
    main()
```
