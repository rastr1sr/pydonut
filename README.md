# pydonut 🍩
A one-line implementation of [donut.c](https://www.a1k0n.net/2011/07/20/donut-math.html) (by a1k0n) using an obfuscated Python format, along with a standard Python implementation.

## Overview
`pydonut` includes two versions of the classic ASCII donut animation:
1. **`donut.py`**: A straightforward Python implementation of the donut animation.
2. **`odonut.opy`**: An obfuscated version written in `.opy` format for fun and experimentation.

The `.opy` format uses:
- Block markers (`{` and `}`) for indentation.
- A capital letter `S` as a line delimiter.

This unique structure condenses the entire script into a single line. While the obfuscated version could be formatted into a torus shape for thematic flair, it was created simply as a lighthearted boredom project.

## How It Works
### Running the Obfuscated Version
1. Use the `opyparser.py` script to parse and execute the `odonut.opy` file.
2. The parser automatically runs the code after parsing.

```bash
python opyparser.py odonut.opy
```

### Running the Standard Version
You can run the standard Python implementation directly:

```bash
python donut.py
```
### File Structure
- **`donut.py`**: The standard Python implementation of the donut animation.
- **`odonut.opy`**: The obfuscated `.opy` version of the donut implementation, where each line ends with `S` as a delimiter, and indentation is marked by `{` at the start and `}` at the end.
- **`opyparser.py`**: The script to parse and execute `.opy` files.

### Why? 🤷
This project was created purely for fun and experimentation. The obfuscated version demonstrates alternative Python formatting, while the standard version provides a more accessible reference for the donut animation. Feel free to explore, modify, or improve both versions!

### Credits
- Inspired by [a1k0n's donut.c](https://www.a1k0n.net/2011/07/20/donut-math.html).
- Original idea and Python adaptation by Rastrisr.

### Better Implementations
For more polished and readable implementations of the same donut animation in Python:
- A standard Python implementation: [Julius-Syvis/DonutPy](https://github.com/Julius-Syvis/DonutPy)
- A torus-shaped formatted implementation: [EvanZhouDev/donut-py](https://github.com/EvanZhouDev/donut-py)
*(Do check them out !)*

---

*(You could format the script into a torus shape, but honestly, who has the time?)*
