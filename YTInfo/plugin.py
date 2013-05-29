###
# Copyright (c) 2013, Transfusion
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import gdata.youtube.service
import gdata.youtube
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('YTInfo')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x
def video_id(value):
        url_data = urlparse.urlparse(value)
        query = urlparse.parse_qs(url_data.query)
        try :
            video = query["v"][0]
        except KeyError:
            video = "null"
        return video

class YTInfo(callbacks.Plugin):
    """Add the help for "@plugin help YTInfo" here
    This should describe *how* to use this plugin."""
    
    def yinfo(self, irc, msg, args, n):
        ''' <valid YouTube URL>
        Gets stats and popularity for this YouTube Video.
        '''
        if video_id(str(n)) == "null":
            irc.reply("not a youtube video")
        else:
            yt_service = gdata.youtube.service.YouTubeService()
            yt_service.ssl = False
            entry = yt_service.GetYouTubeVideoEntry(video_id=video_id(str(params[0])))
            try:
                u = entry.rating.average
            except AttributeError:
                u = "-"
            irc.reply( "\x02Title:\x02 "+\
                                entry.media.title.text+" \x02Cat:\x02 "+\
                                entry.media.category[0].text+" \x02Duration:\x02 "+\
                                str(datetime.timedelta(seconds=int(entry.media.duration.seconds)))+" \x02Published On:\x02 "+\
                                entry.published.text+" \x02Rating:\x02 "+\
                                u+" out of 5")
    yinfo = wrap(yinfo , ['httpUrl'])


Class = YTInfo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
