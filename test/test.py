import pyBigWig

class TestRemote():
    fname = "https://raw.githubusercontent.com/dpryan79/pyBigWig/master/test/test.bw"

    def doOpen(self):
        print(self.fname)
        bw = pyBigWig.open(self.fname)
        assert(bw is not None)
        return bw

    def doChroms(self, bw):
        assert(bw.chroms() == {'1': 195471971L, '10': 130694993L})
        assert(bw.chroms("1") == 195471971L)
        assert(bw.chroms("c") is None)

    def doHeader(self, bw):
        assert(bw.header() == {'maxVal': 2L, 'sumData': 272L, 'minVal': 0L, 'version': 4L, 'sumSquared': 500L, 'nLevels': 1L, 'nBasesCovered': 154L})

    def doStats(self, bw):
        assert(bw.stats("1", 0, 3) == [0.2000000054637591])
        assert(bw.stats("1", 0, 3, type="max") == [0.30000001192092896])
        assert(bw.stats("1",99,200, type="max", nBins=2) == [1.399999976158142, 1.5])
        assert(bw.stats("1") == [1.3351851569281683])

    def doValues(self, bw):
        assert(bw.values("1", 0, 3) == [0.10000000149011612, 0.20000000298023224, 0.30000001192092896])
        #assert(bw.values("1", 0, 4) == [0.10000000149011612, 0.20000000298023224, 0.30000001192092896, 'nan'])

    def doIntervals(self, bw):
        assert(bw.intervals("1", 0, 3) == ((0, 1, 0.10000000149011612), (1, 2, 0.20000000298023224), (2, 3, 0.30000001192092896)))
        assert(bw.intervals("1") == ((0, 1, 0.10000000149011612), (1, 2, 0.20000000298023224), (2, 3, 0.30000001192092896), (100, 150, 1.399999976158142), (150, 151, 1.5)))

    def testAll(self):
        bw = self.doOpen()
        self.doChroms(bw)
        self.doHeader(bw)
        self.doStats(bw)
        self.doValues(bw)
        self.doIntervals(bw)
        bw.close()

class TestLocal():
    def testFoo(self):
        blah = TestRemote()
        blah.fname = "test/test.bw"
        blah.testAll()
