def format_elapsed_time(elapsed_seconds):
    """Format elapsed time as seconds only if under 60 seconds, else minutes and seconds with seconds to 2 decimal places."""
    if elapsed_seconds < 60:
        return f"{elapsed_seconds:.2f} seconds"
    else:
        minutes = int(elapsed_seconds // 60)
        seconds = elapsed_seconds % 60
        return f"{minutes} minutes, {seconds:.2f} seconds"
