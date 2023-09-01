import pygame

pygame.init()

largeur, hauteur = 800, 800

ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("CHESS")
green = (119, 153, 84)

imageBR = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/BR.png")
imageBB = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/BB.png")
imageBN = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/BN.png")
imageBQ = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/BQ.png")
imageBK = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/BK.png")
imageBP = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/BP.png")
imageWR = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/WR.png")
imageWB = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/WB.png")
imageWN = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/WN.png")
imageWQ = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/WQ.png")
imageWK = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/WK.png")
imageWP = pygame.image.load("/home/felar/Bureau/Code/Python/Chess/WP.png")

def background():

    ecran.fill((255, 255, 255))
    for x in range(0, 701, 100):
        if x / 100 % 2 == 0:
            for y in range(100, 701, 200):
                pygame.draw.rect(ecran, green, (x, y, 100, 100))
        else:
            for y in range(0, 701, 200):
                pygame.draw.rect(ecran, green, (x, y, 100, 100))

def afficherpiece(*listes):

    rows, cols = len(listes[0]), len(listes)
    for row in range(rows):
        for col in range(cols):
            y, x = col, row
            x, y = x * 100, y * 100
            if listes[col][row] == 'BR':
                ecran.blit(imageBR, (x, y))
            if listes[col][row] == 'BB':
                ecran.blit(imageBB, (x, y))
            if listes[col][row] == 'BN':
                ecran.blit(imageBN, (x, y))
            if listes[col][row] == 'BQ':
                ecran.blit(imageBQ, (x, y))
            if listes[col][row] == 'BK':
                ecran.blit(imageBK, (x, y))
            if listes[col][row] == 'BP':
                ecran.blit(imageBP, (x, y))
            if listes[col][row] == 'WR':
                ecran.blit(imageWR, (x, y))
            if listes[col][row] == 'WB':
                ecran.blit(imageWB, (x, y))
            if listes[col][row] == 'WN':
                ecran.blit(imageWN, (x, y))
            if listes[col][row] == 'WQ':
                ecran.blit(imageWQ, (x, y))
            if listes[col][row] == 'WK':
                ecran.blit(imageWK, (x, y))
            if listes[col][row] == 'WP':
                ecran.blit(imageWP, (x, y))

def ecrancarre(mouse_x, mouse_y):
    grid_x = (mouse_x // 100 + 1) * 100
    grid_y = (mouse_y // 100 + 1) * 100
    return grid_x, grid_y


lists = {
    '1': ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
    '2': ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    '3': ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
    '4': ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
    '5': ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
    '6': ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
    '7': ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    '8': ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
}

piece_color = {
    'B': 'Black',
    'W': 'White',
    'X': None
}

piece_type = {
    'P': 'Pawn',
    'B': 'Bishop',
    'N': 'Knight',
    'R': 'Rook',
    'Q': 'Queen',
    'K': 'King',
    'X': None
}

def replace(grid_x1, grid_y1, grid_y, grid_x, *listes):
    grid_x1 = (grid_x1 // 100) - 1
    grid_y1 = (grid_y1 // 100) - 1
    grid_x = (grid_x // 100) - 1
    grid_y = (grid_y // 100) - 1
    
    currentpiece = listes[grid_y1][grid_x1]
    currentPieceColor = piece_color[currentpiece[0]]
    lastpiece = listes[grid_y][grid_x]
    lastPieceColor = piece_color[lastpiece[0]]
    if 'player' not in locals():
        player = 'White'
        
    if currentPieceColor == goodColor(player) and currentPieceColor != lastPieceColor and movetype(grid_x1, grid_y1, grid_y, grid_x, currentpiece, currentPieceColor, lastpiece, lastPieceColor, lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8']) == True:
        listes[grid_y][grid_x] = listes[grid_y1][grid_x1]
        listes[grid_y1][grid_x1] = 'XX'
        if player == 'White':
            player = 'Black'
        else:
            player = 'White'

def goodColor(player):
    if player == 'White':
        return 'Black'
    else:
        return 'White'

def movetype(grid_x1, grid_y1, grid_y, grid_x, currentpiece, currentPieceColor, lastpiece, *listes):
    currentPieceType = piece_type[currentpiece[1]]
    lastPieceType = piece_type[lastpiece[1]]
    
    diffx = abs(grid_x - grid_x1)
    diffy = abs(grid_y - grid_y1)
    non = 0

    if currentPieceType == 'Pawn':
        if pieceBlock(diffx, diffy, grid_x1, grid_y1, grid_y, grid_x, lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8']) == 1:
            if currentPieceColor == 'White':
                if grid_y1 == grid_y + 1 and grid_x1 == grid_x and lastPieceType == None or grid_y1 == grid_y + 2 and grid_x1 == grid_x and grid_y1 >= 6 and lastPieceType == None or lastPieceType != None and grid_x1 - 1 == grid_x and grid_y1 - 1 == grid_y or lastPieceType != None and grid_x1 + 1 == grid_x and grid_y1 - 1 == grid_y:
                    return True
            else:
                if grid_y1 == grid_y - 1 and grid_x1 == grid_x and lastPieceType == None or grid_y1 == grid_y - 2 and grid_x1 == grid_x and grid_y1 <= 1 and lastPieceType == None or lastPieceType != None and grid_x1 + 1 == grid_x and grid_y1 + 1 == grid_y or lastPieceType != None and grid_x1 - 1 == grid_x and grid_y1 + 1 == grid_y:
                    return True
    if currentPieceType == 'King':
            if diffx <= 1 and diffy <= 1:
                return True
    if currentPieceType == 'Bishop':
        if diffx == diffy and pieceBlock(diffx, diffy, grid_x1, grid_y1, grid_y, grid_x, lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8']) == 1:
            return True
    if currentPieceType == 'Rook':
        if pieceBlock(diffx, diffy, grid_x1, grid_y1, grid_y, grid_x, lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8']) == 1:
            if grid_y1 == grid_y or grid_x1 == grid_x:
                return True
    if currentPieceType == 'Queen':
        if pieceBlock(diffx, diffy, grid_x1, grid_y1, grid_y, grid_x, lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8']) == 1:
            if diffx == diffy or grid_x1 == grid_x or grid_y1 == grid_y:
                return True
    if currentPieceType == 'Knight':
        if diffx == 1 and diffy == 2 or diffx == 2 and diffy == 1:
            return True
    else:
        return False
            
def pieceBlock(diffx, diffy, grid_x1, grid_y1, grid_y, grid_x, *listes):
    incrementx = 1 if grid_x1 < grid_x else -1
    incrementy = 1 if grid_y1 < grid_y else -1

    if grid_x1 != grid_x and grid_y1 != grid_y:
        for i in range(1, diffx):
            if listes[grid_y1 + incrementy * i][grid_x1 + incrementx * i] != 'XX':
                return 0
    
    if grid_x1 == grid_x:
        for i in range(1, diffy):
            if listes[grid_y1 + incrementy * i][grid_x1] != 'XX':
                return 0
                
    if grid_y1 == grid_y:
        for i in range(1, diffx):
            if listes[grid_y1][grid_x1 + incrementx * i] != 'XX':
                return 0

    print("pieceblock PASS")
    return 1

cols = len(lists['1'])
for key in lists:
    for col in range(cols):
        print(lists[key][col], end=" ")
    print("")

player = 'White'

dragging = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x1, grid_y1 = ecrancarre(mouse_x, mouse_y)
                print("clic ici: x1:", grid_x1, grid_y1)

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x, grid_y = ecrancarre(mouse_x, mouse_y)
            replace(grid_x1, grid_y1, grid_y, grid_x, lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8'])
            print("clic ici: x", grid_x, grid_y)
    
    background()
    afficherpiece(lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'], lists['8'])
    pygame.time.Clock().tick(60)
    

    pygame.display.flip()
pygame.quit()