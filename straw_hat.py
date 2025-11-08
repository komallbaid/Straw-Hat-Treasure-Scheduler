from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

def comp(C1, C2):
    # here crewmate C1 received the latest treasure and is being inserted back into the heap
    # current time = C1.last_load_time = arrival time of latest treasure
    # C1's load is updated at current time but C2's load is not so...
    p1 = C1.load
    t = C2.load - (C1.last_load_time - C2.last_load_time)
    p2 = t if t > 0 else 0  # load of crewmate C2 at current time

    if p1 <= p2: return True
    return False

class StrawHatTreasury:

    def __init__(self, m):
        self.all_crewmates = [CrewMate(i) for i in range(1, m + 1)]
        self.crewmate_heap = Heap(comp, self.all_crewmates)

    def add_treasure(self, treasure):
        crewmate = self.crewmate_heap.extract()
        crewmate.add(treasure)
        self.crewmate_heap.insert(crewmate)

    def copy(self, T):
        return Treasure(T.id, T.size, T.arrival_time)

    def get_completion_time(self):
        done = []

        # 1) already-finished treasures (completed during arrivals)
        for cm in self.crewmate_heap.heap:
            done.extend(cm.processed_treasures)

        # 2) finish remaining treasures on each crewmate in correct priority order
        for cm in self.crewmate_heap.heap:
            t = cm.last_load_time

            # make a scratch heap with the same comparator and current items
            tmp = Heap(cm.pq.comparator, cm.pq.heap[:])

            while tmp.top() is not None:
                tr = tmp.extract()

                # since no new arrivals now, we finish the selected treasure fully
                t += tr.remaining_size()

                # add a copy with completion_time set (avoid mutating originals)
                T = Treasure(tr.id, tr.size, tr.arrival_time)
                T.completion_time = t
                T.size = 0
                done.append(T)

        # 3) sort by id as required
        return sorted(done, key=lambda x: x.id)

