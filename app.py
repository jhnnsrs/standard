from arkitekt import register

@register
def test_gpu(hello: str) -> None:
    """Hello World

    Prints hello world

    Args:
        hello (str): The hello world string
    """
    print("Hello world")