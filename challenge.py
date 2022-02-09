import time
from datetime import datetime, timedelta

from num2words import num2words


# Todo: returns an timedelta:
def calculate_time(sleep_time: float) -> timedelta:
    """Function to calculate time to perform it's action,
    which is takes a .

    Args:
        sleep_time (float) : Time that the function will take to be executed.

    Returns:
        string: A string containing the time needed to execute the loop
                in the format hours:minutes:seconds.milliseconds
    """
    start_time = datetime.now()

    time.sleep(sleep_time)

    end_time = datetime.now()

    difference_time_function = end_time - start_time

    return difference_time_function


def split_time(time: timedelta) -> dict:
    """This function takes the time and create a dictionary from it with the splitted values

    Args:
        time(str) : The time that the function took to be performed.

    Returns:
        splitted_time(dict): A dictionary containing how many hours, minutes, seconds and milliseconds are 			   inside the time argument.
    """

    seconds = time.seconds
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    microseconds = time.microseconds

    # timer = time.split(":")
    # sec = timer[2].split(".")

    splitted_time = {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "milliseconds": microseconds,
    }

    return splitted_time


def readable_time(splitted_time: dict) -> str:
    """This function gets a dictionary containing hours, minutes, seconds and milliseconds and
    translate these numbers to a human comprehension

    Args:
        splitted_time(dict): Dictionary containing hours, minutes, seconds and milliseconds.

    Returns:
        str: How long the operation took to be performed in a human perspective.
    """

    hours = splitted_time["hours"]
    minutes = splitted_time["minutes"]
    seconds = splitted_time["seconds"]
    milliseconds = splitted_time["milliseconds"]
    readable_time = ""

    if hours > 0:
        descriptive_hours = num2words(hours)
        if hours == 1:
            support = "hour"
        else:
            support = "hours"
        readable_time += f"{descriptive_hours} {support}, "

    if minutes > 0:
        if minutes == 1:
            support = "minute"
        else:
            support = "minutes"
        descriptive_minutes = num2words(minutes)
        readable_time += f"{descriptive_minutes} {support} and "

    if seconds > 0:
        descriptive_seconds = num2words(seconds)
        if seconds == 1:
            support = "second"
        else:
            support = "seconds"

        readable_time += f"{descriptive_seconds} {support}"

    if milliseconds > 0 and minutes < 1:
        milli = str(milliseconds)
        rounded_milliseconds = milli[0:2]
        if int(rounded_milliseconds) == 1:
            support = "millisecond"
        else:
            support = "milliseconds"

        descriptive_milliseconds = num2words(rounded_milliseconds)
        readable_time += f" and {descriptive_milliseconds} {support}"

    return (
        f"Your function took {readable_time} to run ({time_to_run_function})"
    )


if __name__ == "__main__":
    sleep_time = 1.5
    time_to_run_function = calculate_time(sleep_time)
    splitted_time = split_time(time_to_run_function)
    human_time = readable_time(splitted_time)
    print(human_time)
