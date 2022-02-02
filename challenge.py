import datetime
from num2words import num2words

number = 99999


def calculate_time(number:int) -> str:
    """Function to calculate time to perform it's action,
    which is execute a loop and print results on screen.

    Args:
        number(int) : Number of loop interations to be performed.

    Returns:
        string: A string containing the time needed to execute the loop
                in the format hours:minutes:seconds.milliseconds
    """
    start_time = datetime.datetime.now()

    result = 0

    for number in range(0, number + 1):
        print(number)

    end_time = datetime.datetime.now()

    difference_time_function = end_time - start_time

    print("#" * 60)

    return str(difference_time_function)


def split_time(time) -> dict:
    """This function takes the time and create a dictionary from it with the splitted values

    Args:
        time(str) : The time that the function took to be performed.

    Returns:
        dictionary: A dictionary containing how many hours, minutes, seconds and milliseconds are 			   inside the time argument.
    """

    timer = time.split(":")
    sec = timer[2].split(".")

    time = {
        "hours": int(timer[0]),
        "minutes": int(timer[1]),
        "seconds": int(sec[0]),
        "milliseconds": int(sec[1]),
    }

    return time


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
        readable_time += f"{descriptive_minutes} {support}, "

    if seconds > 0:
        descriptive_seconds = num2words(seconds)
        if seconds == 1:
            support = "second"
        else:
            support = "seconds"

        readable_time += f"{descriptive_seconds} {support} and "

    if milliseconds > 0:
        milli = str(milliseconds)
        rounded_milliseconds = milli[0:2]
        if int(rounded_milliseconds) == 1:
            support = "millisecond"
        else:
            support = "milliseconds"

        descriptive_milliseconds = num2words(rounded_milliseconds)
        readable_time += f"{descriptive_milliseconds} {support}"

    return f"Your function took {readable_time} to run"


if __name__ == "__main__":
    time_to_run_function = calculate_time(number)
    splitted_time = split_time(time_to_run_function)
    human_time = readable_time(splitted_time)
    print(human_time)
