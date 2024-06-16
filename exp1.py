import sys

from click.testing import CliRunner
from piptools.scripts.compile import cli as pip_compile


def run_pip_compile(input_file="assets/requirements1.in", output_file="requirements.txt"):
    runner = CliRunner()
    result = runner.invoke(pip_compile, [input_file, "--output-file", output_file])

    if result.exit_code == 0:
        print(f"Successfully compiled {input_file} to {output_file}")
    else:
        print(f"Failed to compile {input_file}. Error: {result.output}")
        sys.exit(result.exit_code)


if __name__ == "__main__":
    run_pip_compile()
