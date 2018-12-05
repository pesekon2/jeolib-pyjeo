"""Test suite for module pyjeo.pixops."""

import pyjeo as pj
import unittest


testFile = 'tests/data/modis_ndvi_2010.tif'
tiles = ['tests/data/red1.tif', 'tests/data/red2.tif']
vector = 'tests/data/nuts_italy.sqlite'


class BadPixOps(unittest.TestCase):
    """Test functions and methods from pixops modules."""

    def test_isEqual(self):
        """Test isEqual() function."""
        jim1 = pj.Jim(tiles[0])
        jim2 = pj.Jim(tiles[0])
        jim3 = pj.Jim(tiles[1])

        assert jim1.pixops.isEqual(jim2), \
            'Error in pixops.isEqual() method (for two Jims)'
        assert not jim1.pixops.isEqual(jim3), \
            'Error in pixops.isEqual() method (non-equality)'
        assert not jim1.pixops.isEqual(1), \
            'Error in pixops.isEqual() method (for not Jim object)'

        assert pj.pixops.isEqual(jim1, jim2), \
            'Error in pixops.isEqual() function (for two Jims)'
        assert not pj.pixops.isEqual(jim1, jim3), \
            'Error in pixops.isEqual() function (non-equality)'
        assert not pj.pixops.isEqual(jim1, 1), \
            'Error in pixops.isEqual() function (for not Jim object)'

    def test_NDVI(self):
        """Test computing NDVI in different ways."""
        jim = pj.Jim(testFile)

        jim_red = pj.geometry.cropBand(jim, 0)
        jim_nir = pj.geometry.cropBand(jim, 1)

        ndvi = pj.pixops.NDVI(jim, 0, 1)
        jim.pixops.NDVI(0, 1)

        assert jim.pixops.isEqual(ndvi), 'Error in computing NDVI'

        ndvi = pj.pixops.NDVISeparateBands(jim_red, jim_nir)
        jim_red.pixops.NDVISeparateBands(jim_nir)

        assert jim_red.pixops.isEqual(ndvi), 'Error in computing ' \
                                             'NDVISeparateBands'

        assert jim_red.pixops.isEqual(jim), 'Error in computing NDVI or ' \
                                            'NDVISeparateBands'

        ndvi = pj.pixops.NDVISeparateBands(jim_red, jim_nir.convertToFloat32())

        assert not jim.pixops.isEqual(ndvi), 'Error in computing NDVI'

    def test_supremum(self):
        """Test picking up supremum from different computed NDVIs."""
        for tile in tiles:
            jim4 = pj.Jim(tile)
            jim8 = pj.Jim(tile[:-8] + 'nir' + tile[-5] + '.tif')

            if 'max_ndvi' in locals():
                b = pj.pixops.NDVISeparateBands(jim4, jim8)

                max_ndvi[b > max_ndvi] = b
                max_ndvi_func = pj.pixops.supremum(max_ndvi, b)
                assert max_ndvi.pixops.isEqual(max_ndvi_func), \
                    'Error in computing supremum'
                max_ndvi2.pixops.supremum(b)
                assert max_ndvi.pixops.isEqual(max_ndvi2), \
                    'Error in computing supremum'
            else:
                max_ndvi = pj.pixops.NDVISeparateBands(jim4, jim8)
                max_ndvi2 = pj.Jim(max_ndvi)

    def test_setFunctions(self):
        """Test setData and setThreshold functions and methods."""
        jim = pj.Jim(testFile)

        stats = jim.stats.getStats()
        min = stats['min']
        max = stats['max']

        thresholded = pj.pixops.setThreshold(jim, min=min+1, max=max-1,
                                             nodata=(max+min)/2)

        thresholded_stats = thresholded.stats.getStats()
        nodata = thresholded.properties.getNoDataVals()

        assert thresholded_stats != stats, \
            'Error in pixops.setThreshold() or stats.getStats()'
        assert thresholded_stats['min'] >= min + 1, \
            'Error in pixops.setThreshold() or stats.getStats()'
        assert thresholded_stats['max'] <= max - 1, \
            'Error in pixops.setThreshold() or stats.getStats()'
        assert thresholded.properties.getNoDataVals() == [((max+min)/2)], \
            'Error in pixops.setThreshold() or properties.getNoDataVals()'

        jim.pixops.setThreshold(min=min+1, max=max-1, nodata=(max+min)/2)

        stats = jim.stats.getStats()

        assert stats == thresholded_stats, \
            'Error in pixops.setThreshold() or stats.getStats()'
        assert jim.properties.getNoDataVals() == nodata, \
            'Error in pixops.setThreshold() or properties.getNoDataVals()'

        jim.pixops.setData(5, bands=[0, 1])

        stats = jim.stats.getStats()

        assert all(v==5 for v in [stats['min'], stats['max'], stats['mean']]),\
            'Error in pixops.setData() or stats.getStats()'

        jim.pixops.setData(10, dx=jim.properties.getDeltaX()+0.1, bands=[0, 1])

        stats = jim.stats.getStats()

        assert all(v==10 for v in [stats['min'], stats['max'], stats['mean']]),\
            'Error in pixops.setData() or stats.getStats()'

    def test_convert(self):
        """Test data type conversions."""
        jim = pj.Jim(tiles[0])

        jim.pixops.convert('Byte')
        assert jim.properties.getDataType() == 1, 'Error in pixops.convert()'

        jim.pixops.convert('UInt16')
        assert jim.properties.getDataType() == 2, 'Error in pixops.convert()'

        jim.pixops.convert('Int16')
        assert jim.properties.getDataType() == 3, 'Error in pixops.convert()'

        jim.pixops.convert('UInt32')
        assert jim.properties.getDataType() == 5, 'Error in pixops.convert()'
        # TODO: Change the assertion to 4 after fixing the bug in jiplib

        jim.pixops.convert('Int32')
        assert jim.properties.getDataType() == 5, 'Error in pixops.convert()'

        jim.pixops.convert('Float32')
        assert jim.properties.getDataType() == 6, 'Error in pixops.convert()'

        jim.pixops.convert('Float64')
        assert jim.properties.getDataType() == 7, 'Error in pixops.convert()'

        # jim.pixops.convert('CInt16')
        # assert jim.properties.getDataType() == 8, 'Error in pixops.convert()'
        #
        # jim.pixops.convert('CInt32')
        # assert jim.properties.getDataType() == 9, 'Error in pixops.convert()'
        #
        # jim.pixops.convert('CFloat32')
        # assert jim.properties.getDataType() == 10, 'Error in pixops.convert()'
        #
        # jim.pixops.convert('CFloat64')
        # assert jim.properties.getDataType() == 11, 'Error in pixops.convert()'
        # # TODO: Uncomment when bug fixed in jiplib

        jim.pixops.convert('Byte', a_srs='EPSG:5514')
        assert jim.properties.getDataType() == 1, 'Error in pixops.convert()'

        jim.pixops.convert('UInt16', a_srs='EPSG:5514')
        assert jim.properties.getDataType() == 2, 'Error in pixops.convert()'

        jim.pixops.convert('Float32', a_srs='EPSG:5514')
        assert jim.properties.getDataType() == 6, 'Error in pixops.convert()'

        jim.pixops.convert('Float64', a_srs='EPSG:5514')
        assert jim.properties.getDataType() == 7, 'Error in pixops.convert()'

        try:
            jim.pixops.convert('string')
            failed = True
        except TypeError:
            failed = False

        assert not failed, \
            'Error in checks for non-supported data types in pixops.convert()'

        a = pj.pixops.convert(jim, 'Byte')
        assert a.properties.getDataType() == 1, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'UInt16')
        assert a.properties.getDataType() == 2, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'Int16')
        assert a.properties.getDataType() == 3, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'UInt32')
        assert a.properties.getDataType() == 5, 'Error in pixops.convert()'
        # TODO: Change the assertion to 4 after fixing the bug in jiplib

        a = pj.pixops.convert(a, 'Int32')
        assert a.properties.getDataType() == 5, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'Float32')
        assert a.properties.getDataType() == 6, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'Float64')
        assert a.properties.getDataType() == 7, 'Error in pixops.convert()'

        # a = pj.pixops.convert(jim, 'CInt16')
        # assert a.properties.getDataType() == 8, 'Error in pixops.convert()'
        #
        # a = pj.pixops.convert(jim, 'CInt32')
        # assert a.properties.getDataType() == 9, 'Error in pixops.convert()'
        #
        # a = pj.pixops.convert(jim, 'CFloat32')
        # assert a.properties.getDataType() == 10, 'Error in pixops.convert()'
        #
        # a = pj.pixops.convert(jim, 'CFloat64')
        # assert a.properties.getDataType() == 11, 'Error in pixops.convert()'
        # # TODO: Uncomment when bug fixed in jiplib

        a = pj.pixops.convert(a, 'Byte', a_srs='EPSG:5514')
        assert a.properties.getDataType() == 1, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'UInt16', a_srs='EPSG:5514')
        assert a.properties.getDataType() == 2, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'Float32', a_srs='EPSG:5514')
        assert a.properties.getDataType() == 6, 'Error in pixops.convert()'

        a = pj.pixops.convert(a, 'Float64', a_srs='EPSG:5514')
        assert a.properties.getDataType() == 7, 'Error in pixops.convert()'

        try:
            pj.pixops.convert(a, 'string')
            failed = True
        except TypeError:
            failed = False

        assert not failed, \
            'Error in checks for non-supported data types in pixops.convert()'


class BadPixOpsLists(unittest.TestCase):
    """Test JimList functions and methods from pixops modules."""

    def test_composite(self):
        """Test composite() function."""
        jim1 = pj.Jim(tiles[0])
        jim2 = pj.Jim(tiles[1])
        jim3 = pj.Jim(tiles[0][:-8] + 'nir' + tiles[0][-5] + '.tif')
        jiml1 = pj.JimList([jim1, jim2])
        jiml2 = pj.JimList([jim1, jim3])

        comp1 = pj.pixops.composite(jiml1)
        comp2 = jiml1.pixops.composite()
        comp3 = jiml2.pixops.composite()
        comp4 = jiml1.pixops.composite(otype='Byte')

        assert comp1.pixops.isEqual(comp2)
        assert not comp1.pixops.isEqual(comp3)
        assert not comp2.pixops.isEqual(comp4)


def load_tests(loader=None, tests=None, pattern=None):
    """Load tests."""
    if not loader:
        loader = unittest.TestLoader()
    suite_list = [loader.loadTestsFromTestCase(BadPixOps),
                  loader.loadTestsFromTestCase(BadPixOpsLists)]
    return unittest.TestSuite(suite_list)
