import pstats, sys
file = sys.argv[1]
p = pstats.Stats(file)
p.strip_dirs().sort_stats('cum').print_stats(100)

