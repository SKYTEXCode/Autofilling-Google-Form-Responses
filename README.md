# Attendance Automation Script

## Overview

This Python script automates the attendance process for students using Selenium, a Python web testing library. It is designed to automatically fill out a certain Google Form link with attendance-related information such as student name, ID, phone number, and details about the course attended.

## Features

- Easy-to-use: Simply run the script and input the required information when prompted.
- Customizable: The script allows users to input data for different courses, sessions, and weeks.
- Multiple Lecturers Support: Handles cases where multiple lecturers may teach the same course.

## Prerequisites

Before running the script, please ensure you have the following:

- Python installed on your machine.
- Required Python libraries: Selenium.

```bash
pip install selenium
```

- ChromeDriver: Ensure the ChromeDriver executable is available and its path is correctly set in the script.

## Usage

1. Run the script:

```bash
python seleniumautomate.py
```

2. Input the required information when prompted.

3. Sit back and relax as the script automates the attendance process.

## Configuration

The script includes a matkuldb dictionary, which stores course-related information. Users can customize this dictionary to add new courses or modify existing ones.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.



**Happy automating!**
