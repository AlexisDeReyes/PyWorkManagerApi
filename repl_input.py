from sys import argv


def run_from_repl_separate_args(func_to_run, converter, *defaultArgs):
    if len(argv) > 1:
        return func_to_run(converter(argv[1]))
    if defaultArgs:
        return func_to_run(defaultArgs[0])
    return func_to_run()
