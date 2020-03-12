"""Module for accessing Jim attributes and geospatial informations."""

import pyjeo as _pj

# def imageInfo(jim_object):
#     """Return image information (number of lines, columns, etc.)

#     """
#     return _pj.Jim(jim_object._jipjim.imageInfo())


class _Properties(_pj.modules.JimModuleBase):
    """Define all properties methods."""

    def clearNoData(self):
        """Clear the list of no data values for this raster dataset."""
        self._jim_object._jipjim.clearNoData()

    def copyGeoTransform(self, sec_jim_object):
        """Copy geotransform information from another georeferenced image."""
        self._jim_object._jipjim.copyGeoTransform(sec_jim_object._jipjim)

    def covers(self, *args):
        """Check if a geolocation is covered by this dataset.

        You can check the coverage for a :ref:`point of interest
        <covers1>` or :ref:`region of interest <covers2>`.

        .. _covers1:

        :Using a point coordinates:

        * ``x`` (float): x coordinate in spatial reference system of \
                         the rasterdataset
        * ``y`` (float): y coordinate in spatial reference system of \
                         the raster dataset

        .. _covers2:

        :Using a region of interest:

        * ``ulx`` (float): upper left x coordinate in spatial reference \
                           system of the raster dataset
        * ``uly`` (float): upper left y coordinate in spatial reference \
                           system of the raster dataset
        * ``lrx`` (float): lower right x coordinate in spatial reference \
                           system of the raster dataset
        * ``lry`` (float): lower right x coordinate in spatial reference \
                           system of the raster dataset
        * ``all`` (bool): set to True if the entire bounding box must be \
                          covered by the raster dataset

        Returns:
        True if the raster dataset covers the point or region of interest.
        """
        return self._jim_object._jipjim.covers(*args)

    def getBBox(self):
        """Get the bounding box (georeferenced) coordinates of this dataset.

        :return: A list with upper left x, upper left y, lower right x, and
            lower right y
        """
        return self._jim_object._jipjim.getBoundingBox()

    def getCenterPos(self):
        """
        Get the center position of this dataset in georeferenced coordinates.

        :return: A list with the center position of this dataset in
            georeferenced coordinates.
        """
        return self._jim_object._jipjim.getCenterPos()

    def getDataType(self):
        """Get the internal datatype for this raster dataset.

        :return: The datatype id of this Jim object
        """
        otype = self._jim_object._jipjim.getDataType()
        if otype == 1:
            return 'Byte'
        elif otype == 2:
            return 'UInt16'
        elif otype == 3:
            return 'Int16'
        elif otype == 4:
            return 'UInt32'
        elif otype == 5:
            return 'Int32'
        elif otype == 6:
            return 'Float32'
        elif otype == 7:
            return 'Float64'
        elif otype == 8:
            return 'CInt16'
        elif otype == 9:
            return 'CInt32'
        elif otype == 10:
            return 'CFloat32'
        elif otype == 11:
            return 'CFloat64'
        elif otype == 12:
            return 'TypeCount'
        elif otype == 14:
            return 'Int64'
        elif otype == 15:
            return 'UInt64'
        elif otype == 16:
            return 'JDT_Word'
        else:
            raise TypeError("Unknown data format".format(otype))

    def getDeltaX(self):
        """Get the pixel cell spacing in x.

        :return: The pixel cell spacing in x.
        """
        return self._jim_object._jipjim.getDeltaX()

    def getDeltaY(self):
        """Get the piyel cell spacing in y.

        :return: The piyel cell spacing in y.
        """
        return self._jim_object._jipjim.getDeltaY()

    def getGeoTransform(self):
        """Get the geotransform data for this dataset as a list of floats.

        :returns: List of floats with geotransform data:

        * [0] top left x
        * [1] w-e pixel resolution
        * [2] rotation, 0 if image is "north up"
        * [3] top left y
        * [4] rotation, 0 if image is "north up"
        * [5] n-s pixel resolution
        """
        return self._jim_object._jipjim.getGeoTransform()

    def getLrx(self):
        """Get the lower left corner x coordinate of this dataset.

        :return: The lower left corner x (georeferenced) coordinate of this
            dataset
        """
        return self._jim_object._jipjim.getLrx()

    def getLry(self):
        """Get the lower left corner y coordinate of this dataset.

        :return: The lower left corner y (georeferenced) coordinate of this
            dataset
        """
        return self._jim_object._jipjim.getLry()

    def getNoDataVals(self):
        """Get the list of no data values."""
        return self._jim_object._jipjim.getNoDataValues()

    def getProjection(self):
        """Get the projection for this dataset in well known text (wkt) format.

        :return: The projection string in well known text format.
        """
        return self._jim_object._jipjim.getProjection()

    def getRefPix(self, *args):
        """Calculate the reference pixel as the center of gravity pixel.

        Calculated as the weighted average of all values not taking into
        account no data values for a specific band (start counting from 0).

        :return: The reference pixel as the centre of gravity pixel (weighted
            average of all values not taking into account no data values) for
            a specific band (start counting from 0).
        """
        return self._jim_object._jipjim.getRefPix(*args)

    def getUlx(self):
        """Get the upper left corner x coordinate of this dataset.

        :return: The upper left corner x (georeferenced) coordinate of this
            dataset
        """
        return self._jim_object._jipjim.getUlx()

    def getUly(self):
        """Get the upper left corner y coordinate of this dataset.

        :return: The upper left corner y (georeferenced) coordinate of this
            dataset
        """
        return self._jim_object._jipjim.getUly()

    def imageInfo(self):
        """Return image information (number of lines, columns, etc.)."""
        self._jim_object._jipjim.imageInfo()

    def nrOfBand(self):
        """Get number of bands in this raster dataset.

        :return: The number of bands in this raster dataset
        """
        return self._jim_object._jipjim.nrOfBand()

    def nrOfCol(self):
        """Get number of columns in this raster dataset.

        :return: The number of columns in this raster dataset
        """
        return self._jim_object._jipjim.nrOfCol()

    def nrOfPlane(self):
        """Get number of planes in this raster dataset.

        :return: The number of planes in this raster dataset
        """
        return self._jim_object._jipjim.nrOfPlane()

    def nrOfRow(self):
        """Get number of rows in this raster dataset.

        :return: The number of rows in this raster dataset
        """
        return self._jim_object._jipjim.nrOfRow()

    def printNoDataVals(self):
        """Print the list of no data values of this raster dataset."""
        self._jim_object._jipjim.printNoDataValues()

    def pushNoDataVal(self, value):
        """Push a no data value for this raster dataset."""
        self._jim_object._jipjim.pushNoDataValue(value)

    def setGeoTransform(self, *args):
        """Set the geotransform data for this dataset.

        :args: List of floats with geotransform data:

        * [0] top left x
        * [1] w-e pixel resolution
        * [2] rotation, 0 if image is "north up"
        * [3] top left y
        * [4] rotation, 0 if image is "north up"
        * [5] n-s pixel resolution
        """
        self._jim_object._jipjim.setGeoTransform(*args)

    def setNoDataVals(self, value):
        """Set the list of no data value for this raster dataset."""
        if isinstance(value, list):
            self._jim_object._jipjim.setNoData(value)
        elif type(value) in (float, int):
            self._jim_object._jipjim.setNoDataValue(value)
        else:
            raise TypeError('Error: setNoDataVals not implemented for value '
                            'type {}'.format(type(value)))

    def setProjection(self, *args):
        """Set the projection for this dataset.

        Set it in well known text (wkt) format or as a string epsg:<epsgcode>.

        :args: the projection for this dataset in well known text (wkt) format
            or as a string epsg:<epsgcode>.
        """
        self._jim_object._jipjim.setProjection(*args)


class _PropertiesList(_pj.modules.JimListModuleBase):
    """Define all properties methods for JimLists."""

    def clearNoData(self):
        """Clear the list of no data values for this JimList object."""
        self._jim_list._jipjimlist.clearNoData()

    def covers(self, *args):
        """Check if a geolocation is covered by this dataset.

        You can check the coverage for a :ref:`point of interest
        <coversl1>` or :ref:`region of interest <coversl2>`.

        .. _coversl1:

        :Using a point coordinates:

        * ``x`` (float): x coordinate in spatial reference system of \
                         the raster dataset
        * ``y`` (float): y coordinate in spatial reference system of \
                         the raster dataset

        .. _coversl2:

        :Using a region of interest:

        * ``ulx`` (float): upper left x coordinate in spatial reference \
                           system of the raster dataset
        * ``uly`` (float): upper left y coordinate in spatial reference \
                           system of the raster dataset
        * ``lrx`` (float): lower right x coordinate in spatial reference \
                           system of the raster dataset
        * ``lry`` (float): lower right x coordinate in spatial reference \
                           system of the raster dataset
        * ``all`` (bool): set to True if the entire bounding box must be \
                          covered by the raster dataset

        Returns:
        True if the raster dataset covers the point or region of interest.
        """
        return self._jim_list._jipjimlist.covers(*args)

    def getBBox(self):
        """Get the bounding box (georeferenced) coordinates of this dataset.

        :return: A list with upper left x, upper left y, lower right x, and
            lower right y
        """
        return self._jim_list._jipjimlist.getBoundingBox()

    def getLrx(self):
        """Get the lower left corner x coordinate of this dataset.

        :return: The lower left corner x (georeferenced) coordinate of this
            dataset
        """
        return self._jim_list._jipjimlist.getLrx()

    def getLry(self):
        """Get the lower left corner y coordinate of this dataset.

        :return: The lower left corner y (georeferenced) coordinate of this
            dataset
        """
        return self._jim_list._jipjimlist.getLry()

    def getNoDataVals(self):
        """Get the list of no data values."""
        return self._jim_list._jipjimlist.getNoDataValues()

    def getUlx(self):
        """Get the upper left corner x coordinate of this dataset.

        :return: The upper left corner x (georeferenced) coordinate of this
            dataset
        """
        return self._jim_list._jipjimlist.getUlx()

    def getUly(self):
        """Get the upper left corner y coordinate of this dataset.

        :return: The upper left corner y (georeferenced) coordinate of this
            dataset
        """
        return self._jim_list._jipjimlist.getUly()

    def pushNoDataVal(self, value):
        """Push a no data value for this raster JimList object."""
        self._jim_list._jipjimlist.pushNoDataValue(value)

    def selectGeo(self, *args):
        """Select geographical properties (ulx, uly, ...).
        """
        self._jim_list._jipjimlist.selectGeo(*args)
        self._jim_list._set(self._jim_list)


class _PropertiesVect(_pj.modules.JimVectModuleBase):
    """Define all properties methods for JimVects."""

    def getBBox(self):
        """Get the bounding box (georeferenced) coordinates of this dataset.

        :return: A list with upper left x, upper left y, lower right x, and
            lower right y
        """
        return self._jim_vect._jipjimvect.getBoundingBox()

    def getFeatureCount(self, layer=None):
        """Get the number of features of this dataset.

        :layer: the layer number (default is all layers)
        :return: the number of features of this layer
        """
        if layer is not None:
            return self._jim_vect._jipjimvect.getFeatureCount(layer)
        else:
            return self._jim_vect._jipjimvect.getFeatureCount()

    def getFieldNames(self, layer=0):
        """Get the list of field names for this dataset.

        :param layer: The layer to get the field names, index starting from 0
            (default is 0: first layer)
        :return: The list of field names
            dataset
        """
        return self._jim_vect._jipjimvect.getFieldNames(layer)

    def getLayerCount(self):
        """Get the number of layers of this dataset.

        :return: the number of layers of this dataset
        """
        return self._jim_vect._jipjimvect.getLayerCount()

    def getLrx(self):
        """Get the lower left corner x coordinate of this dataset.

        :return: The lower left corner x (georeferenced) coordinate of this
            dataset
        """
        return self._jim_vect._jipjimvect.getLrx()

    def getLry(self):
        """Get the lower left corner y coordinate of this dataset.

        :return: The lower left corner y (georeferenced) coordinate of this
            dataset
        """
        return self._jim_vect._jipjimvect.getLry()

    def getProjection(self, layer=0):
        """Get the projection for this dataset in well known text (wkt) format.

        :param layer: The layer to get the projection from, index starting
            from 0 (default is 0: first layer)
        :return: The projection string in well known text format.
        """
        return self._jim_vect._jipjimvect.getProjection(layer)

    def getUlx(self):
        """Get the upper left corner x coordinate of this dataset.

        :return: The upper left corner x (georeferenced) coordinate of this
            dataset
        """
        return self._jim_vect._jipjimvect.getUlx()

    def getUly(self):
        """Get the upper left corner y coordinate of this dataset.

        :return: The upper left corner y (georeferenced) coordinate of this
            dataset
        """
        return self._jim_vect._jipjimvect.getUly()

    def isEmpty(self):
        """Check if object contains features (non-emtpy).

        :return: True if empty, False if not
        """
        return self._jim_vect._jipjimvect.isEmpty()
