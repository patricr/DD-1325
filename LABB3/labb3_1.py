# LABB 3 BINÄRA SÖKTRÄD
#Christopher Dahlen, Patrinc Ridell

# för att kolla i hela sökträdet vill vi söka igenom alla sökvägar och noder.
# vilket görs med rekursion
# preorder används till att stoppa in saker i trädet.
# postorder används när man villstäda i trädet. skräpträd.
#







def finns(p,value): # kollar bara en sökväg i trädet
    letar = True
    while letar:
        if p == None: # kollar om rooten är none
            return False
        if value == p.value:
            return True
        if value < p.value:
            p = p.left
        if value > p.value:
            p = p.right
