import argparse
from dataclasses import dataclass

import awswrangler as wr
import loguru

print("argparse version: ", argparse.__version__)
print(f"awswrangler version: {wr.__version__}")
print(f"loguru version: {loguru.__version__}")

parser = argparse.ArgumentParser()
parser.add_argument("bar", type=str, default="foo")
parser.parse_args()


@dataclass()
class Foo:
    bar: str

    def foo(bar: str) -> str:
        """Summary line.

        Extended description of function.

        Args:
            bar: Description of input argument.

        Returns:
            Description of return value
        """
        loguru.logger.info(f"awswrangler version: {wr.__version__}")
        loguru.logger.info("Hello World!")
        loguru.logger.info(bar)
        return bar


if __name__ == "__main__":
    Foo(bar=parser.parse_args().bar).foo()
