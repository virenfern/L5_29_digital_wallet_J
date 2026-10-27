# Reflection

## Lab 5: Static Code Analysis — Digital Wallet & Payment Tracker

### 1. What I Learned

Through this lab, I learned how static code analysis tools can identify code quality issues, security vulnerabilities, and formatting violations without executing the program.

I used three tools: Pylint, Bandit, and Flake8. Each tool served a different purpose. Pylint helped improve code quality and documentation, Bandit identified potentially insecure coding practices, and Flake8 checked compliance with Python style conventions.

### 2. Challenges Faced

One of the main challenges was understanding the security warnings reported by Bandit. The original application used SHA-1 for PIN hashing, `tempfile.mktemp()` for receipt paths, and Python's standard `random` module for OTP generation.

Another challenge was correcting the formatting errors reported by Flake8. Even small issues, such as missing spaces, incorrect indentation, trailing whitespace, and long lines, caused the checks to fail until they were corrected.

### 3. Security Improvements

I replaced SHA-1 with PBKDF2-HMAC-SHA256 to make PIN guessing more computationally expensive. I also replaced `tempfile.mktemp()` with `tempfile.NamedTemporaryFile()` and used the `secrets` module to generate OTPs securely.

The hardcoded gateway secret was replaced with an environment variable. This reduces the risk of exposing the secret directly in the source code, although the environment variable must still be configured correctly.

The PIN hashing implementation uses a fixed salt for the purpose of this lab. In a real payment application, I would use a unique random salt for each PIN and store it with the resulting hash.

### 4. Final Results

The static analysis results improved after the changes:

- **Pylint:** The score improved from 5.69/10 to 10.00/10.
- **Bandit:** The final scan reported zero security issues.
- **Flake8:** The final check reported no style violations.

These results demonstrate that the code became more consistent and addressed the security warnings identified by the tools. However, clean static analysis results alone do not prove that an application is completely secure or functionally correct.

### 5. Key Takeaways

This lab taught me that static analysis should be part of the software development process rather than something performed only at the end. Finding issues early makes code easier to maintain and reduces the risk of insecure programming practices.

I also learned the importance of reviewing tool output, understanding why an issue occurs, applying an appropriate fix, and rerunning the analysis to verify the result.

In future projects, I will use static analysis tools regularly and combine them with functional tests, code reviews, and secure configuration practices.
