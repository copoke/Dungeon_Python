import time
def clear():
    print(chr(27) + "[2J")

fight_ascii = """

 n                                                                 :.
 E%                                                                :"5
z  %                                                              :" `
K   ":                                                           z   R
?     %.                                                       :^    J
 ".    ^s                                                     f     :~
  '+.    #L                                                 z"    .*
    '+     %L                                             z"    .~
      ":    '%.                                         .#     +
        ":    ^%.                                     .#`    +"
          #:    "n                                  .+`   .z"
            #:    ":                               z`    +"
              %:   `*L                           z"    z"
                *:   ^*L                       z*   .+"
                  "s   ^*L                   z#   .*"
                    #s   ^%L               z#   .*"
                      #s   ^%L           z#   .r"
                        #s   ^%.       u#   .r"
                          #i   '%.   u#   .@"
                            #s   ^%u#   .@"
                              #s x#   .*"
                               x#`  .@%.
                             x#`  .d"  "%.
                           xf~  .r" #s   "%.
                     u   x*`  .r"     #s   "%.  x.
                     %Mu*`  x*"         #m.  "%zX"
                     :R(h x*              "h..*dN.
                   u@NM5e#>                 7?dMRMh.
                 z$@M@$#"#"                 *""*@MM$hL
               u@@MM8*                          "*$M@Mh.
             z$RRM8F"                             "N8@M$bL
            5`RM$#                                  'R88f)R
            'h.$"                                     #$x*
"""

heal_ascii = """
      ,;;;;;;, ,;;;;;;,
    ,;;;@@@@@;;;@@@@@;;;,
   ,;;;@@,;;;,@,;;;,@@;;;,
   ;;;@@;;;' ';' ';;;@@;;;
   ;;;@@;;;       ;;;@@;;;
    ;;;@@';;,   ,;;'@@;;;
     ';;;@@';;,;;'@@;;;'
       ';;;@@';'@@;;;'
         ';;;@@@;;;'
           ';;@;;' 
             ';'   
"""

damage_ascii = """
     ,;;;;;;\     ,;;;;;;,
   ,;;;@@@@@/   /;;@@@@@;;;,
  ,;;;@@,;;;\   \,@,;;;,@@;;;,
  ;;;@@;;;' '\   \;' ';;;@@;;;
  ;;;@@;;;   /   /    ;;;@@;;;
   ;;;@@';;, \   \  ,;;'@@;;;
    ';;;@@';;,\   \;;'@@;;;'
      ';;;@@';/   /'@@;;;'
        ';;;@/   /@@;;;'
          ';/   /;@;;'
                \;'
"""

bat_ascii = """
           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/                          \\
                                   ||
                                   ||
                                   \\
                                    '
"""

dragon_frame1 = """

                      ___
                     /   /`
                   // ..-_l
                 ,((:'    /`
                   \\''._\          __
          __//      \\   /`  _____//-- >
        --o  -----_^//    \^^  ---'
       `----^----'( ._____( /--
                   \\_,____\\/__,
                    \-/     \---/
1. FIGHT 2. RUN 3. SPRING
"""

dragon_frame2 = """



                                     __
          __//               _____//-- >
        --o  -----_^^^^^^^^^^  ---'
       `----^----'( \\   /( /--
                   \// _\,_\\/__,
                   //,' /   \---/
                 `((:,  _\,
                   \\ '' /
                     \___l
                          `
1. FIGHT 2. RUN 3. SPRING
"""

gargoyle_ascii = """
           _/          ,          .                                          
       , -' )         ( \-------.,')            (\_________________________  
     , ,-/ |          /\_) )     \/            ,' _.----------------------,\ 
   ,',  /, |         /      >--. ,)           / /\\                          
  / ,  //|,'        /'     '\--'\\)          /,'  \\     `         `   ,     
 / ,  // ||       ,'     (.--^( `')         //     \\                \       
( ,  //  ||,___,-'    (___\\  '^^^'        //       \\              ,        
 \  //   ||--.__     (     \`^--)  _____.-'/         \\   `                  
  >'/    ||,        (       \|_(\-'      ,'           \\         \,          
 /,'     ||          \           \      /              \\                    
(/       ||           \           )  ,'(     `     `    \\      ,            
 `       ||\           \      ) ,'  /_  )                \\    \             
         || `.          `.    ,'   /( `.\  \ , \ \,       \\   ,             
   `     || (_`.          ` .'   .'  )  `)'            ,   \\                
         ||  (_ `-v-------  ^--v' , )                      '\\,              
         ||    (    , _,-  /  -./ )'                         `)              
     `   '|     ),  ,'    '     )'                                           
        ' ;    /  ,'          ,'                                             
       /,'    /  /      '    /     , - --- .                                 
       \|    /  (          ,'   '           `.                               
       ('  ,'    `.    "  / ,'                \                              
         ,'        \    ,/,'        '`)   (_   )                             
        /           \ , /'          ,      /  /                              
       .             )  ,       ,         '  /                               
                      )      ,              /                                
       .            ' `|   ,'              /                                 
                    '  |  /              ,'                                  
        |\             | <    ______,---'                                    
        ` \            ','   (                                               
         \ '          /(____ ,`-._,-.                                        
          `.         /      `._, )---)                                       
            `-------'\         `/ \                                          
               )   )  \          ` \                                         
              /  '(    `.         `                                          
         ___,' _, /      `.         .                                        
        ('.---/ \(          .      '|                                        
        /'    `|^'           .     ,                                         
                             .     /                                         
                                   '                                          
                             '    '                                           
                           ,'  ,                                              
                         (_ '
"""

dragon_ascii = """
                 /           /                                               
                /' .,,,,  ./                                                 
               /';'     ,/                                                   
              / /   ,,//,`'`                                                 
             ( ,, '_,  ,,,' ``                                               
             |    /@  ,,, ;" `                                               
            /    .   ,''/' `,``                                              
           /   .     ./, `,, ` ;                                             
        ,./  .   ,-,',` ,,/''\,'                                             
       |   /; ./,,'`,,'' |   |                                               
       |     /   ','    /    |                                               
        \___/'   '     |     |                                               
          `,,'  |      /     `\                                              
              /      |        ~\                                            
                       '       (                                                      
             :                                                               
            ; .         \--                                                  
          :   \         ;
"""
def death():
    clear()
    print(heal_ascii)
    time.sleep(1)
    clear()
    print(damage_ascii)
    time.sleep(1)
    clear()
def spawn_dragon():
    while True:
        print(dragon_frame1)
        time.sleep(0.5)
        clear()
        print(dragon_frame2)
        time.sleep(0.5)
        clear()
death()
time.sleep(5)
print(gargoyle_ascii)
time.sleep(0.7)
print(dragon_ascii )