SUMMARY_COLUMNS = [
    "experiment_id", "run_id", "iteration_id", "session_id", "is_sub_agent",
    "sub_agent_type", "total_tool_calls", "read_calls", "glob_calls",
    "edit_calls", "skill_calls", "bash_calls", "grep_calls",
    "total_chars", "thinking_chars", "read_chars", "edit_chars",
    "bash_chars", "skill_chars", "total_tokens", "num_messages",
    "cost_usd", "duration_seconds", "started_at", "ended_at",
]
SUMMARY_INT_COLUMNS = [
    "run_id", "iteration_id", "total_tool_calls", "read_calls", "glob_calls",
    "edit_calls", "skill_calls", "bash_calls", "grep_calls", "total_chars",
    "thinking_chars", "read_chars", "edit_chars", "bash_chars", "skill_chars",
    "total_tokens", "num_messages",
]
SUMMARY_FLOAT_COLUMNS = ["cost_usd", "duration_seconds"]
SUMMARY_BOOL_COLUMNS = ["is_sub_agent"]
SUMMARY_DATETIME_COLUMNS = ["started_at", "ended_at"]
SUMMARY_FILENAME_PATTERN = r"^(?P<experiment_id>.+)--summary\.csv$"
