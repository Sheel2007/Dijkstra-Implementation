import pygame

pygame.init()
WINDOW_SIZE = 600
WINDOW = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
WINDOW_CENTER = [WINDOW_SIZE/2, WINDOW_SIZE/2]
clock = pygame.time.Clock()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def least_cost(node_list):
   best_node = node_list[0]
   for node in node_list:
       if node.distance < best_node.distance:
           best_node = node
   return best_node


class Grid:
   def __init__(self):
       self.internal_map = [
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 2, 1, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
           [1, 0, 1, 0, 0, 0, 0, 3, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       ]

       self.found_exit = None
       self.found_path = False

       self.final_path = []
       self.active_nodes = [Node(0, self.find_start())]
       self.processed_nodes = []
       self.iteration = 0  # represents the cost of the tiles too
       self.final_iteration = 0

   def get_value(self, x, y, temp_map = None):
       if temp_map:
           return temp_map[y][x]
       return self.internal_map[y][x]

   def check_wall(self, x, y):
       if self.get_value(x, y) == 1:
           return True
       return False

   def find_start(self):
       for y in range(len(self.internal_map)):
           for x in range(len(self.internal_map)):
               if self.get_value(x, y) == 2:
                   return [x, y]
   def render(self):
       temp_map = [self.internal_map[i][:] for i in range(len(self.internal_map))]

       if self.found_exit:
           for node in self.final_path:
               temp_map[node.y][node.x] = 4
       else:
           for node in self.processed_nodes:
               temp_map[node.y][node.x] = 5

       for y in range(len(temp_map)):
           for x in range(len(temp_map)):
               mapValue = self.get_value(x, y, temp_map)
               if mapValue == 0:
                   continue
               elif mapValue == 1:
                   pygame.draw.rect(WINDOW, (0, 0, 0), (x * 60, y * 60, 60, 60))
               elif mapValue == 2:
                   pygame.draw.rect(WINDOW, (0, 200, 0), (x * 60, y * 60, 60, 60))
               elif mapValue == 3:
                   pygame.draw.rect(WINDOW, (200, 0, 0), (x * 60, y * 60, 60, 60))
               elif mapValue == 4:
                   pygame.draw.rect(WINDOW, (200, 0, 200), (x * 60, y * 60, 60, 60))
               elif mapValue == 5:
                   pygame.draw.rect(WINDOW, (200, 200, 200), (x * 60, y * 60, 60, 60))

   def find_exit(self):
       for y in range(len(self.internal_map)):
           for x in range(len(self.internal_map)):
               if self.get_value(x, y) == 3:
                   return [x, y]


   def find_duplicate_node(self, x, y, node_list):
       for node in node_list:
           if node.x == x and node.y == y:
               return True
       return False



   def step(self):
       if len(self.active_nodes) == 0:
           self.found_exit = False    #the path is imposible
           return
       elif self.found_exit == None:
           new_nodes = []
           self.iteration += 1
           print("Cycle", self.iteration, "  Active nodes:", len(self.active_nodes))
           for node in self.active_nodes:
               for dx, dy in directions:
                   v = self.get_value(node.x + dx, node.y + dy)
                   if v == 1:
                       continue
                   elif v == 0:
                       if not self.find_duplicate_node(node.x + dx, node.y + dy, self.processed_nodes):
                           if not self.find_duplicate_node(node.x + dx, node.y + dy, new_nodes):
                               new_nodes.append(Node(self.iteration, (node.x + dx, node.y + dy)))
                   elif v == 3:
                       new_nodes.append(Node(self.iteration, (node.x + dx, node.y + dy)))
                       self.found_exit = True
                       self.processed_nodes += self.active_nodes[:]
                       self.active_nodes = new_nodes[:]
                       self.final_path = [Node(self.iteration, self.find_exit())]
                       return

           self.processed_nodes += self.active_nodes[:]
           self.active_nodes = new_nodes[:]

       elif self.found_exit and not self.found_path:
           self.final_iteration += 1
           print("Steps Left:", self.iteration - self.final_iteration)
           if not self.found_path:
               adjacent_nodes = []
               for node in self.processed_nodes:
                   if self.final_path[-1].adjacent_to(node):
                       adjacent_nodes.append(node)
               self.final_path.append(least_cost(adjacent_nodes))

               if len(self.final_path) == self.iteration:
                   self.found_path = True
                   print("Complete!")

class Node:
   def __init__(self, distance, position):
       self.x = position[0]    #position is a list
       self.y = position[1]
       self.distance = distance

   def adjacent_to(self, node):
       for dx, dy in directions:
           if self.x + dx == node.x and self.y + dy == node.y:
               return True
       return False

#0 = nothing

#1 = wall






# === Misc ===
def clear_graphics():
   WINDOW.fill((255, 255, 255))


def update_window():
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()               # this is neccesary for some events to happen ;(
   pygame.display.flip()
   clock.tick(1)


w = Grid()



while True:
   clear_graphics()

   w.step()

   # render
   # render
   w.render()

   update_window()
