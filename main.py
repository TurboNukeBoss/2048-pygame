import pygame
import random
import asyncio
pygame.init()

clock = pygame.time.Clock()
WIDTH = 900
HEIGHT = 500

keys_pressed = pygame.key.get_pressed()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

##GRID LISTS
row_1 = []
row_2 = []
row_3 = []
row_4 = []
checked = []
new_qn = []
for i in range(16):
    checked.append(0)
    new_qn.append(0)

#NEW BLOCK SIZE VAR
new_block_size = 10

#SQUARE OUTLINES
bsquare = pygame.Rect(WIDTH/2-150, HEIGHT/2 - 150,300,300)
ssquare = pygame.Rect(WIDTH/2-150, HEIGHT/2 - 150,55,55)

#COLOURS
GREY = (135, 135, 135)
DARK_GREY = (40, 40, 40)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

#Calculate position:
def cal_pos(collumn, row):
    drawx = WIDTH/2 - 150 + collumn * 10 + (collumn != 1)*(collumn - 1) * 62.5
    drawy = HEIGHT/2 - 150 + row * 10 + (row != 1)*(row - 1) * 62.5
    
    return [drawx,drawy]

#POSTIONS LISTS
fut_positions = []
prev_pos = []
cur_pos = []
pos_change = []
for i in range(16):
    fut_positions.append(cal_pos(i % 4 + 1, i//4 + 1))
    prev_pos.append(cal_pos(i % 4 + 1, i//4 + 1))
    cur_pos.append(cal_pos(i % 4 + 1, i//4 + 1))
    pos_change.append((0,0))



#RIGHT MOVEMENT
def block_movementd():
    global row_1
    global row_2
    global row_3
    global row_4
    global checked
    global fut_positions
    global prev_pos
    global cur_pos
    for yes in range(1,5):
        if yes == 1:
            selected_row = row_1
        elif yes == 2:
            selected_row = row_2
        elif yes == 3:
            selected_row = row_3
        elif yes == 4:
            selected_row = row_4
        for block in range(2,-1,-1):
            block_val = selected_row[block]
            #print(block_val)
            if checked[block + (yes != 1) * (yes - 1) * 4] == 0:
                for i in range(block + 1, 4):
                    if selected_row[i] == 0:
                        #if block_val != 0:
                        #    print("CHANGED")
                        selected_row[i] = block_val
                        selected_row[i - 1] = 0
                        fut_positions[i + (yes != 1) * (yes - 1) * 4] = cal_pos(i + 1, yes)
                        fut_positions[block + (yes != 1) * (yes - 1) * 4] = (0, 0)
                        prev_pos[i + (yes != 1) * (yes - 1) * 4] = cal_pos(block + 1, yes)
                        prev_pos[block + (yes != 1) * (yes - 1) * 4] = (0, 0)
                        
                        pos_change[i + (yes - 1) * 4] = (cal_pos(i + 1, yes)[0] - cal_pos(block + 1, yes)[0])/5, (cal_pos(i + 1, yes)[1] - cal_pos(block + 1, yes)[1])/5
                    elif selected_row[i] == block_val and i == block + 1 and checked[i + (yes != 1) * (yes - 1) * 4] != 1 and checked[i - 1 + (yes != 1) * (yes - 1) * 4] != 1:
                        selected_row[i] = block_val * 2
                        selected_row[i - 1] = 0

                        checked[i + (yes != 1) * (yes - 1) * 4] = 1
                        fut_positions[i + (yes != 1) * (yes - 1) * 4] = cal_pos(i + 1, yes)
                        fut_positions[block + (yes != 1) * (yes - 1) * 4] = (0, 0)
                        prev_pos[i + (yes != 1) * (yes - 1) * 4] = cal_pos(block + 1, yes)
                        prev_pos[block + (yes != 1) * (yes - 1) * 4] = (0, 0)

                        pos_change[i + (yes - 1) * 4] = (cal_pos(i + 1, yes)[0] - cal_pos(block + 1, yes)[0])/5, (cal_pos(i + 1, yes)[1] - cal_pos(block + 1, yes)[1])/5
                    else:
                        continue
                    if yes == 1:
                        row_1 = selected_row
                    elif yes == 2:
                        row_2 = selected_row
                    elif yes == 3:
                        row_3 = selected_row
                    elif yes == 4:
                        row_4 = selected_row
    
#LEFT MOVEMENT
def block_movementa():
    global row_1
    global row_2
    global row_3
    global row_4
    global checked
    global fut_positions
    global prev_pos
    global cur_pos
    for yes in range(1,5):
        if yes == 1:
            selected_row = row_1
        elif yes == 2:
            selected_row = row_2
        elif yes == 3:
            selected_row = row_3
        elif yes == 4:
            selected_row = row_4
        for block in range(1,4):
            block_val = selected_row[block]
            #print(block_val)
            #if yes == 2:
                #print(block_val)
                #print("eeeeeee" + str(block))
            if checked[block + (yes != 1) * (yes - 1) * 4] == 0:
                for i in range(block - 1 , -1, -1):
                    #if yes == 2:
                        #print(i)
                        #print(selected_row[i], block_val)
                    if selected_row[i] == 0:
                        #if block_val != 0:
                        #    print("CHANGED")
                        selected_row[i] = block_val
                        selected_row[i + 1] = 0
                        fut_positions[i + (yes != 1) * (yes - 1) * 4] = cal_pos(i + 1, yes)
                        fut_positions[block + (yes != 1) * (yes - 1) * 4] = (0, 0)
                        prev_pos[i + (yes != 1) * (yes - 1) * 4] = cal_pos(block + 1, yes)
                        prev_pos[block + (yes != 1) * (yes - 1) * 4] = (0, 0)
                        pos_change[i + (yes - 1) * 4] = (cal_pos(i + 1, yes)[0] - cal_pos(block + 1, yes)[0])/5, (cal_pos(i + 1, yes)[1] - cal_pos(block + 1, yes)[1])/5
                    elif selected_row[i] == block_val and i == block - 1 and checked[i + (yes != 1) * (yes - 1) * 4] != 1 and checked[i + 1 + (yes != 1) * (yes - 1) * 4] != 1:
                        selected_row[i] = block_val * 2
                        selected_row[i + 1] = 0
                        checked[i + (yes != 1) * (yes - 1) * 4] = 1
                        fut_positions[i + (yes != 1) * (yes - 1) * 4] = cal_pos(i + 1, yes)
                        fut_positions[block + (yes != 1) * (yes - 1) * 4] = (0, 0)
                        prev_pos[i + (yes != 1) * (yes - 1) * 4] = cal_pos(block + 1, yes)
                        prev_pos[block + (yes != 1) * (yes - 1) * 4] = (0, 0)

                        pos_change[i + (yes - 1) * 4] = (cal_pos(i + 1, yes)[0] - cal_pos(block + 1, yes)[0])/5, (cal_pos(i + 1, yes)[1] - cal_pos(block + 1, yes)[1])/5
                    else:
                        break
                    if yes == 1:
                        row_1 = selected_row
                    elif yes == 2:
                        row_2 = selected_row
                    elif yes == 3:
                        row_3 = selected_row
                    elif yes == 4:
                        row_4 = selected_row
    
#UP
def block_movementw():
    global row_1
    global row_2
    global row_3
    global row_4
    global checked
    global fut_positions
    global prev_pos
    global cur_pos
    for yes in range(1,5):
        if yes == 1:
            selected_row = [row_1[0], row_2[0], row_3[0], row_4[0]]
        elif yes == 2:
            selected_row = [row_1[1], row_2[1], row_3[1], row_4[1]]
        elif yes == 3:
            selected_row = [row_1[2], row_2[2], row_3[2], row_4[2]]
        elif yes == 4:
            selected_row = [row_1[3], row_2[3], row_3[3], row_4[3]]
        for block in range(1,4):
            block_val = selected_row[block]
            #print(block_val)
            #if yes == 2:
                #print(block_val)
                #print("eeeeeee" + str(block))
            if checked[block + (yes != 1) * (yes - 1) * 4] == 0:
                for i in range(block - 1 , -1, -1):
                    #if yes == 2:
                        #print(i)
                        #print(selected_row[i], block_val)
                    if selected_row[i] == 0:
                        #if block_val != 0:
                        #    print("CHANGED")
                        selected_row[i] = block_val
                        selected_row[i + 1] = 0
                        fut_positions[yes - 1 + i * 4] = cal_pos(yes, i + 1)
                        fut_positions[yes - 1 + block * 4] = (0, 0)
                        prev_pos[yes - 1 + i * 4] = cal_pos(yes, block + 1)
                        prev_pos[yes - 1 + block * 4] = (0, 0)
                        pos_change[yes - 1 + i * 4] = (cal_pos(yes, i + 1)[0] - cal_pos(yes, block + 1)[0])/5, (cal_pos(yes, i + 1)[1] - cal_pos(yes, block + 1)[1])/5
                    elif selected_row[i] == block_val and i == block - 1 and checked[yes - 1 + i * 4] != 1 and checked[yes - 1 + (i + 1) * 4] != 1:
                        
                        selected_row[i] = block_val * 2
                        selected_row[i + 1] = 0
                        checked[yes - 1 + i * 4] = 1
                        fut_positions[yes - 1 + i * 4] = cal_pos(yes, i + 1)
                        fut_positions[yes - 1 + block * 4] = (0, 0)
                        prev_pos[yes - 1 + i * 4] = cal_pos(yes, block + 1)
                        prev_pos[yes - 1 + block * 4] = (0, 0)

                        pos_change[yes - 1 + i * 4] = (cal_pos(yes, i + 1)[0] - cal_pos(yes, block + 1)[0])/5, (cal_pos(yes, i + 1)[1] - cal_pos(yes, block + 1)[1])/5
                    else:
                        break
                    if yes == 1:
                        row_1[0] = selected_row[0]
                        row_2[0] = selected_row[1]
                        row_3[0] = selected_row[2]
                        row_4[0] = selected_row[3]
                    elif yes == 2:
                        row_1[1] = selected_row[0]
                        row_2[1] = selected_row[1]
                        row_3[1] = selected_row[2]
                        row_4[1] = selected_row[3]
                    elif yes == 3:
                        row_1[2] = selected_row[0]
                        row_2[2] = selected_row[1]
                        row_3[2] = selected_row[2]
                        row_4[2] = selected_row[3]
                    elif yes == 4:
                        row_1[3] = selected_row[0]
                        row_2[3] = selected_row[1]
                        row_3[3] = selected_row[2]
                        row_4[3] = selected_row[3]
    
#DOWN
def block_movements():
    global row_1
    global row_2
    global row_3
    global row_4
    global checked
    global fut_positions
    global prev_pos
    global cur_pos
    for yes in range(1,5):
        if yes == 1:
            selected_row = [row_1[0], row_2[0], row_3[0], row_4[0]]
        elif yes == 2:
            selected_row = [row_1[1], row_2[1], row_3[1], row_4[1]]
        elif yes == 3:
            selected_row = [row_1[2], row_2[2], row_3[2], row_4[2]]
        elif yes == 4:
            selected_row = [row_1[3], row_2[3], row_3[3], row_4[3]]
        for block in range(2,-1,-1):
            block_val = selected_row[block]
            #print(block_val)
            if checked[block + (yes != 1) * (yes - 1) * 4] == 0:
                for i in range(block + 1, 4):
                    if selected_row[i] == 0:
                        #if block_val != 0:
                        #    print("CHANGED")
                        selected_row[i] = block_val
                        selected_row[i - 1] = 0
                        fut_positions[yes - 1 + i * 4] = cal_pos(yes, i + 1)
                        fut_positions[yes - 1 + block * 4] = (0, 0)
                        prev_pos[yes - 1 + i * 4] = cal_pos(yes, block + 1)
                        prev_pos[yes - 1 + block * 4] = (0, 0)
                        pos_change[yes - 1 + i * 4] = (cal_pos(yes, i + 1)[0] - cal_pos(yes, block + 1)[0])/5, (cal_pos(yes, i + 1)[1] - cal_pos(yes, block + 1)[1])/5
                    elif selected_row[i] == block_val and i == block + 1 and checked[yes - 1 + i * 4] != 1 and checked[yes - 1 + (i - 1) * 4] != 1:
                        selected_row[i] = block_val * 2
                        selected_row[i - 1] = 0
                        checked[yes - 1 + i * 4] = 1
                        fut_positions[yes - 1 + i * 4] = cal_pos(yes, i + 1)
                        fut_positions[yes - 1 + block * 4] = (0, 0)
                        prev_pos[yes - 1 + i * 4] = cal_pos(yes, block + 1)
                        prev_pos[yes - 1 + block * 4] = (0, 0)

                        pos_change[yes - 1 + i * 4] = (cal_pos(yes, i + 1)[0] - cal_pos(yes, block + 1)[0])/5, (cal_pos(yes, i + 1)[1] - cal_pos(yes, block + 1)[1])/5
                    else:
                        break
                    if yes == 1:
                        row_1[0] = selected_row[0]
                        row_2[0] = selected_row[1]
                        row_3[0] = selected_row[2]
                        row_4[0] = selected_row[3]
                    elif yes == 2:
                        row_1[1] = selected_row[0]
                        row_2[1] = selected_row[1]
                        row_3[1] = selected_row[2]
                        row_4[1] = selected_row[3]
                    elif yes == 3:
                        row_1[2] = selected_row[0]
                        row_2[2] = selected_row[1]
                        row_3[2] = selected_row[2]
                        row_4[2] = selected_row[3]
                    elif yes == 4:
                        row_1[3] = selected_row[0]
                        row_2[3] = selected_row[1]
                        row_3[3] = selected_row[2]
                        row_4[3] = selected_row[3]
    


##CHECK AND DELETE EMPTY SPACES
def check_empt():
    global fut_positions
    global prev_pos
    global cur_pos
    for yes in range(1,5):
        if yes == 1:
            selected_row = row_1
        elif yes == 2:
            selected_row = row_2
        elif yes == 3:
            selected_row = row_3
        elif yes == 4:
            selected_row = row_4
        for i in range(4):
            if selected_row[i] == 0:
                fut_positions[i + (yes-1) * 4] = (0, 0)
            
#CHANGE BLOCK POSITIONS PARTIALLY
def change_pos():
    global cur_pos
    global fut_positions
    global prev_pos
    for yes in range(16):
        if cur_pos[yes] != fut_positions[yes] and fut_positions[yes]!= 0:
            #if cur_pos == prev_pos:
            #print(fut_positions[yes][0] - prev_pos[yes][0])    
            ##if prev_pos[yes][0] > fut_positions[yes][0]:
            ##    cx = 10
            ##elif prev_pos[yes][0] < fut_positions[yes[0]]:
            ##    cx = -10
            ##elif prev_pos[yes][1] > fut_positions[yes][1]:
            ##    cy = 10
            ##elif prev_pos[yes][1] < fut_positions[yes][1]:
            ##    cy = -10
            cur_pos[yes][0] += pos_change[yes][0]
            cur_pos[yes][1] += pos_change[yes][1]
            ##cur_pos[yes][0] += (fut_positions[yes][0] - prev_pos[yes][0]) / 10
            ##cur_pos[yes][1] += (fut_positions[yes][1] - prev_pos[yes][1]) / 10
            
    #cur_pos = fut_positions
def generate_new_block():
    global row_1
    global row_2
    global row_3
    global row_4
    global checked
    global fut_positions
    global prev_pos
    global cur_pos
    empty_blocks = []
    for i in range(16):
        if i // 4 == 0 and row_1[i % 4] == 0:
            empty_blocks.append(i)
        if i // 4 == 1 and row_2[i % 4] == 0:
            empty_blocks.append(i)
        if i // 4 == 2 and row_3[i % 4] == 0:
            empty_blocks.append(i)
        if i // 4 == 3 and row_4[i % 4] == 0:
            empty_blocks.append(i)
    if len(empty_blocks) != 0:
        block = random.choice(empty_blocks)
        row = block // 4
        collumn = block % 4
        if row == 0:
            if random.randint(1,2) == 1:
                row_1[collumn] = 2
            else:
                row_1[collumn] = 4
        elif row == 1:
            if random.randint(1,2) == 1:
                row_2[collumn] = 2
            else:
                row_2[collumn] = 4
        elif row == 2:
            if random.randint(1,2) == 1:
                row_3[collumn] = 2
            else:
                row_3[collumn] = 4
        elif row == 3:
            if random.randint(1,2) == 1:
                row_4[collumn] = 2
            else:
                row_4[collumn] = 4
                
        fut_positions[block] = cal_pos(collumn + 1, row + 1)
        prev_pos[block] = cal_pos(collumn + 1, row + 1)
        cur_pos[block] = cal_pos(collumn + 1, row + 1)
        pos_change[block] = (0,0)
        new_qn[block] = 1
    else:
        print("GAME OVER")
        pygame.quit()
        quit()


##WINDOW SET UP
def draw_window():
    global row_1
    global row_2
    global row_3
    global row_4
    global new_block_size
    WIN.fill((0,0,0))
    pygame.draw.rect(WIN, GREY, bsquare)
    for i in range(1,5):
        for j in range(1,5):
            ssquare = pygame.Rect(WIDTH/2-150 + j * 10 + (j!= 1)*(j-1) * 62.5, HEIGHT/2 - 150 + i * 10 + (i!= 1)*(i-1) * 62.5, 62.5, 62.5)
            pygame.draw.rect(WIN, DARK_GREY, ssquare)
    #for i in range(1,5):
    #    if i == 1:
    #        sel_row = row_1
    #    elif i == 2:
    #        sel_row = row_2
    #    elif i == 3:
    #        sel_row = row_3
    #    elif i == 4:
    #        sel_row = row_4
    #    for j in range(1,5):
    #        if sel_row[j-1] != 0:
    #            drawx = WIDTH/2-150 + j * 10 + (j!= 1)*(j-1) * 62.5
    #            drawy = HEIGHT/2 - 150 + i * 10 + (i!= 1)*(i-1) * 62.5
    #            blocksquare = pygame.Rect(drawx, drawy, 62.5, 62.5)
    #            pygame.draw.rect(WIN, ORANGE, blocksquare)
    #            draw_num_text(str(sel_row[j-1]), pygame.font.Font(None, 36), WHITE, drawx + 12.5, drawy + 12.5)
    #            draw_num_text(str(blocksquare.x) + str(blocksquare.y), pygame.font.Font(None, 36), WHITE, drawx, drawy)
    if new_block_size != 100:
        new_block_size += 10
    for i in range(16):  
        drawx, drawy = cur_pos[i][0], cur_pos[i][1]
        if new_qn[i] == 1:
            blocksquare = pygame.Rect(drawx + (62.5 -  new_block_size/100 * 62.5)/2, drawy + (62.5 -  new_block_size/100 * 62.5)/2, new_block_size/100 * 62.5, new_block_size/100 * 62.5)
        else:
            blocksquare = pygame.Rect(drawx, drawy, 62.5, 62.5)
        if i // 4 == 0 and row_1[i % 4] != 0:
            pygame.draw.rect(WIN, ORANGE, blocksquare)
            draw_num_text(str(row_1[i % 4]), pygame.font.Font(None, 36), WHITE, drawx, drawy)
        elif i // 4 == 1 and row_2[i % 4] != 0:
            pygame.draw.rect(WIN, ORANGE, blocksquare)
            draw_num_text(str(row_2[i % 4]), pygame.font.Font(None, 36), WHITE, drawx, drawy)
        elif i // 4 == 2 and row_3[i % 4] != 0:
            pygame.draw.rect(WIN, ORANGE, blocksquare)
            draw_num_text(str(row_3[i % 4]), pygame.font.Font(None, 36), WHITE, drawx, drawy)
        elif i // 4 == 3 and row_4[i % 4] != 0:
            pygame.draw.rect(WIN, ORANGE, blocksquare)
            draw_num_text(str(row_4[i % 4]), pygame.font.Font(None, 36), WHITE, drawx, drawy)
    change_pos()
    pygame.display.update()

#NUM TEXT FUNCTION
def draw_num_text(text, font, text_col, x, y):
    numba = font.render(text, True, text_col)
    if numba.get_width() > 50:
        numba = pygame.transform.scale(numba,(50, 50/numba.get_width() * numba.get_height()))
    
    WIN.blit(numba, (x + (62.5 - numba.get_width())/2, y + (62.5 - numba.get_height())/2))

#MAIN SYSTEM
async def main():
    run = True
    global row_1
    global row_2
    global row_3
    global row_4
    global checked
    global fut_positions
    global prev_pos
    global cur_pos
    global new_qn
    global new_block_size
    row_1 = [2,2,0,0]
    row_2 = [2,0,0,0]
    row_3 = [0,0,0,0]
    row_4 = [0,0,0,0]
    checked = []
    new_qn = []
    for i in range(16):
        checked.append(0)
        new_qn.append(0)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    checked = []
                    
                    new_qn =[]
                    new_block_size = 10
                    prev_grid = [tuple(row_1), tuple(row_2), tuple(row_3), tuple(row_4)]
                    for i in range(16):
                        checked.append(0)
                        
                        new_qn.append(0)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        block_movementd()
                        block_movementd()
                        check_empt()
                        
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        block_movementa()
                        block_movementa()
                        check_empt()
                        
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        block_movementw()
                        block_movementw()
                        check_empt()
                        
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        block_movements()
                        block_movements()
                        check_empt()
                    cur_pos = prev_pos
                    
                    #    generate_new_block()
                    if prev_grid != [tuple(row_1), tuple(row_2), tuple(row_3), tuple(row_4)]:
                        generate_new_block()
                    print(str(row_1) + "\n" + str(row_2) + "\n" + str(row_3) + "\n" + str(row_4) + "\n")
                elif event.key == pygame.K_SPACE:
                    print(str(row_1) + "\n" + str(row_2) + "\n" + str(row_3) + "\n" + str(row_4))
                    print(checked)
                    ##print("START")
                    ##print(fut_positions)
                    ##print(prev_pos)
                    ##print(cur_pos)
                    ##print("END")
        draw_window()
        await asyncio.sleep(0)
        #for i in range(4):
        #    for j in range(4):
        #        print(str(positions[j + i * 4]))
        #    print("\n")
        

#MAIN SYSTEM
print("yes")
asyncio.run(main())
