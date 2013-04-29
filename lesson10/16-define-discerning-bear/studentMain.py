from bear import Bear, GrizzlyBear, DiscerningBear
from human import Human

dave = Human("Dave")
bob = Human("Bob")
dave.climb_tree()
bob.climb_tree()

fussy = DiscerningBear("Fussy")
fussy.chase(bob)
fussy.chase(dave)
#>>> Bleech! I'm not eating Dave!
