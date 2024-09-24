import awswrangler as wr
import loguru

loguru.logger.info(wr.__version__)


def foo(bar: str) -> str:
    """Summary line.

    Extended description of function.

    Args:
        bar: Description of input argument.

    Returns:
        Description of return value
    """
    return bar
