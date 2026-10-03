"""Run with python -m churn --config config.yaml."""

import argparse
import json

from churn.config import load_config
from churn.pipeline import run


def main() -> None:
    """Resolve configuration and print the persisted run summary."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()
    print(json.dumps(run(load_config(args.config)), indent=2))


if __name__ == "__main__":
    main()
