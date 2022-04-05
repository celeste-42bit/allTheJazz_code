# ATJ documentation

---

This file contains all existing documentation to the All-The-Jazz game dev project, excluding all documentation for 3rd-party references, modules and libraries.

For information on the licensing and other regulatory and law-related aspects of this product, please refer to "LICENSE.md" and "README.md"

Copyright © 2022 73chn0m4nc3r and ShaeCalmine

## Software

---

### Character

The digital character sheet is represented by the "character.env" file, which is generated as a copy of "character_template.env". While the file "character.env" already contains a lot of preset values for its keys, most of the values are being set during the character creation phase of the story.

Safe and read structure for player data:
```
"character.env": created by: func.: createenv in class: "Player" in file: "player.py"

player object: "Player": created by: constructor of class "Player"
```
Creating a player object:
```python3
player = Player(self, <name>, <surname>, <gender>, <pronoun>, <clan>)
```
Reading from a player object:
general
```python3
storedValue = cast(player.value)
```
Reading from a player object:
use cases
```python3
name = str(player.name)
player_name = {player.name, player.surname}
{gender=player.gender}
```

## Conventions

---

### Story text file naming conventions

For narration parts: ```N_<chapter><page>```

For choice parts: ```C_<chapter><page>_<#choices>```

For option parts: ```O_<chapter><page>_<A,B,...>```

## Story development

Story changes here!