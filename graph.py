class EntityNode:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.neighbors = []

    def add_neighbor(self, neighbor, relationship_strength):
        self.neighbors.append((neighbor, relationship_strength))

class WorldGraph:
    def __init__(self):
        self.entities = {}

    def add_entity(self, entity):
        self.entities[entity.name] = entity

    def simulate_step(self):
        for entity in self.entities.values():
            for neighbor, strength in entity.neighbors:
                # Update attributes based on relationship strength
                # Apply events and interactions

# Create nodes and edges
kingdom_a = EntityNode("Kingdom A", attributes={...})
kingdom_b = EntityNode("Kingdom B", attributes={...})
kingdom_c = EntityNode("Kingdom C", attributes={...})

kingdom_a.add_neighbor(kingdom_b, relationship_strength=0.7)
kingdom_a.add_neighbor(kingdom_c, relationship_strength=0.4)

# Create the world graph and add entities
world = WorldGraph()
world.add_entity(kingdom_a)
world.add_entity(kingdom_b)
world.add_entity(kingdom_c)

# Simulation loop
for _ in range(num_steps):
    world.simulate_step()

# Visualization, analysis, and further interactions
