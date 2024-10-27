# integrity-checker

This project uses the `hashlib` library to compare text and verify file integrity with the SHA-256 hashing algorithm. Integrity checks are essential to ensure that data has not been altered or corrupted.

## How it works

The `integrity-checker` generates a SHA-256 hash for each file or text you want to verify. It then compares the current hash with a reference hash to detect any changes in the original content. This process is useful for ensuring that files remain authentic and unchanged over time.

## Technologies used

- Python
- `hashlib` library

## Next steps

I plan to expand the project to include other hashing algorithms and support integrity checks for files.