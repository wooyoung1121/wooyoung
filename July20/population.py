def read_file(name):
    """
    Reads a file `name`, and returns a list of lines
    First line is column heading
    Real data starts at line number 1
    """
    with open(name, 'r') as file:
        lines = file.readlines()
    return lines


def split_line(line):
    """
    Takes a string, and split into n-parts by splitting it at comma
    'abc, cdv, qqq' is turned into ['abc', 'cdv', 'qqq']
    :param line: 
    :return: 
    """
    return line.split(',')


def tenth_populous_country_name_in_1995(filename):
    """
    Read a file with `filename` in the current directory, line-by-line
    split each line into population for each year (column)
    Find the 10th highest population value in 1995
    :param filename: 
    :return: 
    """
    lines = read_file(filename)
    # write the rest of the function


