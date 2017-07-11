#coding: utf-8
import game
g = game.Game()

while not(g.is_finished()):
    print("")
    g.print()
    currentPos = g.get_position()
    
    # 座標で検索する順番を変える
    # 左上下右
    if(currentPos[0] <= 1 and currentPos[1] <= 1):
        #if(g.start[0] == 2 and g.start[1] == 0):
            #if(g.move(currentPos[0], currentPos[1] + 1)):
                #continue
        
        if(g.move(currentPos[0] - 1, currentPos[1])):
            continue
        elif(g.move(currentPos[0], currentPos[1] - 1)):
            continue
        elif(g.move(currentPos[0], currentPos[1] + 1)):
            continue
        elif(g.move(currentPos[0] + 1, currentPos[1])):
            continue
    
    # 左下上右
    elif(currentPos[0] <= 1 and currentPos[1] >= 2):
        #if(g.start[0] == 2 and g.start[1] == 2):
            #if(g.move(currentPos[0], currentPos[1] - 1)):
                #continue

        if(g.move(currentPos[0] - 1, currentPos[1])):
            continue
        elif(g.move(currentPos[0], currentPos[1] + 1)):
            continue
        elif(g.move(currentPos[0], currentPos[1] - 1)):
            continue
        elif(g.move(currentPos[0] + 1, currentPos[1])):
            continue
    
    # 右上下左
    elif(currentPos[0] >= 2 and currentPos[1] <= 1):
        #if(g.start[0] == 1 and g.start[1] == 0):
            #if(g.move(currentPos[0], currentPos[1] + 1)):
                #continue

        if(g.move(currentPos[0] + 1, currentPos[1])):
            continue
        elif(g.move(currentPos[0], currentPos[1] - 1)):
            continue
        elif(g.move(currentPos[0], currentPos[1] + 1)):
            continue
        elif(g.move(currentPos[0] - 1, currentPos[1])):
            continue
        
    # 右下上左
    elif(currentPos[0] >= 2 and currentPos[1] >= 2):
        if(g.move(currentPos[0] + 1, currentPos[1])):
            continue
        elif(g.move(currentPos[0], currentPos[1] + 1)):
            continue
        elif(g.move(currentPos[0], currentPos[1] - 1)):
            continue
        elif(g.move(currentPos[0] - 1, currentPos[1])):
            continue
        
    g = game.Game()

print("")
g.print()
print("成功")