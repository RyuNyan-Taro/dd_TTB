Competition of Drivendata

https://www.drivendata.org/competitions/143/tick-tick-bloom/

# Record
## satellite
- Two type of satellite image and these have different assets -> some patterns are required to select best image to calculate features.
- The center of spot has no water region at some data
- New method require over 24 hours to finish all process
- sentinel
  - SCL has cell type(water, cloud, etc.) -> but the size is not equals to image size. So simply condition and filter don't act. How to resize?
- landset
  - Lower resolution, but the data has temperature band in assets.
## hrrr
- There is no data of hrrr -> reply to topic which has same problem.
# Submissions score
## 1.5672 -> 1.5505
### modified
- if SCL has water(number==6), it choice as training image.
- The result higher than benchmark score, 1.5641.


# Ref
satellite: https://drivendata.co/blog/tick-tick-bloom-benchmark

hrrr: https://nbviewer.org/github/microsoft/AIforEarthDataSets/blob/main/data/noaa-hrrr.ipynb