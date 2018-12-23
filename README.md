# RRCC_to_Valetudo

Converts the zones created with RoboRock Control Center (https://github.com/LazyT/rrcc) to a Valetudo (https://github.com/Hypfer/Valetudo/) configuration file.

Reads the roborock control center config file located in home/.rrcc/rrcc.cfg and converts the data in a Valetudo configuration file (home/.rrcc/config.json)
you just need to upload it as /mnt/data/valetudo/config.json (/etc/valetudo/config.json for valetudo <= 0.0.8) on your robot.
