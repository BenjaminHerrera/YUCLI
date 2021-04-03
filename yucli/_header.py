def header(header_type, time):
    """ Header Format Method

    :param header_type: [STRING] Type of header to display
    :param time: [STRING] Date to format into header
    :return: [STRING] Formatted header
    """
    # List of possible headers
    headers = {
        "USER": "[b]&bl;USER {}&br;[/b] >> ",
        "INFO": "[b]&bl;INFO {}&br;[/b] >> ",
        "WARN": "[b]&bl;[color=FFFF00]WARN[/color] {}&br;[/b] >> ",
        "FAIL": "[b]&bl;[color=FF0000]FAIL[/color] {}&br;[/b] >> ",
        "PASS": "[b]&bl;[color=00FF00]PASS[/color] {}&br;[/b] >> ",
        "DEAD": "[b]&bl;[color=8B0000]DEAD[/color] {}&br;[/b] >> ",
    }

    # Returns formatted header
    return headers[header_type].format(time)