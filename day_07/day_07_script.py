from collections import defaultdict

class RuleParser():
    
    def __init__(self):
        self.containment_tree = defaultdict(lambda: defaultdict(list))
    
        
    def parse_row(self, row):
        if row.strip()=="": return
        row = row.replace(' bags', '').replace(' bag', '').replace('.','').strip()
        outer, contents = row.split(' contain ')
        content_rules = contents.split(', ')
        for contained_rule in content_rules:
            words = contained_rule.split(' ')
            n = 0 if words[0] == "no" else int(words[0])
            colour = " ".join(words[1:])
            colour = colour if n > 0 else "no other"
            self.containment_tree[outer][colour]=n
    
    
    def find_in_subtree(self, target_color):
        outers = set()
        def search_subtree(for_colour):
            for outer in self.containment_tree:
                if for_colour in self.containment_tree[outer]:
                    outers.add(outer)
                    search_subtree(outer)
        search_subtree(target_color)
        return len(outers)
    
    
    def _n_in_subtree(self, outer_bag):
        total_children = 1
        for inner_bag in parser.containment_tree[outer_bag]:
            n_this_colour = parser.containment_tree[outer_bag][inner_bag]
            n_children = self._n_in_subtree(inner_bag)
            total_children += n_this_colour * n_children
        return total_children
    

    def n_in_children(self, outer_bag):
        return self._n_in_subtree(outer_bag)-1
  

parser = RuleParser()

with open ("input.txt", "r") as input:
    for row in input:
        parser.parse_row(row)

goal_colour = 'shiny gold'
part_1 = parser.find_in_subtree(goal_colour)
print(f"Part 1 solution: {part_1} colours can ultimately contain a {goal_colour} bag")

part_2 = parser.n_in_children(goal_colour)
print(f"Part 2 solution: a {goal_colour} bag has to contain {part_2} other bags")
