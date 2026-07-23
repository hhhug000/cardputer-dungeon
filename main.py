import pygame
import sys

CELL_SIZE = 32
UI_HEIGHT = 64
GRID_COLS = 24
GRID_ROWS = 14

SCREEN_WIDTH = GRID_COLS * CELL_SIZE
SCREEN_HEIGHT = (GRID_ROWS * CELL_SIZE) + UI_HEIGHT

COLOR_BLACK = (0, 0, 0)
COLOR_SAND = (235, 210, 160)
COLOR_DUNGEON_FLOOR = (45, 45, 55)
COLOR_GREEN = (34, 139, 34)
COLOR_DARK_GREEN = (0, 100, 0)
COLOR_BLUE = (30, 144, 255)
COLOR_LIGHT_BLUE = (135, 206, 250)
COLOR_BROWN = (139, 69, 19)
COLOR_GOLD = (255, 215, 0)
COLOR_HEART = (220, 20, 60)
COLOR_WHITE = (255, 255, 255)
COLOR_STONE_DARK = (60, 60, 75)
COLOR_STONE_LIGHT = (120, 120, 140)
COLOR_BUNKER_WALL = (80, 90, 100)
COLOR_PROJECTILE = (255, 69, 0)

WEAPONS = {
    "sword": {"range": 1, "type": "melee"},
    "gun": {"range": 8, "type": "ranged"},
    "spear": {"range": 2, "type": "melee"},
    "wand": {"range": 5, "type": "ranged"}
}

MAPS = {
    "ow_northwest": [
        "%%%%%%%%%%%%%%%%%%%%%%%%",
        "%....###.........######%",
        "%...#####..~~~~...#####%",
        "%..#######.~~~~...####.%",
        "%..#######..~~....###..%",
        "%...#####.........##...%",
        "%....###...............%",
        "%..........~~~~~.......%",
        "%..........~~~~~~......%",
        "%...###.....~~~~.......2",
        "%..#####...............2",
        "%..######..............2",
        "%a...####...............2",
        "%%%%%33333333333333%%%%%"
    ],
    "ow_north": [
        "%%%%%%%%%%%%%%%%%%%%%%%%",
        "%######............####%",
        "%#####....~~~~~.....###%",
        "%.###....~~~~~~~....##.%",
        "%........~~~~~~~~......%",
        "%.........~~~~~~.......%",
        "%..........~~~~........%",
        "%...E..................%",
        "%........###....###....%",
        "2.......#####..#####...3",
        "2.......#####..#####...3",
        "2........###....###....3",
        "2......................3",
        "%%%%%11111111111111%%%%%"
    ],
    "ow_northeast": [
        "%%%%%%%%%%%%%%%%%%%%%%%%",
        "%####..................%",
        "%###....E.......C......%",
        "%.##...................%",
        "%.......~~~~~~~........%",
        "%......~~~~~~~~~.......%",
        "%......~~~~~~~~~...E...%",
        "%.......~~~~~~~........%",
        "%........~~~~~.........%",
        "3......................%",
        "3...$..............$...%",
        "3......................%",
        "3......................%",
        "%%%%%22222222222222%%%%%"
    ],
    "ow_west": [
        "%%%%%33333333333333%%%%%",
        "%...####...............1",
        "%..######..............1",
        "%..#######.............1",
        "%...#####......~~~~....1",
        "%....###......~~~~~~...1",
        "%.............~~~~~~...1",
        "%..............~~~~....1",
        "%......................1",
        "%......................1",
        "%...E.........~~~~.....1",
        "%............~~~~~~....1",
        "%...####......~~~~.....1",
        "%%%%%44444444444444%%%%%"
    ],
    "ow_center": [
        "%%%%%11111111111111%%%%%",
        "4......................3",
        "4......BBBBBBBBBB......3",
        "4......B........B......3",
        "4......B...BB...B......3",
        "4......B...>>...B......3",
        "4......B...>>...B......3",
        "4......B...BB...B......3",
        "4......B........B......3",
        "4......BBBB..BBBB......3",
        "4......................3",
        "4...E..............E...3",
        "4......................3",
        "%%%%%22222222222222%%%%%"
    ],
    "ow_east": [
        "%%%%%22222222222222%%%%%",
        "3......................%",
        "3...~~~~...............%",
        "3..~~~~~~....E.........%",
        "3..~~~~~~..............%",
        "3...~~~~.......####....%",
        "3.............######...%",
        "3............########..%",
        "3...W........########..%",
        "3.............######...%",
        "3..............####....%",
        "3......................%",
        "3......................%",
        "%%%%%55555555555555%%%%%"
    ],
    "ow_southwest": [
        "%%%%%44444444444444%%%%%",
        "%......................1",
        "%...####........E......1",
        "%..######..............1",
        "%..######..............1",
        "%...####...............1",
        "%..........~~~~~~......1",
        "%.........~~~~~~~~.....1",
        "%.........~~~~~~~~.....1",
        "%..........~~~~~~......1",
        "%...C..................1",
        "%......................1",
        "%......................1",
        "%%%%%%%%%%%%%%%%%%%%%%%%"
    ],
    "ow_south": [
        "%%%%%33333333333333%%%%%",
        "1......................2",
        "1......................2",
        "1...E..............E...2",
        "1........~~~~~~........2",
        "1.......~~~~~~~~.......2",
        "1.......~~~~~~~~.......2",
        "1........~~~~~~........2",
        "1......................2",
        "1....G............P....2",
        "1......................2",
        "1..........$$..........2",
        "1......................2",
        "%%%%%%%%%%%%%%%%%%%%%%%%"
    ],
    "ow_southeast": [
        "%%%%%55555555555555%%%%%",
        "2......................%",
        "2......####............%",
        "2.....######...E.......%",
        "2.....######...........%",
        "2......####............%",
        "2..............~~~~....%",
        "2.............~~~~~~...%",
        "2.............~~~~~~...%",
        "2..............~~~~....%",
        "2...M..................%",
        "2......................%",
        "2......................%",
        "%%%%%%%%%%%%%%%%%%%%%%%%"
    ],
    "dun_bunker_entry": [
        "BBBBBBBBBBBBBBBBBBBBBBBB",
        "B......................B",
        "B...BBBB........BBBB...B",
        "B...B..B...>>...B..B...B",
        "B...B..B...>>...B..B...B",
        "B...BBBB........BBBB...B",
        "B......................B",
        "B......................B",
        "%%%%%..................%",
        "%...%%.................%",
        "%....%%..............%%%",
        "%.....%..............%%%",
        "%......................%",
        "%%%%%11111111111111%%%%%"
    ],
    "dun_west_cave": [
        "%%%%%%%%%%%%%%%%%%%%%%%%",
        "%......................1",
        "%...%%%%........%%%%...1",
        "%..%%%%%%..E...%%%%%%..1",
        "%..%%%%%%......%%%%%%..1",
        "%...%%%%........%%%%...1",
        "%......................1",
        "%.........~~~~.........1",
        "%........~~~~~~........1",
        "%........~~~~~~........1",
        "%.........~~~~.........1",
        "%...C..................1",
        "%......................1",
        "%%%%%22222222222222%%%%%"
    ],
    "dun_central_hub": [
        "%%%%%11111111111111%%%%%",
        "4......................2",
        "4...%%%%........%%%%...2",
        "4..%%%%%%..E...%%%%%%..2",
        "4..%%%%%%......%%%%%%..2",
        "4...%%%%........%%%%...2",
        "4......................2",
        "4......~~~~~~~~~~......2",
        "4......~~~~~~~~~~......2",
        "4......~~~~~~~~~~......2",
        "4...%%%%........%%%%...2",
        "4..%%%%%%..E...%%%%%%..2",
        "4...%%%%........%%%%...2",
        "%%%%%33333333333333%%%%%"
    ],
    "dun_east_vault": [
        "%%%%%%%%%%%%%%%%%%%%%%%%",
        "2......................%",
        "2...%%%%........%%%%...%",
        "2..%%%%%%......%%%%%%..%",
        "2..%....%......%....%..%",
        "2..%..C.%...E..%.C..%..%",
        "2..%....%......%....%..%",
        "2..%%%%%%......%%%%%%..%",
        "2......................%",
        "2........$$$$$$........%",
        "2........$CCCC$........%",
        "2........$$$$$$........%",
        "2......................%",
        "%%%%%44444444444444%%%%%"
    ],
    "dun_south_tunnel": [
        "%%%%%22222222222222%%%%%",
        "%......................1",
        "%...%%%%........%%%%...1",
        "%..%%%%%%......%%%%%%..1",
        "%..%%%%%%..E...%%%%%%..1",
        "%...%%%%........%%%%...1",
        "%......................1",
        "%....~~~~......~~~~....1",
        "%...~~~~~~....~~~~~~...1",
        "%...~~~~~~....~~~~~~...1",
        "%....~~~~......~~~~....1",
        "%......................1",
        "%...E..............E...1",
        "%%%%%55555555555555%%%%%"
    ],
    "dun_boss_lair": [
        "%%%%%33333333333333%%%%%",
        "1......................%",
        "1...~~~~..........~~~~.%",
        "1...~~~~...EEEE...~~~~.%",
        "1...~~~~...EEEE...~~~~.%",
        "1......................%",
        "1........>>>>..........%",
        "1........>>>>..........%",
        "1......................%",
        "1...~~~~...EEEE...~~~~.%",
        "1...~~~~...EEEE...~~~~.%",
        "1...~~~~..........~~~~.%",
        "1......................%",
        "%%%%%%%%%%%%%%%%%%%%%%%%"
    ],
    "dun_deep_vault": [
        "%%%%%%%%%%%%%%%%%%%%%%%%",
        "%......................%",
        "%..$$$$$$$$$$$$$$$$$$..%",
        "%..$................$..%",
        "%..$..CCCCCCCCCCCC..$..%",
        "%..$..CCCCCCCCCCCC..$..%",
        "%..$.......>>>>.....$..%",
        "%..$.......>>>>.....$..%",
        "%..$..CCCCCCCCCCCC..$..%",
        "%..$..CCCCCCCCCCCC..$..%",
        "%..$................$..%",
        "%..$$$$$$$$$$$$$$$$$$..%",
        "%......................%",
        "%%%%%%%%%%%%%%%%%%%%%%%%"
    ]
}

MAP_LINKS = {
    "ow_northwest": {
        "1": ("ow_west", 22, 5),
        "2": ("ow_north", 1, 10),
        "3": ("ow_west", 12, 1)
    },
    "ow_north": {
        "1": ("ow_center", 12, 1),
        "2": ("ow_northwest", 22, 10),
        "3": ("ow_northeast", 1, 10)
    },
    "ow_northeast": {
        "1": ("ow_north", 22, 10),
        "2": ("ow_east", 12, 1),
        "3": ("ow_north", 22, 10)
    },
    "ow_west": {
        "1": ("ow_center", 1, 6),
        "2": ("ow_southwest", 22, 10),
        "3": ("ow_northwest", 12, 12),
        "4": ("ow_southwest", 12, 1)
    },
    "ow_center": {
        "1": ("ow_north", 12, 12),
        "2": ("ow_south", 12, 1),
        "3": ("ow_east", 1, 6),
        "4": ("ow_west", 22, 6),
        ">": ("dun_bunker_entry", 11, 8)
    },
    "ow_east": {
        "1": ("ow_northeast", 12, 12),
        "2": ("ow_northeast", 12, 12),
        "3": ("ow_center", 22, 6),
        "5": ("ow_southeast", 12, 1)
    },
    "ow_southwest": {
        "1": ("ow_south", 1, 6),
        "4": ("ow_west", 12, 12)
    },
    "ow_south": {
        "1": ("ow_southwest", 22, 6),
        "2": ("ow_southeast", 1, 6),
        "3": ("ow_center", 12, 12)
    },
    "ow_southeast": {
        "2": ("ow_south", 22, 6),
        "5": ("ow_east", 12, 12)
    },
    "dun_bunker_entry": {
        ">": ("ow_center", 10, 7),
        "1": ("dun_central_hub", 12, 1)
    },
    "dun_west_cave": {
        "1": ("dun_central_hub", 1, 6),
        "2": ("dun_south_tunnel", 12, 1)
    },
    "dun_central_hub": {
        "1": ("dun_bunker_entry", 12, 12),
        "2": ("dun_east_vault", 1, 6),
        "3": ("dun_south_tunnel", 12, 1),
        "4": ("dun_west_cave", 22, 6)
    },
    "dun_east_vault": {
        "2": ("dun_central_hub", 22, 6),
        "4": ("dun_south_tunnel", 12, 1)
    },
    "dun_south_tunnel": {
        "1": ("dun_boss_lair", 1, 6),
        "2": ("dun_central_hub", 12, 12),
        "5": ("dun_boss_lair", 12, 1)
    },
    "dun_boss_lair": {
        "1": ("dun_south_tunnel", 22, 6),
        "3": ("dun_south_tunnel", 12, 12),
        ">": ("dun_deep_vault", 11, 6)
    },
    "dun_deep_vault": {
        ">": ("dun_boss_lair", 11, 8)
    }
}

class Projectile:
    def __init__(self, x, y, dx, dy, friendly=True):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.friendly = friendly

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cardputer Dungeon")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 18, bold=True)

        self.runtime_maps = {k: [list(row) for row in v] for k, v in MAPS.items()}
        self.current_map = "ow_center"

        self.player_x = 12
        self.player_y = 10
        self.player_dx = 0
        self.player_dy = 1

        self.score = 0
        self.hearts = 5
        self.weapon = "sword"

        self.move_cooldown = 120
        self.last_move_time = 0

        self.enemy_move_cooldown = 350
        self.last_enemy_move_time = 0

        self.damage_cooldown = 1000
        self.last_damage_time = 0

        self.attack_cooldown = 180
        self.last_attack_time = 0

        self.projectiles = []
        self.enemies = []
        self.active_grid = []

        self.load_map_state()

    def load_map_state(self):
        self.active_grid = self.runtime_maps[self.current_map]
        self.enemies = []
        self.projectiles = []

        for y in range(len(self.active_grid)):
            for x in range(len(self.active_grid[y])):
                tile = self.active_grid[y][x]
                if tile == "E":
                    self.enemies.append({
                        "x": x, "y": y, "dx": 0, "dy": 1, "health": 1
                    })
                    self.active_grid[y][x] = "."

    def is_obstacle(self, tile):
        return tile in ["#", "%", "~", "B"]

    def is_dungeon(self):
        return self.current_map.startswith("dun_")

    def move_player(self, dx, dy):
        self.player_dx = dx
        self.player_dy = dy

        target_x = self.player_x + dx
        target_y = self.player_y + dy

        if not (0 <= target_x < GRID_COLS and 0 <= target_y < GRID_ROWS):
            return

        target_tile = self.active_grid[target_y][target_x]

        if target_tile in MAP_LINKS.get(self.current_map, {}):
            target_map, dest_x, dest_y = MAP_LINKS[self.current_map][target_tile]
            if target_tile in ["1", "2", "3", "4", "5"]:
                if target_y == 0:
                    new_x, new_y = target_x, GRID_ROWS - 2
                elif target_y == GRID_ROWS - 1:
                    new_x, new_y = target_x, 1
                elif target_x == 0:
                    new_x, new_y = GRID_COLS - 2, target_y
                elif target_x == GRID_COLS - 1:
                    new_x, new_y = 1, target_y
                else:
                    new_x, new_y = dest_x, dest_y
            else:
                new_x, new_y = dest_x, dest_y

            self.current_map = target_map
            self.player_x = new_x
            self.player_y = new_y
            self.load_map_state()
            return

        if self.is_obstacle(target_tile):
            return

        self.player_x = target_x
        self.player_y = target_y
        self.check_enemy_collisions()

        if target_tile == "$":
            self.score += 10
            self.active_grid[target_y][target_x] = "."
        elif target_tile in ["W", "G", "P", "M"]:
            weapon_map = {"W": "sword", "G": "gun", "P": "spear", "M": "wand"}
            self.weapon = weapon_map[target_tile]
            self.active_grid[target_y][target_x] = "."
        elif target_tile == "C":
            self.score += 50
            self.active_grid[target_y][target_x] = "."

    def move_enemies(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_enemy_move_time < self.enemy_move_cooldown:
            return

        for enemy in self.enemies:
            ex, ey = enemy["x"], enemy["y"]
            dx, dy = 0, 0
            if ex < self.player_x: dx = 1
            elif ex > self.player_x: dx = -1
            elif ey < self.player_y: dy = 1
            elif ey > self.player_y: dy = -1

            if dx != 0 or dy != 0:
                enemy["dx"], enemy["dy"] = dx, dy
                tx, ty = ex + dx, ey + dy
                if 0 <= tx < GRID_COLS and 0 <= ty < GRID_ROWS:
                    tile = self.active_grid[ty][tx]
                    if not self.is_obstacle(tile) and tile not in MAP_LINKS.get(self.current_map, {}):
                        if not any(e["x"] == tx and e["y"] == ty for e in self.enemies):
                            enemy["x"], enemy["y"] = tx, ty

        self.check_enemy_collisions()
        self.last_enemy_move_time = current_time

    def update_projectiles(self):
        removes = []
        for p in self.projectiles:
            p.x += p.dx
            p.y += p.dy

            if not (0 <= p.x < GRID_COLS and 0 <= p.y < GRID_ROWS) or self.is_obstacle(self.active_grid[p.y][p.x]):
                removes.append(p)
                continue

            if p.friendly:
                for enemy in self.enemies:
                    if enemy["x"] == p.x and enemy["y"] == p.y:
                        enemy["health"] -= 1
                        if enemy["health"] <= 0:
                            self.enemies.remove(enemy)
                            self.score += 15
                        removes.append(p)
                        break

        for r in removes:
            if r in self.projectiles:
                self.projectiles.remove(r)

    def check_enemy_collisions(self):
        current_time = pygame.time.get_ticks()
        for enemy in self.enemies:
            if enemy["x"] == self.player_x and enemy["y"] == self.player_y:
                if current_time - self.last_damage_time > self.damage_cooldown:
                    self.hearts -= 1
                    self.last_damage_time = current_time
                    if self.hearts <= 0:
                        pygame.quit()
                        sys.exit()

    def use_weapon(self):
        if not self.weapon: return
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time < self.attack_cooldown: return

        w_data = WEAPONS[self.weapon]
        if w_data["type"] == "melee":
            for r in range(1, w_data["range"] + 1):
                tx = self.player_x + (self.player_dx * r)
                ty = self.player_y + (self.player_dy * r)
                if not (0 <= tx < GRID_COLS and 0 <= ty < GRID_ROWS) or self.is_obstacle(self.active_grid[ty][tx]):
                    break
                for enemy in self.enemies:
                    if enemy["x"] == tx and enemy["y"] == ty:
                        enemy["health"] -= 1
                        if enemy["health"] <= 0:
                            self.enemies.remove(enemy)
                            self.score += 15
                        break
        elif w_data["type"] == "ranged":
            self.projectiles.append(Projectile(self.player_x, self.player_y, self.player_dx, self.player_dy, friendly=True))
        self.last_attack_time = current_time

    def handle_continuous_movement(self):
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: self.use_weapon()
        if current_time - self.last_move_time < self.move_cooldown: return

        dx, dy = 0, 0
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]: dy = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]: dx = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx = 1

        if dx != 0 or dy != 0:
            self.move_player(dx, dy)
            self.last_move_time = current_time

    def draw_heart(self, x, y):
        pygame.draw.rect(self.screen, COLOR_HEART, (x+4, y, 6, 4))
        pygame.draw.rect(self.screen, COLOR_HEART, (x+14, y, 6, 4))
        pygame.draw.rect(self.screen, COLOR_HEART, (x, y+4, 24, 6))
        pygame.draw.rect(self.screen, COLOR_HEART, (x+2, y+10, 20, 4))
        pygame.draw.rect(self.screen, COLOR_HEART, (x+6, y+14, 12, 4))
        pygame.draw.rect(self.screen, COLOR_HEART, (x+10, y+18, 4, 4))
        pygame.draw.rect(self.screen, COLOR_WHITE, (x+4, y+4, 4, 4))

    def draw_player(self, x, y):
        px = x * CELL_SIZE
        py = y * CELL_SIZE + UI_HEIGHT
        pygame.draw.rect(self.screen, COLOR_GREEN, (px+4, py+8, 24, 20))
        pygame.draw.rect(self.screen, (240, 180, 120), (px+8, py+2, 16, 12))
        pygame.draw.rect(self.screen, COLOR_BROWN, (px+4, py+2, 24, 4))
        pygame.draw.rect(self.screen, COLOR_BLACK, (px+10, py+6, 4, 4))
        pygame.draw.rect(self.screen, COLOR_BLACK, (px+18, py+6, 4, 4))

    def draw_enemy(self, x, y):
        ex = x * CELL_SIZE
        ey = y * CELL_SIZE + UI_HEIGHT
        pygame.draw.rect(self.screen, (200, 50, 40), (ex+4, ey+4, 24, 24))
        pygame.draw.rect(self.screen, COLOR_BLACK, (ex+6, ey+10, 6, 6))
        pygame.draw.rect(self.screen, COLOR_BLACK, (ex+20, ey+10, 6, 6))
        pygame.draw.rect(self.screen, COLOR_WHITE, (ex+10, ey+20, 12, 4))

    def draw_environment_tile(self, x, y, tile):
        px = x * CELL_SIZE
        py = y * CELL_SIZE + UI_HEIGHT

        bg_col = COLOR_DUNGEON_FLOOR if self.is_dungeon() else COLOR_SAND

        if tile == "#":
            pygame.draw.rect(self.screen, COLOR_DARK_GREEN, (px, py, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, COLOR_GREEN, (px+4, py+4, 24, 24))
            return
        elif tile == "%":
            pygame.draw.rect(self.screen, COLOR_STONE_DARK, (px, py, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, COLOR_STONE_LIGHT, (px+2, py+2, 28, 28))
            return
        elif tile == "B":
            pygame.draw.rect(self.screen, COLOR_BUNKER_WALL, (px, py, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, COLOR_WHITE, (px+2, py+2, 28, 2))
            return
        elif tile == "~":
            pygame.draw.rect(self.screen, COLOR_BLUE, (px, py, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self.screen, COLOR_LIGHT_BLUE, (px+4, py+8, 12, 4))
            return

        pygame.draw.rect(self.screen, bg_col, (px, py, CELL_SIZE, CELL_SIZE))

        if tile == "$":
            pygame.draw.rect(self.screen, COLOR_GOLD, (px+10, py+6, 12, 20))
        elif tile == "W":
            pygame.draw.rect(self.screen, COLOR_WHITE, (px+12, py+4, 8, 14))
        elif tile == "G":
            pygame.draw.rect(self.screen, COLOR_WHITE, (px+6, py+12, 20, 8))
        elif tile == "P":
            pygame.draw.rect(self.screen, COLOR_WHITE, (px+10, py+2, 12, 8))
        elif tile == "M":
            pygame.draw.rect(self.screen, COLOR_LIGHT_BLUE, (px+10, py+2, 12, 10))
        elif tile == "C":
            pygame.draw.rect(self.screen, COLOR_BROWN, (px+4, py+6, 24, 20))
            pygame.draw.rect(self.screen, COLOR_GOLD, (px+12, py+14, 8, 6))
        elif tile == ">":
            pygame.draw.rect(self.screen, COLOR_BLACK, (px+4, py+4, 24, 24))
            pygame.draw.rect(self.screen, COLOR_WHITE, (px+8, py+8, 16, 16))

    def render(self):
        self.screen.fill(COLOR_BLACK)

        info_text = f"MAP: {self.current_map.upper()} | SCORE: {self.score} | WEAPON: {self.weapon.upper()}"
        ui_surface = self.font.render(info_text, True, COLOR_WHITE)
        self.screen.blit(ui_surface, (20, 22))

        for i in range(self.hearts):
            self.draw_heart(SCREEN_WIDTH - 36 - (i * 32), 20)

        for y, row in enumerate(self.active_grid):
            for x, tile in enumerate(row):
                self.draw_environment_tile(x, y, tile)

        for p in self.projectiles:
            px = p.x * CELL_SIZE + 12
            py = p.y * CELL_SIZE + UI_HEIGHT + 12
            pygame.draw.rect(self.screen, COLOR_PROJECTILE, (px, py, 8, 8))

        for enemy in self.enemies:
            self.draw_enemy(enemy["x"], enemy["y"])

        self.draw_player(self.player_x, self.player_y)
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            self.handle_continuous_movement()
            self.move_enemies()
            self.update_projectiles()
            self.render()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
