DIFFSTATS_COLUMNS = [
    "experiment_id", "run_id", "iteration_id",
    "src_added", "src_removed",
    "md_added", "md_removed",
    "total_added", "total_removed",
]
DIFFSTATS_INT_COLUMNS = [
    "run_id", "iteration_id",
    "src_added", "src_removed",
    "md_added", "md_removed",
    "total_added", "total_removed",
]
DIFFSTATS_FILENAME_PATTERN = r"^(?P<experiment_id>.+)--diffstats\.csv$"
