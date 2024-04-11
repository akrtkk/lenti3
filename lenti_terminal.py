import os
import tkinter as tk
from colorama import Fore, init
from cryptography.fernet import Fernet
import gzip
import random
import math
import platform
import psutil
import time # Add this import
import datetime
import webbrowser   # Add this import
import sys
import re   # Add this import
import getpass

# Initialize colorama
init()

class Interpreter:
    def __init__(self):
        self.commands = {
            "print": lambda tokens: self.print_message(tokens),
            "help": lambda _: self.show_help(),
            "add": lambda tokens: self.add_numbers(tokens),
            "read": self.read_file,
            "write": self.write_file,
            "append": self.append_file,
            "copy": self.copy_file,
            "rename": self.rename_file,
            "delete": self.delete_file,
            "browse": self.open_browser,
            "list": self.list_files,
            "create": self.create_file,
            "mkdir": self.create_directory,
            "pwd": self.show_current_directory,
            "cd": self.change_directory,
            "clear": self.clear_screen,
            "calculator": self.calculator,
            "search": self.search_files,
            "uptime": self.system_uptime,
            "cpuinfo": self.cpu_info,
            "meminfo": self.memory_info,
            "diskinfo": self.disk_info,
            "networkinfo": self.network_info,
            "datetime": self.current_datetime,
            "echo": self.echo,
            "exit": self.exit_terminal,
            "encrypt": self.encrypt_file,
            "decrypt": self.decrypt_file,
            "compress": self.compress_file,
            "decompress": self.decompress_file,
            "sort": self.sort_file,
            "shuffle": self.shuffle_file,
            "reverse": self.reverse_file,
            "count": self.count_file,
            "wordcount": self.word_count_file,
            "linecount": self.line_count_file,
            "md5sum": self.md5sum_file,
            "sha1sum": self.sha1sum_file,
            "sha256sum": self.sha256sum_file,
            "permissions": self.file_permissions,
            "size": self.file_size,
            "version": self.python_version,
            "prime": self.prime_numbers,
            "fibonacci": self.fibonacci_sequence,
            "gcd": self.gcd,
            "lcm": self.lcm,
            "factorial": self.factorial,
            "sqrt": self.square_root,
            "log": self.logarithm,
            "exp": self.exponential,
            "sin": self.sine,
            "cos": self.cosine,
            "tan": self.tangent,
            "arc_sin": self.arc_sine,
            "arc_cos": self.arc_cosine,
            "arc_tan": self.arc_tangent,
            "mean": self.mean,
            "median": self.median,
            "mode": self.mode
        }

    def print_message(self, tokens):
        message = ' '.join(tokens[1:])
        print(Fore.BLUE + message)

    def show_help(self) -> None:
        """
        Prints a list of available commands and their descriptions.

        This method iterates over the commands dictionary and retrieves the command
        name and the docstring of the function that implements the command.

        The commands dictionary maps command names to functions that
        implement the command. For example, the entry for the "print" command
        maps to the `print_message` function.

        Before printing each command and its docstring, this method checks
        that neither the command name nor the docstring are None. If either one
        is None, it raises a ValueError exception.

        If there are no exceptions, it prints each command and its docstring
        using the format string "{cmd} - {desc}".

        If there is an exception, it prints an error message and then raises
        the exception so that the user can get more information about what
        went wrong.

        Returns:
            None
        """
        try:
            for cmd, desc in self.commands.items():
                if cmd is None or desc is None:
                    raise ValueError("Null pointer reference in commands dictionary")
                print(Fore.BLUE + f"{cmd} - {desc.__doc__}")
        except Exception as e:
            print(Fore.RED + f"Error showing help: {e}")
            print(Fore.BLUE + "If you don't see anything obvious, reply that things look good" +
                  " and that the user can reply with a stack trace to get more information.")
            raise e

    def add_numbers(self, tokens):
        result = sum(int(token) for token in tokens[1:])
        print(Fore.BLUE + str(result))

    def read_file(self, tokens):
        """
        Reads the content of a file and prints it.

        The `tokens` parameter should contain the name of the file to read.

        If the length of `tokens` is not equal to 2, this function prints an
        error message to the user and returns without doing anything else.

        If the file does not exist, this function prints an error message
        to the user and returns.

        Otherwise, this function opens the file, reads its contents, and prints
        the contents to the user.

        Returns:
            None
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        if not os.path.exists(filename):
            print(Fore.RED + f"File '{filename}' does not exist")
            return
        with open(filename, 'r') as file:
            print(Fore.BLUE + file.read())

    def write_file(self, tokens):
        if len(tokens) < 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename, *content = tokens[1:]
        with open(filename, 'wb') as file:
            file.write(b' '.join(map(str.encode, content)))
            file.write(content)

    def append_file(self, tokens):
        if len(tokens) < 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        content = ' '.join(tokens[2:])
        with open(filename, 'a') as file:
            file.write(content)

    def copy_file(self, tokens):
        if len(tokens) != 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        source_filename = tokens[1]
        destination_filename = tokens[2]
        if not os.path.exists(source_filename):
            print(Fore.RED + f"Source file '{source_filename}' does not exist")
            return
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
            with open(destination_filename, 'w') as destination_file:
                destination_file.write(content)

    def rename_file(self, tokens):
        if len(tokens) != 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        old_filename = tokens[1]
        new_filename = tokens[2]
        if not os.path.exists(old_filename):
            print(Fore.RED + f"File '{old_filename}' does not exist")
            return
        os.rename(old_filename, new_filename)

    def delete_file(self, tokens):
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        if not os.path.exists(filename):
            print(Fore.RED + f"File '{filename}' does not exist")
            return
        os.remove(filename)

    def open_browser(self, tokens):
        if len(tokens) != 2:
            return
        url = tokens[1]
        webbrowser.open(url)

    def list_files(self, tokens):
        path = '.' if len(tokens) < 2 else tokens[1]
        for item in os.listdir(path):
            print(Fore.BLUE + item)

    def create_file(self, tokens):
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'w'):
            pass

    def create_directory(self, tokens):
        """
        Creates a new directory.
        If the directory already exists, nothing happens.
        If the directory could not be created because of a permissions issue,
        an exception is thrown.
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        directory = tokens[1]
        # if directory is None, os.makedirs will raise a TypeError
        if directory is None:
            print(Fore.RED + "Invalid argument. Directory name cannot be None.")
            return
        try:
            os.makedirs(directory)
        except FileExistsError:
            # do nothing if the directory already exists
            pass
        except PermissionError:
            print(Fore.RED + f"Permission denied. Could not create directory '{directory}'.")
            # raise the exception to get a stack trace if needed
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred while creating directory '{directory}'.")
            raise e

    def show_current_directory(self, _):
        try:
            current_directory = os.getcwd()
            if current_directory is None:
                raise ValueError("os.getcwd() returned None")
            print(Fore.BLUE + current_directory)
        except Exception as e:
            print(Fore.RED + f"Error showing current directory: {e}")
            raise e


    def change_directory(self, tokens):
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        directory = tokens[1]
        os.chdir(directory)

    def clear_screen(self, _):
        os.system('cls' if os.name == 'nt' else 'clear')

    def calculator(self, _):
        tk.Tk().mainloop()

    def search_files(self, tokens):
        if len(tokens) != 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        directory = tokens[1]
        filename_pattern = tokens[2]
        for root, _, files in os.walk(directory):
            for file in files:
                if filename_pattern in file:
                    print(Fore.BLUE + os.path.join(root, file))

    def system_uptime(self, _):
        """
        Check for bugs such as null pointer references, unhandled exceptions,
        and more. If you don't see anything obvious, reply that things look good
        and that the user can reply with a stack trace to get more information.
        """
        try:
            with open('/proc/uptime', 'rb', 0) as f:
                uptime_bytes = f.read(12)
                if uptime_bytes is None:
                    raise ValueError("f.read(12) returned None")
                uptime_str = uptime_bytes.decode()
                uptime_seconds = int(uptime_str.split()[0])
                uptime_hours = uptime_seconds / 3600
                print(Fore.BLUE + f"System uptime: {uptime_hours:.2f} hours")
        except Exception as e:
            print(Fore.RED + f"Error getting system uptime: {e}")
            raise e


    def cpu_info(self, _):
        try:
            cpu_info = platform.processor()
            if cpu_info is None:
                raise ValueError("platform.processor() returned None")
            print(Fore.BLUE + cpu_info)
        except Exception as e:
            print(Fore.RED + f"Error getting CPU info: {e}")
            raise e

    def memory_info(self, _):
        try:
            mem_info = psutil.virtual_memory()
            print(Fore.BLUE + str(mem_info))
        except Exception as e:
            print(Fore.RED + f"Error getting memory info: {e}")
            raise e

    def disk_info(self, _):
        try:
            os.system('wmic logicaldisk get caption,description,filesystem,size,freespace')
        except Exception as e:
            print(Fore.RED + f"Error getting disk info: {e}")
            raise e

    def network_info(self, _):
        try:
            os.system('ipconfig')
        except Exception as e:
            print(Fore.RED + f"Error getting network info: {e}")
            raise e

    def current_datetime(self, _):
        try:
            current_datetime = datetime.now()
            print(Fore.BLUE + current_datetime.strftime("%c"))
        except Exception as e:
            print(Fore.RED + f"Error getting current date and time: {e}")
            raise e

    def echo(self, tokens):
        print(Fore.BLUE, end='')
        print(*tokens[1:], sep=' ')

    def exit_terminal(self, _):
        exit()

    # Additional functionalities

    def encrypt_file(self, tokens):
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return

        filename = tokens[1]

        if not os.path.exists(filename):
            print(Fore.RED + "File not found")
            return

        try:
            with open(filename, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            print(Fore.RED + "File not found")
            return

    def decrypt_file(self, tokens):
        """
        Decrypts a file encrypted using Fernet symmetric encryption.
        Usage: decrypt <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'rb') as f:
            encrypted_data = f.read()
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        with open(filename[:-4], 'wb') as f:
            f.write(decrypted_data)
        print(Fore.BLUE + f"{filename} decrypted successfully.")

    def compress_file(self, tokens):
        """
        Compresses a file using gzip compression.
        Usage: compress <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'rb') as f:
            data = f.read()
        with gzip.open(filename + '.gz', 'wb') as f:
            f.write(data)
        print(Fore.BLUE + f"{filename} compressed successfully.")

    def decompress_file(self, tokens):
        """
        Decompresses a file compressed using gzip compression.
        Usage: decompress <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with gzip.open(filename, 'rb') as f:
            data = f.read()
        with open(filename[:-3], 'wb') as f:
            f.write(data)
        print(Fore.BLUE + f"{filename} decompressed successfully.")

    def sort_file(self, tokens):
        """
        Sorts the lines in a file in lexicographical order.
        Usage: sort <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines.sort()
        with open(filename, 'w') as f:
            f.writelines(lines)
        print(Fore.BLUE + f"{filename} sorted successfully.")

    def shuffle_file(self, tokens):
        """
        Shuffles the lines in a file randomly.
        Usage: shuffle <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'r') as f:
            lines = f.readlines()
        random.shuffle(lines)
        with open(filename, 'w') as f:
            f.writelines(lines)
        print(Fore.BLUE + f"{filename} shuffled successfully.")

    def reverse_file(self, tokens):
        """
        Reverses the content of a file.
        Usage: reverse <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'r') as f:
            content = f.read()
        with open(filename, 'w') as f:
            f.write(content[::-1])
        print(Fore.BLUE + f"{filename} content reversed successfully.")

    def count_file(self, tokens):
        """
        Counts the number of characters in a file.
        Usage: count <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'r') as f:
            content = f.read()
        print(Fore.BLUE + f"Number of characters in {filename}: {len(content)}")

    def word_count_file(self, tokens):
        """
        Counts the number of words in a file.
        Usage: wordcount <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'r') as f:
            content = f.read()
        word_count = len(content.split())
        print(Fore.BLUE + f"Number of words in {filename}: {word_count}")

    def line_count_file(self, tokens):
        """
        Counts the number of lines in a file.
        Usage: linecount <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        with open(filename, 'r') as f:
            line_count = sum(1 for _ in f)
        print(Fore.BLUE + f"Number of lines in {filename}: {line_count}")

    def md5sum_file(self, tokens):
        """
        Computes the MD5 checksum of a file.
        Usage: md5sum <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        import hashlib
        filename = tokens[1]
        with open(filename, 'rb') as f:
            md5_hash = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        print(Fore.BLUE + f"MD5 checksum of {filename}: {md5_hash.hexdigest()}")

    def sha1sum_file(self, tokens):
        """
        Computes the SHA-1 checksum of a file.
        Usage: sha1sum <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        import hashlib
        filename = tokens[1]
        with open(filename, 'rb') as f:
            sha1_hash = hashlib.sha1()
            for chunk in iter(lambda: f.read(4096), b""):
                sha1_hash.update(chunk)
        print(Fore.BLUE + f"SHA-1 checksum of {filename}: {sha1_hash.hexdigest()}")

    def sha256sum_file(self, tokens):
        """
        Computes the SHA-256 checksum of a file.
        Usage: sha256sum <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        import hashlib
        filename = tokens[1]
        with open(filename, 'rb') as f:
            sha256_hash = hashlib.sha256()
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        print(Fore.BLUE + f"SHA-256 checksum of {filename}: {sha256_hash.hexdigest()}")

    def file_permissions(self, tokens):
        """
        Displays the permissions of a file.
        Usage: permissions <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        import stat
        filename = tokens[1]
        permissions = oct(os.stat(filename).st_mode & stat.S_IMODE(os.lstat(filename).st_mode))
        print(Fore.BLUE + f"Permissions of {filename}: {permissions}")

    def file_size(self, tokens):
        """
        Displays the size of a file.
        Usage: size <filename>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        filename = tokens[1]
        size = os.path.getsize(filename)
        print(Fore.BLUE + f"Size of {filename}: {size} bytes")

    def python_version(self, _):
        """
        Displays the Python version.
        Usage: version
        """
        import sys
        print(Fore.BLUE + f"Python version: {sys.version}")

    def prime_numbers(self, tokens):
        """
        Generates prime numbers up to a given number.
        Usage: prime <limit>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        limit = int(tokens[1])
        primes = [2]
        for number in range(3, limit + 1, 2):
            if all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1)):
                primes.append(number)
        print(Fore.BLUE + "Prime numbers:", primes)

    def fibonacci_sequence(self, tokens):
        """
        Generates Fibonacci sequence up to a given number.
        Usage: fibonacci <limit>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        limit = int(tokens[1])
        fibonacci_seq = [0, 1]
        while fibonacci_seq[-1] + fibonacci_seq[-2] <= limit:
            fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
        print(Fore.BLUE + "Fibonacci sequence:", fibonacci_seq)

    def gcd(self, tokens):
        """
        Computes the greatest common divisor of two numbers.
        Usage: gcd <num1> <num2>
        """
        if len(tokens) != 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        while num2:
            num1, num2 = num2, num1 % num2
        print(Fore.BLUE + f"GCD: {num1}")

    def lcm(self, tokens):
        """
        Computes the least common multiple of two numbers.
        Usage: lcm <num1> <num2>
        """
        if len(tokens) != 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        lcm = num1 * num2 // math.gcd(num1, num2)
        print(Fore.BLUE + f"LCM: {lcm}")

    def factorial(self, tokens):
        """
        Computes the factorial of a number.
        Usage: factorial <number>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        num = int(tokens[1])
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(Fore.BLUE + f"Factorial: {factorial}")

    def square_root(self, tokens):
        """
        Computes the square root of a number.
        Usage: sqrt <number>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        num = float(tokens[1])
        sqrt = math.sqrt(num)
        print(Fore.BLUE + f"Square root: {sqrt}")

    def logarithm(self, tokens):
        """
        Computes the logarithm of a number with given base.
        Usage: log <number> <base>
        """
        if len(tokens) != 3:
            print(Fore.RED + "Invalid number of arguments")
            return
        num = float(tokens[1])
        base = float(tokens[2])
        log = math.log(num, base)
        print(Fore.BLUE + f"Logarithm: {log}")

    def exponential(self, tokens):
        """
        Computes the exponential of a number.
        Usage: exp <number>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        num = float(tokens[1])
        exp = math.exp(num)
        print(Fore.BLUE + f"Exponential: {exp}")

    def sine(self, tokens):
        """
        Computes the sine of an angle in radians.
        Usage: sin <angle>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        angle = float(tokens[1])
        sin = math.sin(math.radians(angle))
        print(Fore.BLUE + f"Sine: {sin}")

    def cosine(self, tokens):
        """
        Computes the cosine of an angle in radians.
        Usage: cos <angle>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        angle = float(tokens[1])
        cos = math.cos(math.radians(angle))
        print(Fore.BLUE + f"Cosine: {cos}")

    def tangent(self, tokens):
        """
        Computes the tangent of an angle in radians.
        Usage: tan <angle>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        angle = float(tokens[1])
        tan = math.tan(math.radians(angle))
        print(Fore.BLUE + f"Tangent: {tan}")

    def arc_sine(self, tokens):
        """
        Computes the arcsine of a value.
        Usage: arc_sin <value>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        value = float(tokens[1])
        arc_sin = math.degrees(math.asin(value))
        print(Fore.BLUE + f"Arcsine: {arc_sin}")

    def arc_cosine(self, tokens):
        """
        Computes the arccosine of a value.
        Usage: arc_cos <value>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        value = float(tokens[1])
        arc_cos = math.degrees(math.acos(value))
        print(Fore.BLUE + f"Arccosine: {arc_cos}")

    def arc_tangent(self, tokens):
        """
        Computes the arctangent of a value.
        Usage: arc_tan <value>
        """
        if len(tokens) != 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        value = float(tokens[1])
        arc_tan = math.degrees(math.atan(value))
        print(Fore.BLUE + f"Arctangent: {arc_tan}")

    def mean(self, tokens):
        """
        Computes the mean (average) of a list of numbers.
        Usage: mean <num1> <num2> ...
        """
        if len(tokens) < 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        numbers = [float(num) for num in tokens[1:]]
        mean = sum(numbers) / len(numbers)
        print(Fore.BLUE + f"Mean: {mean}")

    def median(self, tokens):
        """
        Computes the median of a list of numbers.
        Usage: median <num1> <num2> ...
        """
        if len(tokens) < 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        numbers = sorted([float(num) for num in tokens[1:]])
        n = len(numbers)
        if n % 2 == 0:
            median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
        else:
            median = numbers[n // 2]
        print(Fore.BLUE + f"Median: {median}")

    def mode(self, tokens):
        """
        Computes the mode of a list of numbers.
        Usage: mode <num1> <num2> ...
        """
        if len(tokens) < 2:
            print(Fore.RED + "Invalid number of arguments")
            return
        numbers = [float(num) for num in tokens[1:]]
        freq_dict = {}
        for num in numbers:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        max_freq = max(freq_dict.values())
        mode = [num for num, freq in freq_dict.items() if freq == max_freq]
        print(Fore.BLUE + f"Mode: {mode}")

def login():
    username = input(Fore.GREEN + "Username: ")
    password = getpass.getpass(Fore.GREEN + "Password: ")
    if username == "davu" and password == "davu123":
        print(Fore.GREEN + "Login successful")
    else:
        print(Fore.RED + "Invalid credentials")
        sys.exit()

if __name__ == "__main__":
    interpreter = Interpreter()
    login()
    while True:
        command = input(Fore.GREEN + "davu@davu-PC~ $ ")
        tokens = command.split()
        if tokens and tokens[0] in interpreter.commands:
            interpreter.commands[tokens[0]](tokens)
        else:
            print(Fore.RED + "Invalid command. Type 'help' to see the list of available commands.")
            