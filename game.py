"""
Justin Oh
A01178154
"""
import random
import time
import math
import itertools
import sys


def create_class() -> dict:
    """
    Create a dictionary of attributes of the four character classes.

    :postcondition: correctly make a dictionary of key value pairs, each representing a character class
    :return: a dictionary of four key value pairs
    """
    return ({
        "Kog'maw": {1: {"NAME": "Ranger",
                        "SKILL": "Caustic Spittle",
                        "MAXIMUM_EXP": 100,
                        "MAXIMUM_HP": 65,
                        "ATTACK": 60},
                    2: {"NAME": "SharpShooter",
                        "SKILL": "Bio-Arcane Barrage",
                        "MAXIMUM_EXP": 150,
                        "MAXIMUM_HP": 150,
                        "ATTACK": 90},
                    3: {"NAME": "ADC",
                        "SKILL": "Living Artillery",
                        "MAXIMUM_EXP": 100000,
                        "MAXIMUM_HP": 230,
                        "ATTACK": 115}
                    },

        "Irelia": {1: {"NAME": "Warrior",
                       "SKILL": "Bladesurge",
                       "MAXIMUM_EXP": 100,
                       "MAXIMUM_HP": 80,
                       "ATTACK": 65},
                   2: {"NAME": "Barbarian",
                       "SKILL": "Flawless Duet",
                       "MAXIMUM_EXP": 150,
                       "MAXIMUM_HP": 170,
                       "ATTACK": 95},
                   3: {"NAME": "Bruiser",
                       "SKILL": "Vanguard's Edge",
                       "MAXIMUM_EXP": 100000,
                       "MAXIMUM_HP": 260,
                       "ATTACK": 130}
                   },

        "Ornn": {1: {"NAME": "Meat Shield",
                     "SKILL": "Volcanic Rupture",
                     "MAXIMUM_EXP": 100,
                     "MAXIMUM_HP": 150,
                     "ATTACK": 30},
                 2: {"NAME": "Damage Sponge",
                     "SKILL": "Searing Charge",
                     "MAXIMUM_EXP": 150,
                     "MAXIMUM_HP": 250,
                     "ATTACK": 50},
                 3: {"NAME": "Tank",
                     "SKILL": "Call of the Forge God",
                     "MAXIMUM_EXP": 100000,
                     "MAXIMUM_HP": 350,
                     "ATTACK": 80}
                 },

        "Syndra": {1: {"NAME": "Mage",
                       "SKILL": "Dark Sphere",
                       "MAXIMUM_EXP": 100,
                       "MAXIMUM_HP": 60,
                       "ATTACK": 65},
                   2: {"NAME": "Sorcerer",
                       "SKILL": "Scatter the Weak",
                       "MAXIMUM_EXP": 150,
                       "MAXIMUM_HP": 140,
                       "ATTACK": 95},
                   3: {"NAME": "AP Carry",
                       "SKILL": "Unleashed Power",
                       "MAXIMUM_EXP": 100000,
                       "MAXIMUM_HP": 200,
                       "ATTACK": 125}
                   },
    })


def create_enemy() -> dict:
    """
    Create nested dictionary of attributes of the three enemies.

    :postcondition: correctly create a nested dictionary that contains three key value pairs, value representing
                    information of a specific enemy
    :return: a nested dictionary
    """
    return ({1: {"NAME": "Elise",
                 "SKILL": "Neurotoxin",
                 "HP": 100,
                 "MAXIMUM_HP": 100,
                 "ATTACK": 10,
                 "EXP": 100},

             2: {"NAME": "Evelynn",
                 "SKILL": "Hate Spike",
                 "HP": 200,
                 "MAXIMUM_HP": 200,
                 "ATTACK": 15,
                 "EXP": 150},

             3: {"NAME": "Karthus",
                 "SKILL": "Requiem",
                 "HP": 300,
                 "MAXIMUM_HP": 300,
                 "ATTACK": 20,
                 "EXP": 200},

             4: {"NAME": "Yuumi",
                 "SKILL": "Final Chapter",
                 "HP": 900,
                 "MAXIMUM_HP": 900,
                 "ATTACK": 25,
                 "EXP": 500}})


def create_boss() -> dict:
    """
    Create dictionary of attribute for boss.

    :postcondition: correctly create a dictionary with six key value pair representing information on boss
    :return: a dictionary
    """
    return ({"NAME": "Yuumi",
             "SKILL": "Final Chapter",
             "HP": 900,
             "MAXIMUM_HP": 900,
             "ATTACK": 25,
             "EXP": 500})


def class_description() -> dict:
    """
    Create dictionary of class descriptions.

    :postcondition: correctly create a dictionary with 4 key value pair representing information on class
    :return: a dictionary
    """
    return ({1: "Low HP but Strong Attack Damage Carry",
             2: "Balanced Melee Fighter",
             3: "High HP but Low Attack",
             4: "Low HP but Strong Attack Mage"})


def get_character_name() -> str:
    """
    Ask user for name of the character and return that name.

    :postcondition: correctly return name of the character
    :return: name of the character as a string
    """
    print('\nPlease name your character, hero of Runeterra: ')
    character_name = input()
    return character_name


def get_character_class():
    """
    Obtain character class choice from the user as an integer from 1, 2, 3, 4 representing Kog'maw, Irelia, Ornn,

    Syndra respectively.

    :postcondition: correctly get the  user choice as an integer
    :return: an integer that represents the user choice for character class
    """
    display_character_class()
    character_choice = int(input("Choose your class as a number: ")) - 1
    return character_choice


def display_character_class():
    """
    Print the classes and descriptions associated with each class.

    :postcondition: display class and description associated with each class
    >>> display_character_class()
    1. Kog'maw:  Low HP but Strong Attack Damage Carry
    2. Irelia:  Balanced Melee Fighter
    3. Ornn:  High HP but Low Attack
    4. Syndra:  Low HP but Strong Attack Mage
    """
    for index, name in enumerate(create_class().keys(), 1):
        print(f"{index}. {name}:  {class_description()[index]}")


def map_description() -> tuple:
    """
    Create tuple of areas that describe the map.

    :postcondition: correctly create a tuple representing information on the map
    :return: a tuple
    """
    return "Bandle City", "BilgeWater", "Demacia", "Ionia", "Ixtal", "Noxus", "Piltover", "Shadow Isles", "Shurima", \
           "Targon", "The Freljord", "The Void", "Zaun"


def make_board(rows: int, columns: int) -> dict:
    """
    Create a dictionary to represent a game board of rows x columns.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns are positive, non-zero integers greater than or equal to two
    :postcondition: correctly create a dictionary that has rows * columns keys
    :postcondition: each key is a tuple that contain a set of coordinates
    :postcondition: each value is a short string description
    :return: a dictionary of coordinates and map description
    """
    return {(row, column): random.choice(map_description()) for row in range(rows) for column in range(columns)}


def make_character(character_name: str, level: int, class_choice: int) -> dict:
    """
    Create a dictionary representing a character that starts at coordinate (0,0).

    :param character_name: a string
    :param level: an integer
    :param class_choice: an integer
    :precondition: character_name is a string chosen by user
    :precondition: level is a positive integer between [1,3]
    :precondition: class_choice is a positive integer between [0,3]
    :return: a dictionary representing a character
    >>> make_character('Justin', 3, 0)
    {'Name': 'Justin', 'Class': "Kog'maw", 'Job': 'ADC', 'Level': 3, 'Current HP': 230, 'Maximum HP': 230, 'Skill': 'Living Artillery', 'Attack': 115, 'Current EXP': 0, 'Maximum EXP': 99999, 'X-coordinate': 0, 'Y-coordinate': 0}
    """
    class_type = list(create_class().keys())[class_choice]
    class_chosen = create_class()[class_type]
    character = {"Name": character_name,
                 "Class": class_type,
                 "Job": class_chosen[level]["NAME"],
                 "Level": level,
                 "Current HP": class_chosen[level]["MAXIMUM_HP"],
                 "Maximum HP": class_chosen[level]["MAXIMUM_HP"],
                 "Skill": class_chosen[level]["SKILL"],
                 "Attack": class_chosen[level]["ATTACK"],
                 "Current EXP": 0,
                 "Maximum EXP": class_chosen[level]["MAXIMUM_EXP"],
                 "X-coordinate": 0,
                 "Y-coordinate": 0}
    return character


def game_intro(character: dict):
    """
    Display game introduction on the screen.

    :param character: dictionary
    :precondition: a dictionary representing character information
    :postcondition: print the game introduction and welcome message with correct character name
    """
    name = character['Name']
    print(f"\n\n\n\n\n\n\n\n\n\n\n Welcome to Runeterra, {name}"
          "\n\n Here begins your adventure into the depths of the world of League of Legends."
          "\n Where dreams are crushed and all hope may be lost."
          "\n But there is always a glimmer of possibility no matter how treacherous the path is.")
    time.sleep(2)
    print(f"\n Wake up from your slumber, {name}. You have been sent to this world to save it from the clutches of "
          "the wicked Yuumi, terrorizing solo queue with her obnoxious behaviour."
          f"\n Go forth and fulfill your destiny {name}!")
    time.sleep(2)
    print(f"\n\n\n\n {name} was a previous CHALLENJOUR player, but lost all their level from teleporting to this world."
          f"\n However, {name} feels confident to regain those skills back and find a way to go back to their "
          f"original world."
          f"Thus, our new adventurer {name} sets off on their journey into the unknown....")
    time.sleep(2)


def display_boss():
    """
    Display boss ascii art and short intro on the screen.

    :postcondition: print the boss introduction and ascii art on the screen
    """
    print(f"\n Welcome to the final stage summoner. I will terrorize your solo queue games!")
    print("""\n
          ````````                                                                                     
   ````.':_,'',,'```````````````````````````````````````````````````````````,````````````````````    
  `.''',~^r!~~~;~''''''''''''''''''''''''...````...``````..``````````````.~==~....,__,,~~;~,'''..``  
 ``',,,~!!+!+>;~~,,,,,'',,,,,,,^^,,,,,,,,''''.;''''..''''''''''.....'''';Lr~~<~',;;~!+!;;~:,,:,''``  
 `.,:,:!7L^*zt|+;_~,,,,,_~~~~~!Aj~~_:___:,,'':\',,,,~~,,''''''',,,,''';?L;~;~=\;~_~sj<z7<,;+!;~,'.`  
 `',~~~^tu*cxi7*;~~____!;;;;;<UQa!;~~~~~~:,,~?:',~+=~,,''''''''''',:;rr;~~;!;;|v;~*K<cEz^~T<=L^:,'`  
 `':~~~!|J||{x\^~;~~~;7o>^!=f%QQf=;;;;;~~~,;r,'''~~,,',,,,,,'',,,,;**!;~;;!!!;;|*~^a+^^*;~i;!w?_,'`  
 `'_;;;!i\<=?\+;;;~~;SBQKXKNQBQ&z=^;;;;;;;*^,,~~_,,,',,,,,,,,,,,!|L=~_~;!^r^!;;;<;;^L<^<|=+ia7;_,'`  
 `'~;;;;=?xz*^;!;;;^zUU6UKNB&BKY*+^!!!!!!}7!~^LL?>!~,::~~~:,,,;|||<~,~;!^+rr^!;;!r;;;!=|IjITr;~:,'`  
 `'~;;;!r7v<;;!!~;|}y}jakKRW&dJ*+^^^=T!^LR{LLxyjIz7|;~;;;?^~_>z>*+~_~~^!==++^^!;;>;~~~;!!;;;~~,,'.`  
 `'~;!!!rr!;!!;~^syyjjowKR8&WSi<=++r+J~=7&Ko5T+++=====;,;!;_=<;;~,,~~!^^=^^!^!!;;!^~,:_:_;;~~,,''``  
 `,~!^!!!^^!;~~<jj5UDEXD6amycL?<>===+i~;+>nhXz;!!;;!=;^L7L?**+^;;~:~;!^+++><^!!;;~+;,,:_~;;~,,':~,.` 
``,;^^^!!!;;;;LPooKyfojz*^!=|*<**<<<>||+<L?*s\^=!;!=zSojfxzzzz77vciii|?*<=^;;!;;~~+=~,_~;;~~:!!~,.`  
`.,;<<r^!!;;;Yf><7}r>L|*+^;~~|zi?||?**jkZiLziu7?c7s6j*|L|iL?=;~~~~;;;;;;;;~;;;;~~~+|;,_;!;~~!~,,''`  
`.,!+==^^!!^=i?|Lac^=<<==^!~~!znJ7JZSma}}ISwfUUkEXdj}yyy}JL*=^^!;;;~~~~~~~~~~;~~~;*|!_~^!;;;~~~:,'`  
`.,!=>=++=*|Li\\7y=!^==^+=**Lt{}{ykbKw5oEAbD%ggRRWqqUEyi;'`````',~;!!!;;;;~~_~;;^+<^;;~^;~~~~_,,,'`  
`.,!><<==*|i\cT.uY!;!+<|ic777i|?**|zZR8RRQ#BQQQ#QBRDqj;:^'```.,'```,;!!!!;;;~;;!!!;;;;~r***<^;;_''`` 
`.:!<*<==*L\c\T\y\;;;*iL**^;!*7jmEX6PhDQQ@@@@@@@@Qgbf~^U|'`` ~<^;,'` '~;!^!!!;;;;;;;;~~~~~~~;;;;;:'` 
`._^**<>=*Lc7Tzym7+<|*^!;~;<7Ixf5mk6KRNQQ@@@@@@@@Q#U^`!!'`  .foy\;~~'.,r??<r^^;;;;;~~:,,,,,,,,,,,:'` 
`._^*?**>*Lvz77YAkyi=!;~~!++;:''.'~+zk%QQ@@@@QQ@@@QU_.,=?==?ZAkoIny5SmSZyjuzzz7\|+;~,,,,,,:~~~~~~,`` 
`'~^*??*<*Lvz775P=;^<*!!!;,`'Yy' ``~;~+d@@QWKUwyaD@@@Q8gNBQQQQQQN%b6kSjYJz7\Lii7zi<^!;;;;!;~~~:,,'.` 
`'~+|L|?*|L7Ijyqa<~,!<^;~.`,;+'```;{j7~z@Uy*||!|q@@@@QQBNWW%DDKUEZ5jYzviLLiLLL||??*^;!;;;;;;;;;~~,'` 
`'~+|LiL|LJomaywj<;?z^;_.`';\*~',LkAUXN@@@QDyLIdWRK6XEwSoooo5yfusz7Ti||||***<<^;;!!;;;;;!!!!;;;;;~'` 
`';*cvT7umkwayxTJ*cyv!;~'`,;|fXd8QQQ@QQQQ#%Dqa7ffnsJzzz777zzJz7v\i|?*<<>===+^;~_~~~~~~;;;~~~;;;;;~'` 
`';Lx}oUb6m}7|*<?Jwf?=*v{nyPKWBQQQNgRb6Pmjjuti~~!^++=<**|i77ciL|?**<<>==++r^!!!!!;;;;;;~~~~~~;;;~:'` 
`'!voqDdhf7|=++<//fJLLznjoZEhkXXkXhwmay{tJzv?>?fqD6EafYJ77T\iL|?*<<===++++++++++^!!;!;~~;;;!;;;;;!;,` 
`'^fKAaYc*++=*zjtcii/v7JJzJJJxssxxzzzzz7TiizyS5yj}Yxzz7TiL|?**<<<<>>>><<<<*****=+*+;;!i^;^^</vci\*;'`
`,=fyt\|<=*izIu7i||||L//\iLLLLii\////T77zJzzzzz7v\iiLL|??*************?||LLiiTjj==<!<Iv7zzIuzi*+!:.`
`'~=*<<*|izs{I7|+^!+=***?**<<*******?||LLLL|LLLL||??*<<<<<<<<<****?||LLi\T7t}S6KKqPoSSEoy5aSSa5jYL;'`
`',~;!!^===r^^!;;!^r++=++r^^^r+++++++==><<>>><<>>====++++=====<<**|LiT7zJfUDR%8N#B###WRbKq6UUXmyfc!,`
`.,;^r=<*<r^!!^^;;;;;!;;!!!!!!!!!!!!!!!!!!!!!!!!^^^^^^r++++++==<**|L/7j6DNBQQQQQQQQ#RD%RR%DKUwSjI|;'`
 `'~;!+>+^!;;;;;;;;~~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;!!^^^^++++++==>+!^{hNQQQQQQB#8WN##Q8dqwfzT777v<_` 
 `':;<*+^!;;;;;~~~~~;;;;!!!!;;;;;;;~~~~~~~~~~~~~~;;;;!!!^^^^!!;~,'',~Lj{K8B&NB&N##BQ8KEPkAqDdw{T*^~'`
 `',^=!;;;+|!^;~~;;~~;LjjYJv**=r;;;~~~~~~~~~~~~~~~~~~~~~~,,''``.''''',~!|/nwD8NNNQBgDqqbU6KUo7=^<+~' 
 `.,;;;~~~;;!;;~~~~~!yXUXXXUXkXEajj}*;<;,'''''''........```.',,,'.'''''~r*|cJumqD%#N8%K6UkhEEaJi*^:` 
 `.^^;~~~~;;!;;;;;;+ykU6KqAqKbDR%Wgmi^;~,'...........'''',,~~,,''...'.''',;^ifomU66AKbbKbqUPaf?;~!~. 
 .,;=*>|v|7T|?**L*7UbddDDDDRgWNBBNUL*~',,'..''''''''..'''',,',,,'''..',,,,,,~^iymUUUXXhPEPmyn|;;<<~.`
`';LzzJxstJzz7c\c7hdD%gNNN#&QQQQBg}>^,'~~'`````........''',,,,,,''.`.''',,_:,,;?yAqAA6UXPSjxTi/tt?;'`
`'~*z}yoaZSmZZmhaXKbDbbRDDDRRg%%%m*;~'.:~'``````````...''',',~;~,```'''''',,,',;7k66Aqqq6UkkES5j}\;'`
``,;+i|****??r!;rjmXDhkkkXXUUUUUE7;,,.`',.```.``..'....`..',_~;,`..``.','''''''_!*nwXXXXUA6Xkway{i;'`
 `,_~~^+r+=<?*^~;jmSwmSSEmmwEhhh}<,''`.''....''.'''''...'''..''``'''.``',''''''_;;!?J}nsJz7vciL|*^:.`
 `'~!*~__~~~~~~~~z5o55aZZSwEEwwu+,'.`.',~,',:~;~,,,,,,'..'',,,,'.`.''.``',''',;?c\||?*|L|?**<>=+^;,` 
 ``',,,,:_~~~~~~_*jyyyyyjfux7i*;,..``.',!~,,~!LLi^=<+r<!~'',_;~~,''....`.'',*fmkPwwmS}\**<<<>=+^!~'` 
 ``',,,,,:_~~~~~~~*|?***?|||?^;~~,```.'',^;,',;>|\<+**<LL=~'.',,,,,'...`.',<z55ySEhkPa}zL***<<=r^;,``
  `',,,,,,:_~~~~~~~r++===<<<***<*^.....'':;!,.'_;!+^;;+==++;,.``..'''....'~<*?*T}fyoaojIzv|*<<<+!;,. 
  `'',,,,,,:~~~~~~~~!^^^^r^++^+r+*,.'....''~;~.`',~~;;~;!!;!;,.`````.....''+>***Lc7zzsamys7LL?<+^;,` 
 ``'',,,,,,,,:~~~~~~~!+++^^^^^+=|='.''''''''',,'```',,,,,:~~:~,'..```....''~<Tn?<*|*i}ma5nz7L|**=;,``
 `',,',,,,,,,,,:_~~~~~;++==r+=+!^~''''''''.''''''.```.'',',:,,,''''``.'''',,,,75z}n\\JnnuJ7J7ci|*!,. 
 `':~_,,,,::,,,,,,:~~~~~!+==^;_,,,'''''',,'..'''''.````.','',,,,''''`.'',:_::,_Lyj}}v}ay}xxjyosL>;,` 
 `'_;;;;~~:,,:_:,,:::_~~~^=!~,'''''''''',~,,'...'''....'''''''',,'''''',;!;,:,,,~?zjwEUXSj5z7z5j|;,` 
 `'~;;!!!;;;~_~______::_;^;:,,,,,,'''''',~~:,'..''.....'''''..',:,,,,',~<|;~:,,_;^*\\xSkmyfJz7ccff+:. 
 `,~!!!^^!;;;!;;~~~~~:,~;~,,,,,,,,,,,'''';;~:,''.'''.'''','''.':~,:_~,:+z?!~~~;!+|\z{aEy}nIJz7i\o|~.`
 `,;^+<<=+^r+^!!;;;;;~;;~,,,,:_~~~~~,,,,';;;~_,,,'''...''',''',~~;!^;_+}z\*!^=?LTx}a6%6wojf{IzTixj;'`
 `,;r<*==<+^^^!!;;;;;;;;~:,:~~~;~~~;;;~:,:!!;~~::,,'''''',,''',~;=i\^<oo5s?**?izImqRg#qkZyjf}tz7vn^'`
 `,;+*****===+r+=^!!!;;~~~:_~;;;;;;;;!!!;,;+!;~~~~_,,,,,,',''':;=zy{JEkwz?*??||L7q%%%QKXmo5yyfYJzi+,`
 `,;=>==|?==+r=^^+^!^;;:~~~~~;;;;^^!!;;!!;~!+!;~~~~______,',',~!\mUE6h{L?||||LLizbR%%QgqXPwSSZyuJ|;,`
 `,!>*|||||||?|?<**<>;~,,~~~~;;;!!!^^!;;;;;~+=^;~~~~~~~~~~,,,~!?SKXw{L|LLiiiii\zyg8WggQgqUXkXkmynL;'`
 `,!><***?LiiLLLLLLL|+;_,~;;;;;!!!!^!!;;;;;;;=+!;~~~~~~~;!!,~;<yqyu7ii\\\cTTv7zyqNW%R%gQQgddKUkSj\;'`
 `,!+<L\i|LLii\L||iLi|=;:,~;;;;;!!!!!!;;;;;;;+<^;;;;;;;~;=z|==sh}Jz777777zzzIjEDNQQB&##BQQQQNRKho7!'`
 `,!*?|LiLi\i\\LiLTzzz7L;::~!^^!!;!!;;;;;;;;;^|=!!!^!!;;^|IZIzsafn}ff}}{}joEUb8QQQQQQQQQQQ88BQB8%S<,`
 .:^<|\7cii\\7v\Tiz7zxYt+;;;~;rr^^^!!^!^^^^^^+?|=^^rr^!^r|so}}ffjyyyoaSmEkU66kU#QQQQQQQRRBQ8NgRbUf+,`
 .:!*i7\L?v|i7v77T7ssfjj*;^=!~;!=***********<<*L*^^+++^^+?smjyyyoSwkUqKbqXZjuIjwRQQQQQQWRNQ#N%DKX}+,`
``,^|/vv7z7zJJJuJzxxfyyo|^*L<<<!!r?c7zv\\\iL||?L\=^r++rr+?tXUXkUqbRgRDDqEa5yyaomqQQQQQB%WQQNW%DK6f+,`
`._^L7zzzzzJsuzsnn}}y5ooL<Li=*7c\c=<|Ttxz7v\iiLL7*++^^^+=*zkDDR%g8&QQB%dqUXkPXqdRQQQQggBQQ#NNWRdUY+,`
`.~<7xu{}fjyjyyyyyjjyaaaL*L\+<vsJfj{7i>|77\iL||LzL=+^++++<7hR%%DD%8BQ@@QB8%%%gWNB#8W#QQQQQQQQB8RKy=,`
`._=i77uJuujf}Yn}yyj5Soa\\cT+^+izx{oXKbU\LL|LLiit{<^^^+++=cwR%%DbDW#BQQ@QQQQQQQQQQQQQQQQQQQBWbkoY|;'`
`._>T7zf}fyy5yfyjoo}omaZs}tv|<=*LzfSP6D%bz\7zzz7sS\>^^^^^rLm%%%DqD%8#&QQQQQQQQQQQQQQQQ#qoxi*=^!;~:'` 
`.~r|\zx}{}}yj}jyoaawEaaL=77|L|*<?i7fmXd8NkzL7nam}zi?<==>*Lo8%%RqdRgW##&QQQQQQQQQQQD5i^;!!!!!!!;;~'` 
`.~<ivJ}fffj5jya5jmwPXmo>=zz\z77YjIzi|\{5wwj*!?yY}yjsz77zJYE88g%qKD%%N#&BQQQQQQQQ5|!;!!!!r<?Li\c\*~'`
`._<ctsJIufuyfj5ZmSEPUmf^=YaUm|LfsiL|ivtYIJ7|^is{Zmaooyyyyyh&Ng%KUD%%WBQQQQQQ@Wj=!!!;!+?xymkm}\=;'` 
`.~<TYj}ufyjyyj5yfaPPPSs<TJ{f}}fymPUqKbdDDRRDdSsja5ywwSaZoSKQ8g%dkd%WgQQBQQQQI^!!;;!*it}uzL=;,,''.`  
 .~<L7Y}}fj}jyjoaawkk}Sa}yEU66AqKKKKbbbdDDRR%%%SjjfaSS5jyyk%&N%RDhKR8WN&QQQ6^;!!;^<||<!:,,,',,,,,'`` 
`.~*z{jooSmmSmmmwPEoy5XXqqqqqKKKbbbKqqAAqKdD%W#BRqmjjjn}yhKW#N8RDkkDW8NQQB\;^!;;=?^~,,,,,,~~~;;;;~'` 
`.~*J{joaZSmwwwwwPkXUU6qqqqqUESyjfYzvi?<>=+=<*LzfEd%g%g8#N%gQ&N%DAwbgN&QB|;^;;^>^,,,,,:~~!+?i7zz7*~'`
`'~?J}yaSSmmwwwEPkkXXXPajnzc|***<=^!!!!;;;;;;;;;;;;!?u6NQQQQQB#gDKmA%8B#T;!;;^!_,,,,~;>Lz}yv=;~:,,`  
`.~*znjyoaZZaoyfnJ7TL*+^rr^^!!!!;;;;;;;;;;;;~~~~~;;;;;;!cwNQQQ#WDKmEDgNJ;!;;;~,,,,~^|zI}J*+:,'''..`  
 `,;+>***<>=r^!!!!!!!!!!!;;;;;;;~~~~~~~~~~~;;;;;;;~~~~;;;~!xdNNgDKwaqRa;;;;~_,,,:!?7ztLr;:''''',''`` 
 `',~~;;;;;;;;;;;;;;;;~~~~~~~_::,,:::::::,,,,,,:_~~~;~~~~~~~;IbRb6wfE6+~;~~:,',_^L\\+_''''',,,,,,'`  
  `':_~~~~~~~~~~;;;~~~;;;;;;;;;;;!!!!!!!;;;~~~_,,,,,,,,_~~~~~_~iXUZIos,~~,,'',~+*=~''''',,,,,,,''``  
  `',,,:_~~~;;;!^^+++==>=^;~:,,~;^+++++r^^^^!;;;~~_,,,,',,_~_~~,!joJIL,,,,,'':!r;''''',,,,,,''.```   
  `.',,,,,,:,,:_::::__::,,,,,,',,,:~;^^^^^!~_,,,,,,,,,,,,''',___,~iJvr,,,,'',;;,.'.'''',,''````````  
  ``````......''''''''''''''''''''''',!!;~'''''',,,''',,,,,''',::,,<|~,','.'__'..'''''''.````...``   
  ```....````````````````````````````.'``````  ```.'',''''','''',,,,;,''''.',.`....'''````...```     
   ```````````````````````````````````````````````  ``.''''''''''',''''....'.`..`...````.```         
   ``````````````````````````````````````````````````````'''''''''''''......``.``..`````             
   `````````````````````````````````````````````````````  `.'.....''''..``````````````               
    ```````````````````                           ``````    `.``..`....`````````````                 
       `````````` `                                          ```````````````````````                 
                                                              `````````````````````                  
                                                                                                     
                                                                                                     """)


def create_map(board: dict, character: dict):
    """
    Display a map showing the current location of the character and boss.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: a dictionary containing key of tuple representing a set of coordinates and value representing a short
                   string description
    :precondition: a dictionary containing character information
    :postcondition: map should show the current location of the player and the boss
    >>> create_map(make_board(5,5), make_character('Justin', 3, 0))
    [x][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][Y]
    """
    size = int(math.sqrt(len(board)))
    map_tile = []
    for row in range(size):
        column_list = []
        for column in range(size):
            column_list.append("[ ]")
        map_tile.append(column_list)
    map_tile[character['Y-coordinate']][character['X-coordinate']] = "[x]"
    map_tile[size - 1][size - 1] = '[Y]'
    for index in range(size):
        all_map = "".join(map_tile[index])
        print(f"{all_map}")


def get_direction() -> str:
    """
    Return direction chosen by the user.

    :postcondition: correct string representing direction user input
    :return: a string representing direction user input
    """
    direction_dict = {"1": "North", "2": "East", "3": "South", "4": "West", "5": "Quit"}
    for num, direction in zip(itertools.count(1), direction_dict.values()):
        print(num, direction)
    user_choice = "0"
    while user_choice not in direction_dict:
        user_choice = input("\n Type number representing direction: ")
    return user_choice


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Determine if the character goes off the board or not.

    :param board: dictionary
    :param character: dictionary
    :param direction: string
    :precondition: a dictionary containing key of tuple representing a set of coordinates and value representing a short
                   string description
    :precondition: a dictionary containing character information
    :precondition: a string of either 1, 2, 3, 4 representing North, East, South, West respectively
    :precondition: the character must be on a valid location on the board
    :postcondition: if the character is on the board, and it can travel in its desired direction, return True as Boolean
    :return: a Boolean value representing if character goes off the board or not
    >>> char = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(make_board(2,2), char, "East")
    True
    >>> validate_move(make_board(2,2), char, "North")
    False
    """
    if direction == "1":
        location = (character["X-coordinate"], character["Y-coordinate"] - 1)
    elif direction == "2":
        location = (character["X-coordinate"] + 1, character["Y-coordinate"])
    elif direction == "3":
        location = (character["X-coordinate"], character["Y-coordinate"] + 1)
    else:
        location = (character["X-coordinate"] - 1, character["Y-coordinate"])
    return location in board


def move_character(character: dict, direction: str) -> dict:
    """
    Update the character location after direction input.

    :param character: dictionary
    :param direction: string
    :precondition: a dictionary containing character information
    :precondition: a string of either 1, 2, 3, 4 representing North, East, South, West respectively
    :precondition: the character must be on a valid location on the board
    :postcondition: correctly update location inside character dictionary after direction input
    :return: character dictionary with new x and y coordinates
    >>> input_direction = "3"
    >>> char = make_character('Justin', 1, 0)
    >>> char["Y-coordinate"]
    0
    >>> move_character(char, input_direction)
    {'Name': 'Justin', 'Class': "Kog'maw", 'Job': 'Ranger', 'Level': 1, 'Current HP': 65, 'Maximum HP': 65, 'Skill': 'Caustic Spittle', 'Attack': 60, 'Current EXP': 0, 'Maximum EXP': 100, 'X-coordinate': 0, 'Y-coordinate': 1}
    >>> char["Y-coordinate"]
    1
    """
    if direction == '1':
        character['Y-coordinate'] -= 1
    elif direction == '2':
        character['X-coordinate'] += 1
    elif direction == '3':
        character['Y-coordinate'] += 1
    else:
        character['X-coordinate'] -= 1
    return character


def describe_current_location(board: dict, character: dict):
    """
    Print the coordinate and description of character's current location.

    :param board: dictionary
    :param character: dictionary
    :precondition: a dictionary containing key of tuple representing a set of coordinates and value representing a short
                   string description
    :precondition: a dictionary containing character information
    :postcondition: print the coordinate of character's current location
    """
    x_coordinate = character['X-coordinate']
    y_coordinate = character['Y-coordinate']
    print(f'You are in ({board[x_coordinate, y_coordinate]})')


def not_valid_move(character: dict):
    """
    Print message for wrong direction

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: print not valid move statement correctly
    """
    name = character['Name']
    print(f"\nSorry {name}, you can't go in that direction. Choose a different direction.")


def battle_choice() -> tuple:
    """
    Create tuple of battle choice.

    :return: a tuple
    """
    return "Attack", "Run Away"


def get_battle_choice() -> int:
    """
    Get user selected battle choice.

    :postcondition: return user choice as an integer
    :return: return correct user choice as an integer
    """
    return int(input("What is your choice summoner? : "))


def display_command(character: dict):
    """
    Print a numbered list of possible battle choices for user.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :precondition: the character must be on a valid location on the board
    :postcondition: print a numbered list of battle choices for user
    >>> char = make_character('Justin', 1, 0)
    >>> display_command(char)
    Justin, enter your next move:
     [1]. Attack
     [2]. Run Away
    """
    print(f"{character['Name']}, enter your next move: ")
    for index, choice in enumerate(battle_choice(), 1):
        print(f" [{index}]. {choice}")


def check_for_enemies(character: dict) -> bool:
    """
    Determine if player will face an enemy that is not the boss as a Boolean value.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: return whether player will face an enemy as a Boolean value
    :return: if player will face an enemy other than boss as a Boolean value
    """
    if (character['X-coordinate'], character['Y-coordinate']) == (4, 4):
        return False
    else:
        return random.randint(1, 3) == 1


def determine_enemy(character: dict) -> dict:
    """
    Determine which enemy player will face.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: enemy will be decided depending on player level
    :return: the enemy the player will face depending on their level
    >>> char = make_character('Justin', 1, 0)
    >>> determine_enemy(char)
    {'NAME': 'Elise', 'SKILL': 'Neurotoxin', 'HP': 100, 'MAXIMUM_HP': 100, 'ATTACK': 10, 'EXP': 100}
    """
    if character["Level"] == 1:
        return create_enemy()[1]
    if character["Level"] == 2:
        return create_enemy()[2]
    if character["X-coordinate"] == 4 and character["Y-coordinate"] == 4:
        return create_enemy()[4]
    else:
        return create_enemy()[3]


def fight_enemy(character: dict):
    """
    Fight enemy until player dies, enemy dies, or player runs away.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: perform combat portion of the game until player dies, enemy dies, or player runs away
    """
    enemy = determine_enemy(character)
    print(f"\n{enemy['NAME']} has challenged you to a 1 vs 1.")
    while character_enemy_alive(character, enemy):
        display_command(character)
        command = get_battle_choice()
        if command == 1:
            battle_round(character, enemy)
        if command == 2:
            if enemy['NAME'] == 'Yuumi':
                print(f"\n {character['Name']}, you can't run away from a boss fight...")
            else:
                print(f"\n {character['Name']} ran away successfully while being called a Bronze noob...")
                break


def character_enemy_alive(character: dict, enemy: dict) -> bool:
    """
    Determine if character and enemy are both alive.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: a dictionary containing character information
    :precondition: a dictionary containing enemy information
    :postcondition: if both character and enemy are alive return True, else False
    :return: whether both character and enemy are alive as a Boolean

    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> character_enemy_alive(char, minion)
    True
    """
    return character['Current HP'] > 0 and enemy['HP'] > 0


def battle_round(character: dict, enemy: dict):
    """
    Print battle description.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: a dictionary containing character information
    :precondition: a dictionary containing enemy information
    :postcondition: print battle description

    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> battle_round(char, minion)
    <BLANKLINE>
     Justin uses Caustic Spittle!
    <BLANKLINE>
     Elise took 48.0 damage.
    <BLANKLINE>
     Elise's new HP is now 52.0.
    <BLANKLINE>
     Elise uses Neurotoxin!
    <BLANKLINE>
     Justin took 8.0 damage.
    <BLANKLINE>
     Justin's new HP is now 56.0.
    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> minion['HP'] = 1
    >>> battle_round(char, minion)
    <BLANKLINE>
     Justin uses Caustic Spittle!
    <BLANKLINE>
     Elise took 48.0 damage.
    <BLANKLINE>
     Elise fainted.
     You showed Elise who's the real king of the rift.
     You earned 100EXP
     You feel power gathering around you. Congratulations Justin, you leveled up!
    """
    print(f"\n {character['Name']} uses {character['Skill']}!")
    modify_enemy_hp(character, enemy)
    if enemy['HP'] > 0:
        print(f"\n {enemy['NAME']}'s new HP is now {enemy['HP']}.")
    else:
        print(f"\n {enemy['NAME']} fainted.")
    if enemy_alive(enemy):
        print(f"\n {enemy['NAME']} uses {enemy['SKILL']}!")
        modify_character_hp(character, enemy)
        if not character_alive(character):
            sys.exit('You have died, your adventure has ended')
        else:
            print(f"\n {character['Name']}'s new HP is now {character['Current HP']}.")

    else:
        earn_exp(character, enemy)
        if enough_exp(character):
            print(f" You showed {enemy['NAME']} who's the real king of the rift.\n You earned {enemy['EXP']}EXP")
            print(f" You feel power gathering around you. Congratulations {character['Name']}, you leveled up!")
        else:
            print(f"\n You showed {enemy['NAME']} who's the real king of the rift. \n You earned {enemy['EXP']}EXP")


def modify_enemy_hp(character: dict, enemy: dict) -> dict:
    """
    Reduce HP of enemy after user attacks enemy.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: a dictionary containing character information
    :precondition: a dictionary containing enemy information
    :postcondition: correct modification of enemy HP after damage subtracted from enemy current HP
    :return: reduce enemy hp by amount of character damage
    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> modify_enemy_hp(char, minion)
    <BLANKLINE>
     Elise took 48.0 damage.
    {'NAME': 'Elise', 'SKILL': 'Neurotoxin', 'HP': 52.0, 'MAXIMUM_HP': 100, 'ATTACK': 10, 'EXP': 100}
    """
    enemy['HP'] -= (character['Attack'] * 0.8)
    print(f"\n {enemy['NAME']} took {(character['Attack'] * 0.8)} damage.")
    return enemy


def enemy_alive(enemy: dict) -> bool:
    """
    Determine if enemy is alive as a Boolean value.

    :param enemy: dictionary
    :precondition: a dictionary containing enemy information
    :postcondition: determine if enemy hp is above 0 or not as a Boolean
    :return: if enemy is alive or dead as a Boolean value
    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> minion["HP"] = 0
    >>> enemy_alive(minion)
    False
    """
    return enemy["HP"] > 0


def modify_character_hp(character: dict, enemy: dict) -> dict:
    """
    Reduce HP of enemy after user attacks enemy.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: a dictionary containing character information
    :precondition: a dictionary containing enemy information
    :postcondition: correct modification of player HP after damage subtracted from player current HP
    :return: reduce player hp by amount of enemy damage
    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> modify_character_hp(char, minion)
    <BLANKLINE>
     Justin took 8.0 damage.
    {'Name': 'Justin', 'Class': "Kog'maw", 'Job': 'Ranger', 'Level': 1, 'Current HP': 56.0, 'Maximum HP': 65, 'Skill': 'Caustic Spittle', 'Attack': 60, 'Current EXP': 0, 'Maximum EXP': 100, 'X-coordinate': 0, 'Y-coordinate': 0}
    """
    character['Current HP'] -= (enemy['ATTACK'] * 0.9)
    print(f"\n {character['Name']} took {(enemy['ATTACK'] * 0.8)} damage.")
    return character


def earn_exp(character: dict, enemy: dict) -> dict:
    """
    Reduce HP of enemy after user attacks enemy.

    :param character: dictionary
    :param enemy: dictionary
    :precondition: a dictionary containing character information
    :precondition: a dictionary containing enemy information
    :postcondition: correct modification of player EXP after defeating enemy
    :return: increase player exp by amount of exp enemy gives
    >>> char = make_character('Justin', 1, 0)
    >>> minion = determine_enemy(char)
    >>> earn_exp(char, minion)
    {'Name': 'Justin', 'Class': "Kog'maw", 'Job': 'Ranger', 'Level': 1, 'Current HP': 65, 'Maximum HP': 65, 'Skill': 'Caustic Spittle', 'Attack': 60, 'Current EXP': 100, 'Maximum EXP': 100, 'X-coordinate': 0, 'Y-coordinate': 0}
    """
    character['Current EXP'] += enemy['EXP']
    return character


def enough_exp(character: dict) -> bool:
    """
    Check if character can level up.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: determine if player can level up or not as a Boolean value
    :return: increase player exp by amount of exp enemy gives
    >>> char = make_character('Justin', 1, 0)
    >>> char["Current EXP"] = 150
    >>> enough_exp(char)
    True
    """
    return character["Current EXP"] >= character["Maximum EXP"]


def level_up(character: dict, class_choice: int) -> dict:
    """
    Increase character level by 1 and update new information for character.

    :param character: dictionary
    :param class_choice: integer
    :precondition: a dictionary containing character information
    :precondition: an integer containing user class choice information
    :postcondition: increase character level by 1 and populate character information with new information relating to
                    user chosen class
    :return: updated character information as a dictionary
    >>> char = make_character('Justin', 1, 0)
    >>> char["X-coordinate"] = 2
    >>> char["Y-coordinate"] = 2
    >>> level_up(char, 0)
    {'Name': 'Justin', 'Class': "Kog'maw", 'Job': 'SharpShooter', 'Level': 2, 'Current HP': 150, 'Maximum HP': 150, 'Skill': 'Bio-Arcane Barrage', 'Attack': 90, 'Current EXP': 0, 'Maximum EXP': 150, 'X-coordinate': 2, 'Y-coordinate': 2}
    """
    x_coordinate = character["X-coordinate"]
    y_coordinate = character["Y-coordinate"]
    character = make_character(character["Name"], character["Level"] + 1, class_choice)
    character["X-coordinate"] = x_coordinate
    character["Y-coordinate"] = y_coordinate
    return character


def check_achieved_goal(character: dict) -> bool:
    """
    Check if character reached the boss (bottom right of map).

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: check if character has reached the bottom right of map as a Boolean
    :return: if character has reached the bottom right of map as a Boolean
    >>> char = make_character('Justin', 1, 0)
    >>> char['X-coordinate'] = 4
    >>> char['Y-coordinate'] = 4
    >>> check_achieved_goal(char)
    True
    """
    return (character['X-coordinate'], character['Y-coordinate']) == (4, 4)


def character_alive(character: dict) -> bool:
    """
    Check if character is alive as a Boolean.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :return: if character is alive as a Boolean
    >>> char = make_character('Justin', 1, 0)
    >>> char['Current HP'] = 0
    >>> character_alive(char)
    False
    """
    return character['Current HP'] > 0


def heal_player(character: dict) -> dict:
    """
    Restore HP to character before boss battle.

    :param character: dictionary
    :precondition: a dictionary containing character information
    :postcondition: character dictionary is modified so that Current HP is set to Max HP
    :return: Current HP set to Max HP for character before boss battle
    """
    character["Current HP"] = character["Maximum HP"]
    print(f"\n You have been healed to full HP before facing off against Yuumi the treacherous cat.")
    print("\n Best of luck to you summoner...")
    time.sleep(2)
    return character


def game_outro(character: dict):
    """
    Display game ending credit on the screen.

    :param character: dictionary
    :precondition: character is a dictionary representing character information
    :postcondition: print the game ending and congratulation message with correct character name
    """
    name = character['Name']
    print(f"\n\n\n\n\n\n\n\n\n\n\n You've done it, {name}"
          "\n\n Here ends your adventure through the world of League of Legends."
          "\n You've proven that you're better than all those junglers on your team who were holding you back.")
    time.sleep(3)
    print(f"\n Thank you {name} for saving this world and defeating Yuumi once and for all. That pesky cat has been "
          f"terrorizing the rift for far too long and a hero was needed to get rid of her once and for all."
          f"\n With this we can finally remove Yuumi, {name}! (Delete Yuumi)")
    time.sleep(3)
    print("""
██╗░░░░░███████╗░█████╗░░██████╗░██╗░░░██╗███████╗  ░█████╗░███████╗
██║░░░░░██╔════╝██╔══██╗██╔════╝░██║░░░██║██╔════╝  ██╔══██╗██╔════╝
██║░░░░░█████╗░░███████║██║░░██╗░██║░░░██║█████╗░░  ██║░░██║█████╗░░
██║░░░░░██╔══╝░░██╔══██║██║░░╚██╗██║░░░██║██╔══╝░░  ██║░░██║██╔══╝░░
███████╗███████╗██║░░██║╚██████╔╝╚██████╔╝███████╗  ╚█████╔╝██║░░░░░
╚══════╝╚══════╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░░░░

██╗░░░░░███████╗░██████╗░███████╗███╗░░██╗██████╗░░██████╗
██║░░░░░██╔════╝██╔════╝░██╔════╝████╗░██║██╔══██╗██╔════╝
██║░░░░░█████╗░░██║░░██╗░█████╗░░██╔██╗██║██║░░██║╚█████╗░
██║░░░░░██╔══╝░░██║░░╚██╗██╔══╝░░██║╚████║██║░░██║░╚═══██╗
███████╗███████╗╚██████╔╝███████╗██║░╚███║██████╔╝██████╔╝""")
    print(f"\n\n\n\n That was all for now summoner, but we may ask for your help again later..."
          f" Thank you once again for your help {name}!"
          f"\n\n\n THE END")
    time.sleep(2)


def game():
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character_name = get_character_name()
    character_class = get_character_class()
    character = make_character(character_name, 1, character_class)
    achieved_goal = False
    game_intro(character)
    create_map(board, character)
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_direction()
        if direction == "5":
            sys.exit('Quitting the game, your adventure has ended')
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            create_map(board, character)
            there_is_a_challenge = check_for_enemies(character)
            if there_is_a_challenge:
                fight_enemy(character)
                create_map(board, character)
                if enough_exp(character):
                    character = level_up(character, character_class)
            achieved_goal = check_achieved_goal(character)
        else:
            create_map(board, character)
            not_valid_move(character)
    display_boss()
    heal_player(character)
    fight_enemy(character)
    game_outro(character)


def main():
    game()


if __name__ == "__main__":
    main()
