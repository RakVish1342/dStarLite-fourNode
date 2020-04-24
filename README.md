5 Node D\* Lite Algorithm
===

Implementation of the incremental path planning algorithm D\* Lite has been done for the graph presented at: ``` https://www.youtube.com/watch?v=_4u9W1xOuts&t=3372s```

Examples
---

** 1. No Obstacles **

```
('RobotLoc: ', 'A')
('gValues: ', {'A': inf, 'C': inf, 'B': inf, 'D': inf, 'G': inf})
('rhs: ', {'A': inf, 'C': inf, 'B': inf, 'D': inf, 'G': 0})
('km: ', 0)
('queue: ', [('G', (3, 0))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'B')
Enter obstacle node:X
('gValues: ', {'A': 3, 'C': 1, 'B': 2, 'D': inf, 'G': 0})
('rhs: ', {'A': 3, 'C': 1, 'B': 2, 'D': 2, 'G': 0})
('km: ', 0)
('queue: ', [('D', (4, 2))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'C')
Enter obstacle node:X
('gValues: ', {'A': 3, 'C': 1, 'B': 2, 'D': inf, 'G': 0})
('rhs: ', {'A': 3, 'C': 1, 'B': 2, 'D': 2, 'G': 0})
('km: ', 0)
('queue: ', [('D', (4, 2))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'G')
Enter obstacle node:X
('gValues: ', {'A': 3, 'C': 1, 'B': 2, 'D': inf, 'G': 0})
('rhs: ', {'A': 3, 'C': 1, 'B': 2, 'D': 2, 'G': 0})
('km: ', 0)
('queue: ', [('D', (4, 2))])
('Goal: ', 'G')
-----
('Path Followed by Robot: ', ['A', 'B', 'C', 'G'])
Press any key to continue . . .
```

** 2. Obstacle That Follows Robot **

```
('RobotLoc: ', 'A')
('gValues: ', {'A': inf, 'C': inf, 'B': inf, 'D': inf, 'G': inf})
('rhs: ', {'A': inf, 'C': inf, 'B': inf, 'D': inf, 'G': 0})
('km: ', 0)
('queue: ', [('G', (3, 0))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'B')
Enter obstacle node:C
('gValues: ', {'A': inf, 'C': inf, 'B': 11, 'D': 10, 'G': 0})
('rhs: ', {'A': 12, 'C': inf, 'B': 11, 'D': 10, 'G': 0})
('km: ', 1)
('queue: ', [('A', (14, 12))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'D')
Enter obstacle node:B
('gValues: ', {'A': inf, 'C': 1, 'B': 11, 'D': 2, 'G': 0})
('rhs: ', {'A': inf, 'C': 1, 'B': inf, 'D': 2, 'G': 0})
('km: ', 2)
('queue: ', [('B', (14, 11))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'C')
Enter obstacle node:D
('gValues: ', {'A': inf, 'C': 1, 'B': 11, 'D': 2, 'G': 0})
('rhs: ', {'A': inf, 'C': 1, 'B': 2, 'D': inf, 'G': 0})
('km: ', 3)
('queue: ', [('B', (6, 2)), ('D', (6, 2))])
('Goal: ', 'G')
-----
('RobotLoc: ', 'G')
Enter obstacle node:C
('gValues: ', {'A': inf, 'C': 1, 'B': 11, 'D': 2, 'G': 0})
('rhs: ', {'A': inf, 'C': inf, 'B': 3, 'D': 10, 'G': 0})
('km: ', 4)
('queue: ', [('C', (6, 1)), ('D', (7, 2)), ('B', (9, 3))])
('Goal: ', 'G')
-----
('Path Followed by Robot: ', ['A', 'B', 'D', 'C', 'G'])
Press any key to continue . . .
```
