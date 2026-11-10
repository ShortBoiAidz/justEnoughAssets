# Just Enough Assets

Just Enough Assets (JEA) is a library based around simplifying Adam Fox's *Pygame Tkinter GUI Tools*
Fox's PTGT is aimed at making game development easier by giving pre-built tools for developers to use.
I didn't really like how he vibe coded the whole thing so I made the library Just Enough Assets.
JEA simplifies Fox's vibe coded library and makes implementation a lot quicker and easier.

<hr>

## Initialisation:

1. Install JEA:
  `pip install git+https://github.com/ShortBoiAidz/JustEnoughAssets`

3. Import JEF using the following syntax in your Python file:
`import justEnoughAssets.py as jea`

2. Initialise the module in your `process_logic()` function using the following syntax:
`jea.init()`

- You do NOT need to initalise in each module. As long as this runs through your `while` loop, everything should work fine.
- You DO need to import the module in each of your files though (obviously).

<hr>

## How To Use:

### Labels

1. Use `createLabel(a, b, c, d, e)` with the following params:
  a. scene
    i. For example: `menu` or `startScreen`
  b. text
    i. Self explanatory. If I need to tell you what "text" is, die.
  c. font size
    i. Same goes here. If you don't know what "font size" is, die.
  d. row
    i. The row on the Y axis. This sets it in place so other labels don't overlap.
    ii. For example: one label could be on row 1, meaning a label below it would be on row 2.
  e. padding on the Y axis
    i. The amount of space above and below the label

2. Putting `.draw()` at the end of initialising the label automatically draws it on screen.
  a. Handy, because it doesn't make you do `thisAwesomeCoolLabel.draw()` after initalising it.
  
**Suggestion:** `createLabel(menu, "Horse Tale", 48, 0).draw()`