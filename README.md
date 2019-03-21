# PewDiePie Prometheus Exporter

## Synopsis
  This is a quick exporter that will query the youtube api to gather the subscriber count from both
  Pewds and T-Series. You can build the docker container, then scrape the port 6969 to get the metrics created.

    // Add your api key to the python script -- get this from youtube dev console.
    // Build the docker container
       $ docker build -t pewdiepie .

    // Run the docker image
       $ docker run -d -p 6969:6969 pewdiepie

    // Add scrape config to prometheus to get the information

#Project Information
##Developers
###Owner:
  __ah824a@att.com__
