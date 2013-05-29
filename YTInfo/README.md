#Description:
* A plugin that fetches info about a YouTube URL for Limnoria/Supybot.

##Dependencies:
* http://code.google.com/p/gdata-python-client/downloads/list Version 2.0.17 or above
* http://docs.python.org/library/urlparse.html

###Expected output:
* [15:46:53] <&Transfusion> !yinfo http://www.youtube.com/watch?v=oTKuWlx-tIY
* [15:46:54] <@yapib> Transfusion: Title: ASUS Transformer AiO P1801 Cat: Tech Duration: 0:01:11 Published On: 2013-03-07T05:30:07.000Z Rating: 4.9447002 out of 5

* [16:07:25] <&Transfusion> !yinfo http://youtu.be/qX0Y09J8ptQ?a
* [16:07:27] <@yapib> Transfusion: Title: Genie - SNSD MV mix (Korean & Japanese) Cat: Music Duration: 0:04:19 Published On: 2010-08-28T11:46:50.000Z Rating: 5.0 out of 5

###Usage:
* [16:09:03] <@yapib> Transfusion: (yinfo \<valid YouTube URL\>) -- Gets stats and popularity for this YouTube Video. 
