# Issues Identified and Fixed

## Lab 5: Static Code Analysis — Digital Wallet & Payment Tracker

## 1. Pylint Issues

**Initial score:** 5.69/10  
**Final score:** 10.00/10

Pylint was used to identify code quality, naming, documentation, and formatting problems.

| Issue                       | Description                                                     | Fix Applied                                                   |
| --------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------- |
| Missing module docstring    | The Python module did not have a suitable description.          | Added a module-level docstring.                               |
| Naming conventions          | Some identifiers did not follow recommended naming conventions. | Updated identifiers where required.                           |
| Missing function docstrings | Functions lacked descriptions.                                  | Added docstrings to functions.                                |
| Mutable default argument    | A mutable default argument was identified.                      | Changed the function definition to avoid the mutable default. |
| Unused parameter            | A function parameter was not used.                              | Renamed the unused parameter with a leading underscore.       |
| Whitespace and formatting   | Some spacing and formatting conventions were not followed.      | Corrected whitespace and formatting.                          |
| Entry-point formatting      | The program entry point required correction.                    | Used the standard `if __name__ == "__main__":` pattern.       |

**Result:** The final Pylint score reached 10.00/10.

## 2. Bandit Security Issues

Bandit initially identified four security-related issues.

| Bandit ID | Severity | Issue                                                    | Fix Applied                                                                     |
| --------- | -------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- |
| B105      | Low      | Hardcoded gateway secret                                 | Replaced the hardcoded secret with an environment variable using `os.getenv()`. |
| B324      | High     | Weak SHA-1 hashing algorithm                             | Replaced SHA-1 with PBKDF2-HMAC-SHA256 using 600,000 iterations.                |
| B306      | Medium   | Insecure `tempfile.mktemp()` function                    | Replaced it with `tempfile.NamedTemporaryFile()` using `delete=False`.          |
| B311      | Low      | Standard pseudo-random generator used for OTP generation | Replaced `random.randint()` with `secrets.randbelow()`.                         |

### Security improvements

- The gateway secret is no longer hardcoded in the source code.
- PIN hashing uses a more computationally expensive password-hashing method.
- Temporary receipt file paths are created using a safer temporary-file API.
- OTP generation uses a cryptographically secure random generator.

**Result:** The final Bandit scan reported no issues.

**Note:** The current PIN hashing implementation uses a fixed salt for this lab demonstration. A production implementation should use a unique random salt per PIN and store the salt with the hash.

## 3. Flake8 Issues

Flake8 identified several PEP 8 style violations during the formatting checks.

| Flake8 ID | Description                                     | Fix Applied                                         |
| --------- | ----------------------------------------------- | --------------------------------------------------- |
| E261      | Insufficient spacing before an inline comment   | Added two spaces before the comment.                |
| E225      | Missing whitespace around an operator           | Corrected operator spacing.                         |
| E231      | Missing whitespace after a comma                | Added the required whitespace.                      |
| E305      | Missing blank lines after a function definition | Added the required blank lines.                     |
| E122      | Incorrect indentation of a continuation line    | Corrected indentation in the list comprehension.    |
| W293      | Whitespace on a blank line                      | Removed trailing whitespace.                        |
| E501      | Line exceeds the maximum allowed length         | Split the list comprehension across multiple lines. |

**Result:** The final Flake8 check completed without reporting any violations.

## Conclusion

The three static analysis tools helped improve the code's quality, security, and readability. Pylint reached a score of 10.00/10, Bandit reported zero issues, and Flake8 reported no remaining style violations.
