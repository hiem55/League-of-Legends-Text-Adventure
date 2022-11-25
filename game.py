"""
Justin Oh
A01178154
"""
import random
import time


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
                 "EXP": 200}
             })


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
    >>> get_character_class()
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

    :param character: a dictionary representing character information
    :precondition: character is a dictionary representing character information
    :postcondition: print the game introduction and welcome message with correct character name
    """
    name = character['name']
    print(f"\n\n\n\n\n\n\n\n\n\n\n Welcome to Runeterra, {name}"
          "\n\n Here begins your adventure into the depths of the world of League of Legends."
          "\n Where dreams are crushed and all hope may be lost."
          "\n But there is always a glimmer of possibility no matter how treacherous the path is.")
    time.sleep(3)
    print(f"\n Wake up from your slumber, {name}. You have been sent to this world to save it from the clutches of "
          "the wicked Yuumi, terrorizing solo queue with her obnoxious behaviour."
          f"\n Go forth and fulfill your destiny {name}!")
    print(f"\n\n\n\n {name} was a previous challenger player, but lost all their level from teleporting to this world."
          f"\n However, {name} feels confident to regain those skills back and find a way to go back to their "
          f"original world."
          f"Thus, our new adventurer {name} sets off on their journey into the unknown....")


def display_boss():
    """
    Display boss ascii art and short intro on the screen.

    :postcondition: print the boss introduction and ascii art on the screen
    """
    print("""\n``                                                                                            `.``                                                                
                    <LLi+,                                                   `         ~=  .,~!^~                                                               
                    `uQkqQs`~`    `+odDZ'                    `^       '` `,,.`````` `;+;^^'`:iz+;!'                     `:;;;;;;;;'                             
                     .|Ed%gy\v  `*ADY7ndU.               _  ,XT      `,.';'        ~^;;^;*, >*c;|rv                   `;!'  ~!~,``~+,                           
                     `|\77UQD; ^D5~     ?m`             jDzEQR,     ,~~~~'   .`  ,*;~;^r^;^``~<c\v:                  ,?.  `=<;~,,;: ;+   ;!^^^*+;+~ ,<^'        
                          zQQQD%!     ~, y,           '75wKND`     'u*xnv?~'~^``!*;~;^=+^!;;  '~.                   `\.  *\~*!` `_r  r;  `''.:,'... '''         
                          !#QQ8D~    !,^'|~          +5Umqqq;    ';imk|^^^+;*=^*!~,~^++=^!;!,       `````   ``      '?  ,\,;,,`~,i~  ,< .;;!;;~^~^;~r^,         
                          iSg#m'|   .!<.^t;         ;^IYfvr!^'    >T|7i=r|j}zTi|*||?>++;!;~;^    `,.     ,,'` ``    .c` ~;. `!=~i*`  ;! .''''.,'.'',,,          
                          ;~8KR*;   `sL'Kd.        `  ^=*<r;;Jz+;;sjoaXwXX}f{\<^;;;~~~~~;;~!*,          :'    ``     ~<`';,,~;|=`   :?.'''''',,''','',,'        
                           <DL^m`    ``S%;           ,+^>*|TzvcJmdKDWBQN#DUi;```.',;^!!;~;^^!;,,:'`     '`   `.       ,<,``';;,`  .!!``,~~~;,;;~;;~;~~;~        
                          `6;:`,}L:'~iqS'           `<!r|*^!|swUKbQ@@@@@QR<^^``~\^,.'!+^!;;;;~~~~~~;~~,,`  ``           ';!;~~~;;!~`                            
                          .d`    ,ifjt~             ,hfi!~;^;;,~*ZQ@@@QQ@N^;<<7q6yyjyyfxz\|+;,,_~~~~~~~~~,,                 ````                                
                          'E                       `<x~;=!,.^!`.T<7QknzzQ@@@QQQ#RqEoI7Tii\i|^!!;;;;;;;;~~~~~'                                                   
                           z                     ~z5}7*z!,`~7i7d#B@@QdnXkSyj}ff}szTi??*<+;~;;;;;;;;^^^!;;;~~~;,`                                                
                           z          `:.``.   ~oEnL*Toi|z}ZqWBNRqhajJ>*vTiii77iL|*<<=+r^!!!;;;~;~;!^^r=^;;!;~;;`                                               
                           z.   `      '`    'Eqs|=*xJ\vzYY{}}}}Yxz7czmwy}szTi|?**<<<*****=+;!=!=ii\IYItYn7\\*!;~ `;;'                                          
                           |i    ,`     ````~kyc|iujz*<?|ii||Liiiicv777v\iL|?*****?||i\c+~.~z7nfyyfu{uunziL|oA}5I^` jD7                                         
                           ,E|    `,'.     zkL+^**+^!;^^r+^^^r^r+++===>>======><*?|\7*;'~LZD6EyyhbK6qDDqqUmfT?i7Lii' ~w`                                        
                            !zc`     `.'''zyL+^*>^;;;;;;;;;;!!!;;;;;;;;;!!^^++++==^^7*nY|;',*omnZj}fI7|cTtjmwmj7|;.~, `                                         
                            `;*wr`       `m\+!<>;!=!;~;~~'',~~;;~~~~~~~~~;;;;~~,''',^?r_^^+LNz `7f7*i}|^+;;;^?znyJ~ `:`          ```                            
                              =^jDJ~     ;\?;^+;~;;;;~~,       `~^!,''''....'',,,'.''~^|z~ .ifv<+7jL!>!;!;;;;!!<iuji` ,`    `,_:~,''                            
                               <sr^iy5fv*ZZjzvi*Lii*>*~    `.',!|~,,..''''''',,,,''.,,,:;cr     .r!' .|;;;;;~~;, '*Yn~`~ '=|r:_^,,.`   '.                       
                               `,!Lr~!=*Lzoo5ayooao5oI;;^^^^!;,i;,,:.```....',,~~'`.'',,,~;           ~>;~;!~;:    ;uj<zZS>~~~|!,,`   _^'                       
                                  ..?`T\,}\|\|=|||L*!.        `!'..'....''...'':,....''''';;,.....'''.~c!;^;!?7T7: `To5{JzJm{z*:`    ,^:'`                      
                                       ~`'=*!^^;~~;~~.       `~,..,~',;;:~~,'',,,'....''~=77ciLL?*****7\;!!+**L7zz=;+fouTxYjT!'`    ,,<,'`                      
                                         `~~~~,,,~~~~~~~;r*|*!~'`.';;,~*L<<?*;,,,,''..';}ZwhXmsL***<*?\!^+*?**|\zffz=zyyc|!,`     '~,:^~'`                      
                                   ` ,',^?*!:,,,,,~~~~~^r++==><;...':;,'~;;;^^;,```...'!*?vJ}jafc||*?*=+!!^+?|LcczfmZUSm~`      ';;~~;!~.                       
                  `.,,,~~_,.      `=v\+^=**^;~,,,,,:~~~~!+rr^=*;''''',,'`.,,,~~~'..`..',=t|iiYZyzciiL||+^^^^<\77ztuXw6kDSx\|i7`'+^!;<|*,`                       
                  '~!!;~;;;!^~~;;,~~**!!*??<=^;~,,::,:~~~;r>!~,,''','''''``.',,,,''.',~~:!tj}faf}fyz||*<=+==?\Jt}}}yXkXdSEkXXdY?i*!i7\;.                        
                    `_;;~,,~~;^r*|~!*^;^*||?*+^!!;~~~~~~_~^;,,,'''',~,'.'...'''',,,''~<~:,~=smXo}ztw7|??***?i7sfjjah6kd6XXhESbi~;~=i|;.                         
         ,v|;'        `,+*^*7|r!;~;;<;!=*L?||*<=+^!!;;~~~~~,,,::,,',;~,'''.'','',~~;~cL!;^?7fXhy}IznXJ7T\i||LiTzywXUUbdZwwSEqDf<^+<<~.                          
         `~;;!;,,,`     `,^Ln77v>,;;^>^*?|*|L?*|<<r^^!;;!;_:~~~~;;~,!!~~,'''',''~!i*zaJ*?cIhRNASyjunDmj}}}YJ7z{jammEdD6XwwUqDdv\z{j?'`                          
          `,;;!!~~^+~'      `.,:,~~^!=*|||?||*|*?*<=++^^;~~~~;!!!!!!~^!~~~_~:,,,;7kEm7||LizDgBDXwmSoSqb6XkwSaamSoom6hAUAAqUdDu|ixjn^!~,'``                      
           `,!*|!;;!^^;'       `,~~r+*||||iLiiL||LiL|||?!,~;;;!^^!;;;!=!~~~~~;,~LUSYi\ccvzENW8Q%KqqXEmZZaooy5yjaSwZ5aUUAqKKD}**++=r<?<!~~:,'`                   
            `';7JfJ<=v|^;.    `,;:^<*iiL?i|*|LL\\iiT\i\vi!,;!!!!!!;;;;<+;!!;!Tc?SfstzJJnobQQQQQQQQNgD6ESoyoaSwmZjYjoEkXqqqXT*\v++?|>+!~~!r;.`                   
             `.,7oXX7?i7L^:`  ';:;!>\7c|i\L|iv\cTiT7cc7zu7;;;^^^^^^^^^<?^^^^+zo}jyyoZmhUqRQQQQB&Q&BQQ8RdAUhwaooooSSSwwkXUu=^+|7?|<+^~,,,~,``                    
               `.^}fjs?^ivr!''!~_!riu}t7zc\T7\7zT77zszxfyf^*^!^*i\iiL|?L=+=+=7hwEUKDDbkyjaKQQQQNQ#N8gRDdDDDKUkwmmSSSSmyT^^<|*|*^;;~:,',:.`                      
                 `,<izzi;;^^~!!,~^ijy}xxzzttJzsuss{f}fjoSj*i<zz7iizJ7\ii|+++=Tq%gWBQQgbqqDNQQBQQQBB&gg%dq6UUXhEEwafz|=^^!^=r^;~~~~,',:'`                        
                  `';<|i*^,,^^,~;imSju}J77vzuIuY{fyjfyy5wyi7=*7fwUwviiiTs=+++L6W%DNQQ@QQQQQQQQQQQgdUwS5juxz7i|*=^!!^^^!!!;;~~:,,,'','``                         
                    ,'~!!~,!^:~;}Ukofjuzz77IsstsfjyyyaaSEyTJL??TjkDga7tjj\*+=|U8gd%NQQQQQQQQgS7*^!^^^^!!;;;~~~~~~~~~:,::_~,,,,'''''``                           
                     `..,,!!,~+a6Ukaaju{Yn}jf}uufjyyaaEXE}>{jvfj\|7}fi+}yojnnfKBWbRWBQQQQQ6\!!^<\nj}z\|<^!!;~~_:::,,,:~_,,'''..'.``                             
                       `'',,~;a6UXa}ajt77Ixuj}}yfjjo5owXw{7jaomEUKDDRDKjooEmSm%BWKd8&QQQZ+!!+\ci*!_,,,,::_~~~~~~;~~_,'''''.....``                               
                      `''',~;+*7SXEy}j}{s{n{fjjy5SmSwkkmSUqKbbdddbbdDg#gXaojyU#B8d6W#QQ7!!^*!~,,:~~;!!!!!!;;;;!;;~,''''.....``                                  
                     `;^;,,~;;;^=|7uyyj{Yn}fjyoaSmwhkXUUq6hajI7i?<+^!!^=cjk8QQBQNRX%B#|!!^;,,~!*7i|?|<+^;~~_,,'''''..``..``                                     
                    `.;!^^;~~:~;;!^r+*Li\7ztY}fjjjj}Izci*=+^^!!;;;;;;;;;;;;;\kQQB%XdNi!;~,,~<zf\^,',,,,,,,,,'''..```````                                        
                        ``':;^+^;~~~;;;;;;;;!!!!!;;!!!!!;;;~~~~~~~~~~~~~~;;;;;!xWg6Xj;;~,,^ci!,,,,__:,,'''....```````                                           
                             `'~!=^;~~::~~~~~~;;;;;!^+==<**^;;^***<<+^!;~~:_~~;;^wKw*~~,,^*;,,,:__,''..''..```..``                                              
                                  `.',:~::,,,,,,,_~~~~~;;;~~~~~~;<||+;~~~~~~~,:~;;Ta!~~,!;,,,::,'..'''.````...`                                                 
                                       ``.''''''''...........```.,,'```.',:~~~~:_;~=~_,,_',,,,'.''.`````...`                                                    
                                             ````..'''''''''''........``````,~~~~_~~:,,,',','''.`````````        """)
    time.sleep(3)
    print("")
    time.sleep(3)
    print("")
    time.sleep(3)
    print("")
    time.sleep(3)
    print("")
    time.sleep(3)
# board has tuples and description
# character = make_character # make dictionary()
# use enumeration for direction
# check for challenges can be a different wording
# if character is level 1 do easy challenge, if character is level 2 do medium challenge, if character is level 3 do
# hardest challenge
# if character levels up, use ascii art
# 150 x 50 for ascii art
# dont use dictionary .get()
# combat function, does it hit function, initiative
#
# def game(): # called from main
#     rows = 5
#     columns = 5
#     board = make_board(rows, columns)
#     character = make_character("Player name")
#     achieved_goal = False
#     while not achieved_goal:
#     #Tell the user where they are
#         describe_current_location(board, character)
#         direction = get_user_choice( )
#         valid_move = validate_move(board, character, direction)
#         if valid_move:
#             move_character(character)
#             describe_current_location(board, character)
#             there_is_a_challenge = check_for_challenges()
#             if there_is_a_challenge:
#                 execute_challenge_protocol(character)
#                 if character_has_leveled():
#                     execute_glow_up_protocol()
#             achieved_goal = check_if_goal_attained(board, character)
#         else:
# Tell the user they can’t go in that direction
# Print end of game stuff like congratulations or sorry you died


def main():
    game_intro()


if __name__ == "__main__":
    main()
