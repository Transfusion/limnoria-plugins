#Description:
* A plugin that fetches info about a YouTube URL for Limnoria/Supybot.

##Dependencies:
* http://code.google.com/p/gdata-python-client/downloads/list Version 2.0.17 or above
* http://docs.python.org/library/urlparse.html

###Expected output:
* [21:58:22] <@Transfusion> $yinfo http://www.youtube.com/watch?v=oTKuWlx-tIY
* [21:58:23] <yapib> Transfusion: **Title:** ASUS Transformer AiO P1801 **Cat:** Tech Duration: 0:01:11 **Published On:** 2013-03-07T05:30:07.000Z **Rating:** 4.9408865 out of 5 **Views:** 170603
* [21:58:24] <@Transfusion> $yinfo http://youtu.be/qX0Y09J8ptQ?a
* [21:58:25] <yapib> Transfusion: **Title:** Genie - SNSD MV mix (Korean & Japanese) **Cat:** Music **Duration:** 0:04:19 **Published On:** 2010-08-28T11:46:50.000Z **Rating:** 5.0 out of 5 **Views:** 15256
* [22:02:53] <@Transfusion> I think both AMD http://www.youtube.com/watch?v=Xo1jJJGhneg and nVidia http://www.youtube.com/watch?v=tnEB5xRQtpw have something up their sleeves. 
* [22:02:56] <yapib> **Title:** AMD GPU 14 Product Showcase **Cat:** Tech **Duration:** 2:44:36 **Published On:** 2013-09-27T14:34:04.000Z **Rating:** 4.8876753 out of 5 **Views:** 29162
* [22:02:57] <yapib> **Title:** NVIDIA Flame Works Film-Quality Volumetric Effect Engine Demo **Cat:** Tech **Duration:** 0:00:37 **Published On:** 2013-10-17T16:52:09.000Z **Rating:** 4.5555553 out of 5 **Views:** 3911

###Usage:
* [16:09:03] <@yapib> Transfusion: (**yinfo** \<**valid YouTube URL**\>) -- Gets stats and popularity for this YouTube Video. 

* [22:01:26] <@Transfusion> $config help supybot.plugins.YTInfo.ytSnarfer
* [22:01:27] <yapib> Transfusion: Determines whether the bot will automatically 'snarf' YouTube URLs and print information about them. (Current value: True)
