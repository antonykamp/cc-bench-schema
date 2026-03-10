BENCHMARK_COLUMNS = ["experiment_id", "run_id", "iteration_id", "outer_iteration_id", "runtime_us"]
BENCHMARK_INT_COLUMNS = ["run_id", "iteration_id", "outer_iteration_id", "runtime_us"]
BENCHMARK_FILENAME_PATTERN = r"^(?P<experiment_id>.+)--run-(?P<run_id>\d+)--iteration-(?P<iteration_id>\d+)--(?P<benchmark>.+)\.csv$"
