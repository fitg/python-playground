import time


def hello_world():
    return "Hello World!"


def why_python():
    return """
        Tcl -- It is short (only three letters) and does a suprising
            amount given that it doesn't have a vowel.  It can be
            pronounced "Tickle", which is a command.

        Perl -- Bigger and has a vowel.  However you'll note that it isn't
            a common english word; you'll have to know what you're doing to
            use it, especially with spell-checkers which otherwise complain
            that it looks like noise.

        Python -- This is a Real English Word (honest, look it up!) that
            happens to refer to a type of snake, which you'll notice is an
            object.  With the two vowels, python is quite readable.
    """


def _add_elements(element=[]):
    element.append("New")
    return element


def mutable_default_attributes():
    _add_elements()

    return _add_elements()


def _range(alphabet: str):
    output = ""
    start = time.time()
    for i in range(len(alphabet)):
        output += alphabet[i]

    end = time.time()
    exec_time = end - start
    return exec_time, output


def _enumerator(alphabet: str):
    output = ""
    start = time.time()
    for i, letter in enumerate(alphabet):
        output += letter

    end = time.time()
    exec_time = end - start
    return exec_time, output


def _no_specials(alphabet: str):
    output = ""
    start = time.time()
    for letter in alphabet:
        output += letter

    end = time.time()
    exec_time = end - start
    return exec_time, output


def enumerator_over_range():
    # initialize alphabet
    alphabet_array = list(map(chr, range(ord("a"), ord("z") + 1)))
    # run different algoritms and measure them
    r_time, alphabet_ranges = _range(alphabet_array)
    e_time, alphabet_enumerate = _enumerator(alphabet_array)
    ns_time, alphabet_nospecials = _no_specials(alphabet_array)

    return f"""Enumerate alphabet: {alphabet_enumerate}; Time: {e_time}s
Range alphabet: {alphabet_ranges}; Time: {r_time}s
No Specials alphabet: {alphabet_nospecials}; Time: {ns_time}s"""


def run_lesson_one():
    return f"""
    1. Simple Hello World
    {hello_world()}
    #######################################
    2. Why Python?
    {why_python()}
    #######################################
    3. Mutable default attributes - what do you get after calling
    a method with _add_elements(element=[]) more than once?
    {mutable_default_attributes()}
    #######################################
    Is Enumerator better optimized than range?
    {enumerator_over_range()}
    Yes, but if you dont need that index just use in <collection> syntax
    #######################################
    """
