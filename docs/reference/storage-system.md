# Storage System

## Basics

To store files like the garden images, logs or plant pointclouds we use the storage folder.
Images is a common folder, which allows to store files that are not accessible through an url.
The logs folder uses the [django logging system](https://docs.djangoproject.com/en/4.1/topics/logging/).
It is configured to contain two logs. `debug.log`, which shows all logs but can get kind of messy.
For a cleaner logging experience we added the second log `info.log`, which shows everything except the logs defined as debug.
As a third option for storage we added the media folder.
everything inside this folder can be accessed through an url.
For this we implemented the [django storage system](https://docs.djangoproject.com/en/4.1/ref/files/storage/).
There is currently no system implemented to restrict the access to the data inside of the media folder.

## Folder Structure

Files inside the media folder can be accessed by `http://localhost:8000/media/`.
An example GET request to the pointcloud of plant1 would look like this `http://localhost:8000/media/pointclouds/ply/05717c979b0d4bd790d31ce218cd58ee/06694a57e7cf4ee1acce970ab9d9d67a.ply`.

```text
storage
├── images
│   └── garden1.png <garden-image.png>
├── logs
│   ├── debug.log
│   └── info.log
└── media
    └── pointclouds
        └── ply
            ├── 05717c979b0d4bd790d31ce218cd58ee <bed1-uuid>
            │   ├── 06694a57e7cf4ee1acce970ab9d9d67a.ply <plant1-uuid>
            │   ├── 0bf37a0851b7402d88674e153f58e6f8.ply <plant2-uuid>
            │   ├── 0d927fa6b3534f9580d1db73d483b254.ply <plant3-uuid>
            │   ├── ...
```
