from models.stats import DataCapture

datacapture = DataCapture()
datacapture.add(3)
datacapture.add(9)
datacapture.add(3)
datacapture.add(4)
datacapture.add(6)
stats = datacapture.build_stats()
print(datacapture.__repr__)
print(stats.less(4))
print(stats.greater(4))
print(stats.between(3, 6))