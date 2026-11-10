# Just Enough Assets

Just Enough Assets (JEA) is a library based around simplifying Adam Fox's *Pygame Tkinter GUI Tools*
Fox's PTGT is aimed at making game development easier by giving pre-built tools for developers to use.
I didn't really like how he vibe coded the whole thing so I made the library Just Enough Assets.
JEA simplifies Fox's vibe coded library and makes implementation a lot quicker and easier.

<hr>

## Initialisation:

1. Install JEA:
  `pip install just-enough-assets`

3. Import JEA using the following syntax in your Python file:
`from justEnoughAssets import *` or `import justEnoughAssets as jea`

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

<br>

### Characters

1. The syntax goes as follows:
  a. `Character(
          character:str,
          x:int, y:int,
          pathToImg:str,
          animation:bool, pathToAnimation:str,
          width:int, height:int,
          rows:int, cols:int,
          allowJSON:bool, pathToJSON:str,
          speakingSound:str,
          themeMusic:str, themeMusicVolume:float
         )`

2. `character` is a string parameter. This is the name of both the file of the character's idle image, as well as the object name in the JSON dialog file.

3. `x` and `y` are both integers. These are the coordinates of the character.

4. `pathToImg` is a string parameter, being the path to the character's idle image. This should NOT include the actual image; just the path.

5. `animation` and `pathToAnimation` are pretty self-explanatory. They follow the same structure as `pathToImage` but you must include the file, with the file being a spritesheet (mandatory).

6. `width` and `height` are the sizes of the individual sprites in the spritesheet.

7. `rows` and `cols` are the rows and columns in the spritesheet.

8. `allowJSON` and `pathToJSON` determine whether there is dialog. If so, `pathToJSON` is the path to the JSON file containing all of the dialog.

9. `speakingSound` is the sound that plays on each individual letter in the character's dialog.

10. `themeMusic` and `themeMusicVolume` hold the path and volume of any theme music that plays when the character is speaking.
  

**Suggestion:** `Character(
                          character="danielPrank",
                          x=100, y=500,
                          pathToImage="assets/textures/characters/danielPrank", 
                          animation=True, 
                          pathToAnimation="assets/textures/characters/danielPrank/danielPrank_sheet.png",
                          width=21, height=48,
                          rows=1, cols=3,
                          allowJSON=True, pathToJSON="data/jsonFiles/danielPrank.json",
                          speakingSound="assets/sounds/danielPrankSpeak.wav",
                          themeMusic="assets/sounds/danielPrankTheme.wav", themeMusicVolume=0.7
                        )`

<br>

### Map creation
*Map creation description coming soon*