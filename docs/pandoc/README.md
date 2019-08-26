# How to use Pandoc to create RADON's type specification

## Prerequisites

* Bash environment
* [Pandoc](https://pandoc.org) 2.7.x is required as universal document converter

## Create the specification

The file [`pandoc-input.txt`](pandoc-input.txt) contains an ordered list of README files that will be part of the final specification document
This file is the input to Pandoc in order to create the specification

* Open a bash-enabled command-prompt
* Execute the following command from the root of the repository:
  ```shell
  cat ./docs/pandoc/pandoc-input.txt | xargs -I{} sh -c "cat {}; echo ''; echo'';" | pandoc -f markdown -t docx --data-dir=./docs/pandoc -s -o spec.docx
  ```
* There will be a new file called `appendix.docx` containing RADON's type specification

> *Note:* By modifying the `-t` parameter of the command above you can change the output format, e.g., change `docx` to `html`.

> To update the `pandoc-input.txt` file you could use the following command:
>   `find . -name README.md > docs/pandoc/pandoc-input.txt`