# Improvements

The following section contains suggestions for improving the application and may be extended much further.

## Tiling of garden images to increase loading speed

Administrators of companies or gardens have the ability to upload a (self-taken) picture of a garden using
the web interface. The image can be displayed in the dashboard-, beds- or plants-view in the web interface,
replacing the satellite image at the exact location of the garden, providing a much more detailed
view of the beds and plants.

High resolution images can have a large file size, this can lead to long loading times
of the web interface, especially for users which have a slow internet connection.

To solve this problem, a functionality could be implemented, which splits the uploaded image into many little
square tiles. A single tile can be loaded much faster, because of the smaller file size. The tiles will be loaded
incrementally, building the hole image. Users will have the advantage of seeing parts of the image earlier
and having better visual feedback of the loading process.
