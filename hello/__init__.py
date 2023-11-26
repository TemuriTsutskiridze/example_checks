import check50


@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def testoto():
    """hello world"""
    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)

